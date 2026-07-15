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
# MAGIC ### Notebook 5.2: Análisis de Datos Financieros con IA
# MAGIC ### 📊 **CASOS PRÁCTICOS CON IA**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introduccion
# MAGIC %md
# MAGIC # 5.2 - Analisis de Datos Financieros con IA
# MAGIC
# MAGIC ## Objetivo
# MAGIC Aplicar IA para analizar datos financieros reales y generar insights.
# MAGIC
# MAGIC ## Que Aprenderemos
# MAGIC * Analisis de series temporales con IA
# MAGIC * Deteccion de anomalias
# MAGIC * Predicciones basicas
# MAGIC * Generacion de reportes automaticos
# MAGIC * Optimizacion de portafolios con IA

# COMMAND ----------

# DBTITLE 1,Librerias y Datos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

sns.set_style('whitegrid')

# Simular datos de 5 acciones durante 2 anos
np.random.seed(42)
n_dias = 504  # 2 anos aprox
fecha_inicio = datetime(2022, 1, 1)

fechas = pd.date_range(fecha_inicio, periods=n_dias, freq='D')

# Simular precios de acciones
precios_iniciales = [100, 50, 150, 80, 120]
acciones = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

precios_dict = {}
for i, accion in enumerate(acciones):
    retornos = np.random.normal(0.0005, 0.02, n_dias)
    precios = precios_iniciales[i] * np.exp(np.cumsum(retornos))
    precios_dict[accion] = precios

df_precios = pd.DataFrame(precios_dict, index=fechas)

print("Dataset de precios creado")
print(f"Periodo: {df_precios.index[0].date()} a {df_precios.index[-1].date()}")
print(f"Acciones: {', '.join(acciones)}")
print(f"\nPrimeros precios:")
print(df_precios.head())

# COMMAND ----------

# DBTITLE 1,Caso 1 - Analisis de Tendencias
# MAGIC %md
# MAGIC ## Caso 1: Analisis de Tendencias con IA
# MAGIC
# MAGIC ### Problema
# MAGIC Identificar cual accion ha tenido mejor desempeno en diferentes periodos.

# COMMAND ----------

# DBTITLE 1,Visualizacion de Precios
# Graficar evolucion de precios normalizados
df_normalizado = df_precios / df_precios.iloc[0] * 100

plt.figure(figsize=(14, 7))
for col in df_normalizado.columns:
    plt.plot(df_normalizado.index, df_normalizado[col], label=col, linewidth=2)

plt.title('Evolucion de Precios (Base 100)', fontsize=14, fontweight='bold')
plt.xlabel('Fecha')
plt.ylabel('Precio Normalizado')
plt.legend(loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nConsulta con Genie:")
print('"Cual accion tuvo mejor retorno acumulado?"')
print('"Identifica periodos de alta volatilidad"')

# COMMAND ----------

# DBTITLE 1,Caso 2 - Deteccion de Anomalias
# MAGIC %md
# MAGIC ## Caso 2: Deteccion de Anomalias
# MAGIC
# MAGIC ### Problema
# MAGIC Identificar dias con movimientos anormales en los precios.

# COMMAND ----------

# DBTITLE 1,Calcular Retornos Diarios
# Calcular retornos diarios
df_retornos = df_precios.pct_change().dropna()

# Identificar retornos extremos (>3 desviaciones estandar)
for accion in acciones:
    media = df_retornos[accion].mean()
    std = df_retornos[accion].std()
    umbral_superior = media + 3 * std
    umbral_inferior = media - 3 * std
    
    anomalias = df_retornos[
        (df_retornos[accion] > umbral_superior) | 
        (df_retornos[accion] < umbral_inferior)
    ]
    
    if len(anomalias) > 0:
        print(f"\n{accion}:")
        print(f"  Anomalias detectadas: {len(anomalias)}")
        print(f"  Mayor caida: {anomalias[accion].min()*100:.2f}%")
        print(f"  Mayor subida: {anomalias[accion].max()*100:.2f}%")

print("\n" + "="*60)
print("Consulta con Genie:")
print('"Grafica los retornos de AAPL con los outliers marcados"')
print('"Que dias tuvieron movimientos anomalos simultaneos?"')

# COMMAND ----------

# DBTITLE 1,Caso 3 - Correlaciones y Diversificacion
# MAGIC %md
# MAGIC ## Caso 3: Analisis de Correlaciones
# MAGIC
# MAGIC ### Problema
# MAGIC Identificar acciones que se mueven juntas para optimizar diversificacion.

# COMMAND ----------

# DBTITLE 1,Matriz de Correlacion
# Calcular matriz de correlacion
corr_matrix = df_retornos.corr()

# Visualizar con heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Matriz de Correlacion de Retornos', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

print("\nPares con mayor correlacion:")
corr_pairs = []
for i in range(len(acciones)):
    for j in range(i+1, len(acciones)):
        corr_pairs.append((
            acciones[i], 
            acciones[j], 
            corr_matrix.iloc[i, j]
        ))

corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
for i, (a1, a2, corr) in enumerate(corr_pairs[:3]):
    print(f"{i+1}. {a1} - {a2}: {corr:.3f}")

print("\n" + "="*60)
print("Consulta con Genie:")
print('"Sugiere un portafolio de 3 acciones con baja correlacion"')
print('"Calcula el beneficio de diversificacion"')

# COMMAND ----------

# DBTITLE 1,Caso 4 - Optimizacion de Portafolio
# MAGIC %md
# MAGIC ## Caso 4: Optimizacion Automatica de Portafolio
# MAGIC
# MAGIC ### Problema
# MAGIC Encontrar los pesos optimos para maximizar Sharpe Ratio.

# COMMAND ----------

# DBTITLE 1,Simulacion de Portafolios
# Calcular metricas anualizadas
retorno_anual = df_retornos.mean() * 252
volatilidad_anual = df_retornos.std() * np.sqrt(252)
cov_matrix = df_retornos.cov() * 252

# Simular 5000 portafolios aleatorios
n_portafolios = 5000
resultados = np.zeros((3, n_portafolios))
pesos_portafolios = []

np.random.seed(42)
for i in range(n_portafolios):
    pesos = np.random.random(len(acciones))
    pesos /= pesos.sum()
    pesos_portafolios.append(pesos)
    
    ret_port = np.dot(pesos, retorno_anual)
    vol_port = np.sqrt(np.dot(pesos.T, np.dot(cov_matrix, pesos)))
    sharpe = ret_port / vol_port
    
    resultados[0, i] = ret_port
    resultados[1, i] = vol_port
    resultados[2, i] = sharpe

# Encontrar portafolio optimo
idx_max_sharpe = resultados[2].argmax()
mejor_retorno = resultados[0, idx_max_sharpe]
mejor_volatilidad = resultados[1, idx_max_sharpe]
mejor_sharpe = resultados[2, idx_max_sharpe]
mejores_pesos = pesos_portafolios[idx_max_sharpe]

print("PORTAFOLIO OPTIMO (Maximo Sharpe Ratio)")
print("="*60)
for i, accion in enumerate(acciones):
    print(f"{accion}: {mejores_pesos[i]*100:.2f}%")
print(f"\nRetorno esperado: {mejor_retorno*100:.2f}%")
print(f"Volatilidad: {mejor_volatilidad*100:.2f}%")
print(f"Sharpe Ratio: {mejor_sharpe:.3f}")

# COMMAND ----------

# DBTITLE 1,Grafico de Frontera Eficiente
# Graficar frontera eficiente
plt.figure(figsize=(12, 8))

# Scatter de todos los portafolios
sc = plt.scatter(resultados[1]*100, resultados[0]*100, 
                 c=resultados[2], cmap='viridis', alpha=0.6, s=10)
plt.colorbar(sc, label='Sharpe Ratio')

# Marcar portafolio optimo
plt.scatter(mejor_volatilidad*100, mejor_retorno*100, 
            marker='*', color='red', s=500, edgecolors='black', 
            linewidths=2, label='Portafolio Optimo')

# Marcar acciones individuales
for i, accion in enumerate(acciones):
    plt.scatter(volatilidad_anual[accion]*100, retorno_anual[accion]*100,
                marker='o', s=200, edgecolors='black', linewidths=2,
                label=accion)

plt.xlabel('Volatilidad Anualizada (%)', fontsize=12)
plt.ylabel('Retorno Esperado Anualizado (%)', fontsize=12)
plt.title('Frontera Eficiente - Optimizacion con IA', fontsize=14, fontweight='bold')
plt.legend(loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nConsulta con Genie:")
print('"Encuentra el portafolio de minima varianza"')
print('"Compara este portafolio con uno equiponderado"')

# COMMAND ----------

# DBTITLE 1,Resumen y Ejercicios
# MAGIC %md
# MAGIC ## Resumen
# MAGIC
# MAGIC ### Casos Analizados
# MAGIC 1. **Tendencias**: Identificacion de mejor desempeno
# MAGIC 2. **Anomalias**: Deteccion de movimientos extremos
# MAGIC 3. **Correlaciones**: Analisis de diversificacion
# MAGIC 4. **Optimizacion**: Busqueda de portafolio optimo
# MAGIC
# MAGIC ### Ejercicios con Genie
# MAGIC
# MAGIC **Ejercicio 1**: Analisis Temporal
# MAGIC * Divide los datos en 4 trimestres
# MAGIC * Identifica cual trimestre tuvo mayor volatilidad
# MAGIC * Grafica el retorno acumulado por trimestre
# MAGIC
# MAGIC **Ejercicio 2**: Riesgo vs Retorno
# MAGIC * Calcula el Coefficient of Variation de cada accion
# MAGIC * Identifica la accion con mejor retorno ajustado por riesgo
# MAGIC * Crea un ranking de acciones
# MAGIC
# MAGIC **Ejercicio 3**: Backtesting
# MAGIC * Crea una estrategia simple (ej: comprar la mejor accion del mes anterior)
# MAGIC * Calcula el retorno de la estrategia
# MAGIC * Comparala con comprar y mantener
# MAGIC
# MAGIC **Ejercicio 4**: Reporte Automatico
# MAGIC * Usa Genie para generar un reporte ejecutivo
# MAGIC * Incluye metricas clave, graficos y recomendaciones
# MAGIC * Exporta a formato presentable
# MAGIC
# MAGIC ### Proximos Pasos
# MAGIC * **Notebook 5.3**: Caso integrador - Portfolio inteligente completo

# COMMAND ----------

