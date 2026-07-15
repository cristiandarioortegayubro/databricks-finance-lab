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
# MAGIC ### Módulo 03: Análisis Financiero
# MAGIC ### Notebook 3.1: Ratios Financieros
# MAGIC ### 📊 **LIQUIDEZ, ENDEUDAMIENTO Y RENTABILIDAD**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción
# MAGIC %md
# MAGIC # 3.1 - Ratios Financieros
# MAGIC
# MAGIC ## Objetivo del Módulo
# MAGIC Aprender a analizar la salud financiera de una empresa mediante ratios e indicadores clave.
# MAGIC
# MAGIC ## Conceptos Clave
# MAGIC * **Ratios de Liquidez**: Capacidad de pagar obligaciones de corto plazo
# MAGIC * **Ratios de Endeudamiento**: Estructura de capital y apalancamiento
# MAGIC * **Ratios de Actividad**: Eficiencia en el uso de activos
# MAGIC * **Ratios de Rentabilidad**: Capacidad de generar utilidades
# MAGIC * **Ratios de Valor de Mercado**: Valoración relativa de la empresa
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Referencias del Libro
# MAGIC %md
# MAGIC ## 📚 Referencias del Libro de Texto
# MAGIC
# MAGIC **Libro**: Finanzas Corporativas - Un Enfoque Latinoamericano (2ª ed.)
# MAGIC **Autor**: Guillermo L. Dumrauf
# MAGIC **Capítulos**: 2 y 3
# MAGIC **Ubicación**: `/Workspace/Shared/Databricks Finance Lab/Libros/Finanzas corporativas.pdf`
# MAGIC
# MAGIC ### 📝 Contenido cubierto:
# MAGIC
# MAGIC **Capítulo 2**: Panorama de estados financieros (pág. 25-52)
# MAGIC * Estado de resultados
# MAGIC * Balance general
# MAGIC * Estado de flujo de efectivo
# MAGIC * Impuestos
# MAGIC
# MAGIC **Capítulo 3**: Análisis financiero (pág. 53-82)
# MAGIC * Análisis vertical y horizontal
# MAGIC * Índices de liquidez (pág. 59-63)
# MAGIC * Índices de endeudamiento (pág. 63-67)
# MAGIC * Índices de actividad (pág. 67-71)
# MAGIC * Índices de rentabilidad (pág. 71-75)
# MAGIC * Índices de valor de mercado (pág. 75-78)
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

print("✓ Librerías cargadas")

# COMMAND ----------

# DBTITLE 1,Estados Financieros de Ejemplo
# MAGIC %md
# MAGIC ## 📊 Estados Financieros de Ejemplo
# MAGIC
# MAGIC Crearemos estados financieros simulados de una empresa para calcular los ratios.

# COMMAND ----------

# DBTITLE 1,Balance General
# Balance General (en miles de $)
balance = {
    'ACTIVOS': {
        'Activo Corriente': {
            'Efectivo y equivalentes': 50000,
            'Inversiones temporales': 30000,
            'Cuentas por cobrar': 120000,
            'Inventarios': 80000,
            'Total Activo Corriente': 280000
        },
        'Activo No Corriente': {
            'Propiedad, planta y equipo': 400000,
            'Depreciación acumulada': -100000,
            'Activos intangibles': 50000,
            'Total Activo No Corriente': 350000
        },
        'TOTAL ACTIVOS': 630000
    },
    'PASIVOS Y PATRIMONIO': {
        'Pasivo Corriente': {
            'Cuentas por pagar': 60000,
            'Deuda corto plazo': 40000,
            'Gastos acumulados': 30000,
            'Total Pasivo Corriente': 130000
        },
        'Pasivo No Corriente': {
            'Deuda largo plazo': 200000,
            'Total Pasivo No Corriente': 200000
        },
        'Patrimonio': {
            'Capital social': 150000,
            'Utilidades retenidas': 150000,
            'Total Patrimonio': 300000
        },
        'TOTAL PASIVOS Y PATRIMONIO': 630000
    }
}

# Crear DataFrame del Balance
df_balance = pd.DataFrame([
    {'Cuenta': 'Efectivo y equivalentes', 'Monto': 50000, 'Sección': 'Activo Corriente'},
    {'Cuenta': 'Inversiones temporales', 'Monto': 30000, 'Sección': 'Activo Corriente'},
    {'Cuenta': 'Cuentas por cobrar', 'Monto': 120000, 'Sección': 'Activo Corriente'},
    {'Cuenta': 'Inventarios', 'Monto': 80000, 'Sección': 'Activo Corriente'},
    {'Cuenta': 'Propiedad, planta y equipo (neto)', 'Monto': 300000, 'Sección': 'Activo No Corriente'},
    {'Cuenta': 'Activos intangibles', 'Monto': 50000, 'Sección': 'Activo No Corriente'},
    {'Cuenta': 'Cuentas por pagar', 'Monto': 60000, 'Sección': 'Pasivo Corriente'},
    {'Cuenta': 'Deuda corto plazo', 'Monto': 40000, 'Sección': 'Pasivo Corriente'},
    {'Cuenta': 'Gastos acumulados', 'Monto': 30000, 'Sección': 'Pasivo Corriente'},
    {'Cuenta': 'Deuda largo plazo', 'Monto': 200000, 'Sección': 'Pasivo No Corriente'},
    {'Cuenta': 'Capital social', 'Monto': 150000, 'Sección': 'Patrimonio'},
    {'Cuenta': 'Utilidades retenidas', 'Monto': 150000, 'Sección': 'Patrimonio'}
])

print("📊 BALANCE GENERAL (en miles de $)\n")
print("="*60)
for seccion in ['Activo Corriente', 'Activo No Corriente', 'Pasivo Corriente', 'Pasivo No Corriente', 'Patrimonio']:
    print(f"\n{seccion.upper()}:")
    seccion_df = df_balance[df_balance['Sección'] == seccion]
    for _, row in seccion_df.iterrows():
        print(f"  {row['Cuenta']:<40} ${row['Monto']:>10,}")
    print(f"  {'-'*52}")
    print(f"  Total {seccion:<33} ${seccion_df['Monto'].sum():>10,}")

print(f"\n{'='*60}")
print(f"TOTAL ACTIVOS: ${df_balance[df_balance['Sección'].str.contains('Activo')]['Monto'].sum():,}")
print(f"TOTAL PASIVOS Y PATRIMONIO: ${df_balance[~df_balance['Sección'].str.contains('Activo')]['Monto'].sum():,}")

# COMMAND ----------

# DBTITLE 1,Estado de Resultados
# Estado de Resultados (en miles de $)
estado_resultados = {
    'Ventas': 1000000,
    'Costo de ventas': -600000,
    'Utilidad bruta': 400000,
    'Gastos operativos': -200000,
    'EBIT (Utilidad operativa)': 200000,
    'Gastos financieros': -20000,
    'EBT (Utilidad antes de impuestos)': 180000,
    'Impuestos (30%)': -54000,
    'Utilidad neta': 126000
}

print("📈 ESTADO DE RESULTADOS (en miles de $)\n")
print("="*60)
for concepto, valor in estado_resultados.items():
    if concepto in ['Utilidad bruta', 'EBIT (Utilidad operativa)', 'EBT (Utilidad antes de impuestos)', 'Utilidad neta']:
        print(f"  {'-'*60}")
        print(f"  {concepto:<45} ${valor:>12,}")
    else:
        print(f"  {concepto:<45} ${valor:>12,}")
print("="*60)

# COMMAND ----------

# DBTITLE 1,Información de Mercado
# Información de mercado
info_mercado = {
    'Número de acciones': 100000,  # en miles
    'Precio por acción': 15,  # $
    'Dividendos por acción': 0.80  # $
}

print("📉 INFORMACIÓN DE MERCADO\n")
print(f"  Número de acciones en circulación: {info_mercado['Número de acciones']:,} mil")
print(f"  Precio por acción: ${info_mercado['Precio por acción']}")
print(f"  Dividendos por acción: ${info_mercado['Dividendos por acción']}")
print(f"  Capitalización de mercado: ${info_mercado['Número de acciones'] * info_mercado['Precio por acción'] * 1000:,}")

# COMMAND ----------

# DBTITLE 1,Ratios de Liquidez
# MAGIC %md
# MAGIC ## 1️⃣ Ratios de Liquidez
# MAGIC
# MAGIC **Miden**: Capacidad de la empresa para cumplir con sus obligaciones de corto plazo.
# MAGIC
# MAGIC ### 💧 Ratios principales:
# MAGIC
# MAGIC 1. **Razón Corriente (Current Ratio)**:
# MAGIC    $$\text{Razón Corriente} = \frac{\text{Activo Corriente}}{\text{Pasivo Corriente}}$$
# MAGIC
# MAGIC 2. **Prueba Ácida (Quick Ratio)**:
# MAGIC    $$\text{Prueba Ácida} = \frac{\text{Activo Corriente - Inventarios}}{\text{Pasivo Corriente}}$$
# MAGIC
# MAGIC 3. **Prueba Defensiva**:
# MAGIC    $$\text{Prueba Defensiva} = \frac{\text{Efectivo + Inversiones Temporales}}{\text{Pasivo Corriente}}$$

# COMMAND ----------

# DBTITLE 1,Cálculo Ratios de Liquidez
# Extraer valores del balance
activo_corriente = 280000
pasivo_corriente = 130000
efectivo = 50000
inversiones_temp = 30000
inventarios = 80000

# Calcular ratios de liquidez
razon_corriente = activo_corriente / pasivo_corriente
prueba_acida = (activo_corriente - inventarios) / pasivo_corriente
prueba_defensiva = (efectivo + inversiones_temp) / pasivo_corriente

# Capital de trabajo
capital_trabajo = activo_corriente - pasivo_corriente

ratios_liquidez = pd.DataFrame({
    'Ratio': ['Razón Corriente', 'Prueba Ácida', 'Prueba Defensiva', 'Capital de Trabajo'],
    'Fórmula': [
        'Activo Corriente / Pasivo Corriente',
        '(Act. Corriente - Inventarios) / Pas. Corriente',
        '(Efectivo + Inv. Temp) / Pas. Corriente',
        'Activo Corriente - Pasivo Corriente'
    ],
    'Valor': [razon_corriente, prueba_acida, prueba_defensiva, capital_trabajo],
    'Interpretación': [
        f'{razon_corriente:.2f} veces - Por cada $1 de deuda CP, hay ${razon_corriente:.2f} de activos CP',
        f'{prueba_acida:.2f} veces - Sin inventarios, hay ${prueba_acida:.2f} por cada $1 de deuda CP',
        f'{prueba_defensiva:.2f} veces - Con activos más líquidos',
        f'${capital_trabajo:,} - Excedente de activos CP sobre pasivos CP'
    ]
})

print("💧 RATIOS DE LIQUIDEZ\n")
for _, row in ratios_liquidez.iterrows():
    print(f"• {row['Ratio']}:")
    print(f"  Fórmula: {row['Fórmula']}")
    if isinstance(row['Valor'], float) and row['Ratio'] != 'Capital de Trabajo':
        print(f"  Resultado: {row['Valor']:.2f}x")
    else:
        print(f"  Resultado: ${row['Valor']:,.0f}" if row['Ratio'] == 'Capital de Trabajo' else f"  Resultado: {row['Valor']}")
    print(f"  {row['Interpretación']}")
    print()

print("💡 Referencia:")
print("  - Razón Corriente > 1.5: Buena liquidez")
print("  - Prueba Ácida > 1.0: Liquidez inmediata saludable")
print("  - Prueba Defensiva > 0.5: Capacidad de pago inmediata adecuada")

# COMMAND ----------

# DBTITLE 1,Ratios de Endeudamiento
# MAGIC %md
# MAGIC ## 2️⃣ Ratios de Endeudamiento (Apalancamiento)
# MAGIC
# MAGIC **Miden**: Proporción de financiamiento con deuda vs patrimonio.
# MAGIC
# MAGIC ### 🏛️ Ratios principales:
# MAGIC
# MAGIC 1. **Razón de Endeudamiento**:
# MAGIC    $$\text{Endeudamiento} = \frac{\text{Pasivo Total}}{\text{Activo Total}}$$
# MAGIC
# MAGIC 2. **Deuda a Patrimonio (D/E)**:
# MAGIC    $$\text{D/E} = \frac{\text{Pasivo Total}}{\text{Patrimonio}}$$
# MAGIC
# MAGIC 3. **Multiplicador de Capital**:
# MAGIC    $$\text{Mult. Capital} = \frac{\text{Activo Total}}{\text{Patrimonio}}$$
# MAGIC
# MAGIC 4. **Cobertura de Intereses**:
# MAGIC    $$\text{Cob. Intereses} = \frac{\text{EBIT}}{\text{Gastos Financieros}}$$

# COMMAND ----------

# DBTITLE 1,Cálculo Ratios de Endeudamiento
# Extraer valores
activo_total = 630000
pasivo_total = 330000  # Corriente + No Corriente
patrimonio = 300000
ebit = estado_resultados['EBIT (Utilidad operativa)']
gastos_financieros = abs(estado_resultados['Gastos financieros'])

# Calcular ratios de endeudamiento
endeudamiento = pasivo_total / activo_total
deuda_patrimonio = pasivo_total / patrimonio
multiplicador_capital = activo_total / patrimonio
cobertura_intereses = ebit / gastos_financieros

ratios_endeudamiento = pd.DataFrame({
    'Ratio': ['Endeudamiento', 'Deuda / Patrimonio', 'Multiplicador de Capital', 'Cobertura de Intereses'],
    'Fórmula': [
        'Pasivo Total / Activo Total',
        'Pasivo Total / Patrimonio',
        'Activo Total / Patrimonio',
        'EBIT / Gastos Financieros'
    ],
    'Valor': [endeudamiento, deuda_patrimonio, multiplicador_capital, cobertura_intereses],
    'Unidad': ['%', 'veces', 'veces', 'veces']
})

print("🏛️ RATIOS DE ENDEUDAMIENTO\n")
for _, row in ratios_endeudamiento.iterrows():
    print(f"• {row['Ratio']}:")
    print(f"  Fórmula: {row['Fórmula']}")
    if row['Unidad'] == '%':
        print(f"  Resultado: {row['Valor']*100:.1f}%")
    else:
        print(f"  Resultado: {row['Valor']:.2f}x")
    print()

print("💡 Interpretación:")
print(f"  - Endeudamiento: {endeudamiento*100:.1f}% de los activos están financiados con deuda")
print(f"  - D/E: Por cada $1 de patrimonio, hay ${deuda_patrimonio:.2f} de deuda")
print(f"  - Cobertura: El EBIT puede pagar {cobertura_intereses:.1f} veces los intereses")
print(f"\n🚨 Referencia:")
print(f"  - Endeudamiento < 50%: Bajo apalancamiento (conservador)")
print(f"  - Endeudamiento 50-70%: Apalancamiento moderado")
print(f"  - Endeudamiento > 70%: Alto apalancamiento (riesgoso)")
print(f"  - Cobertura > 3x: Buena capacidad de pago de intereses")

# COMMAND ----------

# DBTITLE 1,Ratios de Actividad
# MAGIC %md
# MAGIC ## 3️⃣ Ratios de Actividad (Eficiencia)
# MAGIC
# MAGIC **Miden**: Eficiencia en el uso de los activos de la empresa.
# MAGIC
# MAGIC ### ⚡ Ratios principales:
# MAGIC
# MAGIC 1. **Rotación de Cuentas por Cobrar**:
# MAGIC    $$\text{Rotación CxC} = \frac{\text{Ventas}}{\text{Cuentas por Cobrar}}$$
# MAGIC    
# MAGIC    **Período de Cobro**:
# MAGIC    $$\text{Días} = \frac{365}{\text{Rotación CxC}}$$
# MAGIC
# MAGIC 2. **Rotación de Inventarios**:
# MAGIC    $$\text{Rotación Inv} = \frac{\text{Costo de Ventas}}{\text{Inventarios}}$$
# MAGIC    
# MAGIC    **Días de Inventario**:
# MAGIC    $$\text{Días} = \frac{365}{\text{Rotación Inv}}$$
# MAGIC
# MAGIC 3. **Rotación de Activos Totales**:
# MAGIC    $$\text{Rotación Activos} = \frac{\text{Ventas}}{\text{Activo Total}}$$

# COMMAND ----------

# DBTITLE 1,Cálculo Ratios de Actividad
# Extraer valores
ventas = estado_resultados['Ventas']
costo_ventas = abs(estado_resultados['Costo de ventas'])
cuentas_cobrar = 120000

# Calcular ratios de actividad
rotacion_cxc = ventas / cuentas_cobrar
periodo_cobro = 365 / rotacion_cxc

rotacion_inventarios = costo_ventas / inventarios
dias_inventario = 365 / rotacion_inventarios

rotacion_activos = ventas / activo_total

ratios_actividad = pd.DataFrame({
    'Ratio': [
        'Rotación de CxC',
        'Período de Cobro',
        'Rotación de Inventarios',
        'Días de Inventario',
        'Rotación de Activos Totales'
    ],
    'Valor': [
        rotacion_cxc,
        periodo_cobro,
        rotacion_inventarios,
        dias_inventario,
        rotacion_activos
    ],
    'Unidad': ['veces', 'días', 'veces', 'días', 'veces']
})

print("⚡ RATIOS DE ACTIVIDAD (EFICIENCIA)\n")
for _, row in ratios_actividad.iterrows():
    print(f"• {row['Ratio']}: ", end="")
    if row['Unidad'] == 'veces':
        print(f"{row['Valor']:.2f}x")
    else:
        print(f"{row['Valor']:.1f} días")

print(f"\n💡 Interpretación:")
print(f"  - Las cuentas por cobrar rotan {rotacion_cxc:.1f} veces al año")
print(f"  - Se cobra en promedio cada {periodo_cobro:.0f} días")
print(f"  - El inventario se vende {rotacion_inventarios:.1f} veces al año")
print(f"  - El inventario dura en promedio {dias_inventario:.0f} días")
print(f"  - Por cada $1 de activos se generan ${rotacion_activos:.2f} de ventas")
print(f"\n🎯 Ciclo de Conversión de Efectivo:")
ciclo_operativo = periodo_cobro + dias_inventario
print(f"  Ciclo operativo: {ciclo_operativo:.0f} días (cobro + inventario)")

# COMMAND ----------

# DBTITLE 1,Ratios de Rentabilidad
# MAGIC %md
# MAGIC ## 4️⃣ Ratios de Rentabilidad
# MAGIC
# MAGIC **Miden**: Capacidad de la empresa para generar utilidades.
# MAGIC
# MAGIC ### 💰 Ratios principales:
# MAGIC
# MAGIC 1. **Margen Bruto**:
# MAGIC    $$\text{Margen Bruto} = \frac{\text{Utilidad Bruta}}{\text{Ventas}}$$
# MAGIC
# MAGIC 2. **Margen Operativo**:
# MAGIC    $$\text{Margen Operativo} = \frac{\text{EBIT}}{\text{Ventas}}$$
# MAGIC
# MAGIC 3. **Margen Neto**:
# MAGIC    $$\text{Margen Neto} = \frac{\text{Utilidad Neta}}{\text{Ventas}}$$
# MAGIC
# MAGIC 4. **ROA (Return on Assets)**:
# MAGIC    $$\text{ROA} = \frac{\text{Utilidad Neta}}{\text{Activo Total}}$$
# MAGIC
# MAGIC 5. **ROE (Return on Equity)**:
# MAGIC    $$\text{ROE} = \frac{\text{Utilidad Neta}}{\text{Patrimonio}}$$

# COMMAND ----------

# DBTITLE 1,Cálculo Ratios de Rentabilidad
# Extraer valores del estado de resultados
utilidad_bruta = estado_resultados['Utilidad bruta']
utilidad_neta = estado_resultados['Utilidad neta']

# Calcular ratios de rentabilidad
margen_bruto = utilidad_bruta / ventas
margen_operativo = ebit / ventas
margen_neto = utilidad_neta / ventas
roa = utilidad_neta / activo_total
roe = utilidad_neta / patrimonio

ratios_rentabilidad = pd.DataFrame({
    'Ratio': [
        'Margen Bruto',
        'Margen Operativo (EBIT)',
        'Margen Neto',
        'ROA (Return on Assets)',
        'ROE (Return on Equity)'
    ],
    'Valor': [
        margen_bruto,
        margen_operativo,
        margen_neto,
        roa,
        roe
    ],
    'Interpretación': [
        f'Por cada $1 de ventas, quedan ${margen_bruto:.2f} después del costo de ventas',
        f'Por cada $1 de ventas, quedan ${margen_operativo:.2f} de utilidad operativa',
        f'Por cada $1 de ventas, quedan ${margen_neto:.2f} de utilidad neta',
        f'Por cada $1 de activos, se generan ${roa:.2f} de utilidad',
        f'Por cada $1 de patrimonio, se generan ${roe:.2f} de utilidad'
    ]
})

print("💰 RATIOS DE RENTABILIDAD\n")
for _, row in ratios_rentabilidad.iterrows():
    print(f"• {row['Ratio']}: {row['Valor']*100:.2f}%")
    print(f"  {row['Interpretación']}")
    print()

# Análisis DuPont
print("🔍 ANÁLISIS DuPONT:")
print(f"\nROE = Margen Neto × Rotación Activos × Multiplicador Capital")
print(f"ROE = {margen_neto:.4f} × {rotacion_activos:.4f} × {multiplicador_capital:.4f}")
roe_dupont = margen_neto * rotacion_activos * multiplicador_capital
print(f"ROE = {roe_dupont*100:.2f}%")
print(f"\n✓ Verificación: ROE directo = {roe*100:.2f}%")
print(f"\n💡 El ROE se descompone en:")
print(f"  - Rentabilidad de ventas (margen): {margen_neto*100:.2f}%")
print(f"  - Eficiencia de activos (rotación): {rotacion_activos:.2f}x")
print(f"  - Apalancamiento financiero: {multiplicador_capital:.2f}x")

# COMMAND ----------

# DBTITLE 1,Ratios de Valor de Mercado
# MAGIC %md
# MAGIC ## 5️⃣ Ratios de Valor de Mercado
# MAGIC
# MAGIC **Miden**: Valoración de la empresa por el mercado.
# MAGIC
# MAGIC ### 💹 Ratios principales:
# MAGIC
# MAGIC 1. **EPS (Earnings Per Share)**:
# MAGIC    $$\text{EPS} = \frac{\text{Utilidad Neta}}{\text{Número de Acciones}}$$
# MAGIC
# MAGIC 2. **P/E (Price-Earnings Ratio)**:
# MAGIC    $$\text{P/E} = \frac{\text{Precio por Acción}}{\text{EPS}}$$
# MAGIC
# MAGIC 3. **P/B (Price-to-Book Ratio)**:
# MAGIC    $$\text{P/B} = \frac{\text{Precio por Acción}}{\text{Valor Libro por Acción}}$$
# MAGIC
# MAGIC 4. **Dividend Yield**:
# MAGIC    $$\text{Dividend Yield} = \frac{\text{Dividendo por Acción}}{\text{Precio por Acción}}$$

# COMMAND ----------

# DBTITLE 1,Cálculo Ratios de Mercado
# Extraer información
num_acciones = info_mercado['Número de acciones'] * 1000  # Convertir a unidades
precio_accion = info_mercado['Precio por acción']
dividendo_accion = info_mercado['Dividendos por acción']

# Calcular ratios de mercado
eps = (utilidad_neta * 1000) / num_acciones  # Convertir utilidad a unidades
valor_libro_accion = (patrimonio * 1000) / num_acciones
pe_ratio = precio_accion / eps
pb_ratio = precio_accion / valor_libro_accion
dividend_yield = dividendo_accion / precio_accion
cap_mercado = num_acciones * precio_accion

ratios_mercado = pd.DataFrame({
    'Ratio': [
        'EPS (Utilidad por Acción)',
        'Valor Libro por Acción',
        'P/E (Precio / Utilidad)',
        'P/B (Precio / Valor Libro)',
        'Dividend Yield',
        'Capitalización de Mercado'
    ],
    'Valor': [
        f'${eps:.2f}',
        f'${valor_libro_accion:.2f}',
        f'{pe_ratio:.2f}x',
        f'{pb_ratio:.2f}x',
        f'{dividend_yield*100:.2f}%',
        f'${cap_mercado:,.0f}'
    ],
    'Interpretación': [
        f'La empresa genera ${eps:.2f} de utilidad por cada acción',
        f'Cada acción tiene un valor contable de ${valor_libro_accion:.2f}',
        f'Los inversores pagan {pe_ratio:.1f} veces las utilidades',
        f'El precio es {pb_ratio:.2f} veces el valor libro',
        f'Rentabilidad por dividendos: {dividend_yield*100:.2f}% anual',
        f'Valor total de mercado de la empresa'
    ]
})

print("💹 RATIOS DE VALOR DE MERCADO\n")
for _, row in ratios_mercado.iterrows():
    print(f"• {row['Ratio']}: {row['Valor']}")
    print(f"  {row['Interpretación']}")
    print()

print("💡 Comparación Mercado vs Contable:")
print(f"  - Precio de mercado: ${precio_accion}")
print(f"  - Valor libro: ${valor_libro_accion:.2f}")
if precio_accion > valor_libro_accion:
    print(f"  - La acción cotiza CON PRIMA ({(precio_accion/valor_libro_accion - 1)*100:.1f}% sobre valor libro)")
else:
    print(f"  - La acción cotiza CON DESCUENTO")

# COMMAND ----------

# DBTITLE 1,Dashboard de Ratios
# MAGIC %md
# MAGIC ## 📊 Dashboard: Resumen de Todos los Ratios

# COMMAND ----------

# DBTITLE 1,Tabla Resumen
# Crear tabla resumen consolidada
resumen_todos = pd.DataFrame({
    'Categoría': [
        'Liquidez', 'Liquidez', 'Liquidez',
        'Endeudamiento', 'Endeudamiento', 'Endeudamiento',
        'Actividad', 'Actividad', 'Actividad',
        'Rentabilidad', 'Rentabilidad', 'Rentabilidad', 'Rentabilidad',
        'Mercado', 'Mercado', 'Mercado'
    ],
    'Ratio': [
        'Razón Corriente', 'Prueba Ácida', 'Capital de Trabajo',
        'Endeudamiento', 'D/E', 'Cobertura Intereses',
        'Rotación CxC', 'Rotación Inventarios', 'Rotación Activos',
        'Margen Bruto', 'Margen Operativo', 'Margen Neto', 'ROE',
        'EPS', 'P/E', 'Dividend Yield'
    ],
    'Valor': [
        f'{razon_corriente:.2f}x', f'{prueba_acida:.2f}x', f'${capital_trabajo:,.0f}',
        f'{endeudamiento*100:.1f}%', f'{deuda_patrimonio:.2f}x', f'{cobertura_intereses:.1f}x',
        f'{rotacion_cxc:.1f}x', f'{rotacion_inventarios:.1f}x', f'{rotacion_activos:.2f}x',
        f'{margen_bruto*100:.1f}%', f'{margen_operativo*100:.1f}%', f'{margen_neto*100:.1f}%', f'{roe*100:.1f}%',
        f'${eps:.2f}', f'{pe_ratio:.1f}x', f'{dividend_yield*100:.2f}%'
    ],
    'Benchmark': [
        '> 1.5', '> 1.0', 'Positivo',
        '< 50%', '< 1.0', '> 3.0',
        'Industria', 'Industria', 'Industria',
        'Industria', 'Industria', '> 10%', '> 15%',
        'Industria', 'Industria', 'Industria'
    ]
})

print("📄 RESUMEN COMPLETO DE RATIOS FINANCIEROS\n")
print(resumen_todos.to_string(index=False))
print("\n" + "="*80)

# COMMAND ----------

# DBTITLE 1,Visualización Dashboard
# Crear dashboard visual
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Gráfico 1: Ratios de Liquidez
ax1 = axes[0, 0]
categorias_liq = ['Razón\nCorriente', 'Prueba\nÁcida', 'Prueba\nDefensiva']
valores_liq = [razon_corriente, prueba_acida, prueba_defensiva]
referencias_liq = [1.5, 1.0, 0.5]
ax1.bar(categorias_liq, valores_liq, color=['green' if v > r else 'orange' for v, r in zip(valores_liq, referencias_liq)], alpha=0.7, edgecolor='black')
ax1.axhline(y=1, color='red', linestyle='--', linewidth=2, label='Mínimo aceptable')
for i, v in enumerate(valores_liq):
    ax1.text(i, v + 0.05, f'{v:.2f}x', ha='center', fontweight='bold', fontsize=11)
ax1.set_ylabel('Veces', fontsize=12, fontweight='bold')
ax1.set_title('Ratios de Liquidez', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3, axis='y')

# Gráfico 2: Estructura de Capital
ax2 = axes[0, 1]
labels_capital = ['Deuda', 'Patrimonio']
valores_capital = [pasivo_total, patrimonio]
colores_capital = ['#ff6b6b', '#4ecdc4']
ax2.pie(valores_capital, labels=labels_capital, autopct='%1.1f%%', colors=colores_capital, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
ax2.set_title(f'Estructura de Capital\n(Endeudamiento: {endeudamiento*100:.1f}%)', fontsize=14, fontweight='bold')

# Gráfico 3: Márgenes de Rentabilidad
ax3 = axes[1, 0]
categorias_rent = ['Margen\nBruto', 'Margen\nOperativo', 'Margen\nNeto']
valores_rent = [margen_bruto*100, margen_operativo*100, margen_neto*100]
colores_rent = ['#95e1d3', '#38ada9', '#079992']
bars = ax3.bar(categorias_rent, valores_rent, color=colores_rent, alpha=0.8, edgecolor='black')
for bar, v in zip(bars, valores_rent):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 1, f'{v:.1f}%', ha='center', fontweight='bold', fontsize=11)
ax3.set_ylabel('Porcentaje (%)', fontsize=12, fontweight='bold')
ax3.set_title('Márgenes de Rentabilidad', fontsize=14, fontweight='bold')
ax3.grid(True, alpha=0.3, axis='y')

# Gráfico 4: ROA vs ROE
ax4 = axes[1, 1]
ratios_rendimiento = ['ROA', 'ROE']
valores_rendimiento = [roa*100, roe*100]
colores_rend = ['#f38181', '#aa96da']
bars2 = ax4.barh(ratios_rendimiento, valores_rendimiento, color=colores_rend, alpha=0.8, edgecolor='black')
for bar, v in zip(bars2, valores_rendimiento):
    width = bar.get_width()
    ax4.text(width + 1, bar.get_y() + bar.get_height()/2., f'{v:.1f}%', va='center', fontweight='bold', fontsize=12)
ax4.set_xlabel('Porcentaje (%)', fontsize=12, fontweight='bold')
ax4.set_title('Retorno sobre Activos y Patrimonio', fontsize=14, fontweight='bold')
ax4.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
display(plt.show())

print("📊 Dashboard generado con éxito")

# COMMAND ----------

# DBTITLE 1,Ejercicios
# MAGIC %md
# MAGIC ## 💪 Ejercicios Prácticos
# MAGIC
# MAGIC ### Ejercicio 1: Cálculo de Ratios Básicos
# MAGIC
# MAGIC Dados los siguientes datos de la Empresa XYZ (en miles):
# MAGIC * Activo Corriente: $200,000
# MAGIC * Inventarios: $60,000
# MAGIC * Pasivo Corriente: $120,000
# MAGIC * Pasivo Total: $300,000
# MAGIC * Activo Total: $500,000
# MAGIC * Ventas: $800,000
# MAGIC * Utilidad Neta: $80,000
# MAGIC * Patrimonio: $200,000
# MAGIC
# MAGIC **Calcule**:
# MAGIC a) Razón Corriente
# MAGIC b) Prueba Ácida
# MAGIC c) Endeudamiento
# MAGIC d) ROA
# MAGIC e) ROE
# MAGIC
# MAGIC ### Ejercicio 2: Análisis DuPont
# MAGIC
# MAGIC Empresa ABC tiene:
# MAGIC * Margen Neto: 8%
# MAGIC * Rotación de Activos: 1.5x
# MAGIC * Multiplicador de Capital: 2.0x
# MAGIC
# MAGIC a) Calcule el ROE usando el modelo DuPont
# MAGIC b) ¿Qué componente tiene mayor impacto?
# MAGIC c) Si la empresa quiere aumentar ROE a 30%, ¿qué estrategias podría usar?
# MAGIC
# MAGIC ### Ejercicio 3: Comparación de Empresas
# MAGIC
# MAGIC Compare estas dos empresas del mismo sector:
# MAGIC
# MAGIC **Empresa A**:
# MAGIC * ROE: 18%, ROA: 12%, Endeudamiento: 40%
# MAGIC
# MAGIC **Empresa B**:
# MAGIC * ROE: 20%, ROA: 10%, Endeudamiento: 60%
# MAGIC
# MAGIC a) ¿Cuál es más rentable operativamente?
# MAGIC b) ¿Cuál usa más apalancamiento?
# MAGIC c) ¿Cuál es menos riesgosa?
# MAGIC d) ¿En cuál invertirías?
# MAGIC
# MAGIC ### Ejercicio 4: Ratios de Mercado
# MAGIC
# MAGIC Una empresa tiene:
# MAGIC * Utilidad Neta: $5,000,000
# MAGIC * Acciones en circulación: 1,000,000
# MAGIC * Precio por acción: $75
# MAGIC * Dividendo anual por acción: $2
# MAGIC * Patrimonio: $40,000,000
# MAGIC
# MAGIC a) Calcule EPS
# MAGIC b) Calcule P/E
# MAGIC c) Calcule P/B
# MAGIC d) Calcule Dividend Yield
# MAGIC e) ¿La acción está cara o barata según P/E?
# MAGIC
# MAGIC ---

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
# MAGIC ### Las 5 Categorías de Ratios Financieros
# MAGIC
# MAGIC #### 1️⃣ Liquidez
# MAGIC * **Qué miden**: Capacidad de pagar deudas de corto plazo
# MAGIC * **Ratios clave**: Razón Corriente, Prueba Ácida
# MAGIC * **Interpretación**: > 1.5 es saludable
# MAGIC
# MAGIC #### 2️⃣ Endeudamiento
# MAGIC * **Qué miden**: Proporción de financiamiento con deuda
# MAGIC * **Ratios clave**: Endeudamiento, D/E, Cobertura de Intereses
# MAGIC * **Interpretación**: < 50% es conservador, > 70% es riesgoso
# MAGIC
# MAGIC #### 3️⃣ Actividad
# MAGIC * **Qué miden**: Eficiencia en uso de activos
# MAGIC * **Ratios clave**: Rotación de CxC, Inventarios, Activos
# MAGIC * **Interpretación**: Mayor rotación = Mayor eficiencia
# MAGIC
# MAGIC #### 4️⃣ Rentabilidad
# MAGIC * **Qué miden**: Capacidad de generar utilidades
# MAGIC * **Ratios clave**: Márgenes (Bruto, Operativo, Neto), ROA, ROE
# MAGIC * **Interpretación**: ROE > 15% es excelente
# MAGIC
# MAGIC #### 5️⃣ Valor de Mercado
# MAGIC * **Qué miden**: Valoración por el mercado
# MAGIC * **Ratios clave**: EPS, P/E, P/B, Dividend Yield
# MAGIC * **Interpretación**: Depende del sector y crecimiento
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Análisis DuPont
# MAGIC
# MAGIC **Descompone el ROE en 3 componentes**:
# MAGIC
# MAGIC $$ROE = \underbrace{\frac{\text{Utilidad}}{\text{Ventas}}}_{\text{Rentabilidad}} \times \underbrace{\frac{\text{Ventas}}{\text{Activos}}}_{\text{Eficiencia}} \times \underbrace{\frac{\text{Activos}}{\text{Patrimonio}}}_{\text{Apalancamiento}}$$
# MAGIC
# MAGIC **Permite identificar**:
# MAGIC * ¿La empresa es rentable por márgenes altos?
# MAGIC * ¿O por eficiencia operativa?
# MAGIC * ¿O por uso de apalancamiento financiero?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 Puntos Clave
# MAGIC
# MAGIC 1. **Ningún ratio es suficiente solo**: Analiza en conjunto
# MAGIC 2. **Compara con**: Industria, competidores, historia propia
# MAGIC 3. **Contexto importa**: Un ratio "malo" puede ser estratégico
# MAGIC 4. **Tendencias > Valores absolutos**: Mejorando o empeorando
# MAGIC 5. **Ratios de mercado son expectativas**: Reflejan futuro, no pasado
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🚀 Próximos Pasos
# MAGIC
# MAGIC * **Capítulo 4 del libro**: Planificación financiera de largo plazo
# MAGIC * **Módulo 04**: Riesgo y portafolios
# MAGIC * **Práctica**: Analizar empresas reales con yfinance
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🤖 Consultas con Genie
# MAGIC
# MAGIC * "Calcula todos los ratios financieros de [EMPRESA] usando datos de yfinance"
# MAGIC * "Compara los ratios de estas 3 empresas y recomiéndame la mejor inversión"
# MAGIC * "Explica por qué el ROE de [EMPRESA] es alto pero el ROA es bajo"
# MAGIC * "Crea un dashboard interactivo de ratios financieros"
# MAGIC * "Analiza la evolución histórica de ratios de [EMPRESA] últimos 5 años"
# MAGIC * "Implementa el análisis DuPont para mi empresa"

# COMMAND ----------

