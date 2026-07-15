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
# MAGIC ### Módulo 02: Valoración de Instrumentos Financieros
# MAGIC ### Notebook 2.1: Valoración de Bonos
# MAGIC ### 📋 **PRECIO, YTM Y DURACIÓN**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción
# MAGIC %md
# MAGIC # 2.1 - Valoración de Bonos
# MAGIC
# MAGIC ## Objetivo del Módulo
# MAGIC Comprender cómo valorar bonos y entender la relación entre precio, tasa de interés y riesgo.
# MAGIC
# MAGIC ## Conceptos Clave
# MAGIC * **Bono**: Instrumento de deuda que paga intereses periódicos (cupones) y devuelve el principal al vencimiento
# MAGIC * **Valor Nominal (VN)**: Monto principal del bono
# MAGIC * **Cupón**: Pago periódico de intereses
# MAGIC * **Tasa Cupón**: Tasa de interés anual del bono
# MAGIC * **Yield to Maturity (YTM)**: Tasa de retorno si se mantiene hasta el vencimiento
# MAGIC * **Precio del Bono**: Valor presente de todos los flujos futuros
# MAGIC * **Duración**: Medida de sensibilidad del precio a cambios en tasas
# MAGIC * **Convexidad**: Curvatura de la relación precio-tasa

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📚 Referencias del Libro de Texto
# MAGIC
# MAGIC **Libro**: Finanzas Corporativas - Un Enfoque Latinoamericano (2ª ed.)
# MAGIC **Autor**: Guillermo L. Dumrauf
# MAGIC **Capítulo**: 6 - Valoración de títulos valores
# MAGIC **Sección**: 6.1-6.3 - Valoración de bonos (pág. 147-165)
# MAGIC **Ubicación**: `/Workspace/Users/cortega@uda.edu.ar/Databricks Finance Lab/Libros/Finanzas corporativas.pdf`
# MAGIC
# MAGIC ### 📝 Contenido cubierto:
# MAGIC
# MAGIC * **Pág. 147-152**: Características de los bonos y flujos de caja
# MAGIC * **Pág. 153-158**: Valoración de bonos con cupones
# MAGIC * **Pág. 159-162**: Relación precio-tasa de interés
# MAGIC * **Pág. 162-165**: Duración y convexidad
# MAGIC
# MAGIC ---

# COMMAND ----------

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

UDA_COLORS = {'primary': '#003366', 'accent': '#FF6600', 'success': '#28A745', 'danger': '#DC3545'}

print("✓ Librerías cargadas correctamente")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📐 Fórmulas Fundamentales
# MAGIC
# MAGIC ### Precio de un Bono con Cupones
# MAGIC
# MAGIC El precio de un bono es el **valor presente** de todos sus flujos futuros:
# MAGIC
# MAGIC $$P = \sum_{t=1}^{n} \frac{C}{(1 + r)^t} + \frac{VN}{(1 + r)^n}$$
# MAGIC
# MAGIC Donde:
# MAGIC * $P$ = Precio del bono
# MAGIC * $C$ = Cupón periódico (VN × tasa_cupón)
# MAGIC * $VN$ = Valor Nominal
# MAGIC * $r$ = Yield to Maturity (YTM)
# MAGIC * $n$ = Número de períodos hasta el vencimiento
# MAGIC
# MAGIC ### Bono Cupón Cero
# MAGIC
# MAGIC Para bonos sin cupones:
# MAGIC
# MAGIC $$P = \frac{VN}{(1 + r)^n}$$
# MAGIC
# MAGIC ### Relación Precio-Tasa (INVERSA)
# MAGIC
# MAGIC * **YTM < Tasa Cupón** → Precio > VN (bono a **premium**)
# MAGIC * **YTM = Tasa Cupón** → Precio = VN (bono a **par**)
# MAGIC * **YTM > Tasa Cupón** → Precio < VN (bono a **discount**)
# MAGIC
# MAGIC ### Duración de Macaulay
# MAGIC
# MAGIC $$D = \frac{\sum_{t=1}^{n} t \times \frac{C}{(1+r)^t} + n \times \frac{VN}{(1+r)^n}}{P}$$
# MAGIC
# MAGIC La duración mide la **sensibilidad del precio** a cambios en las tasas de interés.
# MAGIC
# MAGIC ---

# COMMAND ----------

def precio_bono_cupones(vn, tasa_cupon, ytm, periodos):
    """
    Calcula el precio de un bono con cupones
    
    Parámetros:
    vn: Valor nominal del bono
    tasa_cupon: Tasa de cupón anual (decimal)
    ytm: Yield to Maturity (decimal)
    periodos: Número de períodos hasta vencimiento
    
    Retorna:
    Precio del bono
    """
    cupon = vn * tasa_cupon
    
    # Valor presente de los cupones
    vp_cupones = sum([cupon / (1 + ytm)**t for t in range(1, periodos + 1)])
    
    # Valor presente del valor nominal
    vp_principal = vn / (1 + ytm)**periodos
    
    return vp_cupones + vp_principal


def precio_bono_cero(vn, ytm, periodos):
    """
    Calcula el precio de un bono cupón cero
    
    Parámetros:
    vn: Valor nominal
    ytm: Yield to Maturity (decimal)
    periodos: Número de períodos
    
    Retorna:
    Precio del bono
    """
    return vn / (1 + ytm)**periodos


def ytm_aproximado(precio, vn, cupon_anual, periodos):
    """
    Calcula YTM aproximado usando fórmula simplificada
    
    Parámetros:
    precio: Precio actual del bono
    vn: Valor nominal
    cupon_anual: Cupón anual en pesos
    periodos: Períodos hasta vencimiento
    
    Retorna:
    YTM aproximado
    """
    numerador = cupon_anual + (vn - precio) / periodos
    denominador = (vn + precio) / 2
    return numerador / denominador


def duracion_macaulay(flujos, ytm):
    """
    Calcula la duración de Macaulay
    
    Parámetros:
    flujos: Lista de flujos de caja [cupon1, cupon2, ..., cupon_n + VN]
    ytm: Yield to Maturity (decimal)
    
    Retorna:
    Duración en períodos
    """
    vp_flujos = [flujo / (1 + ytm)**(t+1) for t, flujo in enumerate(flujos)]
    precio = sum(vp_flujos)
    
    duracion = sum([(t+1) * vp / precio for t, vp in enumerate(vp_flujos)])
    return duracion


print("✓ Funciones de valoración de bonos definidas")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejemplo 1: Valoración de un Bono con Cupones
# MAGIC
# MAGIC **Problema**: 
# MAGIC Una empresa emite un bono con las siguientes características:
# MAGIC * Valor Nominal: $1,000
# MAGIC * Tasa de cupón: 8% anual
# MAGIC * Vencimiento: 5 años
# MAGIC * Yield to Maturity (YTM) del mercado: 10%
# MAGIC
# MAGIC **Pregunta**: ¿Cuál es el precio justo del bono?
# MAGIC
# MAGIC ---

# COMMAND ----------

# Datos del bono
vn = 1000
tasa_cupon = 0.08
ytm = 0.10
periodos = 5

# Calcular precio
precio = precio_bono_cupones(vn, tasa_cupon, ytm, periodos)

# Cupón anual
cupon = vn * tasa_cupon

print("="*60)
print("VALORACIÓN DE BONO CON CUPONES")
print("="*60)
print(f"\n📋 Características del Bono:")
print(f"  Valor Nominal: ${vn:,.2f}")
print(f"  Tasa de Cupón: {tasa_cupon*100}% anual")
print(f"  Cupón anual: ${cupon:,.2f}")
print(f"  Vencimiento: {periodos} años")
print(f"  YTM del mercado: {ytm*100}%")

print(f"\n💰 Precio del Bono: ${precio:,.2f}")

# Análisis
if precio < vn:
    print(f"\n🔻 El bono cotiza a DESCUENTO (discount)")
    print(f"   Diferencia: ${vn - precio:,.2f} ({(1 - precio/vn)*100:.2f}%)")
    print(f"   Razón: YTM ({ytm*100}%) > Tasa Cupón ({tasa_cupon*100}%)")
elif precio > vn:
    print(f"\n🔺 El bono cotiza a PREMIUM")
    print(f"   Diferencia: ${precio - vn:,.2f} ({(precio/vn - 1)*100:.2f}%)")
    print(f"   Razón: YTM ({ytm*100}%) < Tasa Cupón ({tasa_cupon*100}%)")
else:
    print(f"\n➡️ El bono cotiza a LA PAR")

print(f"\n📊 Retorno total esperado: {ytm*100}% anual")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejemplo 2: Bono Cupón Cero (Zero-Coupon Bond)
# MAGIC
# MAGIC **Problema**:
# MAGIC El gobierno emite un bono cupón cero:
# MAGIC * Valor Nominal: $1,000
# MAGIC * Vencimiento: 3 años
# MAGIC * YTM del mercado: 6%
# MAGIC
# MAGIC **Pregunta**: ¿Cuánto debemos pagar hoy por este bono?
# MAGIC
# MAGIC ---

# COMMAND ----------

# Datos del bono cupón cero
vn_cero = 1000
ytm_cero = 0.06
periodos_cero = 3

# Calcular precio
precio_cero = precio_bono_cero(vn_cero, ytm_cero, periodos_cero)

print("="*60)
print("VALORACIÓN DE BONO CUPÓN CERO")
print("="*60)
print(f"\n📋 Características:")
print(f"  Valor Nominal: ${vn_cero:,.2f}")
print(f"  Cupones: NINGUNO (cupón cero)")
print(f"  Vencimiento: {periodos_cero} años")
print(f"  YTM: {ytm_cero*100}%")

print(f"\n💰 Precio del Bono: ${precio_cero:,.2f}")
print(f"\n📊 Análisis:")
print(f"  Inversión inicial: ${precio_cero:,.2f}")
print(f"  Valor al vencimiento: ${vn_cero:,.2f}")
print(f"  Ganancia total: ${vn_cero - precio_cero:,.2f}")
print(f"  Retorno total: {(vn_cero/precio_cero - 1)*100:.2f}%")
print(f"  Retorno anualizado: {ytm_cero*100}%")

# Verificación
retorno_anual = (vn_cero / precio_cero)**(1/periodos_cero) - 1
print(f"\n✓ Verificación: {retorno_anual*100:.2f}% anual")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejemplo 3: Relación Inversa entre Precio y Tasa
# MAGIC
# MAGIC Veamos cómo cambia el precio de nuestro bono cuando varía el YTM del mercado.
# MAGIC
# MAGIC **Bono de referencia**:
# MAGIC * VN = $1,000
# MAGIC * Tasa cupón = 8%
# MAGIC * Vencimiento = 5 años
# MAGIC
# MAGIC Graficaremos el precio para YTM entre 4% y 14%.
# MAGIC
# MAGIC ---

# COMMAND ----------

# Rango de YTMs a analizar
ytms = np.linspace(0.04, 0.14, 50)
precios = [precio_bono_cupones(1000, 0.08, y, 5) for y in ytms]

# Crear gráfico interactivo con Plotly
fig = go.Figure()

# Curva principal precio-tasa
fig.add_trace(go.Scatter(
    x=ytms * 100,
    y=precios,
    mode='lines',
    line=dict(color=UDA_COLORS['primary'], width=3),
    name='Precio del Bono',
    hovertemplate='YTM: %{x:.2f}%<br>Precio: $%{y:,.2f}<extra></extra>'
))

# Punto "a la par" (YTM = tasa cupón)
fig.add_trace(go.Scatter(
    x=[8],
    y=[1000],
    mode='markers',
    marker=dict(size=15, color=UDA_COLORS['danger'], symbol='circle',
               line=dict(width=2, color='black')),
    name='A la Par (YTM = Tasa Cupón)',
    hovertemplate='<b>A la Par</b><br>YTM: %{x}%<br>Precio: $%{y:,.2f}<extra></extra>'
))

# Línea de valor nominal
fig.add_hline(
    y=1000,
    line_dash='dash',
    line_color='gray',
    annotation_text='Valor Nominal = $1,000',
    annotation_position='right'
)

# Zonas de premium y discount (usando shapes)
fig.add_vrect(
    x0=4, x1=8,
    fillcolor=UDA_COLORS['success'], opacity=0.1,
    layer='below', line_width=0,
    annotation_text='PREMIUM<br>(Precio > VN)',
    annotation_position='top left'
)

fig.add_vrect(
    x0=8, x1=14,
    fillcolor=UDA_COLORS['danger'], opacity=0.1,
    layer='below', line_width=0,
    annotation_text='DISCOUNT<br>(Precio < VN)',
    annotation_position='top right'
)

# Configurar layout
fig.update_layout(
    title=dict(
        text='Relación INVERSA entre Precio y Tasa de Interés<br><sub>Bono VN=$1,000, Cupón=8%, 5 años</sub>',
        font=dict(size=18, family='Arial, sans-serif', color=UDA_COLORS['primary']),
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title=dict(text='Yield to Maturity (%)', font=dict(size=14)),
        gridcolor='#E5E5E5',
        showgrid=True,
        range=[4, 14]
    ),
    yaxis=dict(
        title=dict(text='Precio del Bono ($)', font=dict(size=14)),
        gridcolor='#E5E5E5',
        showgrid=True,
        tickformat='$,.0f'
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
        'filename': 'relacion_precio_tasa_bono',
        'height': 700,
        'width': 1400,
        'scale': 2
    }
}

fig.show(config=config)

print("📊 Observaciones:")
print("1. La relación es INVERSA: ↑ YTM → ↓ Precio")
print("2. La relación es NO LINEAL (curva convexa)")
print("3. Cuando YTM = Tasa Cupón → Precio = VN (a la par)")
print("4. Cuando YTM < Tasa Cupón → Precio > VN (premium)")
print("5. Cuando YTM > Tasa Cupón → Precio < VN (discount)")
print("\n💡 TIP: Pasa el mouse sobre la curva para explorar valores exactos")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📏 Duración de Macaulay
# MAGIC
# MAGIC La **duración** es una medida del tiempo promedio ponderado hasta recibir los flujos de caja.
# MAGIC
# MAGIC ### ¿Para qué sirve?
# MAGIC
# MAGIC * Mide la **sensibilidad del precio** a cambios en tasas
# MAGIC * Aproxima el cambio porcentual en precio: 
# MAGIC   $$\Delta P \approx -D \times \Delta r \times P$$
# MAGIC * Útil para gestión de riesgo de tasas (inmunización)
# MAGIC
# MAGIC ### Interpretación:
# MAGIC
# MAGIC * **Duración alta** → Mayor sensibilidad a tasas → Mayor riesgo
# MAGIC * **Duración baja** → Menor sensibilidad a tasas → Menor riesgo
# MAGIC
# MAGIC ---

# COMMAND ----------

# Calcular duración para nuestro bono ejemplo
vn = 1000
tasa_cupon = 0.08
ytm = 0.10
periodos = 5

cupon = vn * tasa_cupon

# Crear lista de flujos de caja
flujos = [cupon] * (periodos - 1) + [cupon + vn]

# Calcular duración
duracion = duracion_macaulay(flujos, ytm)
precio_actual = precio_bono_cupones(vn, tasa_cupon, ytm, periodos)

print("="*60)
print("DURACIÓN DE MACAULAY")
print("="*60)
print(f"\n📋 Bono:")
print(f"  VN = ${vn:,.2f}")
print(f"  Cupón = {tasa_cupon*100}%")
print(f"  YTM = {ytm*100}%")
print(f"  Vencimiento = {periodos} años")
print(f"  Precio = ${precio_actual:,.2f}")

print(f"\n⏱️ Duración de Macaulay: {duracion:.2f} años")

print(f"\n📊 Interpretación:")
print(f"  Si las tasas suben 1%, el precio caerá aprox. {duracion:.2f}%")
print(f"  Si las tasas bajan 1%, el precio subirá aprox. {duracion:.2f}%")

# Verificar con cambio de 1%
ytm_nuevo = ytm + 0.01
precio_nuevo = precio_bono_cupones(vn, tasa_cupon, ytm_nuevo, periodos)
cambio_real = (precio_nuevo - precio_actual) / precio_actual * 100

print(f"\n✓ Verificación (YTM ↑ 1%):")
print(f"  Cambio predicho: -{duracion:.2f}%")
print(f"  Cambio real: {cambio_real:.2f}%")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🇦🇷 Bonos Argentinos: Contexto Local
# MAGIC
# MAGIC ### Tipos de Bonos en Argentina
# MAGIC
# MAGIC 1. **Bonos Soberanos** (Tesoro Nacional)
# MAGIC    * En pesos (ARS) o dólares (USD)
# MAGIC    * Ejemplos: Bonares, Globales (GD30, GD35, GD38, GD41, GD46)
# MAGIC    * Alto riesgo país → Altos rendimientos
# MAGIC
# MAGIC 2. **Bonos Provinciales**
# MAGIC    * Emitidos por provincias argentinas
# MAGIC    * Ejemplos: Mendoza, Buenos Aires, Córdoba
# MAGIC    * Riesgo variable según provincia
# MAGIC
# MAGIC 3. **Obligaciones Negociables (ONs)**
# MAGIC    * Emitidas por empresas privadas
# MAGIC    * Ejemplos: YPF, Pampa Energía, Telecom
# MAGIC    * Rating corporativo
# MAGIC
# MAGIC ### Particularidades del Mercado Argentino
# MAGIC
# MAGIC * **Alta inflación** → Bonos CER (ajustados por inflación)
# MAGIC * **Volatilidad cambiaria** → Preferencia por bonos en USD
# MAGIC * **Riesgo país elevado** → Spreads sobre bonos del tesoro USA
# MAGIC * **Reestructuraciones frecuentes** → Descuentos (haircuts) históricos
# MAGIC
# MAGIC ### Ejemplo Real: Bono GD30
# MAGIC
# MAGIC * Bono Global 2030 en USD
# MAGIC * Tasa cupón: ~1% anual
# MAGIC * Cotiza con alto descuento (YTM >> tasa cupón)
# MAGIC * Refleja riesgo de default soberano
# MAGIC
# MAGIC ---

# COMMAND ----------

# Ejemplo: Bono corporativo argentino
print("="*60)
print("EJEMPLO: OBLIGACIÓN NEGOCIABLE ARGENTINA")
print("="*60)

vn_on = 1000  # USD
tasa_cupon_on = 0.08  # 8% en USD (tasa alta para Argentina)
periodos_on = 3
ytm_argentina = 0.15  # 15% - refleja riesgo argentino

precio_on = precio_bono_cupones(vn_on, tasa_cupon_on, ytm_argentina, periodos_on)

print(f"\n📋 Obligación Negociable (ON) en USD:")
print(f"  Emisor: Empresa argentina de primera línea")
print(f"  Valor Nominal: USD {vn_on:,.2f}")
print(f"  Tasa Cupón: {tasa_cupon_on*100}% anual")
print(f"  Vencimiento: {periodos_on} años")
print(f"  YTM exigida (riesgo país): {ytm_argentina*100}%")

print(f"\n💰 Precio: USD {precio_on:,.2f}")
print(f"  Descuento: USD {vn_on - precio_on:,.2f} ({(1 - precio_on/vn_on)*100:.1f}%)")

print(f"\n🌎 Comparación con bono USA:")
ytm_usa = 0.04  # 4% - tasa libre de riesgo
precio_usa = precio_bono_cupones(vn_on, tasa_cupon_on, ytm_usa, periodos_on)
print(f"  Si fuera bono USA (4% YTM): USD {precio_usa:,.2f}")
print(f"  Diferencia (riesgo país): USD {precio_usa - precio_on:,.2f}")

riesgo_pais = ytm_argentina - ytm_usa
print(f"\n🚨 Riesgo país implícito: {riesgo_pais*100:.0f}% anual")
print(f"   ({riesgo_pais*10000:.0f} puntos básicos)")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📈 Curva de Rendimientos (Yield Curve)
# MAGIC
# MAGIC La **curva de rendimientos** muestra la relación entre el vencimiento de los bonos y su YTM.
# MAGIC
# MAGIC ### Formas de la Curva:
# MAGIC
# MAGIC 1. **Normal (ascendente)**: Bonos largo plazo → Mayor YTM
# MAGIC    * Refleja expectativas de crecimiento económico
# MAGIC
# MAGIC 2. **Invertida (descendente)**: Bonos largo plazo → Menor YTM
# MAGIC    * Señal de recesión inminente
# MAGIC
# MAGIC 3. **Plana**: YTM similar para todos los vencimientos
# MAGIC    * Incertidumbre económica
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Gráfico Curva de Rendimientos
# Simular curvas de rendimientos
vencimientos = np.array([1, 2, 3, 5, 7, 10, 15, 20, 30])

# Curva normal (economía estable)
ytm_normal = 0.03 + 0.02 * (1 - np.exp(-vencimientos/10))

# Curva invertida (recesión)
ytm_invertida = 0.05 - 0.015 * (vencimientos / 30)

# Curva argentina (alto riesgo)
ytm_argentina_curva = 0.12 + 0.03 * (1 - np.exp(-vencimientos/8))

# Crear gráfico interactivo con Plotly
fig = go.Figure()

# Curva Normal (USA)
fig.add_trace(go.Scatter(
    x=vencimientos,
    y=ytm_normal * 100,
    mode='lines+markers',
    line=dict(color=UDA_COLORS['success'], width=2.5),
    marker=dict(size=8, symbol='circle'),
    name='Curva Normal (USA)',
    hovertemplate='<b>USA - Curva Normal</b><br>Vencimiento: %{x} años<br>YTM: %{y:.2f}%<extra></extra>'
))

# Curva Invertida (Recesión)
fig.add_trace(go.Scatter(
    x=vencimientos,
    y=ytm_invertida * 100,
    mode='lines+markers',
    line=dict(color=UDA_COLORS['danger'], width=2.5),
    marker=dict(size=8, symbol='square'),
    name='Curva Invertida (Recesión)',
    hovertemplate='<b>Recesión - Curva Invertida</b><br>Vencimiento: %{x} años<br>YTM: %{y:.2f}%<extra></extra>'
))

# Curva Argentina (Alto Riesgo)
fig.add_trace(go.Scatter(
    x=vencimientos,
    y=ytm_argentina_curva * 100,
    mode='lines+markers',
    line=dict(color=UDA_COLORS['accent'], width=2.5),
    marker=dict(size=8, symbol='triangle-up'),
    name='Curva Argentina (Alto riesgo)',
    hovertemplate='<b>Argentina - Alto Riesgo</b><br>Vencimiento: %{x} años<br>YTM: %{y:.2f}%<extra></extra>'
))

# Configurar layout
fig.update_layout(
    title=dict(
        text='Curvas de Rendimientos Comparadas<br><sub>USA vs Recesión vs Argentina</sub>',
        font=dict(size=18, family='Arial, sans-serif', color=UDA_COLORS['primary']),
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title=dict(text='Vencimiento (años)', font=dict(size=14)),
        gridcolor='#E5E5E5',
        showgrid=True
    ),
    yaxis=dict(
        title=dict(text='Yield to Maturity (%)', font=dict(size=14)),
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
        'filename': 'curvas_rendimientos_comparadas',
        'height': 700,
        'width': 1400,
        'scale': 2
    }
}

fig.show(config=config)

print("📊 Análisis de Curvas:")
print("\n🟢 Curva Normal (USA):")
print("   - Bonos corto plazo: 3-4%")
print("   - Bonos largo plazo: 4-5%")
print("   - Refleja: Economía estable, expectativa de crecimiento")

print("\n🔴 Curva Invertida:")
print("   - Bonos corto plazo: 5%")
print("   - Bonos largo plazo: 3.5%")
print("   - Refleja: Expectativa de recesión, políticas restrictivas")

print("\n🟠 Curva Argentina:")
print("   - Bonos corto plazo: 12-14%")
print("   - Bonos largo plazo: 15%")
print("   - Refleja: Alto riesgo país, historial de defaults")

print("\n💡 TIP: Pasa el mouse sobre las curvas para comparar YTM por vencimiento")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 💪 Ejercicios Prácticos
# MAGIC
# MAGIC ### Ejercicio 1: Valoración Básica
# MAGIC Una empresa argentina emite un bono con:
# MAGIC * VN = USD 1,000
# MAGIC * Tasa cupón = 10% anual
# MAGIC * Vencimiento = 4 años
# MAGIC * YTM del mercado = 12%
# MAGIC
# MAGIC **Tareas**:
# MAGIC a) Calcule el precio del bono
# MAGIC b) ¿Cotiza a premium, par o discount? ¿Por qué?
# MAGIC c) Si las tasas bajan a 9%, ¿qué pasará con el precio?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ejercicio 2: Bono Cupón Cero
# MAGIC El gobierno emite LETES (bonos cupón cero) a 180 días:
# MAGIC * VN = ARS 100,000
# MAGIC * Plazo = 0.5 años
# MAGIC * YTM = 80% anual (inflación alta en Argentina)
# MAGIC
# MAGIC **Tareas**:
# MAGIC a) Calcule cuánto debe pagar hoy
# MAGIC b) Calcule su ganancia total
# MAGIC c) Compare con tasa de inflación esperada
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ejercicio 3: Duración
# MAGIC Calcule la duración de Macaulay para un bono:
# MAGIC * VN = USD 1,000
# MAGIC * Cupón = 6%
# MAGIC * Vencimiento = 3 años
# MAGIC * YTM = 8%
# MAGIC
# MAGIC **Tareas**:
# MAGIC a) Calcule la duración
# MAGIC b) Si las tasas suben 0.5%, estime el cambio de precio
# MAGIC c) Calcule el cambio real y compare
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ejercicio 4: Comparación de Bonos
# MAGIC Compare estos dos bonos y decida cuál comprar:
# MAGIC
# MAGIC **Bono A**:
# MAGIC * VN = USD 1,000
# MAGIC * Cupón = 8%
# MAGIC * Vencimiento = 5 años
# MAGIC * Precio = USD 950
# MAGIC
# MAGIC **Bono B**:
# MAGIC * VN = USD 1,000
# MAGIC * Cupón = 6%
# MAGIC * Vencimiento = 5 años
# MAGIC * Precio = USD 900
# MAGIC
# MAGIC **Tareas**:
# MAGIC a) Calcule el YTM aproximado de cada uno
# MAGIC b) ¿Cuál tiene mejor retorno?
# MAGIC c) Calcule la duración de ambos. ¿Cuál es más riesgoso?
# MAGIC
# MAGIC ---

# COMMAND ----------

# Resuelva los ejercicios aquí

# Ejercicio 1
print("="*60)
print("EJERCICIO 1: Valoración Básica")
print("="*60)
# Su código aquí



print("\n" + "="*60)
print("EJERCICIO 2: Bono Cupón Cero (LETES)")
print("="*60)
# Su código aquí



print("\n" + "="*60)
print("EJERCICIO 3: Duración")
print("="*60)
# Su código aquí



print("\n" + "="*60)
print("EJERCICIO 4: Comparación de Bonos")
print("="*60)
# Su código aquí

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🤖 Consultas Sugeridas con Genie Code
# MAGIC
# MAGIC Prueba estas consultas con Genie para profundizar tu análisis:
# MAGIC
# MAGIC ### Análisis Básico
# MAGIC * "Calcula el precio de un bono con VN=$1000, cupón 7%, 10 años, YTM=8%"
# MAGIC * "¿Cuál es el YTM de un bono que cotiza a $920, VN=$1000, cupón 6%, 5 años?"
# MAGIC * "Explica por qué los bonos caen cuando suben las tasas de interés"
# MAGIC
# MAGIC ### Análisis de Sensibilidad
# MAGIC * "Grafica cómo cambia el precio de este bono cuando YTM varía entre 5% y 15%"
# MAGIC * "Compara la sensibilidad de bonos a 5, 10 y 30 años ante cambio de tasas"
# MAGIC * "¿Qué bono es más sensible: cupón 3% o cupón 9%?"
# MAGIC
# MAGIC ### Duración y Riesgo
# MAGIC * "Calcula la duración modificada de este portafolio de bonos"
# MAGIC * "¿Cuánto cambiará el precio si las tasas suben 50 puntos básicos?"
# MAGIC * "Construye un portafolio de bonos con duración objetivo de 7 años"
# MAGIC
# MAGIC ### Contexto Argentino
# MAGIC * "Analiza por qué los bonos argentinos tienen YTM tan alto"
# MAGIC * "Compara bonos CER vs bonos en USD para protección inflacionaria"
# MAGIC * "Calcula el riesgo país implícito de un bono argentino"
# MAGIC * "¿Cómo afecta una reestructuración de deuda al valor de los bonos?"
# MAGIC
# MAGIC ### Análisis Avanzado
# MAGIC * "Construye una curva de rendimientos con datos de bonos del tesoro"
# MAGIC * "Calcula la convexidad de este bono"
# MAGIC * "Estima el precio limpio (clean price) vs precio sucio (dirty price)"
# MAGIC * "Analiza el impacto fiscal de intereses de bonos"
# MAGIC
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📚 Resumen y Conclusiones
# MAGIC
# MAGIC ### Conceptos Clave Aprendidos
# MAGIC
# MAGIC 1. **Valoración de Bonos**
# MAGIC    * El precio es el valor presente de todos los flujos futuros
# MAGIC    * Fórmula: VP(cupones) + VP(valor nominal)
# MAGIC
# MAGIC 2. **Relación Precio-Tasa**
# MAGIC    * **INVERSA**: ↑ tasas → ↓ precio
# MAGIC    * **NO LINEAL**: La curva es convexa
# MAGIC    * Premium/Par/Discount según YTM vs Tasa Cupón
# MAGIC
# MAGIC 3. **Duración**
# MAGIC    * Mide sensibilidad del precio a cambios en tasas
# MAGIC    * Útil para gestión de riesgo (inmunización)
# MAGIC    * Duración alta = Mayor riesgo
# MAGIC
# MAGIC 4. **Contexto Argentino**
# MAGIC    * Alto riesgo país → Altos rendimientos exigidos
# MAGIC    * Bonos CER para protección inflacionaria
# MAGIC    * Volatilidad y reestructuraciones frecuentes
# MAGIC
# MAGIC ### Aplicaciones Prácticas
# MAGIC
# MAGIC * **Inversión**: Evaluar si un bono está bien precio
# MAGIC * **Gestión de Riesgo**: Medir exposición a tasas
# MAGIC * **Portafolios**: Diversificación con renta fija
# MAGIC * **Arbitraje**: Detectar oportunidades de valor
# MAGIC
# MAGIC ### Próximos Pasos
# MAGIC
# MAGIC * **Notebook 2.2**: Valoración de Acciones (DDM, P/E, múltiplos)
# MAGIC * **Notebook 3.1**: Ratios Financieros para analizar emisores
# MAGIC * **Notebook 4.1**: Riesgo y Retorno de bonos en portafolios
# MAGIC
# MAGIC ### Referencias Adicionales
# MAGIC
# MAGIC * **Dumrauf**: Capítulo 6, págs. 147-165
# MAGIC * **Comisión Nacional de Valores (CNV)**: Datos de bonos argentinos
# MAGIC * **BYMA**: Cotizaciones en tiempo real
# MAGIC * **Banco Central (BCRA)**: Estadísticas de tasas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎯 ¡Has completado el módulo de Valoración de Bonos!
# MAGIC
# MAGIC **Siguiente:** [2.2 - Valoración de Acciones](#notebook/1265694461779443)
# MAGIC
# MAGIC ---