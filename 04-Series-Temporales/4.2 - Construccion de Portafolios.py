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
# MAGIC ### Módulo 04: Series Temporales y Portafolios
# MAGIC ### Notebook 4.2: Construcción de Portafolios
# MAGIC ### 📈 **DIVERSIFICACIÓN Y FRONTERA EFICIENTE**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introduccion
# MAGIC %md
# MAGIC # 4.2 - Construccion de Portafolios
# MAGIC
# MAGIC ## Objetivo
# MAGIC Aprender a construir y optimizar portafolios de inversion.
# MAGIC
# MAGIC ## Conceptos Clave
# MAGIC * Portafolio: Combinacion de activos
# MAGIC * Ponderacion: Peso de cada activo
# MAGIC * Retorno del portafolio
# MAGIC * Riesgo del portafolio
# MAGIC * Diversificacion
# MAGIC * Frontera eficiente
# MAGIC * Portafolio optimo

# COMMAND ----------

# DBTITLE 1,Referencias
# MAGIC %md
# MAGIC ## Referencias del Libro
# MAGIC
# MAGIC **Libro**: Finanzas Corporativas - Un Enfoque Latinoamericano (2a ed.)
# MAGIC **Autor**: Guillermo L. Dumrauf
# MAGIC **Capitulo**: 7 - Riesgo y rentabilidad
# MAGIC **Seccion**: 7.4-7.6 (pag. 204-225)
# MAGIC **Ubicacion**: `/Workspace/Shared/Databricks Finance Lab/Libros/Finanzas corporativas.pdf`

# COMMAND ----------

# DBTITLE 1,Librerias
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from scipy.optimize import minimize

UDA_COLORS = {'primary': '#003366', 'accent': '#FF6600', 'success': '#28A745', 'danger': '#DC3545'}

print("✓ Librerías cargadas correctamente (Plotly + SciPy)")

# COMMAND ----------

# DBTITLE 1,Formulas
# MAGIC %md
# MAGIC ## Formulas de Portafolios
# MAGIC
# MAGIC ### Retorno del Portafolio
# MAGIC E(Rp) = suma(wi * E(Ri))
# MAGIC
# MAGIC ### Riesgo del Portafolio (2 activos)
# MAGIC SD(Rp) = sqrt[w1^2*SD1^2 + w2^2*SD2^2 + 2*w1*w2*Cov(R1,R2)]
# MAGIC
# MAGIC ### Riesgo del Portafolio (n activos)
# MAGIC Var(Rp) = suma_i suma_j (wi * wj * Cov(Ri, Rj))
# MAGIC
# MAGIC Donde:
# MAGIC * wi = Peso del activo i
# MAGIC * E(Ri) = Retorno esperado del activo i
# MAGIC * Cov(Ri, Rj) = Covarianza entre activos i y j

# COMMAND ----------

# DBTITLE 1,Datos de Ejemplo
# Crear datos de 3 activos
np.random.seed(42)

retornos_esperados = np.array([0.10, 0.12, 0.08])
desv_estandar = np.array([0.15, 0.20, 0.10])

# Matriz de correlacion
corr_matrix = np.array([
    [1.00, 0.30, 0.10],
    [0.30, 1.00, 0.20],
    [0.10, 0.20, 1.00]
])

# Matriz de covarianza
cov_matrix = np.outer(desv_estandar, desv_estandar) * corr_matrix

activos = ['Activo A', 'Activo B', 'Activo C']

print("Datos de activos:")
for i, activo in enumerate(activos):
    print(f"{activo}: Retorno={retornos_esperados[i]*100:.1f}%, Riesgo={desv_estandar[i]*100:.1f}%")

# COMMAND ----------

# DBTITLE 1,Funciones de Portafolio
def retorno_portafolio(pesos, retornos):
    """Calcula retorno del portafolio"""
    return np.dot(pesos, retornos)

def riesgo_portafolio(pesos, cov_matrix):
    """Calcula riesgo del portafolio"""
    return np.sqrt(np.dot(pesos.T, np.dot(cov_matrix, pesos)))

def ratio_sharpe(pesos, retornos, cov_matrix, rf=0.03):
    """Calcula ratio de Sharpe"""
    ret = retorno_portafolio(pesos, retornos)
    riesgo = riesgo_portafolio(pesos, cov_matrix)
    return (ret - rf) / riesgo

print("Funciones definidas")

# COMMAND ----------

# DBTITLE 1,Ejemplo de Portafolio
# Ejemplo: Portafolio equiponderado
pesos_igual = np.array([1/3, 1/3, 1/3])

ret_port = retorno_portafolio(pesos_igual, retornos_esperados)
riesgo_port = riesgo_portafolio(pesos_igual, cov_matrix)
sharpe = ratio_sharpe(pesos_igual, retornos_esperados, cov_matrix)

print("PORTAFOLIO EQUIPONDERADO")
print("="*50)
print(f"Pesos: {pesos_igual}")
print(f"Retorno esperado: {ret_port*100:.2f}%")
print(f"Riesgo (SD): {riesgo_port*100:.2f}%")
print(f"Ratio de Sharpe: {sharpe:.2f}")

print("\nCOMPARACION CON ACTIVOS INDIVIDUALES:")
for i, activo in enumerate(activos):
    print(f"{activo}: {retornos_esperados[i]*100:.1f}% retorno, {desv_estandar[i]*100:.1f}% riesgo")

print(f"\nBeneficio de diversificacion:")
print(f"Riesgo promedio activos: {desv_estandar.mean()*100:.2f}%")
print(f"Riesgo del portafolio: {riesgo_port*100:.2f}%")
print(f"Reduccion: {(desv_estandar.mean() - riesgo_port)*100:.2f}%")

# COMMAND ----------

# DBTITLE 1,Frontera Eficiente Interactiva
# Simular muchos portafolios aleatorios para la frontera eficiente
num_portafolios = 5000
resultados = np.zeros((3, num_portafolios))

np.random.seed(42)
for i in range(num_portafolios):
    pesos = np.random.random(3)
    pesos /= pesos.sum()
    
    ret = retorno_portafolio(pesos, retornos_esperados)
    riesgo = riesgo_portafolio(pesos, cov_matrix)
    sharpe = ratio_sharpe(pesos, retornos_esperados, cov_matrix)
    
    resultados[0, i] = ret
    resultados[1, i] = riesgo
    resultados[2, i] = sharpe

# Crear gráfico interactivo con Plotly
fig = go.Figure()

# Scatter de portafolios simulados (frontera eficiente)
fig.add_trace(go.Scatter(
    x=resultados[1]*100,
    y=resultados[0]*100,
    mode='markers',
    marker=dict(
        size=6,
        color=resultados[2],
        colorscale='Viridis',
        showscale=True,
        colorbar=dict(title='Sharpe Ratio'),
        line=dict(width=0.5, color='white'),
        opacity=0.6
    ),
    name='Portafolios Simulados',
    hovertemplate='<b>Portafolio</b><br>Riesgo: %{x:.2f}%<br>Retorno: %{y:.2f}%<br>Sharpe: %{marker.color:.2f}<extra></extra>'
))

# Marcar activos individuales
for i, activo in enumerate(activos):
    fig.add_trace(go.Scatter(
        x=[desv_estandar[i]*100],
        y=[retornos_esperados[i]*100],
        mode='markers+text',
        marker=dict(
            size=20,
            symbol='star',
            color=UDA_COLORS['danger'],
            line=dict(width=2, color='black')
        ),
        text=[activo],
        textposition='top center',
        name=activo,
        hovertemplate=f'<b>{activo}</b><br>Riesgo: %{{x:.2f}}%<br>Retorno: %{{y:.2f}}%<extra></extra>'
    ))

# Configurar layout
fig.update_layout(
    title=dict(
        text='Frontera Eficiente - Simulación de Portafolios<br><sub>5,000 portafolios aleatorios - Colorear por Sharpe Ratio</sub>',
        font=dict(size=18, family='Arial, sans-serif', color=UDA_COLORS['primary']),
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title=dict(text='Riesgo (Desviación Estándar %)', font=dict(size=14)),
        gridcolor='#E5E5E5',
        showgrid=True
    ),
    yaxis=dict(
        title=dict(text='Retorno Esperado (%)', font=dict(size=14)),
        gridcolor='#E5E5E5',
        showgrid=True
    ),
    plot_bgcolor='white',
    paper_bgcolor='white',
    height=700,
    showlegend=True,
    legend=dict(
        orientation='v',
        yanchor='top',
        y=1,
        xanchor='left',
        x=1.02,
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='#E5E5E5',
        borderwidth=1
    ),
    hovermode='closest'
)

config = {
    'locale': 'es',
    'displayModeBar': True,
    'displaylogo': False,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'frontera_eficiente_portafolios',
        'height': 700,
        'width': 1400,
        'scale': 2
    }
}

fig.show(config=config)

print(f"✓ Simulados {num_portafolios:,} portafolios")
print("💡 TIP: Pasa el mouse sobre los puntos para ver riesgo, retorno y Sharpe Ratio")
print("🎯 Los puntos más amarillos (Sharpe alto) son los mejores portafolios")
print("⭐ Las estrellas rojas muestran los activos individuales")

# COMMAND ----------

# DBTITLE 1,Resumen
# MAGIC %md
# MAGIC ## Resumen
# MAGIC
# MAGIC ### Puntos Clave
# MAGIC 1. Diversificacion reduce riesgo sin sacrificar retorno
# MAGIC 2. Frontera eficiente muestra mejores portafolios
# MAGIC 3. Ratio de Sharpe mide retorno ajustado por riesgo
# MAGIC 4. Correlacion baja entre activos mejora diversificacion
# MAGIC 5. Portafolio optimo depende de aversion al riesgo
# MAGIC
# MAGIC ### Consultas con Genie
# MAGIC * "Optimiza un portafolio de 5 acciones para maximo Sharpe"
# MAGIC * "Grafica la frontera eficiente de estos activos"
# MAGIC * "Calcula el portafolio de minima varianza"
# MAGIC * "Explica como la correlacion afecta el riesgo del portafolio"

# COMMAND ----------

