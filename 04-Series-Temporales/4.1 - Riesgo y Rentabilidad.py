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
# MAGIC ### Notebook 4.1: Riesgo y Rentabilidad
# MAGIC ### 📉 **RETORNO, VOLATILIDAD Y CORRELACIÓN**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introduccion
# MAGIC %md
# MAGIC # 4.1 - Riesgo y Rentabilidad
# MAGIC
# MAGIC ## Objetivo
# MAGIC Analizar riesgo y retorno de inversiones.
# MAGIC
# MAGIC ## Conceptos Clave
# MAGIC * Rentabilidad: Retorno de una inversion
# MAGIC * Riesgo: Variabilidad de retornos
# MAGIC * Desviacion estandar: Medida de riesgo
# MAGIC * Covarianza: Movimiento conjunto
# MAGIC * Correlacion: Relacion entre activos
# MAGIC * Coeficiente de variacion: Riesgo por unidad de retorno

# COMMAND ----------

# DBTITLE 1,Referencias
# MAGIC %md
# MAGIC ## Referencias del Libro
# MAGIC
# MAGIC **Libro**: Finanzas Corporativas - Un Enfoque Latinoamericano (2a ed.)
# MAGIC **Autor**: Guillermo L. Dumrauf
# MAGIC **Capitulo**: 7 - Riesgo y rentabilidad
# MAGIC **Seccion**: 7.1-7.3 (pag. 185-204)
# MAGIC **Ubicacion**: `/Workspace/Shared/Databricks Finance Lab/Libros/Finanzas corporativas.pdf`

# COMMAND ----------

# DBTITLE 1,Librerias
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

UDA_COLORS = {'primary': '#003366', 'accent': '#FF6600', 'success': '#28A745', 'danger': '#DC3545'}

print("✓ Librerías cargadas correctamente (Plotly)")

# COMMAND ----------

# DBTITLE 1,Formulas
# MAGIC %md
# MAGIC ## Medidas de Riesgo y Rentabilidad
# MAGIC
# MAGIC ### Rentabilidad esperada
# MAGIC E(R) = suma(pi * ri)
# MAGIC
# MAGIC ### Varianza
# MAGIC Var(R) = suma[pi * (ri - E(R))^2]
# MAGIC
# MAGIC ### Desviacion estandar
# MAGIC SD(R) = sqrt(Var(R))
# MAGIC
# MAGIC ### Coeficiente de variacion
# MAGIC CV = SD(R) / E(R)
# MAGIC
# MAGIC ### Covarianza
# MAGIC Cov(Ra, Rb) = E[(Ra - E(Ra)) * (Rb - E(Rb))]
# MAGIC
# MAGIC ### Correlacion
# MAGIC Corr(Ra, Rb) = Cov(Ra, Rb) / (SD(Ra) * SD(Rb))

# COMMAND ----------

# DBTITLE 1,Datos Ejemplo
# Retornos historicos de dos activos (ejemplo)
np.random.seed(42)
periodos = 50

retornos_a = np.random.normal(0.10, 0.15, periodos)
retornos_b = np.random.normal(0.08, 0.10, periodos)

df_retornos = pd.DataFrame({
    'Activo A': retornos_a,
    'Activo B': retornos_b
})

print("Datos de retornos creados")
print(df_retornos.head())

# COMMAND ----------

# DBTITLE 1,Analisis de Riesgo
# Calcular metricas
retorno_a = df_retornos['Activo A'].mean()
retorno_b = df_retornos['Activo B'].mean()

riesgo_a = df_retornos['Activo A'].std()
riesgo_b = df_retornos['Activo B'].std()

cv_a = riesgo_a / retorno_a
cv_b = riesgo_b / retorno_b

print("ANALISIS DE RIESGO Y RENTABILIDAD")
print("="*50)
print(f"\nActivo A:")
print(f"  Retorno promedio: {retorno_a*100:.2f}%")
print(f"  Riesgo (SD): {riesgo_a*100:.2f}%")
print(f"  CV: {cv_a:.2f}")
print(f"\nActivo B:")
print(f"  Retorno promedio: {retorno_b*100:.2f}%")
print(f"  Riesgo (SD): {riesgo_b*100:.2f}%")
print(f"  CV: {cv_b:.2f}")

# COMMAND ----------

# DBTITLE 1,Covarianza y Correlacion
# Calcular covarianza y correlacion
covarianza = df_retornos['Activo A'].cov(df_retornos['Activo B'])
correlacion = df_retornos['Activo A'].corr(df_retornos['Activo B'])

print("\nRELACION ENTRE ACTIVOS")
print("="*50)
print(f"Covarianza: {covarianza:.6f}")
print(f"Correlacion: {correlacion:.4f}")

if correlacion > 0.7:
    print("\nInterpretacion: Correlacion ALTA positiva")
elif correlacion > 0.3:
    print("\nInterpretacion: Correlacion MODERADA positiva")
elif correlacion > -0.3:
    print("\nInterpretacion: Correlacion BAJA o nula")
else:
    print("\nInterpretacion: Correlacion NEGATIVA")

# COMMAND ----------

# DBTITLE 1,Visualizacion Interactiva
# Crear subplots interactivos con Plotly
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=('Riesgo vs Retorno Esperado', 
                    f'Correlación entre Activos: {correlacion:.2f}'),
    specs=[[{'type': 'scatter'}, {'type': 'scatter'}]],
    horizontal_spacing=0.12
)

# Subplot 1: Riesgo vs Retorno
fig.add_trace(
    go.Scatter(
        x=[riesgo_a*100],
        y=[retorno_a*100],
        mode='markers+text',
        marker=dict(size=20, color=UDA_COLORS['primary'], 
                   line=dict(width=2, color='white')),
        text=['Activo A'],
        textposition='top center',
        name='Activo A',
        hovertemplate='<b>Activo A</b><br>Riesgo: %{x:.2f}%<br>Retorno: %{y:.2f}%<extra></extra>'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=[riesgo_b*100],
        y=[retorno_b*100],
        mode='markers+text',
        marker=dict(size=20, color=UDA_COLORS['danger'], 
                   line=dict(width=2, color='white')),
        text=['Activo B'],
        textposition='top center',
        name='Activo B',
        hovertemplate='<b>Activo B</b><br>Riesgo: %{x:.2f}%<br>Retorno: %{y:.2f}%<extra></extra>'
    ),
    row=1, col=1
)

# Subplot 2: Dispersión (Correlación)
fig.add_trace(
    go.Scatter(
        x=df_retornos['Activo A']*100,
        y=df_retornos['Activo B']*100,
        mode='markers',
        marker=dict(size=8, color=UDA_COLORS['accent'], opacity=0.6,
                   line=dict(width=1, color='white')),
        name='Retornos Históricos',
        hovertemplate='Activo A: %{x:.2f}%<br>Activo B: %{y:.2f}%<extra></extra>',
        showlegend=False
    ),
    row=1, col=2
)

# Actualizar ejes
fig.update_xaxes(title_text='Riesgo (Desv. Est. %)', gridcolor='#E5E5E5', row=1, col=1)
fig.update_yaxes(title_text='Retorno Esperado (%)', gridcolor='#E5E5E5', row=1, col=1)
fig.update_xaxes(title_text='Retornos Activo A (%)', gridcolor='#E5E5E5', row=1, col=2)
fig.update_yaxes(title_text='Retornos Activo B (%)', gridcolor='#E5E5E5', row=1, col=2)

# Configurar layout general
fig.update_layout(
    title=dict(
        text='Análisis de Riesgo-Retorno y Correlación',
        font=dict(size=18, family='Arial, sans-serif', color=UDA_COLORS['primary']),
        x=0.5,
        xanchor='center'
    ),
    height=600,
    plot_bgcolor='white',
    paper_bgcolor='white',
    showlegend=True,
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=-0.15,
        xanchor='center',
        x=0.5
    )
)

config = {
    'locale': 'es',
    'displayModeBar': True,
    'displaylogo': False,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'riesgo_retorno_correlacion',
        'height': 600,
        'width': 1400,
        'scale': 2
    }
}

fig.show(config=config)

print("✓ Visualización interactiva generada con Plotly")
print("💡 TIP: Pasa el mouse sobre los puntos para ver detalles exactos")

# COMMAND ----------

# DBTITLE 1,Resumen
# MAGIC %md
# MAGIC ## Resumen
# MAGIC
# MAGIC ### Puntos Clave
# MAGIC 1. Mayor retorno esperado implica mayor riesgo
# MAGIC 2. Desviacion estandar mide volatilidad
# MAGIC 3. CV permite comparar riesgos relativos
# MAGIC 4. Correlacion negativa ayuda a diversificar
# MAGIC 5. Covarianza mide movimiento conjunto
# MAGIC
# MAGIC ### Consultas con Genie
# MAGIC * "Calcula riesgo y retorno de estos datos historicos"
# MAGIC * "Compara el CV de 3 activos diferentes"
# MAGIC * "Explica por que la diversificacion reduce riesgo"
# MAGIC * "Grafica la frontera eficiente de un portafolio"

# COMMAND ----------

