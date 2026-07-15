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
# MAGIC ### Módulo 01: Fundamentos de Finanzas
# MAGIC ### Notebook 1.1: Valor del Dinero en el Tiempo
# MAGIC ### 📈 **VALOR PRESENTE Y FUTURO**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción
# MAGIC %md
# MAGIC # 1.1 - Valor del Dinero en el Tiempo
# MAGIC
# MAGIC ## Objetivo del Módulo
# MAGIC Comprender el concepto fundamental de que el dinero tiene un valor temporal: un peso hoy vale más que un peso mañana.
# MAGIC
# MAGIC ## Conceptos Clave
# MAGIC * **Valor Presente (VP)**: Valor actual de un flujo de efectivo futuro
# MAGIC * **Valor Futuro (VF)**: Valor de una inversión en una fecha futura
# MAGIC * **Tasa de interés (r)**: Rendimiento o costo del dinero en el tiempo
# MAGIC * **Períodos (n)**: Número de períodos de capitalización
# MAGIC
# MAGIC ## Fórmulas Fundamentales
# MAGIC
# MAGIC ### Valor Futuro
# MAGIC $$VF = VP \times (1 + r)^n$$
# MAGIC
# MAGIC ### Valor Presente
# MAGIC $$VP = \frac{VF}{(1 + r)^n}$$

# COMMAND ----------

# DBTITLE 1,Referencias del Libro
# MAGIC %md
# MAGIC ---
# MAGIC
# MAGIC ## 📚 Referencias del Libro de Texto
# MAGIC
# MAGIC **Libro**: Finanzas Corporativas - Un Enfoque Latinoamericano (2ª ed.)
# MAGIC **Autor**: Guillermo L. Dumrauf
# MAGIC **Capítulo**: 5 - El valor tiempo del dinero (pág. 123-146)
# MAGIC **Ubicación**: `/Workspace/Users/cortega@uda.edu.ar/Databricks Finance Lab/Libros/Finanzas corporativas.pdf`
# MAGIC
# MAGIC ### 📝 Temas del capítulo 5 que cubre este notebook:
# MAGIC
# MAGIC * **Sección 5.1**: Concepto y función del valor futuro (pág. 124)
# MAGIC * **Sección 5.2**: Concepto y función del valor actual (pág. 125)
# MAGIC * **Sección 5.3**: Tasas de interés - nominal, efectiva, equivalente (pág. 126-131)
# MAGIC * **Sección 5.4**: Calcular el valor de un flujo de efectivo (pág. 132-143)
# MAGIC
# MAGIC ### 🎯 Cómo usar este material:
# MAGIC
# MAGIC 1. **Leer primero**: Capítulo 5 del libro (páginas 123-146) para teoría completa
# MAGIC 2. **Ejecutar**: Las celdas de este notebook para ver implementaciones en Python
# MAGIC 3. **Contrastar**: Ejercicios del libro vs. ejemplos con código
# MAGIC 4. **Preguntar a Genie**: "Explica la diferencia entre tasa nominal y efectiva del capítulo 5" o "Crea ejercicios adicionales sobre valor presente"
# MAGIC
# MAGIC ### 💡 Ejercicios del libro recomendados:
# MAGIC * Problemas al final del capítulo 5 (pág. 144-146)
# MAGIC * Resuelve algunos manualmente, luego verifícalos con las funciones Python de este notebook
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Funciones Básicas - Valor Presente y Futuro
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

UDA_COLORS = {'primary': '#003366', 'accent': '#FF6600', 'success': '#28A745', 'danger': '#DC3545'}

def valor_futuro(vp, r, n):
    """
    Calcula el Valor Futuro de una inversión
    
    Parámetros:
    vp: Valor Presente (monto inicial)
    r: Tasa de interés por período (decimal, ej: 0.05 para 5%)
    n: Número de períodos
    
    Retorna:
    Valor Futuro
    """
    return vp * (1 + r) ** n

def valor_presente(vf, r, n):
    """
    Calcula el Valor Presente de un flujo futuro
    
    Parámetros:
    vf: Valor Futuro
    r: Tasa de descuento por período (decimal)
    n: Número de períodos
    
    Retorna:
    Valor Presente
    """
    return vf / (1 + r) ** n

print("✓ Funciones definidas correctamente")

# COMMAND ----------

# DBTITLE 1,Ejemplo 1 - Inversión Simple
# MAGIC %md
# MAGIC ## Ejemplo 1: Inversión en Plazo Fijo
# MAGIC
# MAGIC **Problema**: Invertimos $10,000 en un plazo fijo a 3 años con una tasa anual del 8%. ¿Cuánto tendremos al final?

# COMMAND ----------

# DBTITLE 1,Solución Ejemplo 1
# Datos
vp = 10000  # Valor presente
r = 0.08    # Tasa anual 8%
n = 3       # Años

# Calcular valor futuro
vf = valor_futuro(vp, r, n)

print(f"Inversión inicial: ${vp:,.2f}")
print(f"Tasa de interés: {r*100}% anual")
print(f"Plazo: {n} años")
print(f"\nValor futuro: ${vf:,.2f}")
print(f"Interés ganado: ${vf - vp:,.2f}")

# COMMAND ----------

# DBTITLE 1,Ejemplo 2 - Valor Presente
# MAGIC %md
# MAGIC ## Ejemplo 2: ¿Cuánto Debo Invertir Hoy?
# MAGIC
# MAGIC **Problema**: Necesitamos $50,000 dentro de 5 años para un proyecto. Si la tasa de interés es 6% anual, ¿cuánto debemos invertir hoy?

# COMMAND ----------

# DBTITLE 1,Solución Ejemplo 2
# Datos
vf_objetivo = 50000  # Valor futuro deseado
r = 0.06             # Tasa anual 6%
n = 5                # Años

# Calcular valor presente necesario
vp_necesario = valor_presente(vf_objetivo, r, n)

print(f"Objetivo en {n} años: ${vf_objetivo:,.2f}")
print(f"Tasa de interés: {r*100}% anual")
print(f"\nMonto a invertir hoy: ${vp_necesario:,.2f}")
print(f"Interés que se ganará: ${vf_objetivo - vp_necesario:,.2f}")

# COMMAND ----------

# DBTITLE 1,Visualización - Crecimiento en el Tiempo
# MAGIC %md
# MAGIC ## Visualización: Crecimiento de una Inversión
# MAGIC
# MAGIC Veamos cómo crece una inversión de $10,000 a diferentes tasas de interés durante 10 años:

# COMMAND ----------

# DBTITLE 1,Gráfico de Crecimiento
# Parámetros
vp_inicial = 10000
anios = np.arange(0, 11)  # 0 a 10 años
tasas = [0.04, 0.06, 0.08, 0.10]  # 4%, 6%, 8%, 10%
colores = [UDA_COLORS['primary'], UDA_COLORS['success'], UDA_COLORS['accent'], UDA_COLORS['danger']]

# Crear gráfico interactivo con Plotly
fig = go.Figure()

# Agregar una línea por cada tasa de interés
for i, tasa in enumerate(tasas):
    valores = [valor_futuro(vp_inicial, tasa, n) for n in anios]
    fig.add_trace(go.Scatter(
        x=anios,
        y=valores,
        name=f'{tasa*100:.0f}% anual',
        mode='lines+markers',
        line=dict(color=colores[i], width=2.5),
        marker=dict(size=8),
        hovertemplate=f'<b>{tasa*100:.0f}% anual</b><br>' +
                     'Año: %{x}<br>' +
                     'Valor: $%{y:,.2f}<extra></extra>'
    ))

# Línea de inversión inicial
fig.add_hline(
    y=vp_inicial, 
    line_dash='dash', 
    line_color='gray',
    annotation_text='Inversión inicial: $10,000',
    annotation_position='right'
)

# Configurar layout
fig.update_layout(
    title=dict(
        text='Crecimiento de $10,000 a Diferentes Tasas de Interés',
        font=dict(size=18, family='Arial, sans-serif', color=UDA_COLORS['primary']),
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title=dict(text='Años', font=dict(size=14)),
        gridcolor='#E5E5E5',
        showgrid=True
    ),
    yaxis=dict(
        title=dict(text='Valor de la Inversión ($)', font=dict(size=14)),
        gridcolor='#E5E5E5',
        showgrid=True,
        tickformat='$,.0f'
    ),
    plot_bgcolor='white',
    paper_bgcolor='white',
    height=600,
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

# Configuración en español
config = {
    'locale': 'es',
    'displayModeBar': True,
    'displaylogo': False,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'crecimiento_inversion',
        'height': 600,
        'width': 1200,
        'scale': 2
    }
}

fig.show(config=config)

print("\n📊 Observación: A mayor tasa de interés, mayor es el efecto del interés compuesto")
print("💡 TIP: Pasa el mouse sobre las líneas para ver valores exactos")

# COMMAND ----------

# DBTITLE 1,Ejercicios Prácticos
# MAGIC %md
# MAGIC ## 💪 Ejercicios Prácticos
# MAGIC
# MAGIC ### Ejercicio 1
# MAGIC Una empresa invierte $25,000 a una tasa del 7% anual durante 4 años. Calcule:
# MAGIC a) El valor futuro de la inversión
# MAGIC b) El interés total ganado
# MAGIC
# MAGIC ### Ejercicio 2
# MAGIC Si queremos tener $100,000 dentro de 8 años y la tasa de interés es del 5.5% anual, ¿cuánto debemos invertir hoy?
# MAGIC
# MAGIC ### Ejercicio 3
# MAGIC Compare dos inversiones de $15,000 durante 6 años:
# MAGIC * Opción A: 6% anual
# MAGIC * Opción B: 7% anual
# MAGIC
# MAGIC ¿Cuál es la diferencia en el valor futuro?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **💡 Tip**: Use las funciones `valor_futuro()` y `valor_presente()` definidas anteriormente para resolver estos ejercicios.

# COMMAND ----------

# DBTITLE 1,Espacio para Ejercicios
# Resuelva los ejercicios aquí
# Ejercicio 1


# Ejercicio 2


# Ejercicio 3


# COMMAND ----------

# DBTITLE 1,Análisis con SQL
# MAGIC %md
# MAGIC ## 🔍 Análisis con SQL
# MAGIC
# MAGIC Creemos un dataset de ejemplo con diferentes escenarios de inversión y analicemos con SQL:

# COMMAND ----------

# DBTITLE 1,Crear Dataset de Inversiones
# Generar dataset de escenarios de inversión
escenarios = []

for inversion in [5000, 10000, 25000, 50000]:
    for tasa in [0.04, 0.06, 0.08, 0.10, 0.12]:
        for periodo in [1, 3, 5, 10, 15, 20]:
            vf = valor_futuro(inversion, tasa, periodo)
            interes = vf - inversion
            escenarios.append({
                'inversion_inicial': inversion,
                'tasa_anual': tasa,
                'periodo_anios': periodo,
                'valor_futuro': round(vf, 2),
                'interes_ganado': round(interes, 2),
                'retorno_porcentual': round((vf/inversion - 1) * 100, 2)
            })

df_inversiones = pd.DataFrame(escenarios)

# Crear vista temporal para SQL
df_inversiones.createOrReplaceTempView("inversiones")

print(f"✓ Dataset creado: {len(df_inversiones)} escenarios de inversión")
print("\nPrimeras filas:")
df_inversiones.head(10)

# COMMAND ----------

# DBTITLE 1,Consulta SQL - Top Inversiones
# MAGIC %sql
# MAGIC -- ¿Cuáles son las 10 mejores inversiones en términos de retorno absoluto?
# MAGIC SELECT 
# MAGIC   inversion_inicial,
# MAGIC   tasa_anual * 100 as tasa_porcentaje,
# MAGIC   periodo_anios,
# MAGIC   valor_futuro,
# MAGIC   interes_ganado,
# MAGIC   retorno_porcentual
# MAGIC FROM inversiones
# MAGIC ORDER BY interes_ganado DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# DBTITLE 1,Consulta SQL - Análisis por Período
# MAGIC %sql
# MAGIC -- Comparar el efecto del tiempo: promedio de retorno por período
# MAGIC SELECT 
# MAGIC   periodo_anios,
# MAGIC   COUNT(*) as num_escenarios,
# MAGIC   ROUND(AVG(retorno_porcentual), 2) as retorno_promedio_pct,
# MAGIC   ROUND(MIN(retorno_porcentual), 2) as retorno_minimo_pct,
# MAGIC   ROUND(MAX(retorno_porcentual), 2) as retorno_maximo_pct
# MAGIC FROM inversiones
# MAGIC GROUP BY periodo_anios
# MAGIC ORDER BY periodo_anios;

# COMMAND ----------

# DBTITLE 1,Conclusiones y Próximos Pasos
# MAGIC %md
# MAGIC ## 📚 Resumen y Conclusiones
# MAGIC
# MAGIC ### Conceptos Aprendidos
# MAGIC 1. El dinero tiene valor temporal debido a:
# MAGIC    * Oportunidades de inversión
# MAGIC    * Inflación
# MAGIC    * Riesgo y preferencia por liquidez
# MAGIC
# MAGIC 2. Las fórmulas de VP y VF son fundamentales para:
# MAGIC    * Evaluar inversiones
# MAGIC    * Comparar alternativas financieras
# MAGIC    * Planificación financiera
# MAGIC
# MAGIC 3. El interés compuesto genera crecimiento exponencial
# MAGIC
# MAGIC ### 🚀 Próximos Módulos
# MAGIC * **1.2 - Tasas de Interés y Conversiones**: Tasas nominales vs efectivas, capitalización continua
# MAGIC * **1.3 - Anualidades y Amortización**: Flujos de caja múltiples, préstamos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🤖 Interacción con Genie Code
# MAGIC Puedes preguntarle a Genie:
# MAGIC * "Crea un escenario con inversión de $X a tasa Y% durante Z años"
# MAGIC * "Compara dos inversiones con diferentes tasas"
# MAGIC * "Visualiza el efecto del interés compuesto en 15 años"
# MAGIC * "¿Qué inversión inicial necesito para tener $X en Y años al Z%?"