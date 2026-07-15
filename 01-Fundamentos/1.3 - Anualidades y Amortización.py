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
# MAGIC ### Notebook 1.3: Anualidades y Amortización
# MAGIC ### 🏦 **SISTEMAS FRANCÉS Y ALEMÁN**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción
# MAGIC %md
# MAGIC # 1.3 - Anualidades y Amortización
# MAGIC
# MAGIC ## Objetivo del Módulo
# MAGIC Comprender el cálculo de flujos de efectivo múltiples periódicos y sistemas de amortización de préstamos.
# MAGIC
# MAGIC ## Conceptos Clave
# MAGIC * **Anualidad**: Serie de pagos iguales en intervalos regulares
# MAGIC * **Anualidad Ordinaria**: Pagos al final de cada período
# MAGIC * **Anualidad Anticipada**: Pagos al inicio de cada período
# MAGIC * **Anualidad Temporaria**: Número finito de pagos
# MAGIC * **Perpetuidad**: Anualidad infinita
# MAGIC * **Amortización**: Proceso de pago gradual de una deuda
# MAGIC * **Sistema Francés**: Cuotas constantes
# MAGIC * **Sistema Alemán**: Amortización constante
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
# MAGIC **Sección**: 5.4 - Calcular el valor de un flujo de efectivo (pág. 132-143)
# MAGIC **Ubicación**: `/Workspace/Users/cortega@uda.edu.ar/Databricks Finance Lab/Libros/Finanzas corporativas.pdf`
# MAGIC
# MAGIC ### 📝 Contenido cubierto:
# MAGIC
# MAGIC * **Pág. 133-137**: Valor actual de una corriente temporaria de pagos fijos (anualidades)
# MAGIC * **Pág. 137-140**: Valor actual de una corriente de pagos perpetua (perpetuidades)
# MAGIC * **Pág. 140-141**: Valuación de una perpetuidad con crecimiento
# MAGIC * **Pág. 141-143**: Valor final de una corriente de pagos (imposiciones)
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Funciones de Anualidades
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy_financial as npf  # Para funciones financieras adicionales

# Colores institucionales UDA
UDA_COLORS = {'primary': '#003366', 'accent': '#FF6600', 'success': '#28A745', 'danger': '#DC3545'}

def va_anualidad_ordinaria(pago, r, n):
    """
    Valor Actual de una anualidad ordinaria (pagos al final)
    
    VA = Pago × [(1 - (1+r)^-n) / r]
    
    Parámetros:
    pago: Monto del pago periódico
    r: Tasa de interés por período
    n: Número de períodos
    
    Retorna:
    Valor actual de la anualidad
    """
    if r == 0:
        return pago * n
    return pago * ((1 - (1 + r)**(-n)) / r)

def vf_anualidad_ordinaria(pago, r, n):
    """
    Valor Futuro de una anualidad ordinaria
    
    VF = Pago × [((1+r)^n - 1) / r]
    """
    if r == 0:
        return pago * n
    return pago * (((1 + r)**n - 1) / r)

def va_perpetuidad(pago, r):
    """
    Valor Actual de una perpetuidad (anualidad infinita)
    
    VA = Pago / r
    """
    return pago / r

def va_perpetuidad_creciente(pago, r, g):
    """
    Valor Actual de una perpetuidad con crecimiento constante
    
    VA = Pago / (r - g)
    
    Condición: r > g
    """
    if r <= g:
        raise ValueError("La tasa de interés debe ser mayor que la tasa de crecimiento")
    return pago / (r - g)

def calcular_cuota(va, r, n):
    """
    Calcula el pago periódico de una anualidad dado el VA
    
    Pago = VA × [r / (1 - (1+r)^-n)]
    """
    if r == 0:
        return va / n
    return va * (r / (1 - (1 + r)**(-n)))

def tabla_amortizacion_frances(monto, r, n):
    """
    Genera tabla de amortización sistema francés (cuota constante)
    
    Parámetros:
    monto: Monto del préstamo
    r: Tasa de interés por período
    n: Número de cuotas
    
    Retorna:
    DataFrame con tabla de amortización
    """
    # Calcular cuota constante
    cuota = calcular_cuota(monto, r, n)
    
    tabla = []
    saldo = monto
    
    for periodo in range(1, n + 1):
        interes = saldo * r
        amortizacion = cuota - interes
        saldo = saldo - amortizacion
        
        tabla.append({
            'Período': periodo,
            'Saldo Inicial': round(saldo + amortizacion, 2),
            'Cuota': round(cuota, 2),
            'Interés': round(interes, 2),
            'Amortización': round(amortizacion, 2),
            'Saldo Final': round(max(0, saldo), 2)
        })
    
    return pd.DataFrame(tabla)

def tabla_amortizacion_aleman(monto, r, n):
    """
    Genera tabla de amortización sistema alemán (amortización constante)
    """
    # Amortización constante
    amortizacion = monto / n
    
    tabla = []
    saldo = monto
    
    for periodo in range(1, n + 1):
        interes = saldo * r
        cuota = amortizacion + interes
        saldo = saldo - amortizacion
        
        tabla.append({
            'Período': periodo,
            'Saldo Inicial': round(saldo + amortizacion, 2),
            'Cuota': round(cuota, 2),
            'Interés': round(interes, 2),
            'Amortización': round(amortizacion, 2),
            'Saldo Final': round(max(0, saldo), 2)
        })
    
    return pd.DataFrame(tabla)

print("✓ Funciones de anualidades y amortización definidas")

# COMMAND ----------

# DBTITLE 1,Ejemplo 1: Valor Presente de Anualidad
# MAGIC %md
# MAGIC ## Ejemplo 1: ¿Cuánto Vale Hoy una Serie de Pagos Futuros?
# MAGIC
# MAGIC **Problema**: Ganarás $5,000 al final de cada año durante los próximos 10 años. Si la tasa de descuento es 8% anual, ¿cuánto vale hoy esa serie de pagos?

# COMMAND ----------

# DBTITLE 1,Solución Ejemplo 1
# Datos
pago = 5000  # Pago anual
r = 0.08     # 8% anual
n = 10       # 10 años

# Calcular valor actual
va = va_anualidad_ordinaria(pago, r, n)

# Total de pagos (sin descontar)
total_pagos = pago * n

print(f"Serie de pagos:")
print(f"  Pago anual: ${pago:,.2f}")
print(f"  Número de pagos: {n}")
print(f"  Tasa de descuento: {r*100}%")
print(f"\nTotal sin descontar: ${total_pagos:,.2f}")
print(f"Valor actual (descontado): ${va:,.2f}")
print(f"\n💡 Diferencia: ${total_pagos - va:,.2f}")
print(f"   El valor presente es {(va/total_pagos)*100:.1f}% del total nominal")
print(f"\n   Esto significa que ${va:,.2f} hoy equivalen a recibir ${pago:,.2f} anuales por {n} años")

# COMMAND ----------

# DBTITLE 1,Ejemplo 2: Calcular la Cuota
# MAGIC %md
# MAGIC ## Ejemplo 2: ¿Cuánto Debo Pagar Mensualmente?
# MAGIC
# MAGIC **Problema**: Pides un préstamo de $100,000 a 5 años con tasa del 12% anual (capitalización mensual). ¿Cuál será tu cuota mensual?

# COMMAND ----------

# DBTITLE 1,Solución Ejemplo 2
# Datos
monto = 100000   # Préstamo
tasa_anual = 0.12  # 12% anual
n_anios = 5
n_meses = n_anios * 12  # 60 meses
r_mensual = tasa_anual / 12  # Tasa mensual

# Calcular cuota mensual
cuota = calcular_cuota(monto, r_mensual, n_meses)

# Total a pagar
total = cuota * n_meses

# Intereses totales
intereses = total - monto

print(f"Préstamo: ${monto:,.2f}")
print(f"Plazo: {n_anios} años ({n_meses} cuotas mensuales)")
print(f"Tasa: {tasa_anual*100}% anual ({r_mensual*100:.2f}% mensual)")
print(f"\n💳 Cuota mensual: ${cuota:,.2f}")
print(f"\nTotal a pagar: ${total:,.2f}")
print(f"Intereses totales: ${intereses:,.2f}")
print(f"\nRelación intereses/capital: {(intereses/monto)*100:.1f}%")
print(f"Por cada $1 prestado, pagas ${intereses/monto:.2f} de interés")

# COMMAND ----------

# DBTITLE 1,Ejemplo 3: Perpetuidad
# MAGIC %md
# MAGIC ## Ejemplo 3: Perpetuidad - Pagos Infinitos
# MAGIC
# MAGIC **Problema**: Una acción preferida paga $8 de dividendo anual a perpetuidad. Si requieres un rendimiento del 10%, ¿cuánto pagarías por la acción?

# COMMAND ----------

# DBTITLE 1,Solución Ejemplo 3
# Datos
dividendo = 8    # Dividendo anual
r_req = 0.10     # 10% rendimiento requerido

# Valor de la perpetuidad
valor = va_perpetuidad(dividendo, r_req)

print(f"Dividendo anual: ${dividendo}")
print(f"Rendimiento requerido: {r_req*100}%")
print(f"\nValor de la acción: ${valor:,.2f}")
print(f"\n💡 Fórmula simple: Dividendo / Tasa = ${dividendo} / {r_req} = ${valor:,.2f}")
print(f"\nVerificación: ${valor:,.2f} × {r_req*100}% = ${valor * r_req:,.2f} de dividendo anual")

# Sensibilidad a cambios en la tasa
print(f"\n📉 Sensibilidad a cambios en la tasa requerida:")
for tasa in [0.08, 0.09, 0.10, 0.11, 0.12]:
    v = va_perpetuidad(dividendo, tasa)
    print(f"  Con tasa {tasa*100}%: ${v:,.2f}")

# COMMAND ----------

# DBTITLE 1,Ejemplo 4: Perpetuidad Creciente
# MAGIC %md
# MAGIC ## Ejemplo 4: Perpetuidad con Crecimiento
# MAGIC
# MAGIC **Problema**: Una empresa pagará $10 de dividendo el próximo año, y los dividendos crecerán 5% anual a perpetuidad. Con tasa de descuento del 12%, ¿cuánto vale la acción?

# COMMAND ----------

# DBTITLE 1,Solución Ejemplo 4
# Datos
div1 = 10        # Dividendo año 1
g = 0.05         # 5% crecimiento anual
r_desc = 0.12    # 12% descuento

# Valor con crecimiento (Modelo de Gordon)
valor_creciente = va_perpetuidad_creciente(div1, r_desc, g)

# Comparar con perpetuidad sin crecimiento
valor_constante = va_perpetuidad(div1, r_desc)

print(f"Dividendo año 1: ${div1}")
print(f"Crecimiento anual: {g*100}%")
print(f"Tasa de descuento: {r_desc*100}%")
print(f"\nValor con crecimiento: ${valor_creciente:,.2f}")
print(f"Valor sin crecimiento: ${valor_constante:,.2f}")
print(f"\nPrima por crecimiento: ${valor_creciente - valor_constante:,.2f}")
print(f"  ({((valor_creciente/valor_constante - 1)*100):.1f}% más)")

# Proyección de dividendos
print(f"\n📈 Proyección de dividendos:")
for anio in range(1, 6):
    div = div1 * (1 + g)**(anio - 1)
    print(f"  Año {anio}: ${div:.2f}")

# COMMAND ----------

# DBTITLE 1,Sistema Francés de Amortización
# MAGIC %md
# MAGIC ## 🏦 Sistema Francés: Cuota Constante
# MAGIC
# MAGIC **Características**:
# MAGIC * La cuota es constante durante toda la vida del préstamo
# MAGIC * Al principio pagas más interés, al final más capital
# MAGIC * Es el sistema más común en préstamos hipotecarios y personales
# MAGIC
# MAGIC **Ejemplo**: Préstamo de $50,000 a 12 meses con 2% mensual

# COMMAND ----------

# DBTITLE 1,Tabla Amortización Francesa
# Parámetros
monto_frances = 50000
r_frances = 0.02  # 2% mensual
n_frances = 12    # 12 meses

# Generar tabla
tabla_frances = tabla_amortizacion_frances(monto_frances, r_frances, n_frances)

print(f"📊 TABLA DE AMORTIZACIÓN - SISTEMA FRANCÉS")
print(f"\nPréstamo: ${monto_frances:,.2f} | Tasa: {r_frances*100}% mensual | Plazo: {n_frances} meses\n")
print(tabla_frances.to_string(index=False))

# Resúmenes
cuota_const = tabla_frances['Cuota'].iloc[0]
total_intereses = tabla_frances['Interés'].sum()
total_pagado = tabla_frances['Cuota'].sum()

print(f"\n\n📄 RESUMEN:")
print(f"  Cuota mensual constante: ${cuota_const:,.2f}")
print(f"  Total intereses: ${total_intereses:,.2f}")
print(f"  Total pagado: ${total_pagado:,.2f}")
print(f"  Costo financiero: {(total_intereses/monto_frances)*100:.2f}%")

# COMMAND ----------

# DBTITLE 1,Sistema Alemán de Amortización
# MAGIC %md
# MAGIC ## 🏦 Sistema Alemán: Amortización Constante
# MAGIC
# MAGIC **Características**:
# MAGIC * La amortización de capital es constante
# MAGIC * Las cuotas son decrecientes (primera cuota es la más alta)
# MAGIC * Pagas menos intereses totales que en sistema francés
# MAGIC * Primera cuota más alta puede ser una barrera
# MAGIC
# MAGIC **Mismo ejemplo**: $50,000 a 12 meses con 2% mensual

# COMMAND ----------

# DBTITLE 1,Tabla Amortización Alemana
# Generar tabla sistema alemán (mismos parámetros)
tabla_aleman = tabla_amortizacion_aleman(monto_frances, r_frances, n_frances)

print(f"📊 TABLA DE AMORTIZACIÓN - SISTEMA ALEMÁN")
print(f"\nPréstamo: ${monto_frances:,.2f} | Tasa: {r_frances*100}% mensual | Plazo: {n_frances} meses\n")
print(tabla_aleman.to_string(index=False))

# Resúmenes
total_intereses_aleman = tabla_aleman['Interés'].sum()
total_pagado_aleman = tabla_aleman['Cuota'].sum()

print(f"\n\n📄 RESUMEN:")
print(f"  Primera cuota: ${tabla_aleman['Cuota'].iloc[0]:,.2f}")
print(f"  Última cuota: ${tabla_aleman['Cuota'].iloc[-1]:,.2f}")
print(f"  Total intereses: ${total_intereses_aleman:,.2f}")
print(f"  Total pagado: ${total_pagado_aleman:,.2f}")
print(f"  Costo financiero: {(total_intereses_aleman/monto_frances)*100:.2f}%")

# COMMAND ----------

# DBTITLE 1,Comparación de Sistemas
# MAGIC %md
# MAGIC ## ⚖️ Comparación: Francés vs Alemán

# COMMAND ----------

# DBTITLE 1,Comparación Visual
# Comparación numérica
comparacion = pd.DataFrame({
    'Concepto': [
        'Primera cuota',
        'Última cuota',
        'Total intereses',
        'Total pagado',
        'Ahorro en intereses'
    ],
    'Sistema Francés': [
        f"${tabla_frances['Cuota'].iloc[0]:,.2f}",
        f"${tabla_frances['Cuota'].iloc[-1]:,.2f}",
        f"${total_intereses:,.2f}",
        f"${total_pagado:,.2f}",
        '-'
    ],
    'Sistema Alemán': [
        f"${tabla_aleman['Cuota'].iloc[0]:,.2f}",
        f"${tabla_aleman['Cuota'].iloc[-1]:,.2f}",
        f"${total_intereses_aleman:,.2f}",
        f"${total_pagado_aleman:,.2f}",
        f"${total_intereses - total_intereses_aleman:,.2f}"
    ]
})

print("\n⚖️ COMPARACIÓN DE SISTEMAS:\n")
print(comparacion.to_string(index=False))

# Gráfico comparativo interactivo con Plotly
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Evolución de las Cuotas',
        'Sistema Francés: Composición de la Cuota',
        'Evolución del Saldo Deudor',
        'Intereses Acumulados - Ahorro del Sistema Alemán'
    ),
    vertical_spacing=0.12,
    horizontal_spacing=0.10
)

# Gráfico 1: Evolución de cuotas
fig.add_trace(go.Scatter(
    x=tabla_frances['Período'], y=tabla_frances['Cuota'],
    mode='lines+markers', name='Francés (constante)',
    line=dict(color=UDA_COLORS['primary'], width=2),
    marker=dict(size=6),
    hovertemplate='Período: %{x}<br>Cuota: $%{y:,.2f}<extra></extra>'
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=tabla_aleman['Período'], y=tabla_aleman['Cuota'],
    mode='lines+markers', name='Alemán (decreciente)',
    line=dict(color=UDA_COLORS['danger'], width=2),
    marker=dict(size=6, symbol='square'),
    hovertemplate='Período: %{x}<br>Cuota: $%{y:,.2f}<extra></extra>'
), row=1, col=1)

# Gráfico 2: Interés vs Amortización (Francés)
fig.add_trace(go.Scatter(
    x=tabla_frances['Período'], y=tabla_frances['Interés'],
    mode='lines+markers', name='Interés',
    line=dict(color=UDA_COLORS['danger'], width=2),
    marker=dict(size=6),
    hovertemplate='Período: %{x}<br>Interés: $%{y:,.2f}<extra></extra>',
    showlegend=False
), row=1, col=2)

fig.add_trace(go.Scatter(
    x=tabla_frances['Período'], y=tabla_frances['Amortización'],
    mode='lines+markers', name='Amortización',
    line=dict(color=UDA_COLORS['success'], width=2),
    marker=dict(size=6, symbol='square'),
    hovertemplate='Período: %{x}<br>Amortización: $%{y:,.2f}<extra></extra>',
    showlegend=False
), row=1, col=2)

# Gráfico 3: Saldo deudor
fig.add_trace(go.Scatter(
    x=tabla_frances['Período'], y=tabla_frances['Saldo Final'],
    mode='lines+markers', name='Francés',
    line=dict(color=UDA_COLORS['primary'], width=2),
    marker=dict(size=6),
    hovertemplate='Período: %{x}<br>Saldo: $%{y:,.2f}<extra></extra>',
    showlegend=False
), row=2, col=1)

fig.add_trace(go.Scatter(
    x=tabla_aleman['Período'], y=tabla_aleman['Saldo Final'],
    mode='lines+markers', name='Alemán',
    line=dict(color=UDA_COLORS['danger'], width=2),
    marker=dict(size=6, symbol='square'),
    hovertemplate='Período: %{x}<br>Saldo: $%{y:,.2f}<extra></extra>',
    showlegend=False
), row=2, col=1)

# Gráfico 4: Intereses acumulados con área de ahorro
intereses_acum_frances = tabla_frances['Interés'].cumsum()
intereses_acum_aleman = tabla_aleman['Interés'].cumsum()

fig.add_trace(go.Scatter(
    x=tabla_frances['Período'], y=intereses_acum_frances,
    mode='lines+markers', name='Francés',
    line=dict(color=UDA_COLORS['primary'], width=2),
    marker=dict(size=6),
    hovertemplate='Período: %{x}<br>Intereses: $%{y:,.2f}<extra></extra>',
    showlegend=False
), row=2, col=2)

fig.add_trace(go.Scatter(
    x=tabla_aleman['Período'], y=intereses_acum_aleman,
    mode='lines+markers', name='Alemán',
    line=dict(color=UDA_COLORS['danger'], width=2),
    marker=dict(size=6, symbol='square'),
    hovertemplate='Período: %{x}<br>Intereses: $%{y:,.2f}<extra></extra>',
    showlegend=False
), row=2, col=2)

# Área de ahorro
fig.add_trace(go.Scatter(
    x=tabla_frances['Período'].tolist() + tabla_frances['Período'].tolist()[::-1],
    y=intereses_acum_aleman.tolist() + intereses_acum_frances.tolist()[::-1],
    fill='toself',
    fillcolor='rgba(40, 167, 69, 0.3)',
    line=dict(width=0),
    name='Ahorro Alemán',
    hoverinfo='skip',
    showlegend=False
), row=2, col=2)

# Layout general
fig.update_xaxes(title_text='Período', gridcolor='#E5E5E5', showgrid=True)
fig.update_yaxes(title_text='Cuota ($)', gridcolor='#E5E5E5', showgrid=True, row=1, col=1)
fig.update_yaxes(title_text='Monto ($)', gridcolor='#E5E5E5', showgrid=True, row=1, col=2)
fig.update_yaxes(title_text='Saldo ($)', gridcolor='#E5E5E5', showgrid=True, row=2, col=1)
fig.update_yaxes(title_text='Intereses ($)', gridcolor='#E5E5E5', showgrid=True, row=2, col=2)

fig.update_layout(
    title=dict(
        text='Comparación: Sistema Francés vs Alemán',
        font=dict(size=18, color=UDA_COLORS['primary']),
        x=0.5,
        xanchor='center'
    ),
    height=900,
    plot_bgcolor='white',
    paper_bgcolor='white',
    hovermode='closest',
    showlegend=True,
    legend=dict(x=0.5, y=-0.05, xanchor='center', orientation='h')
)

fig.show(config={'locale': 'es', 'displayModeBar': True, 'displaylogo': False})

print(f"\n💡 Conclusiones:")
print(f"1. Sistema Francés: Cuota constante, más predecible")
print(f"2. Sistema Alemán: Ahorra ${total_intereses - total_intereses_aleman:,.2f} en intereses")
print(f"3. Alemán requiere mayor capacidad de pago inicial (primera cuota más alta)")
print(f"4. Saldo se reduce más rápido en sistema Alemán")

# COMMAND ----------

# DBTITLE 1,Ejercicios Prácticos
# MAGIC %md
# MAGIC ## 💪 Ejercicios Prácticos
# MAGIC
# MAGIC ### Ejercicio 1: Valor de Anualidad
# MAGIC Recibirás $3,000 al final de cada semestre durante 8 años. Con tasa del 6% semestral:
# MAGIC a) ¿Cuál es el valor actual?
# MAGIC b) ¿Cuál sería el valor futuro al final del año 8?
# MAGIC
# MAGIC ### Ejercicio 2: Ahorro para Retiro
# MAGIC Quieres juntar $500,000 en 20 años ahorrando mensualmente. Con rendimiento del 8% anual:
# MAGIC a) ¿Cuánto debes ahorrar cada mes?
# MAGIC b) ¿Cuánto del total serán intereses ganados?
# MAGIC
# MAGIC ### Ejercicio 3: Préstamo Automotriz
# MAGIC Compras un auto de $30,000 con enganche del 20%. Financias el resto a 4 años al 9% anual (mensual):
# MAGIC a) ¿Cuál es tu cuota mensual?
# MAGIC b) Genera la tabla de amortización completa
# MAGIC c) ¿Cuánto habrás pagado de intereses al terminar?
# MAGIC
# MAGIC ### Ejercicio 4: Comparación
# MAGIC Préstamo de $80,000 a 24 meses con 1.5% mensual:
# MAGIC a) Genera ambas tablas (francesa y alemana)
# MAGIC b) Compara el total de intereses
# MAGIC c) ¿Cuál sistema conviene y por qué?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **💡 Tip**: Use las funciones y generadores de tablas de este notebook.

# COMMAND ----------

# DBTITLE 1,Espacio para Ejercicios
# Resuelva los ejercicios aquí

# Ejercicio 1


# Ejercicio 2


# Ejercicio 3


# Ejercicio 4


# COMMAND ----------

# DBTITLE 1,Resumen
# MAGIC %md
# MAGIC ## 📚 Resumen y Conclusiones
# MAGIC
# MAGIC ### Conceptos Clave
# MAGIC
# MAGIC 1. **Anualidades**: Serie de pagos iguales y periódicos
# MAGIC    * Valor actual: Suma descontada de todos los pagos
# MAGIC    * Valor futuro: Suma capitalizada
# MAGIC
# MAGIC 2. **Perpetuidades**: Anualidades infinitas
# MAGIC    * Simple: VA = Pago / r
# MAGIC    * Con crecimiento: VA = Pago / (r - g)
# MAGIC
# MAGIC 3. **Sistema Francés**:
# MAGIC    * Cuota constante
# MAGIC    * Más predecible
# MAGIC    * Más intereses totales
# MAGIC
# MAGIC 4. **Sistema Alemán**:
# MAGIC    * Amortización constante
# MAGIC    * Cuotas decrecientes
# MAGIC    * Menos intereses totales
# MAGIC    * Primera cuota más alta
# MAGIC
# MAGIC ### Fórmulas Esenciales
# MAGIC
# MAGIC **Valor Actual Anualidad**:
# MAGIC $$VA = Pago \times \frac{1 - (1+r)^{-n}}{r}$$
# MAGIC
# MAGIC **Valor Futuro Anualidad**:
# MAGIC $$VF = Pago \times \frac{(1+r)^n - 1}{r}$$
# MAGIC
# MAGIC **Cuota (Sistema Francés)**:
# MAGIC $$Cuota = VA \times \frac{r}{1 - (1+r)^{-n}}$$
# MAGIC
# MAGIC **Perpetuidad**:
# MAGIC $$VA = \frac{Pago}{r}$$
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🚀 Próximos Pasos
# MAGIC
# MAGIC * **Módulo 2**: Valoración de Instrumentos Financieros
# MAGIC   * Bonos (ya disponible)
# MAGIC   * Acciones
# MAGIC * **Módulo 4**: Riesgo y Portafolios
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🤖 Consultas con Genie
# MAGIC
# MAGIC * "Calcula la cuota de un préstamo de $X a Y meses al Z%"
# MAGIC * "Compara sistema francés vs alemán para mi caso"
# MAGIC * "Genera una tabla de amortización personalizada"
# MAGIC * "¿Cuánto debo ahorrar mensualmente para juntar $X en Y años?"
# MAGIC * "Explica qué es una perpetuidad con ejemplos reales"

# COMMAND ----------

