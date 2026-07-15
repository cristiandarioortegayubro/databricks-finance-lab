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
# MAGIC ### Notebook 1.2: Tasas de Interés y Conversiones
# MAGIC ### 💹 **TASA NOMINAL, EFECTIVA Y REAL**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción
# MAGIC %md
# MAGIC # 1.2 - Tasas de Interés y Conversiones
# MAGIC
# MAGIC ## Objetivo del Módulo
# MAGIC Comprender los diferentes tipos de tasas de interés y cómo convertir entre ellas.
# MAGIC
# MAGIC ## Conceptos Clave
# MAGIC * **Tasa Nominal**: Tasa anual declarada sin considerar capitalización
# MAGIC * **Tasa Proporcional**: División simple de la tasa nominal por el número de períodos
# MAGIC * **Tasa Efectiva**: Tasa real que incorpora el efecto de la capitalización
# MAGIC * **Tasa Equivalente**: Tasas con diferentes períodos que producen el mismo resultado
# MAGIC * **Tasa Real**: Tasa ajustada por inflación
# MAGIC * **Tasa de Descuento Comercial**: Usada en instrumentos de corto plazo
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Referencias del Libro
# MAGIC %md
# MAGIC ## 📚 Referencias del Libro de Texto
# MAGIC
# MAGIC **Libro**: Finanzas Corporativas - Un Enfoque Latinoamericano (2ª ed.)
# MAGIC **Autor**: Guillermo L. Dumrauf
# MAGIC **Capítulo**: 5 - El valor tiempo del dinero
# MAGIC **Sección**: 5.3 - Tasas de interés (pág. 126-132)
# MAGIC **Ubicación**: `/Workspace/Users/cortega@uda.edu.ar/Databricks Finance Lab/Libros/Finanzas corporativas.pdf`
# MAGIC
# MAGIC ### 📝 Contenido cubierto:
# MAGIC
# MAGIC * **Pág. 126-127**: Tasa nominal y tasa proporcional
# MAGIC * **Pág. 127-129**: La tasa efectiva
# MAGIC * **Pág. 129-131**: La tasa equivalente
# MAGIC * **Pág. 131**: Tasa de interés real en contexto inflacionario
# MAGIC * **Pág. 131-132**: Tasa de descuento comercial
# MAGIC * **Pág. 132**: Conversión entre tasa de descuento y tasa vencida
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Funciones de Conversión de Tasas
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

UDA_COLORS = {'primary': '#003366', 'accent': '#FF6600', 'success': '#28A745', 'danger': '#DC3545'}

def tasa_proporcional(tasa_nominal, periodos_por_anio):
    """
    Calcula la tasa proporcional (división simple)
    
    Parámetros:
    tasa_nominal: Tasa nominal anual (decimal)
    periodos_por_anio: Número de períodos (12=mensual, 4=trimestral, 2=semestral)
    
    Retorna:
    Tasa proporcional por período
    """
    return tasa_nominal / periodos_por_anio

def tasa_efectiva(tasa_nominal, periodos_por_anio):
    """
    Calcula la tasa efectiva anual (TEA)
    
    TEA = (1 + r_periodo)^n - 1
    donde r_periodo = tasa_nominal / periodos_por_anio
    """
    r_periodo = tasa_nominal / periodos_por_anio
    tea = (1 + r_periodo)**periodos_por_anio - 1
    return tea

def tasa_equivalente(tasa_periodo, periodos_origen, periodos_destino):
    """
    Convierte una tasa de un período a otro período equivalente
    
    Ejemplo: tasa mensual a tasa trimestral
    
    Parámetros:
    tasa_periodo: Tasa en el período de origen
    periodos_origen: Períodos por año del origen (12 si es mensual)
    periodos_destino: Períodos por año del destino (4 si es trimestral)
    
    Retorna:
    Tasa equivalente en el período destino
    """
    # Primero calcular TEA
    tea = (1 + tasa_periodo)**periodos_origen - 1
    
    # Luego convertir a la nueva frecuencia
    tasa_nueva = (1 + tea)**(1/periodos_destino) - 1
    
    return tasa_nueva

def tasa_real(tasa_nominal, inflacion):
    """
    Calcula la tasa de interés real ajustada por inflación
    
    Fórmula de Fisher:
    (1 + r_real) = (1 + r_nominal) / (1 + inflación)
    
    Parámetros:
    tasa_nominal: Tasa nominal (decimal)
    inflacion: Tasa de inflación (decimal)
    
    Retorna:
    Tasa real
    """
    return ((1 + tasa_nominal) / (1 + inflacion)) - 1

def descuento_a_vencida(tasa_descuento, n=1):
    """
    Convierte tasa de descuento comercial a tasa vencida
    
    r_vencida = d / (1 - d*n)
    
    Parámetros:
    tasa_descuento: Tasa de descuento comercial (decimal)
    n: Número de períodos
    
    Retorna:
    Tasa vencida equivalente
    """
    return tasa_descuento / (1 - tasa_descuento * n)

print("✓ Funciones de conversión de tasas definidas")

# COMMAND ----------

# DBTITLE 1,Ejemplo 1: Tasa Nominal vs Efectiva
# MAGIC %md
# MAGIC ## Ejemplo 1: Tasa Nominal vs Tasa Efectiva
# MAGIC
# MAGIC **Problema**: Un banco ofrece una tarjeta de crédito con tasa nominal anual (TNA) del 36% con capitalización mensual.
# MAGIC
# MAGIC ¿Cuál es la **Tasa Efectiva Anual (TEA)** real que pagarás?

# COMMAND ----------

# DBTITLE 1,Solución Ejemplo 1
# Datos
tna = 0.36  # 36% anual
periodos = 12  # capitalización mensual

# Tasa proporcional (simple)
r_proporcional = tasa_proporcional(tna, periodos)

# Tasa efectiva anual (con capitalización)
tea = tasa_efectiva(tna, periodos)

print(f"Tasa Nominal Anual (TNA): {tna*100}%")
print(f"Capitalización: Mensual ({periodos} veces al año)")
print(f"\nTasa proporcional mensual: {r_proporcional*100:.4f}%")
print(f"  (Cálculo simple: {tna*100}% / {periodos} = {r_proporcional*100:.4f}%)")
print(f"\nTasa Efectiva Anual (TEA): {tea*100:.2f}%")
print(f"\n💡 Diferencia: {(tea - tna)*100:.2f} puntos porcentuales")
print(f"   La TEA es MAYOR que la TNA debido al efecto de la capitalización mensual.")
print(f"\n   Si pides prestado $1,000:")
print(f"   - Con TNA simple: deberías ${1000 * (1 + tna):,.2f}")
print(f"   - Con TEA (real): debes ${1000 * (1 + tea):,.2f}")
print(f"   - Diferencia: ${1000 * (tea - tna):,.2f} más")

# COMMAND ----------

# DBTITLE 1,Ejemplo 2: Tasas Equivalentes
# MAGIC %md
# MAGIC ## Ejemplo 2: Conversión entre Tasas Equivalentes
# MAGIC
# MAGIC **Problema**: Tienes una tasa mensual del 2.5%. ¿Cuáles son las tasas equivalentes:
# MAGIC * Trimestral
# MAGIC * Semestral
# MAGIC * Anual

# COMMAND ----------

# DBTITLE 1,Solución Ejemplo 2
# Tasa mensual dada
r_mensual = 0.025  # 2.5% mensual

# Convertir a diferentes períodos
r_trimestral = tasa_equivalente(r_mensual, 12, 4)  # mensual a trimestral
r_semestral = tasa_equivalente(r_mensual, 12, 2)   # mensual a semestral
r_anual = tasa_equivalente(r_mensual, 12, 1)       # mensual a anual (TEA)

print(f"Tasa de partida: {r_mensual*100}% mensual")
print(f"\nTasas equivalentes:")
print(f"  Trimestral:  {r_trimestral*100:.4f}%")
print(f"  Semestral:   {r_semestral*100:.4f}%")
print(f"  Anual (TEA): {r_anual*100:.4f}%")

# Verificación: todas producen el mismo resultado en 1 año
inversion = 1000

print(f"\n✓ Verificación con inversión de ${inversion:,.2f}:")
print(f"  Con tasa mensual ({r_mensual*100}% x 12): ${inversion * (1 + r_mensual)**12:,.2f}")
print(f"  Con tasa trimestral ({r_trimestral*100:.4f}% x 4): ${inversion * (1 + r_trimestral)**4:,.2f}")
print(f"  Con tasa semestral ({r_semestral*100:.4f}% x 2): ${inversion * (1 + r_semestral)**2:,.2f}")
print(f"  Con tasa anual ({r_anual*100:.4f}% x 1): ${inversion * (1 + r_anual)**1:,.2f}")
print(f"\n💡 Todas las tasas equivalentes producen exactamente el mismo resultado final")

# COMMAND ----------

# DBTITLE 1,Ejemplo 3: Tasa Real vs Inflación
# MAGIC %md
# MAGIC ## Ejemplo 3: Tasa Real Ajustada por Inflación
# MAGIC
# MAGIC **Problema**: Un plazo fijo ofrece 12% anual. La inflación proyectada es 8% anual.
# MAGIC
# MAGIC ¿Cuál es tu **ganancia real** en poder adquisitivo?
# MAGIC
# MAGIC **Fórmula de Fisher**:
# MAGIC $$(1 + r_{real}) = \frac{1 + r_{nominal}}{1 + inflación}$$

# COMMAND ----------

# DBTITLE 1,Solución Ejemplo 3
# Datos
r_nominal = 0.12  # 12% anual
inflacion = 0.08  # 8% anual

# Calcular tasa real
r_real = tasa_real(r_nominal, inflacion)

# Aproximación simple (incorrecta pero usada a veces)
r_aprox = r_nominal - inflacion

print(f"Tasa nominal del plazo fijo: {r_nominal*100}%")
print(f"Inflación esperada: {inflacion*100}%")
print(f"\nTasa real (Fórmula de Fisher): {r_real*100:.2f}%")
print(f"Aproximación simple (incompleta): {r_aprox*100:.2f}%")
print(f"\n💡 La diferencia: {(r_real - r_aprox)*100:.2f} puntos porcentuales")

# Ejemplo práctico
inversion = 10000
vf_nominal = inversion * (1 + r_nominal)
vf_real = inversion * (1 + r_real)
perdida_inflacion = inversion * inflacion

print(f"\n📊 Ejemplo con inversión de ${inversion:,.2f}:")
print(f"\n  Al año tendrás (nominal): ${vf_nominal:,.2f}")
print(f"  Pero la inflación te quitó: ${perdida_inflacion:,.2f} de poder adquisitivo")
print(f"  Tu ganancia real es solo: ${inversion * r_real:,.2f}")
print(f"\n  Es decir, tu ${vf_nominal:,.2f} solo te permite comprar lo que hoy comprarías con ${vf_real:,.2f}")

# COMMAND ----------

# DBTITLE 1,Visualización: Efecto de la Capitalización
# MAGIC %md
# MAGIC ## 📊 Visualización: Efecto de la Frecuencia de Capitalización
# MAGIC
# MAGIC ¿Cómo afecta la frecuencia de capitalización a la tasa efectiva?

# COMMAND ----------

# DBTITLE 1,Gráfico TEA vs Frecuencia
# Comparar diferentes frecuencias de capitalización
tna_base = 0.24  # 24% nominal anual

frecuencias = {
    'Anual': 1,
    'Semestral': 2,
    'Trimestral': 4,
    'Mensual': 12,
    'Semanal': 52,
    'Diaria': 365
}

resultados = []

for nombre, n in frecuencias.items():
    tea = tasa_efectiva(tna_base, n)
    resultados.append({
        'Frecuencia': nombre,
        'Períodos': n,
        'TEA (%)': tea * 100
    })

df_resultados = pd.DataFrame(resultados)

# Crear gráficos interactivos con Plotly
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=('TEA según Frecuencia de Capitalización',
                    'Convergencia con Mayor Frecuencia'),
    specs=[[{'type': 'bar'}, {'type': 'scatter'}]],
    horizontal_spacing=0.12
)

# Gráfico 1: Barras
fig.add_trace(
    go.Bar(
        x=df_resultados['Frecuencia'],
        y=df_resultados['TEA (%)'],
        marker=dict(color=UDA_COLORS['primary'], line=dict(width=1, color='white')),
        text=[f'{v:.2f}%' for v in df_resultados['TEA (%)']],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>TEA: %{y:.2f}%<extra></extra>',
        showlegend=False,
        name='TEA'
    ),
    row=1, col=1
)

# Línea de TNA en gráfico 1
fig.add_hline(
    y=tna_base*100,
    line_dash='dash',
    line_color=UDA_COLORS['danger'],
    annotation_text=f'TNA = {tna_base*100}%',
    annotation_position='right',
    row=1, col=1
)

# Gráfico 2: Línea con escala log en X
fig.add_trace(
    go.Scatter(
        x=df_resultados['Períodos'],
        y=df_resultados['TEA (%)'],
        mode='lines+markers',
        line=dict(color=UDA_COLORS['success'], width=2.5),
        marker=dict(size=10),
        hovertemplate='<b>%{text}</b><br>Períodos/año: %{x}<br>TEA: %{y:.2f}%<extra></extra>',
        text=df_resultados['Frecuencia'],
        showlegend=False,
        name='TEA'
    ),
    row=1, col=2
)

# Línea de TNA en gráfico 2
fig.add_hline(
    y=tna_base*100,
    line_dash='dash',
    line_color=UDA_COLORS['danger'],
    annotation_text=f'TNA = {tna_base*100}%',
    annotation_position='right',
    row=1, col=2
)

# Actualizar layout general
fig.update_layout(
    title=dict(
        text=f'Efecto de la Frecuencia de Capitalización (TNA = {tna_base*100}%)',
        font=dict(size=18, family='Arial, sans-serif', color=UDA_COLORS['primary']),
        x=0.5,
        xanchor='center'
    ),
    height=600,
    showlegend=False,
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Actualizar ejes
fig.update_xaxes(title_text='Frecuencia de Capitalización', gridcolor='#E5E5E5', row=1, col=1)
fig.update_yaxes(title_text='Tasa Efectiva Anual (%)', gridcolor='#E5E5E5', row=1, col=1)
fig.update_xaxes(
    title_text='Número de Períodos por Año (escala log)',
    type='log',
    gridcolor='#E5E5E5',
    row=1, col=2
)
fig.update_yaxes(title_text='TEA (%)', gridcolor='#E5E5E5', row=1, col=2)

# Configuración en español
config = {
    'locale': 'es',
    'displayModeBar': True,
    'displaylogo': False,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'tea_vs_frecuencia',
        'height': 600,
        'width': 1400,
        'scale': 2
    }
}

fig.show(config=config)

print("\n📊 Tabla de resultados:")
print(df_resultados.to_string(index=False))

print(f"\n💡 Observaciones:")
print(f"1. La TEA SIEMPRE es mayor que la TNA cuando hay capitalización")
print(f"2. A mayor frecuencia, mayor TEA (pero el efecto disminuye)")
print(f"3. De mensual a diaria solo aumenta {(df_resultados.iloc[-1]['TEA (%)'] - df_resultados.iloc[3]['TEA (%)']):,.2f} puntos")
print(f"4. Capitalización continua (límite): {(np.exp(tna_base) - 1)*100:.2f}%")
print("\n💡 TIP: Pasa el mouse sobre las barras/líneas para ver detalles exactos")

# COMMAND ----------

# DBTITLE 1,Ejemplo 4: Tasa de Descuento Comercial
# MAGIC %md
# MAGIC ## Ejemplo 4: Tasa de Descuento Comercial
# MAGIC
# MAGIC **Problema**: Un pagaré se descuenta con tasa del 18% anual a 90 días.
# MAGIC
# MAGIC ¿Cuál es la tasa de interés vencida equivalente?

# COMMAND ----------

# DBTITLE 1,Solución Ejemplo 4
# Datos
d = 0.18  # 18% anual de descuento
n_dias = 90
n_anios = 90/360  # Año comercial de 360 días

# Tasa de descuento por el período
d_periodo = d * n_anios

# Convertir a tasa vencida
r_vencida = descuento_a_vencida(d_periodo)

# Anualizar
r_vencida_anual = r_vencida / n_anios

print(f"Tasa de descuento: {d*100}% anual")
print(f"Período: {n_dias} días ({n_anios*360:.0f} días)")
print(f"\nTasa de descuento para {n_dias} días: {d_periodo*100:.2f}%")
print(f"Tasa vencida equivalente para {n_dias} días: {r_vencida*100:.2f}%")
print(f"Tasa vencida anual: {r_vencida_anual*100:.2f}%")

# Ejemplo práctico
vn = 10000  # Valor nominal del pagaré

# Con descuento
importe_descontado = vn * (1 - d_periodo)

# Verificación con tasa vencida
vf_con_vencida = importe_descontado * (1 + r_vencida)

print(f"\n💰 Ejemplo práctico con pagaré de ${vn:,.2f}:")
print(f"\n  Descuento aplicado: ${vn * d_periodo:,.2f}")
print(f"  Recibes hoy: ${importe_descontado:,.2f}")
print(f"  Pagas al vencimiento: ${vn:,.2f}")
print(f"\n  Interés efectivo pagado: ${vn - importe_descontado:,.2f}")
print(f"  Tasa de interés sobre lo recibido: {r_vencida*100:.2f}%")
print(f"\n✓ Verificación: ${importe_descontado:,.2f} × (1 + {r_vencida*100:.2f}%) = ${vf_con_vencida:,.2f}")

# COMMAND ----------

# DBTITLE 1,Comparación de Tasas
# MAGIC %md
# MAGIC ## 📊 Comparación: ¿Qué Tasa es Mejor?
# MAGIC
# MAGIC Cuando comparas productos financieros, es crucial convertir todas las tasas a la **misma base** (TEA).

# COMMAND ----------

# DBTITLE 1,Tabla Comparativa
# Comparar diferentes productos
productos = [
    {'Producto': 'Plazo Fijo A', 'Tasa': 0.30, 'Frecuencia': 'Anual', 'Periodos': 1},
    {'Producto': 'Plazo Fijo B', 'Tasa': 0.28, 'Frecuencia': 'Mensual', 'Periodos': 12},
    {'Producto': 'Bono C', 'Tasa': 0.29, 'Frecuencia': 'Semestral', 'Periodos': 2},
    {'Producto': 'Inversión D', 'Tasa': 0.285, 'Frecuencia': 'Trimestral', 'Periodos': 4},
]

comparacion = []

for p in productos:
    if p['Frecuencia'] == 'Anual':
        tea = p['Tasa']
    else:
        tea = tasa_efectiva(p['Tasa'], p['Periodos'])
    
    comparacion.append({
        'Producto': p['Producto'],
        'Tasa Declarada': f"{p['Tasa']*100:.1f}% {p['Frecuencia']}",
        'TEA': f"{tea*100:.2f}%",
        'TEA_num': tea
    })

df_comparacion = pd.DataFrame(comparacion)
df_comparacion = df_comparacion.sort_values('TEA_num', ascending=False).reset_index(drop=True)
df_comparacion['Ranking'] = range(1, len(df_comparacion) + 1)

print("📋 Comparación de Productos Financieros\n")
print(df_comparacion[['Ranking', 'Producto', 'Tasa Declarada', 'TEA']].to_string(index=False))

mejor = df_comparacion.iloc[0]
print(f"\n🏆 Mejor opción: {mejor['Producto']} con TEA de {mejor['TEA']}")
print(f"\n💡 Lección: ¡Siempre convierte a TEA para comparar manzanas con manzanas!")

# COMMAND ----------

# DBTITLE 1,Ejercicios Prácticos
# MAGIC %md
# MAGIC ## 💪 Ejercicios Prácticos
# MAGIC
# MAGIC ### Ejercicio 1: Conversión de Tasas
# MAGIC Un préstamo tiene TNA del 42% con capitalización mensual.
# MAGIC a) Calcule la TEA
# MAGIC b) Calcule la tasa mensual equivalente
# MAGIC c) Si pides $50,000, ¿cuánto debes al año?
# MAGIC
# MAGIC ### Ejercicio 2: Tasa Real
# MAGIC Una inversión rinde 15% anual. La inflación es 10%.
# MAGIC a) Calcule la tasa real de rendimiento
# MAGIC b) Si inviertes $20,000, ¿cuál es tu ganancia real en poder adquisitivo?
# MAGIC
# MAGIC ### Ejercicio 3: Comparación
# MAGIC Tres bancos ofrecen:
# MAGIC * Banco A: 25% anual
# MAGIC * Banco B: 24% semestral
# MAGIC * Banco C: 23% trimestral
# MAGIC
# MAGIC ¿Cuál ofrece la mejor TEA?
# MAGIC
# MAGIC ### Ejercicio 4: Descuento
# MAGIC Un documento se descuenta al 20% anual a 180 días.
# MAGIC a) Calcule la tasa vencida equivalente
# MAGIC b) Si el documento es por $100,000, ¿cuánto recibes hoy?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **💡 Tip**: Use las funciones definidas en este notebook.

# COMMAND ----------

# DBTITLE 1,Espacio para Ejercicios
# Resuelva los ejercicios aquí

# Ejercicio 1


# Ejercicio 2


# Ejercicio 3


# Ejercicio 4


# COMMAND ----------

# DBTITLE 1,Resumen y Conclusiones
# MAGIC %md
# MAGIC ## 📚 Resumen y Conclusiones
# MAGIC
# MAGIC ### Conceptos Clave
# MAGIC
# MAGIC 1. **TNA ≠ TEA**: La tasa nominal NO es lo que realmente pagas/ganas
# MAGIC
# MAGIC 2. **Capitalización importa**: Cuanto más frecuente, mayor la TEA
# MAGIC
# MAGIC 3. **Tasas equivalentes**: Producen el mismo resultado en el mismo plazo
# MAGIC
# MAGIC 4. **Inflación**: Siempre ajusta por inflación para conocer tu ganancia/costo real
# MAGIC
# MAGIC 5. **Comparación**: Convierte TODO a TEA antes de comparar
# MAGIC
# MAGIC ### Fórmulas Esenciales
# MAGIC
# MAGIC $$TEA = \left(1 + \frac{TNA}{n}\right)^n - 1$$
# MAGIC
# MAGIC $$r_{real} = \frac{1 + r_{nominal}}{1 + inflación} - 1$$
# MAGIC
# MAGIC $$r_{vencida} = \frac{d}{1 - d \times t}$$
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🚀 Próximos Pasos
# MAGIC
# MAGIC * **1.3 - Anualidades y Amortización**: Flujos múltiples, cuotas, préstamos
# MAGIC * **Módulo 2**: Valoración de instrumentos financieros
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🤖 Consultas con Genie
# MAGIC
# MAGIC * "Explica la diferencia entre TNA y TEA con un ejemplo"
# MAGIC * "Calcula la tasa real si tengo 18% nominal y 12% de inflación"
# MAGIC * "Compara 3 préstamos con diferentes frecuencias de capitalización"
# MAGIC * "Crea una calculadora de conversión de tasas"

# COMMAND ----------

