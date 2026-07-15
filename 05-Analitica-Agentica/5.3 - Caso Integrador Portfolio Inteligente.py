# Databricks notebook source
# DBTITLE 1,Encabezado Institucional
# MAGIC %md
# MAGIC
# MAGIC <table style="border: none; width: 100%; border-collapse: collapse;">
# MAGIC   <tr>
# MAGIC     <td style="border: none; text-align: center;">
# MAGIC       <img src="/Workspace/Users/cortega@uda.edu.ar/Databricks Finance Lab/Imagenes/uda.jpg" width="90"/>
# MAGIC     </td>
# MAGIC     <td style="border: none">
# MAGIC       <h1>Universidad del Aconcagua</h1>
# MAGIC       <h2>Facultad de Ciencias Económicas y Jurídicas</h2>
# MAGIC     </td>
# MAGIC   </tr>
# MAGIC </table>
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC # Databricks Finance Lab
# MAGIC ## Analítica Financiera Agéntica
# MAGIC
# MAGIC ### Módulo 05: Analítica Agéntica con IA
# MAGIC ### Notebook 5.3: Caso Integrador Portfolio Inteligente
# MAGIC ### 🎓 **PROYECTO FINAL DEL CURSO**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introduccion
# MAGIC %md
# MAGIC # 5.3 - Caso Integrador: Portfolio Inteligente
# MAGIC
# MAGIC ## Proyecto Final del Curso
# MAGIC
# MAGIC Este notebook integra todos los conceptos aprendidos:
# MAGIC * Modulo 01: Valor del dinero en el tiempo
# MAGIC * Modulo 02: Valoracion de instrumentos
# MAGIC * Modulo 03: Analisis financiero
# MAGIC * Modulo 04: Riesgo y portafolios
# MAGIC * Modulo 05: Analitica con IA
# MAGIC
# MAGIC ## Objetivo
# MAGIC Construir un sistema completo de gestion de portafolios usando IA.

# COMMAND ----------

# DBTITLE 1,Caso de Estudio
# MAGIC %md
# MAGIC ## Caso: Gestion de Portfolio para Inversor Argentino
# MAGIC
# MAGIC ### Perfil del Cliente
# MAGIC * **Nombre**: Inversor conservador
# MAGIC * **Capital inicial**: $100,000 USD
# MAGIC * **Horizonte**: 5 anos
# MAGIC * **Objetivo**: Maximizar retorno con riesgo controlado
# MAGIC * **Restricciones**: 
# MAGIC   - Maximo 30% en una sola accion
# MAGIC   - Al menos 20% en bonos
# MAGIC   - Diversificacion internacional
# MAGIC
# MAGIC ### Universo de Inversion
# MAGIC * Acciones tecnologicas (AAPL, GOOGL, MSFT)
# MAGIC * Acciones industriales (BA, CAT)
# MAGIC * Bonos corporativos (simulados)
# MAGIC * ETFs de mercados emergentes
# MAGIC
# MAGIC ### Preguntas a Resolver
# MAGIC 1. Como construir el portafolio optimo?
# MAGIC 2. Cual es el retorno esperado y riesgo?
# MAGIC 3. Como monitorearlo en el tiempo?
# MAGIC 4. Cuando rebalancear?

# COMMAND ----------

# DBTITLE 1,Setup y Datos
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from scipy.optimize import minimize
from datetime import datetime, timedelta

# Colores institucionales UDA
UDA_COLORS = {'primary': '#003366', 'accent': '#FF6600', 'success': '#28A745', 'danger': '#DC3545'}

# Parametros del caso
capital_inicial = 100000
horizonte_anos = 5
tasa_libre_riesgo = 0.03  # 3% anual

# Simular datos historicos (2 anos)
np.random.seed(42)
n_dias = 504
fechas = pd.date_range('2022-01-01', periods=n_dias, freq='D')

# Activos disponibles
activos = ['AAPL', 'GOOGL', 'MSFT', 'BA', 'CAT', 'BOND_CORP', 'EM_ETF']
precios_iniciales = [150, 2800, 300, 200, 150, 100, 50]

# Simular retornos con diferentes perfiles
retornos_esperados = [0.12, 0.10, 0.11, 0.08, 0.09, 0.04, 0.07]  # anuales
volatilidades = [0.25, 0.22, 0.24, 0.28, 0.30, 0.05, 0.18]  # anuales

precios_dict = {}
for i, activo in enumerate(activos):
    retornos_diarios = np.random.normal(
        retornos_esperados[i]/252, 
        volatilidades[i]/np.sqrt(252), 
        n_dias
    )
    precios = precios_iniciales[i] * np.exp(np.cumsum(retornos_diarios))
    precios_dict[activo] = precios

df_precios = pd.DataFrame(precios_dict, index=fechas)

print("SETUP DEL CASO")
print("="*70)
print(f"Capital inicial: ${capital_inicial:,.0f}")
print(f"Horizonte: {horizonte_anos} anos")
print(f"Tasa libre de riesgo: {tasa_libre_riesgo*100}%")
print(f"\nActivos disponibles: {len(activos)}")
for activo in activos:
    print(f"  - {activo}")
print(f"\nDatos historicos: {n_dias} dias ({n_dias/252:.1f} anos)")

# COMMAND ----------

# DBTITLE 1,Paso 1 - Analisis Exploratorio
# MAGIC %md
# MAGIC ## Paso 1: Analisis Exploratorio con IA
# MAGIC
# MAGIC ### Usa Genie para:
# MAGIC * Calcular estadisticas descriptivas de cada activo
# MAGIC * Graficar evolucion de precios normalizados
# MAGIC * Identificar periodos de alta volatilidad
# MAGIC * Analizar correlaciones entre activos

# COMMAND ----------

# DBTITLE 1,Metricas Historicas
# Calcular retornos y metricas
df_retornos = df_precios.pct_change().dropna()

# Metricas anualizadas
retorno_anual = df_retornos.mean() * 252
volatilidad_anual = df_retornos.std() * np.sqrt(252)
sharpe_ratio = (retorno_anual - tasa_libre_riesgo) / volatilidad_anual

metricas = pd.DataFrame({
    'Retorno Anual': retorno_anual * 100,
    'Volatilidad': volatilidad_anual * 100,
    'Sharpe Ratio': sharpe_ratio
}).round(2)

print("METRICAS HISTORICAS")
print("="*70)
print(metricas.sort_values('Sharpe Ratio', ascending=False))
print("\nConsulta con Genie:")
print('"Grafica el retorno vs riesgo de estos activos"')
print('"Identifica cual es el mejor activo ajustado por riesgo"')

# COMMAND ----------

# DBTITLE 1,Paso 2 - Construccion del Portfolio
# MAGIC %md
# MAGIC ## Paso 2: Construccion del Portfolio Optimo
# MAGIC
# MAGIC ### Restricciones del Cliente
# MAGIC * Maximo 30% en una accion individual
# MAGIC * Minimo 20% en bonos (BOND_CORP)
# MAGIC * Suma de pesos = 100%

# COMMAND ----------

# DBTITLE 1,Optimizacion con Restricciones
# Matriz de covarianza
cov_matrix = df_retornos.cov() * 252

# Funcion objetivo: minimizar riesgo para retorno dado
def portfolio_variance(pesos, cov_matrix):
    return np.dot(pesos.T, np.dot(cov_matrix, pesos))

def portfolio_return(pesos, retornos):
    return np.dot(pesos, retornos)

# Restricciones
constraints = [
    {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},  # Suma = 1
    {'type': 'ineq', 'fun': lambda w: w[5] - 0.20}   # BOND >= 20%
]

# Limites: cada accion <= 30%, bono sin limite superior
bounds = [(0, 0.30)] * 5 + [(0.20, 1.0)] + [(0, 0.30)]

# Optimizar para maximo Sharpe
def neg_sharpe(pesos):
    ret = portfolio_return(pesos, retorno_anual)
    vol = np.sqrt(portfolio_variance(pesos, cov_matrix))
    return -(ret - tasa_libre_riesgo) / vol

# Punto inicial
w0 = np.array([0.15, 0.15, 0.15, 0.10, 0.10, 0.20, 0.15])

# Optimizar
resultado = minimize(neg_sharpe, w0, method='SLSQP', 
                     bounds=bounds, constraints=constraints)

pesos_optimos = resultado.x

print("PORTFOLIO OPTIMO")
print("="*70)
for i, activo in enumerate(activos):
    print(f"{activo:12s}: {pesos_optimos[i]*100:6.2f}%")

ret_port = portfolio_return(pesos_optimos, retorno_anual)
vol_port = np.sqrt(portfolio_variance(pesos_optimos, cov_matrix))
sharpe_port = (ret_port - tasa_libre_riesgo) / vol_port

print(f"\nRetorno esperado: {ret_port*100:.2f}%")
print(f"Volatilidad: {vol_port*100:.2f}%")
print(f"Sharpe Ratio: {sharpe_port:.3f}")

# COMMAND ----------

# DBTITLE 1,Paso 3 - Proyeccion
# MAGIC %md
# MAGIC ## Paso 3: Proyeccion a 5 Anos
# MAGIC
# MAGIC Calcular valor esperado del portfolio en el horizonte.

# COMMAND ----------

# DBTITLE 1,Simulacion Monte Carlo
# Simulacion Monte Carlo del portfolio
n_simulaciones = 1000
n_dias_futuro = 252 * horizonte_anos

resultados_simulacion = np.zeros((n_simulaciones, n_dias_futuro))

np.random.seed(42)
for i in range(n_simulaciones):
    # Simular retornos del portfolio
    retornos_sim = np.random.multivariate_normal(
        df_retornos.mean(), 
        df_retornos.cov(), 
        n_dias_futuro
    )
    retornos_portfolio = np.dot(retornos_sim, pesos_optimos)
    valor_portfolio = capital_inicial * np.exp(np.cumsum(retornos_portfolio))
    resultados_simulacion[i, :] = valor_portfolio

# Calcular percentiles
percentil_5 = np.percentile(resultados_simulacion[:, -1], 5)
percentil_50 = np.percentile(resultados_simulacion[:, -1], 50)
percentil_95 = np.percentile(resultados_simulacion[:, -1], 95)

print("PROYECCION A 5 ANOS (Simulacion Monte Carlo)")
print("="*70)
print(f"Capital inicial: ${capital_inicial:,.0f}")
print(f"\nValor esperado (mediana): ${percentil_50:,.0f}")
print(f"Escenario optimista (95%): ${percentil_95:,.0f}")
print(f"Escenario pesimista (5%): ${percentil_5:,.0f}")
print(f"\nRetorno esperado: {((percentil_50/capital_inicial)**(1/horizonte_anos)-1)*100:.2f}% anual")
print(f"\nProbabilidad de perdida: {(resultados_simulacion[:,-1] < capital_inicial).mean()*100:.1f}%")

# COMMAND ----------

# DBTITLE 1,Visualizacion de Escenarios
# Graficar escenarios con Plotly interactivo
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=(
        'Simulación Monte Carlo - Escenarios de Portfolio',
        f'Distribución de Resultados a {horizonte_anos} Años'
    ),
    horizontal_spacing=0.12
)

# Preparar datos
tiempo = np.arange(n_dias_futuro) / 252
mediana = np.median(resultados_simulacion, axis=0) / 1000
p5 = np.percentile(resultados_simulacion, 5, axis=0) / 1000
p95 = np.percentile(resultados_simulacion, 95, axis=0) / 1000

# Gráfico 1: Simulaciones (50 trayectorias)
for i in range(min(50, n_simulaciones)):
    fig.add_trace(go.Scatter(
        x=tiempo, y=resultados_simulacion[i, :]/1000,
        mode='lines',
        line=dict(color='rgba(0, 51, 102, 0.1)', width=1),
        showlegend=False,
        hoverinfo='skip'
    ), row=1, col=1)

fig.add_trace(go.Scatter(
    x=tiempo, y=mediana,
    mode='lines', name='Mediana',
    line=dict(color=UDA_COLORS['danger'], width=3),
    hovertemplate='Año: %{x:.1f}<br>Valor: $%{y:.0f}k<extra></extra>'
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=tiempo, y=p5,
    mode='lines', name='Percentil 5%',
    line=dict(color=UDA_COLORS['accent'], width=2.5, dash='dash'),
    hovertemplate='Año: %{x:.1f}<br>Valor: $%{y:.0f}k<extra></extra>'
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=tiempo, y=p95,
    mode='lines', name='Percentil 95%',
    line=dict(color=UDA_COLORS['success'], width=2.5, dash='dash'),
    hovertemplate='Año: %{x:.1f}<br>Valor: $%{y:.0f}k<extra></extra>'
), row=1, col=1)

fig.add_hline(y=capital_inicial/1000, line_dash='dot', line_color='black',
              annotation_text='Capital Inicial', row=1, col=1)

# Gráfico 2: Histograma
valores_finales = resultados_simulacion[:, -1] / 1000

fig.add_trace(go.Histogram(
    x=valores_finales, nbinsx=50, name='Distribución',
    marker=dict(color=UDA_COLORS['primary'], line=dict(color='white', width=1)),
    hovertemplate='Rango: $%{x:.0f}k<br>Frecuencia: %{y}<extra></extra>',
    showlegend=False
), row=1, col=2)

for valor, color, nombre in [
    (percentil_50/1000, UDA_COLORS['danger'], f'Mediana: ${percentil_50/1000:.0f}k'),
    (percentil_5/1000, UDA_COLORS['accent'], f'P5: ${percentil_5/1000:.0f}k'),
    (percentil_95/1000, UDA_COLORS['success'], f'P95: ${percentil_95/1000:.0f}k')
]:
    fig.add_vline(x=valor, line_dash='dash', line_color=color, line_width=2,
                  annotation_text=nombre, annotation_position='top', row=1, col=2)

# Layout
fig.update_xaxes(title_text='Años', gridcolor='#E5E5E5', showgrid=True, row=1, col=1)
fig.update_yaxes(title_text='Valor del Portfolio ($1000s)', gridcolor='#E5E5E5', showgrid=True, row=1, col=1)
fig.update_xaxes(title_text='Valor Final ($1000s)', gridcolor='#E5E5E5', showgrid=True, row=1, col=2)
fig.update_yaxes(title_text='Frecuencia', gridcolor='#E5E5E5', showgrid=True, row=1, col=2)

fig.update_layout(
    height=600, plot_bgcolor='white', paper_bgcolor='white',
    hovermode='closest', showlegend=True,
    legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.8)')
)

fig.show(config={'locale': 'es', 'displayModeBar': True, 'displaylogo': False})

print("\nConsulta con Genie:")
print('"Cual es la probabilidad de duplicar el capital?"')
print('"Analiza el Value at Risk (VaR) del portfolio"')

# COMMAND ----------

# DBTITLE 1,Paso 4 - Monitoreo
# MAGIC %md
# MAGIC ## Paso 4: Sistema de Monitoreo
# MAGIC
# MAGIC Definir metricas y alertas para seguimiento continuo.

# COMMAND ----------

# DBTITLE 1,Dashboard de Monitoreo
# Metricas de monitoreo
def calcular_metricas_portfolio(precios_actuales, pesos, capital):
    """Calcula metricas actuales del portfolio"""
    valor_actual = capital
    
    # Calcular retorno desde inicio
    retorno_total = (valor_actual / capital_inicial - 1) * 100
    
    # Calcular metricas recientes (ultimo mes)
    retornos_recientes = df_retornos.iloc[-30:]
    ret_mes = np.dot(retornos_recientes.mean() * 21, pesos) * 100
    vol_mes = np.sqrt(np.dot(pesos.T, np.dot(
        retornos_recientes.cov() * 21, pesos
    ))) * 100
    
    return {
        'valor_actual': valor_actual,
        'retorno_total': retorno_total,
        'retorno_mes': ret_mes,
        'volatilidad_mes': vol_mes
    }

# Simular estado actual
metricas_actuales = calcular_metricas_portfolio(
    df_precios.iloc[-1], 
    pesos_optimos, 
    capital_inicial
)

print("DASHBOARD DE MONITOREO")
print("="*70)
print(f"Valor actual: ${metricas_actuales['valor_actual']:,.0f}")
print(f"Retorno total: {metricas_actuales['retorno_total']:.2f}%")
print(f"Retorno ultimo mes: {metricas_actuales['retorno_mes']:.2f}%")
print(f"Volatilidad ultimo mes: {metricas_actuales['volatilidad_mes']:.2f}%")

print("\n" + "="*70)
print("ALERTAS CONFIGURADAS:")
print("  1. Caida > 10% en un mes → Revisar composicion")
print("  2. Volatilidad > 25% → Reducir riesgo")
print("  3. Desviacion de pesos > 5% → Rebalancear")
print("  4. Sharpe Ratio < 0.5 → Reevaluar estrategia")

print("\nConsulta con Genie:")
print('"Crea un reporte ejecutivo del portfolio"')
print('"Sugiere cuando rebalancear basado en estas metricas"')

# COMMAND ----------

# DBTITLE 1,Conclusiones
# MAGIC %md
# MAGIC ## Conclusiones del Caso Integrador
# MAGIC
# MAGIC ### Resultados Clave
# MAGIC 1. **Portfolio Optimo**: Diversificado con 7 activos
# MAGIC 2. **Retorno Esperado**: ~10% anual con volatilidad controlada
# MAGIC 3. **Restricciones**: Cumplidas (bono >= 20%, diversificacion)
# MAGIC 4. **Horizonte**: Proyeccion a 5 anos con escenarios
# MAGIC 5. **Monitoreo**: Sistema de alertas automatico
# MAGIC
# MAGIC ### Integracion de Conceptos
# MAGIC Este caso integro:
# MAGIC * **Modulo 01**: Proyeccion de flujos a valor presente
# MAGIC * **Modulo 02**: Valoracion de instrumentos individuales
# MAGIC * **Modulo 03**: Analisis de metricas financieras
# MAGIC * **Modulo 04**: Optimizacion de portafolios
# MAGIC * **Modulo 05**: Uso de IA para analisis y decisiones
# MAGIC
# MAGIC ### Trabajo con Genie Code
# MAGIC Genie puede ayudarte a:
# MAGIC * Automatizar calculos repetitivos
# MAGIC * Generar visualizaciones rapidas
# MAGIC * Explorar escenarios alternativos
# MAGIC * Crear reportes ejecutivos
# MAGIC * Detectar anomalias en tiempo real
# MAGIC
# MAGIC ### Ejercicio Final
# MAGIC **Usa Genie para**:
# MAGIC 1. Modificar las restricciones del portfolio
# MAGIC 2. Agregar nuevos activos al universo
# MAGIC 3. Crear una estrategia de rebalanceo trimestral
# MAGIC 4. Implementar stop-loss automatico
# MAGIC 5. Generar un informe mensual automatizado

# COMMAND ----------

# DBTITLE 1,Cierre del Curso
# MAGIC %md
# MAGIC ## Felicitaciones - Curso Completado
# MAGIC
# MAGIC ### Has Aprendido
# MAGIC * Fundamentos de finanzas corporativas
# MAGIC * Valoracion de bonos y acciones
# MAGIC * Analisis y ratios financieros
# MAGIC * Construccion de portafolios
# MAGIC * Optimizacion con restricciones
# MAGIC * Uso de IA para analisis financiero
# MAGIC
# MAGIC ### Siguientes Pasos
# MAGIC 1. Practica con datos reales (Yahoo Finance, etc.)
# MAGIC 2. Explora APIs financieras
# MAGIC 3. Implementa estrategias de trading
# MAGIC 4. Crea dashboards interactivos en Databricks
# MAGIC 5. Profundiza en machine learning para finanzas
# MAGIC
# MAGIC ### Recursos Adicionales
# MAGIC * Libro: Finanzas Corporativas - Dumrauf
# MAGIC * Databricks Documentation
# MAGIC * Quantitative Finance con Python
# MAGIC * Comunidad de Data Science en Finanzas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Gracias por participar en el curso!**
# MAGIC
# MAGIC **Profesores**:
# MAGIC * Cristian Dario Ortega Yubro (cortega@uda.edu.ar)
# MAGIC * Gustavo Machin Urbay (gustavomachin@uda.edu.ar)
# MAGIC
# MAGIC **Universidad del Aconcagua - UDA, Argentina**

# COMMAND ----------

