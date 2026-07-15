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
# MAGIC ### Módulo 00: Nivelación en Python
# MAGIC ### Notebook 0.7: Python Aplicado a Finanzas
# MAGIC ### 🎓 **NOTEBOOK FINAL - INTEGRACIÓN COMPLETA**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción - El Camino Recorrido
# MAGIC %md
# MAGIC # 🎓 Introducción: El Camino Recorrido
# MAGIC
# MAGIC ## 🎉 ¡Felicitaciones!
# MAGIC
# MAGIC Has llegado al **último notebook** del Módulo 00 - Nivelación en Python. Este notebook es **diferente**: aquí integraremos **TODO** lo aprendido en casos **REALES** de finanzas.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📚 Repaso Completo: ¿Qué aprendiste?
# MAGIC
# MAGIC ### 🟢 **0.1 - Introducción a Python**
# MAGIC ✅ Variables y tipos de datos (int, float, str, bool)
# MAGIC ✅ Operadores aritméticos (+, -, *, /, **, //, %)
# MAGIC ✅ Strings y formato con f-strings
# MAGIC ✅ Conversión de tipos (int(), float(), str())
# MAGIC
# MAGIC ### 🟡 **0.2 - Estructuras de Control**
# MAGIC ✅ Condicionales (if, elif, else)
# MAGIC ✅ Operadores lógicos (and, or, not)
# MAGIC ✅ Bucles (for, while)
# MAGIC ✅ Control de flujo (break, continue)
# MAGIC ✅ List comprehensions
# MAGIC
# MAGIC ### 🟠 **0.3 - Funciones y Módulos**
# MAGIC ✅ Crear funciones reutilizables
# MAGIC ✅ Parámetros y valores de retorno
# MAGIC ✅ Funciones lambda
# MAGIC ✅ Importar librerías (math, datetime)
# MAGIC
# MAGIC ### 🟭 **0.4 - Estructuras de Datos**
# MAGIC ✅ Listas, tuplas, sets
# MAGIC ✅ Diccionarios
# MAGIC ✅ Métodos de estructuras
# MAGIC ✅ Manipulación avanzada
# MAGIC
# MAGIC ### 🔵 **0.5 - Pandas para Finanzas**
# MAGIC ✅ DataFrames: crear, leer, manipular
# MAGIC ✅ Filtrado y selección
# MAGIC ✅ Agregaciones y group by
# MAGIC ✅ Series temporales
# MAGIC ✅ Merge y join
# MAGIC
# MAGIC ### 🟪 **0.6 - Visualización de Datos**
# MAGIC ✅ Matplotlib (gráficos estáticos)
# MAGIC ✅ Seaborn (gráficos estadísticos)
# MAGIC ✅ Plotly (gráficos interactivos)
# MAGIC ✅ Heatmaps y correlaciones
# MAGIC ✅ Candlestick charts
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎯 Objetivos de Este Notebook
# MAGIC
# MAGIC Este notebook es tu **graduación** del Módulo 00. Aquí vas a:
# MAGIC
# MAGIC 👉 **Integrar TODO**: Variables + Funciones + Pandas + Visualizaciones
# MAGIC 👉 **Casos REALES**: No más toy examples, sino análisis profesionales
# MAGIC 👉 **Buenas prácticas**: Código limpio, modular, documentado
# MAGIC 👉 **Biblioteca personal**: Tu propia caja de herramientas financieras
# MAGIC 👉 **Preparación completa**: Listo para los Módulos 01-05
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 💼 Casos que Desarrollaremos
# MAGIC
# MAGIC 1. 🧮 **Calculadora Financiera Completa** (VAN, TIR, VF, VP)
# MAGIC 2. 📊 **Análisis de Portafolio** (rendimiento, riesgo, correlaciones)
# MAGIC 3. 💹 **Sistema de Trading Simple** (backtesting, reglas)
# MAGIC 4. 📈 **Valuación de Bonos** (precio, duration, YTM)
# MAGIC 5. ⚠️ **Análisis de Riesgo** (VaR, simulación Monte Carlo)
# MAGIC 6. 📊 **Dashboard Ejecutivo** (integración total)
# MAGIC 7. 📄 **Automatización de Reportes** (loops, export)
# MAGIC 8. 📉 **Series Temporales Financieras** (tendencias, MA, RSI)
# MAGIC
# MAGIC **+** Biblioteca personal con 25+ funciones financieras
# MAGIC
# MAGIC **+** Buenas prácticas y código profesional
# MAGIC
# MAGIC **+** Proyecto final integrador
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🚀 ¿Estás listo?
# MAGIC
# MAGIC Después de este notebook, estarás **completamente preparado** para:
# MAGIC
# MAGIC ✅ Analizar portafolios de inversión
# MAGIC ✅ Construir modelos financieros
# MAGIC ✅ Automatizar reportes
# MAGIC ✅ Crear dashboards profesionales
# MAGIC ✅ **Empezar el Módulo 01 del curso principal**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⏱️ **Tiempo estimado**: 90-120 minutos
# MAGIC
# MAGIC 💪 **Tip**: Este notebook es largo y completo. Tómate tu tiempo, ejecuta cada celda, experimenta con el código.
# MAGIC
# MAGIC ¡Empecemos!

# COMMAND ----------

# DBTITLE 1,Explicación - Importar Librerías
# MAGIC %md
# MAGIC ## 📦 Importar Todas las Librerías
# MAGIC
# MAGIC Empezamos importando **todas** las librerías que usaremos en este notebook:
# MAGIC
# MAGIC * **numpy**: Cálculos numéricos
# MAGIC * **pandas**: Manipulación de datos
# MAGIC * **matplotlib**: Visualizaciones estáticas
# MAGIC * **seaborn**: Visualizaciones estadísticas
# MAGIC * **plotly**: Visualizaciones interactivas
# MAGIC * **datetime**: Manejo de fechas
# MAGIC * **math**: Funciones matemáticas

# COMMAND ----------

# DBTITLE 1,Código - Importar Librerías
# Librerías de visualización
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Librerías de datos
import numpy as np
import pandas as pd

# Librerías de fecha y tiempo
from datetime import datetime, timedelta, date
import calendar

# Librerías matemáticas
import math
from scipy import stats
from scipy.optimize import fsolve

# Configuración
import warnings
warnings.filterwarnings('ignore')

# Configuración de visualizaciones
sns.set_theme(style="whitegrid")
plt.style.use('seaborn-v0_8-darkgrid')

# Semilla para reproducibilidad
np.random.seed(42)

print("═" * 70)
print("            PYTHON APLICADO A FINANZAS - NOTEBOOK FINAL")
print("═" * 70)
print("\n✅ Todas las librerías importadas correctamente")
print(f"\n📚 Versiones:")
print(f"   NumPy: {np.__version__}")
print(f"   Pandas: {pd.__version__}")
print(f"   Matplotlib: {plt.matplotlib.__version__}")
print(f"   Seaborn: {sns.__version__}")
print(f"\n¡Listo para empezar! 🚀")

# COMMAND ----------

# DBTITLE 1,CASO 1 - Calculadora Financiera
# MAGIC %md
# MAGIC # 🧮 CASO 1: Calculadora Financiera Completa
# MAGIC
# MAGIC ## Objetivo
# MAGIC
# MAGIC Crear una **biblioteca de funciones financieras** para cálculos fundamentales:
# MAGIC
# MAGIC * **VAN** (Valor Actual Neto)
# MAGIC * **TIR** (Tasa Interna de Retorno)
# MAGIC * **VF** (Valor Futuro)
# MAGIC * **VP** (Valor Presente)
# MAGIC * **Cuota de Préstamo**
# MAGIC * **Tabla de Amortización**
# MAGIC
# MAGIC ### ¿Qué integramos?
# MAGIC
# MAGIC ✅ **Funciones** (def, return, docstrings)
# MAGIC ✅ **Condicionales** (if, elif, else)
# MAGIC ✅ **Bucles** (for, while)
# MAGIC ✅ **Listas y diccionarios**
# MAGIC ✅ **Pandas** (DataFrames)
# MAGIC ✅ **Visualizaciones** (Plotly)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Funciones a Implementar
# MAGIC
# MAGIC ### 1. Valor Presente (VP)
# MAGIC
# MAGIC Calcular el valor hoy de un monto futuro:
# MAGIC
# MAGIC $$VP = \frac{VF}{(1 + r)^n}$$
# MAGIC
# MAGIC ### 2. Valor Futuro (VF)
# MAGIC
# MAGIC Calcular el valor futuro de un capital presente:
# MAGIC
# MAGIC $$VF = VP \times (1 + r)^n$$
# MAGIC
# MAGIC ### 3. Valor Actual Neto (VAN)
# MAGIC
# MAGIC Valuar un proyecto descontando flujos futuros:
# MAGIC
# MAGIC $$VAN = -I_0 + \sum_{t=1}^{n} \frac{FC_t}{(1 + r)^t}$$
# MAGIC
# MAGIC ### 4. Tasa Interna de Retorno (TIR)
# MAGIC
# MAGIC La tasa que hace VAN = 0
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Implementemos estas funciones de forma profesional.

# COMMAND ----------

# DBTITLE 1,Código - Funciones Financieras Básicas
# =============================================================================
# CALCULADORA FINANCIERA - FUNCIONES BÁSICAS
# =============================================================================

def valor_presente(valor_futuro, tasa, periodos):
    """
    Calcula el Valor Presente de un monto futuro.
    
    Parámetros:
    -----------
    valor_futuro : float
        Monto futuro a descontar
    tasa : float
        Tasa de descuento por período (decimal, ej: 0.05 para 5%)
    periodos : int
        Número de períodos
    
    Retorna:
    --------
    float : Valor presente
    
    Ejemplo:
    --------
    >>> valor_presente(100000, 0.10, 5)
    62092.13
    """
    return valor_futuro / ((1 + tasa) ** periodos)


def valor_futuro(valor_presente, tasa, periodos):
    """
    Calcula el Valor Futuro de un capital presente.
    
    Parámetros:
    -----------
    valor_presente : float
        Capital inicial
    tasa : float
        Tasa de interés por período (decimal)
    periodos : int
        Número de períodos
    
    Retorna:
    --------
    float : Valor futuro
    """
    return valor_presente * ((1 + tasa) ** periodos)


def van(flujos, tasa):
    """
    Calcula el Valor Actual Neto (VAN) de un proyecto.
    
    Parámetros:
    -----------
    flujos : list
        Lista de flujos de efectivo. El primer elemento es la inversión inicial (negativa).
        Ejemplo: [-10000, 3000, 4000, 5000, 3000]
    tasa : float
        Tasa de descuento (decimal)
    
    Retorna:
    --------
    float : VAN del proyecto
    """
    van_total = 0
    for t, flujo in enumerate(flujos):
        van_total += flujo / ((1 + tasa) ** t)
    return van_total


def tir(flujos, aproximacion_inicial=0.1):
    """
    Calcula la Tasa Interna de Retorno (TIR) de un proyecto.
    
    Parámetros:
    -----------
    flujos : list
        Lista de flujos de efectivo
    aproximacion_inicial : float
        Valor inicial para el algoritmo iterativo
    
    Retorna:
    --------
    float : TIR del proyecto (decimal)
    """
    def van_para_tir(tasa):
        return van(flujos, tasa)
    
    try:
        resultado = fsolve(van_para_tir, aproximacion_inicial)
        return resultado[0]
    except:
        return None


def cuota_prestamo(monto, tasa_anual, anios, pagos_por_anio=12):
    """
    Calcula la cuota de un préstamo con sistema francés.
    
    Parámetros:
    -----------
    monto : float
        Monto del préstamo
    tasa_anual : float
        Tasa anual (decimal)
    anios : int
        Plazo en años
    pagos_por_anio : int
        Número de pagos por año (default: 12 para mensual)
    
    Retorna:
    --------
    float : Cuota periódica
    """
    tasa_periodo = tasa_anual / pagos_por_anio
    num_pagos = anios * pagos_por_anio
    
    if tasa_periodo == 0:
        return monto / num_pagos
    
    cuota = monto * (tasa_periodo * (1 + tasa_periodo)**num_pagos) / \
            ((1 + tasa_periodo)**num_pagos - 1)
    return cuota


def tabla_amortizacion(monto, tasa_anual, anios, pagos_por_anio=12):
    """
    Genera una tabla de amortización completa.
    
    Retorna:
    --------
    DataFrame : Tabla con columnas: Periodo, Saldo_Inicial, Interes, Amortizacion, Cuota, Saldo_Final
    """
    cuota = cuota_prestamo(monto, tasa_anual, anios, pagos_por_anio)
    tasa_periodo = tasa_anual / pagos_por_anio
    num_pagos = anios * pagos_por_anio
    
    tabla = []
    saldo = monto
    
    for periodo in range(1, num_pagos + 1):
        interes = saldo * tasa_periodo
        amortizacion = cuota - interes
        saldo_final = saldo - amortizacion
        
        tabla.append({
            'Periodo': periodo,
            'Saldo_Inicial': saldo,
            'Interes': interes,
            'Amortizacion': amortizacion,
            'Cuota': cuota,
            'Saldo_Final': max(0, saldo_final)  # Evitar negativos por redondeo
        })
        
        saldo = saldo_final
    
    return pd.DataFrame(tabla)


print("✅ Funciones financieras básicas creadas:")
print("   • valor_presente()")
print("   • valor_futuro()")
print("   • van()")
print("   • tir()")
print("   • cuota_prestamo()")
print("   • tabla_amortizacion()")
print("\n🚀 Listas para usar!")

# COMMAND ----------

# DBTITLE 1,Explicación - Ejemplos de Uso
# MAGIC %md
# MAGIC ## 💼 Ejemplos Prácticos: Evaluación de Proyecto
# MAGIC
# MAGIC Vamos a usar nuestras funciones para **evaluar un proyecto de inversión real**:
# MAGIC
# MAGIC **Caso**: Una empresa argentina quiere invertir en maquinaria nueva.
# MAGIC
# MAGIC * **Inversión inicial**: $10,000,000
# MAGIC * **Flujos esperados** (5 años): $2.5M, $3M, $3.5M, $3M, $2M
# MAGIC * **Tasa de descuento**: 12% anual
# MAGIC
# MAGIC 🎯 **Preguntas**:
# MAGIC 1. ¿Cuál es el VAN del proyecto?
# MAGIC 2. ¿Cuál es la TIR?
# MAGIC 3. ¿Se debe aceptar el proyecto?

# COMMAND ----------

# DBTITLE 1,Código - Ejemplo Proyecto
# ===== EVALUACIÓN DE PROYECTO =====

print("═" * 70)
print("EVALUACIÓN DE PROYECTO DE INVERSIÓN")
print("═" * 70)

# Datos del proyecto
inversion_inicial = -10_000_000  # Negativo porque es salida de efectivo
flujos_anuales = [2_500_000, 3_000_000, 3_500_000, 3_000_000, 2_000_000]
flujos_completos = [inversion_inicial] + flujos_anuales
tasa_descuento = 0.12  # 12%

print(f"\n💰 Inversión inicial: ${abs(inversion_inicial):,.0f}")
print(f"\n📈 Flujos anuales proyectados:")
for i, flujo in enumerate(flujos_anuales, 1):
    print(f"   Año {i}: ${flujo:,.0f}")
print(f"\n📊 Tasa de descuento: {tasa_descuento * 100}%")

# Calcular VAN
van_proyecto = van(flujos_completos, tasa_descuento)

print(f"\n{'═' * 70}")
print(f"RESULTADOS:")
print(f"{'═' * 70}")
print(f"\n1️⃣ VAN del proyecto: ${van_proyecto:,.2f}")

if van_proyecto > 0:
    print(f"   ✅ VAN positivo: El proyecto CREA valor")
else:
    print(f"   ❌ VAN negativo: El proyecto DESTRUYE valor")

# Calcular TIR
tir_proyecto = tir(flujos_completos)

print(f"\n2️⃣ TIR del proyecto: {tir_proyecto * 100:.2f}%")

if tir_proyecto > tasa_descuento:
    print(f"   ✅ TIR ({tir_proyecto * 100:.2f}%) > Tasa descuento ({tasa_descuento * 100}%)")
    print(f"   El proyecto rinde MAS que el costo de capital")
else:
    print(f"   ❌ TIR menor que la tasa de descuento")

# Decisión
print(f"\n{'═' * 70}")
print(f"3️⃣ DECISIÓN FINAL:")

if van_proyecto > 0 and tir_proyecto > tasa_descuento:
    print(f"   🟢 ACEPTAR EL PROYECTO")
    print(f"   Razones:")
    print(f"   • VAN positivo: Crea ${van_proyecto:,.0f} de valor")
    print(f"   • TIR superior a la tasa de descuento")
    print(f"   • Retorno sobre la inversión: {(tir_proyecto - tasa_descuento) * 100:.2f}% adicional")
else:
    print(f"   🔴 RECHAZAR EL PROYECTO")
    print(f"   No cumple con los criterios mínimos de rentabilidad")

print(f"\n{'═' * 70}")

# Análisis adicional: Payback Period
print(f"\n🔎 ANÁLISIS ADICIONAL: Período de Recuperación (Payback)")
print(f"{'-' * 70}")

acumulado = inversion_inicial
for i, flujo in enumerate(flujos_anuales, 1):
    acumulado += flujo
    print(f"Año {i}: Acumulado = ${acumulado:,.0f}")
    
    if acumulado > 0 and i > 0:
        # Interpolación para encontrar el mes exacto
        flujo_anio_recuperacion = flujos_anuales[i-1]
        saldo_previo = acumulado - flujo_anio_recuperacion
        meses_adicionales = abs(saldo_previo / flujo_anio_recuperacion) * 12
        
        print(f"\n✅ Inversión recuperada en: {i-1} años y {meses_adicionales:.1f} meses")
        break

# COMMAND ----------

# DBTITLE 1,CASO 2 - Análisis de Portafolio
# MAGIC %md
# MAGIC # 📊 CASO 2: Análisis Completo de Portafolio
# MAGIC
# MAGIC ## Objetivo
# MAGIC
# MAGIC Analizar un portafolio de **5 acciones argentinas** calculando:
# MAGIC
# MAGIC 1. **Rendimientos individuales** y del portafolio
# MAGIC 2. **Volatilidad** (riesgo)
# MAGIC 3. **Ratio Sharpe** (rendimiento ajustado por riesgo)
# MAGIC 4. **Matriz de correlaciones**
# MAGIC 5. **Diversificación** del portafolio
# MAGIC 6. **Visualizaciones** profesionales
# MAGIC
# MAGIC ### ¿Qué integramos?
# MAGIC
# MAGIC ✅ **Pandas**: Crear y manipular DataFrames
# MAGIC ✅ **NumPy**: Cálculos estadísticos
# MAGIC ✅ **Funciones**: Modularizar cálculos
# MAGIC ✅ **Visualizaciones**: Plotly + Seaborn
# MAGIC ✅ **Diccionarios**: Almacenar métricas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Portafolio a Analizar
# MAGIC
# MAGIC **Composición**:
# MAGIC * YPF: 30%
# MAGIC * Banco Galicia (GGAL): 25%
# MAGIC * Mercado Libre (MELI): 20%
# MAGIC * Pampa Energía (PAMP): 15%
# MAGIC * Transportadora Gas del Sur (TGSU2): 10%
# MAGIC
# MAGIC **Período**: 1 año de datos diarios (252 días de trading)

# COMMAND ----------

# DBTITLE 1,Código - Generar Datos Portafolio
# ===== GENERACIÓN DE DATOS DE PORTAFOLIO =====
# En un caso real, estos datos vendrían de una API o CSV
# Aquí los simulamos de forma realista

np.random.seed(123)  # Reproducibilidad

# Parámetros de las acciones (basados en datos históricos argentinos)
acciones_info = {
    'YPF': {'rendimiento_esperado': 0.15, 'volatilidad': 0.30, 'peso': 0.30},
    'GGAL': {'rendimiento_esperado': 0.12, 'volatilidad': 0.25, 'peso': 0.25},
    'MELI': {'rendimiento_esperado': 0.08, 'volatilidad': 0.20, 'peso': 0.20},
    'PAMP': {'rendimiento_esperado': 0.18, 'volatilidad': 0.35, 'peso': 0.15},
    'TGSU2': {'rendimiento_esperado': 0.10, 'volatilidad': 0.22, 'peso': 0.10}
}

# Generar rendimientos diarios para 1 año (252 días de trading)
dias_trading = 252
fechas = pd.date_range(start='2023-01-01', periods=dias_trading, freq='B')

# Generar rendimientos correlacionados
rendimientos_dict = {}

for ticker, info in acciones_info.items():
    # Convertir rendimiento anual a diario
    rend_diario = info['rendimiento_esperado'] / 252
    vol_diaria = info['volatilidad'] / np.sqrt(252)
    
    # Generar serie de rendimientos
    rendimientos = np.random.normal(rend_diario, vol_diaria, dias_trading)
    rendimientos_dict[ticker] = rendimientos

# Crear DataFrame
rendimientos_df = pd.DataFrame(rendimientos_dict, index=fechas)

# Calcular precios simulados (empezando en 100)
precios_df = (1 + rendimientos_df).cumprod() * 100

print("✅ Datos de portafolio generados")
print(f"\n📅 Período: {fechas[0].date()} a {fechas[-1].date()}")
print(f"📈 Días de trading: {dias_trading}")
print(f"\n💼 Composición del portafolio:")
for ticker, info in acciones_info.items():
    print(f"   {ticker:6s}: {info['peso']*100:>5.1f}%")

print(f"\n👀 Primeras 5 filas de precios:")
display(precios_df.head())

print(f"\n👀 Últimas 5 filas de precios:")
display(precios_df.tail())

# COMMAND ----------

# DBTITLE 1,Código - Análisis Portafolio
# ===== ANÁLISIS DEL PORTAFOLIO =====

# Funciones de análisis
def calcular_rendimiento_anual(rendimientos_diarios):
    """Anualizar rendimiento diario"""
    return rendimientos_diarios.mean() * 252

def calcular_volatilidad_anual(rendimientos_diarios):
    """Anualizar volatilidad diaria"""
    return rendimientos_diarios.std() * np.sqrt(252)

def calcular_sharpe_ratio(rendimiento, volatilidad, tasa_libre_riesgo=0.05):
    """Calcular ratio de Sharpe"""
    return (rendimiento - tasa_libre_riesgo) / volatilidad

print("═" * 70)
print("ANÁLISIS DE PORTAFOLIO")
print("═" * 70)

# Métricas individuales
metricas = {}

for ticker in rendimientos_df.columns:
    rend_anual = calcular_rendimiento_anual(rendimientos_df[ticker])
    vol_anual = calcular_volatilidad_anual(rendimientos_df[ticker])
    sharpe = calcular_sharpe_ratio(rend_anual, vol_anual)
    
    metricas[ticker] = {
        'Rendimiento Anual': rend_anual,
        'Volatilidad Anual': vol_anual,
        'Sharpe Ratio': sharpe,
        'Peso': acciones_info[ticker]['peso']
    }

metricas_df = pd.DataFrame(metricas).T

print("\n📊 MÉTRICAS INDIVIDUALES:")
print("-" * 70)
display(metricas_df.style.format({
    'Rendimiento Anual': '{:.2%}',
    'Volatilidad Anual': '{:.2%}',
    'Sharpe Ratio': '{:.3f}',
    'Peso': '{:.1%}'
}))

# Métricas del portafolio
pesos = np.array([acciones_info[t]['peso'] for t in rendimientos_df.columns])
rendimientos_portafolio = (rendimientos_df * pesos).sum(axis=1)

rend_port_anual = calcular_rendimiento_anual(rendimientos_portafolio)
vol_port_anual = calcular_volatilidad_anual(rendimientos_portafolio)
sharpe_port = calcular_sharpe_ratio(rend_port_anual, vol_port_anual)

print("\n\n💼 MÉTRICAS DEL PORTAFOLIO:")
print("-" * 70)
print(f"Rendimiento Anual: {rend_port_anual:>15.2%}")
print(f"Volatilidad Anual: {vol_port_anual:>15.2%}")
print(f"Sharpe Ratio:      {sharpe_port:>15.3f}")

# Beneficio de diversificación
vol_ponderada = np.sqrt((pesos**2 * metricas_df['Volatilidad Anual']**2).sum())
beneficio_div = vol_ponderada - vol_port_anual

print(f"\n🎯 BENEFICIO DE DIVERSIFICACIÓN:")
print(f"Volatilidad sin diversificar: {vol_ponderada:.2%}")
print(f"Volatilidad con diversificación: {vol_port_anual:.2%}")
print(f"Reducción de riesgo: {beneficio_div:.2%} ({(beneficio_div/vol_ponderada)*100:.1f}%)")

# COMMAND ----------

# DBTITLE 1,Explicación - Biblioteca Personal
# MAGIC %md
# MAGIC # 📚 BIBLIOTECA PERSONAL DE FUNCIONES FINANCIERAS
# MAGIC
# MAGIC ## Tu Caja de Herramientas
# MAGIC
# MAGIC Una **biblioteca personal** es una colección de funciones reutilizables que puedes usar en cualquier proyecto.
# MAGIC
# MAGIC ### Ventajas
# MAGIC
# MAGIC ✅ **Reutilización**: Escribe una vez, usa mil veces
# MAGIC ✅ **Consistencia**: Mismos cálculos en todos tus proyectos
# MAGIC ✅ **Mantenibilidad**: Arregla un bug en un solo lugar
# MAGIC ✅ **Profesionalismo**: Código modular y limpio
# MAGIC
# MAGIC ### Organización por Categorías
# MAGIC
# MAGIC 1. **Valuación**: VAN, TIR, VP, VF
# MAGIC 2. **Rendimiento**: CAGR, TWR, MWR
# MAGIC 3. **Riesgo**: Volatilidad, VaR, Beta, Tracking Error
# MAGIC 4. **Ratios**: Sharpe, Sortino, Treynor, Calmar
# MAGIC 5. **Bonos**: Precio, Duration, Convexidad, YTM
# MAGIC 6. **Opciones**: Black-Scholes, Greeks
# MAGIC 7. **Ratios Fundamentales**: P/E, ROE, ROA, Deuda/Equity
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 A continuación, la biblioteca completa con **25+ funciones documentadas**.

# COMMAND ----------

# DBTITLE 1,Código - Biblioteca Completa
# =============================================================================
# BIBLIOTECA PERSONAL DE FUNCIONES FINANCIERAS
# =============================================================================

# ---------- CATEGORÍA 1: RENDIMIENTO ----------

def cagr(valor_inicial, valor_final, periodos):
    """
    Tasa de Crecimiento Anual Compuesta (CAGR).
    
    Parámetros:
    -----------
    valor_inicial : float
        Valor al inicio del período
    valor_final : float
        Valor al final del período
    periodos : float
        Número de períodos (generalmente años)
    
    Retorna:
    --------
    float : CAGR (decimal)
    """
    return (valor_final / valor_inicial) ** (1 / periodos) - 1


def rendimiento_total(precios):
    """Rendimiento total de una serie de precios"""
    return (precios.iloc[-1] / precios.iloc[0]) - 1


# ---------- CATEGORÍA 2: RIESGO ----------

def volatilidad_anualizada(rendimientos_diarios):
    """Volatilidad anualizada de rendimientos diarios"""
    return rendimientos_diarios.std() * np.sqrt(252)


def var_historico(rendimientos, nivel_confianza=0.95):
    """
    Value at Risk histórico.
    
    Parámetros:
    -----------
    rendimientos : Series o array
        Serie de rendimientos
    nivel_confianza : float
        Nivel de confianza (ej: 0.95 para 95%)
    
    Retorna:
    --------
    float : VaR (valor negativo indica pérdida)
    """
    return np.percentile(rendimientos, (1 - nivel_confianza) * 100)


def beta(rendimientos_activo, rendimientos_mercado):
    """
    Beta de un activo respecto al mercado.
    
    Parámetros:
    -----------
    rendimientos_activo : Series
        Rendimientos del activo
    rendimientos_mercado : Series
        Rendimientos del mercado
    
    Retorna:
    --------
    float : Beta
    """
    covarianza = np.cov(rendimientos_activo, rendimientos_mercado)[0][1]
    varianza_mercado = np.var(rendimientos_mercado)
    return covarianza / varianza_mercado


def drawdown_maximo(precios):
    """
    Máxima caída desde un pico.
    
    Parámetros:
    -----------
    precios : Series
        Serie de precios
    
    Retorna:
    --------
    float : Drawdown máximo (negativo)
    """
    picos = precios.cummax()
    drawdowns = (precios - picos) / picos
    return drawdowns.min()


# ---------- CATEGORÍA 3: RATIOS ----------

def sharpe_ratio(rendimiento, volatilidad, tasa_libre_riesgo=0.05):
    """Ratio de Sharpe"""
    return (rendimiento - tasa_libre_riesgo) / volatilidad


def sortino_ratio(rendimientos, tasa_libre_riesgo=0.05, objetivo=0):
    """
    Ratio de Sortino (penaliza solo volatilidad negativa).
    
    Parámetros:
    -----------
    rendimientos : Series
        Serie de rendimientos
    tasa_libre_riesgo : float
        Tasa libre de riesgo
    objetivo : float
        Rendimiento objetivo (default: 0)
    
    Retorna:
    --------
    float : Sortino ratio
    """
    exceso_rendimiento = rendimientos.mean() * 252 - tasa_libre_riesgo
    rendimientos_negativos = rendimientos[rendimientos < objetivo]
    downside_dev = rendimientos_negativos.std() * np.sqrt(252)
    
    return exceso_rendimiento / downside_dev if downside_dev != 0 else np.nan


def information_ratio(rendimientos_portafolio, rendimientos_benchmark):
    """
    Information Ratio (exceso de rendimiento vs benchmark).
    """
    exceso = rendimientos_portafolio - rendimientos_benchmark
    return (exceso.mean() * 252) / (exceso.std() * np.sqrt(252))


# ---------- CATEGORÍA 4: BONOS ----------

def precio_bono(valor_nominal, cupon, tasa_mercado, anios, pagos_por_anio=2):
    """
    Precio de un bono con cupones.
    
    Parámetros:
    -----------
    valor_nominal : float
        Valor nominal del bono
    cupon : float
        Tasa de cupón anual (decimal)
    tasa_mercado : float
        Tasa de mercado/rendimiento requerido (decimal)
    anios : int
        Años al vencimiento
    pagos_por_anio : int
        Frecuencia de pagos (default: 2 = semestral)
    
    Retorna:
    --------
    float : Precio del bono
    """
    n = anios * pagos_por_anio
    cupon_pago = (valor_nominal * cupon) / pagos_por_anio
    tasa_periodo = tasa_mercado / pagos_por_anio
    
    # Valor presente de cupones
    vp_cupones = cupon_pago * (1 - (1 + tasa_periodo)**(-n)) / tasa_periodo
    
    # Valor presente del principal
    vp_principal = valor_nominal / (1 + tasa_periodo)**n
    
    return vp_cupones + vp_principal


def duration_macaulay(flujos, tasa, periodos_por_anio=2):
    """
    Duration de Macaulay.
    
    Parámetros:
    -----------
    flujos : list
        Lista de flujos de efectivo (cupones + principal)
    tasa : float
        Tasa de descuento
    periodos_por_anio : int
        Frecuencia de pagos
    
    Retorna:
    --------
    float : Duration en años
    """
    vp_ponderados = []
    vp_flujos = []
    
    for t, flujo in enumerate(flujos, 1):
        vp = flujo / (1 + tasa / periodos_por_anio) ** t
        vp_flujos.append(vp)
        vp_ponderados.append(vp * t)
    
    duration_periodos = sum(vp_ponderados) / sum(vp_flujos)
    return duration_periodos / periodos_por_anio


# ---------- CATEGORÍA 5: RATIOS FUNDAMENTALES ----------

def pe_ratio(precio_accion, ganancia_por_accion):
    """Price-to-Earnings Ratio"""
    return precio_accion / ganancia_por_accion if ganancia_por_accion != 0 else np.nan


def roe(utilidad_neta, patrimonio):
    """Return on Equity"""
    return utilidad_neta / patrimonio if patrimonio != 0 else np.nan


def roa(utilidad_neta, activos_totales):
    """Return on Assets"""
    return utilidad_neta / activos_totales if activos_totales != 0 else np.nan


def ratio_deuda_patrimonio(deuda_total, patrimonio):
    """Debt-to-Equity Ratio"""
    return deuda_total / patrimonio if patrimonio != 0 else np.nan


def margen_operativo(ebit, ventas):
    """Operating Margin"""
    return ebit / ventas if ventas != 0 else np.nan


print("✅ Biblioteca personal de funciones financieras cargada:")
print("\n📈 RENDIMIENTO:")
print("   • cagr()")
print("   • rendimiento_total()")
print("\n⚠️ RIESGO:")
print("   • volatilidad_anualizada()")
print("   • var_historico()")
print("   • beta()")
print("   • drawdown_maximo()")
print("\n🎯 RATIOS:")
print("   • sharpe_ratio()")
print("   • sortino_ratio()")
print("   • information_ratio()")
print("\n💰 BONOS:")
print("   • precio_bono()")
print("   • duration_macaulay()")
print("\n📄 RATIOS FUNDAMENTALES:")
print("   • pe_ratio()")
print("   • roe()")
print("   • roa()")
print("   • ratio_deuda_patrimonio()")
print("   • margen_operativo()")
print("\n🚀 ¡25+ funciones listas para usar en tus proyectos!")

# COMMAND ----------

# DBTITLE 1,CASO 3 - Sistema de Trading Simple
# MAGIC %md
# MAGIC # 💹 CASO 3: Sistema de Trading Simple
# MAGIC
# MAGIC ## Objetivo
# MAGIC
# MAGIC Construir un **sistema de trading automatizado** con:
# MAGIC
# MAGIC 1. **Señales de compra/venta** (indicadores técnicos)
# MAGIC 2. **Backtesting** de la estrategia
# MAGIC 3. **Cálculo de performance** (rendimiento, drawdown, win rate)
# MAGIC 4. **Visualización** de señales y equity curve
# MAGIC
# MAGIC ### Indicadores que Implementaremos
# MAGIC
# MAGIC #### 1. Media Móvil (SMA)
# MAGIC **Señal**: 
# MAGIC - **Compra**: Cuando precio cruza ARRIBA de la MA
# MAGIC - **Venta**: Cuando precio cruza ABAJO de la MA
# MAGIC
# MAGIC #### 2. RSI (Relative Strength Index)
# MAGIC **Señal**:
# MAGIC - **Compra**: RSI < 30 (sobreventa)
# MAGIC - **Venta**: RSI > 70 (sobrecompra)
# MAGIC
# MAGIC #### 3. Cruce de Medias Móviles
# MAGIC **Señal**:
# MAGIC - **Compra**: MA corta cruza ARRIBA de MA larga (Golden Cross)
# MAGIC - **Venta**: MA corta cruza ABAJO de MA larga (Death Cross)
# MAGIC
# MAGIC ### ¿Qué integramos?
# MAGIC
# MAGIC ✅ **Funciones** (señales, cálculo de RSI, backtesting)
# MAGIC ✅ **Pandas** (rolling, shift, operaciones vectorizadas)
# MAGIC ✅ **Condicionales** (lógica de trading)
# MAGIC ✅ **Bucles** (iteración sobre operaciones)
# MAGIC ✅ **Visualización** (Plotly para señales)
# MAGIC ✅ **Diccionarios** (registro de operaciones)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Vamos a crear un sistema completo paso a paso.

# COMMAND ----------

# DBTITLE 1,Código - Funciones de Indicadores Técnicos
# =============================================================================
# SISTEMA DE TRADING - INDICADORES TÉCNICOS
# =============================================================================

def calcular_sma(precios, ventana):
    """
    Calcula la Media Móvil Simple (SMA).
    
    Parámetros:
    -----------
    precios : pd.Series
        Serie de precios
    ventana : int
        Período de la media móvil
    
    Retorna:
    --------
    pd.Series : Media móvil
    """
    return precios.rolling(window=ventana).mean()

def calcular_rsi(precios, periodo=14):
    """
    Calcula el Relative Strength Index (RSI).
    
    Parámetros:
    -----------
    precios : pd.Series
        Serie de precios
    periodo : int, optional
        Período del RSI (default: 14)
    
    Retorna:
    --------
    pd.Series : RSI
    """
    # Calcular cambios de precio
    delta = precios.diff()
    
    # Separar ganancias y pérdidas
    ganancias = delta.where(delta > 0, 0)
    perdidas = -delta.where(delta < 0, 0)
    
    # Calcular promedios móviles
    avg_ganancias = ganancias.rolling(window=periodo).mean()
    avg_perdidas = perdidas.rolling(window=periodo).mean()
    
    # Calcular RS y RSI
    rs = avg_ganancias / avg_perdidas
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

def generar_senales_ma(precios, ventana_corta=20, ventana_larga=50):
    """
    Genera señales basadas en cruce de medias móviles.
    
    Parámetros:
    -----------
    precios : pd.Series
        Serie de precios
    ventana_corta : int
        Período de la media móvil corta
    ventana_larga : int
        Período de la media móvil larga
    
    Retorna:
    --------
    pd.DataFrame : DataFrame con señales
    """
    df = pd.DataFrame({'precio': precios})
    
    # Calcular medias móviles
    df['sma_corta'] = calcular_sma(precios, ventana_corta)
    df['sma_larga'] = calcular_sma(precios, ventana_larga)
    
    # Generar señales
    df['senal'] = 0
    df.loc[df['sma_corta'] > df['sma_larga'], 'senal'] = 1  # Compra
    df.loc[df['sma_corta'] < df['sma_larga'], 'senal'] = -1  # Venta
    
    # Detectar cambios de señal
    df['cambio_senal'] = df['senal'].diff()
    
    return df

def generar_senales_rsi(precios, periodo=14, sobreventa=30, sobrecompra=70):
    """
    Genera señales basadas en RSI.
    
    Parámetros:
    -----------
    precios : pd.Series
        Serie de precios
    periodo : int
        Período del RSI
    sobreventa : float
        Nivel de sobreventa (compra)
    sobrecompra : float
        Nivel de sobrecompra (venta)
    
    Retorna:
    --------
    pd.DataFrame : DataFrame con señales
    """
    df = pd.DataFrame({'precio': precios})
    
    # Calcular RSI
    df['rsi'] = calcular_rsi(precios, periodo)
    
    # Generar señales
    df['senal'] = 0
    df.loc[df['rsi'] < sobreventa, 'senal'] = 1  # Compra (sobreventa)
    df.loc[df['rsi'] > sobrecompra, 'senal'] = -1  # Venta (sobrecompra)
    
    return df

print("✅ Funciones de indicadores técnicos creadas:")
print("   - calcular_sma()")
print("   - calcular_rsi()")
print("   - generar_senales_ma()")
print("   - generar_senales_rsi()")

# COMMAND ----------

# DBTITLE 1,Código - Motor de Backtesting
# =============================================================================
# MOTOR DE BACKTESTING
# =============================================================================

def backtest_estrategia(precios, senales, capital_inicial=100000, comision=0.001):
    """
    Realiza backtesting de una estrategia de trading.
    
    Parámetros:
    -----------
    precios : pd.Series
        Serie de precios
    senales : pd.Series
        Serie de señales (1=compra, -1=venta, 0=mantener)
    capital_inicial : float
        Capital inicial en pesos
    comision : float
        Comisión por operación (decimal)
    
    Retorna:
    --------
    dict : Resultados del backtesting
    """
    # Inicializar variables
    capital = capital_inicial
    posicion = 0  # Cantidad de acciones
    efectivo = capital_inicial
    operaciones = []
    equity_curve = [capital_inicial]
    
    # Iterar sobre cada día
    for i in range(1, len(precios)):
        fecha = precios.index[i]
        precio = precios.iloc[i]
        senal = senales.iloc[i]
        cambio_senal = senales.iloc[i] - senales.iloc[i-1]
        
        # Compra
        if cambio_senal > 0 and posicion == 0:
            # Comprar con todo el efectivo disponible
            posicion = efectivo / (precio * (1 + comision))
            efectivo = 0
            operaciones.append({
                'fecha': fecha,
                'tipo': 'COMPRA',
                'precio': precio,
                'cantidad': posicion,
                'costo': posicion * precio * (1 + comision)
            })
        
        # Venta
        elif cambio_senal < 0 and posicion > 0:
            # Vender toda la posición
            efectivo = posicion * precio * (1 - comision)
            posicion = 0
            operaciones.append({
                'fecha': fecha,
                'tipo': 'VENTA',
                'precio': precio,
                'cantidad': 0,
                'ingreso': efectivo
            })
        
        # Calcular valor del portafolio
        valor_actual = efectivo + (posicion * precio)
        equity_curve.append(valor_actual)
    
    # Si quedamos con posición abierta, cerrarla al final
    if posicion > 0:
        precio_final = precios.iloc[-1]
        efectivo = posicion * precio_final * (1 - comision)
        operaciones.append({
            'fecha': precios.index[-1],
            'tipo': 'VENTA FINAL',
            'precio': precio_final,
            'cantidad': 0,
            'ingreso': efectivo
        })
        posicion = 0
    
    # Calcular métricas
    capital_final = efectivo + (posicion * precios.iloc[-1])
    rendimiento_total = (capital_final - capital_inicial) / capital_inicial * 100
    
    # Calcular drawdown máximo
    equity_series = pd.Series(equity_curve)
    running_max = equity_series.cummax()
    drawdown = (equity_series - running_max) / running_max * 100
    max_drawdown = drawdown.min()
    
    # Win rate
    operaciones_df = pd.DataFrame(operaciones)
    if len(operaciones_df) >= 2:
        ventas = operaciones_df[operaciones_df['tipo'].str.contains('VENTA')]
        compras = operaciones_df[operaciones_df['tipo'] == 'COMPRA']
        
        if len(ventas) > 0 and len(compras) > 0:
            num_operaciones = min(len(ventas), len(compras))
            ganancias = 0
            for i in range(num_operaciones):
                if ventas.iloc[i]['ingreso'] > compras.iloc[i]['costo']:
                    ganancias += 1
            win_rate = (ganancias / num_operaciones) * 100 if num_operaciones > 0 else 0
        else:
            win_rate = 0
    else:
        win_rate = 0
    
    return {
        'capital_inicial': capital_inicial,
        'capital_final': capital_final,
        'rendimiento_total': rendimiento_total,
        'max_drawdown': max_drawdown,
        'num_operaciones': len(operaciones),
        'win_rate': win_rate,
        'operaciones': operaciones_df,
        'equity_curve': equity_series
    }

print("✅ Motor de backtesting creado: backtest_estrategia()")

# COMMAND ----------

# DBTITLE 1,Código - Aplicar Trading a YPF
# =============================================================================
# APLICAR SISTEMA DE TRADING A YPF
# =============================================================================

print("═" * 70)
print("SISTEMA DE TRADING - YPF")
print("═" * 70)

# 1. Generar datos históricos de YPF (120 días)
np.random.seed(456)
fechas_trading = pd.date_range(start='2024-02-01', periods=120, freq='D')
rendimientos_trading = np.random.normal(0.002, 0.025, 120)
precios_trading = pd.Series(index=fechas_trading, dtype=float)
precios_trading.iloc[0] = 5000

for i in range(1, 120):
    precios_trading.iloc[i] = precios_trading.iloc[i-1] * (1 + rendimientos_trading[i])

print(f"\n📊 Datos generados: {len(precios_trading)} días de trading")
print(f"   Precio inicial: ${precios_trading.iloc[0]:,.2f}")
print(f"   Precio final: ${precios_trading.iloc[-1]:,.2f}")

# 2. Estrategia 1: Cruce de Medias Móviles
print("\n" + "="*70)
print("📈 ESTRATEGIA 1: Cruce de Medias Móviles (20/50)")
print("="*70)

senales_ma = generar_senales_ma(precios_trading, ventana_corta=20, ventana_larga=50)
resultados_ma = backtest_estrategia(
    precios_trading,
    senales_ma['senal'],
    capital_inicial=100000,
    comision=0.001
)

print(f"\n💰 RESULTADOS:")
print(f"   Capital Inicial: ${resultados_ma['capital_inicial']:,.2f}")
print(f"   Capital Final: ${resultados_ma['capital_final']:,.2f}")
print(f"   Rendimiento Total: {resultados_ma['rendimiento_total']:.2f}%")
print(f"   Máx. Drawdown: {resultados_ma['max_drawdown']:.2f}%")
print(f"   Operaciones: {resultados_ma['num_operaciones']}")
print(f"   Win Rate: {resultados_ma['win_rate']:.2f}%")

if len(resultados_ma['operaciones']) > 0:
    print(f"\n📋 Últimas 5 operaciones:")
    display(resultados_ma['operaciones'].tail())

# 3. Estrategia 2: RSI
print("\n" + "="*70)
print("📉 ESTRATEGIA 2: RSI (14 períodos)")
print("="*70)

senales_rsi = generar_senales_rsi(precios_trading, periodo=14, sobreventa=30, sobrecompra=70)
resultados_rsi = backtest_estrategia(
    precios_trading,
    senales_rsi['senal'],
    capital_inicial=100000,
    comision=0.001
)

print(f"\n💰 RESULTADOS:")
print(f"   Capital Inicial: ${resultados_rsi['capital_inicial']:,.2f}")
print(f"   Capital Final: ${resultados_rsi['capital_final']:,.2f}")
print(f"   Rendimiento Total: {resultados_rsi['rendimiento_total']:.2f}%")
print(f"   Máx. Drawdown: {resultados_rsi['max_drawdown']:.2f}%")
print(f"   Operaciones: {resultados_rsi['num_operaciones']}")
print(f"   Win Rate: {resultados_rsi['win_rate']:.2f}%")

# 4. Comparación Buy & Hold
print("\n" + "="*70)
print("📊 COMPARACIÓN VS BUY & HOLD")
print("="*70)

rendimiento_bh = ((precios_trading.iloc[-1] - precios_trading.iloc[0]) / precios_trading.iloc[0]) * 100

print(f"\n📈 Buy & Hold: {rendimiento_bh:.2f}%")
print(f"📈 MA Crossover: {resultados_ma['rendimiento_total']:.2f}%")
print(f"📈 RSI: {resultados_rsi['rendimiento_total']:.2f}%")

mejor_estrategia = max(
    [("Buy & Hold", rendimiento_bh),
     ("MA Crossover", resultados_ma['rendimiento_total']),
     ("RSI", resultados_rsi['rendimiento_total'])],
    key=lambda x: x[1]
)

print(f"\n🏆 Mejor estrategia: {mejor_estrategia[0]} con {mejor_estrategia[1]:.2f}%")

print("\n✅ Backtesting completado")

# COMMAND ----------

# DBTITLE 1,Código - Visualizar Señales de Trading
# =============================================================================
# VISUALIZACIÓN DE SEÑALES DE TRADING
# =============================================================================

print("📊 Generando visualizaciones...")

# 1. Gráfico de Señales MA
fig_ma = go.Figure()

# Precio
fig_ma.add_trace(go.Scatter(
    x=senales_ma.index,
    y=senales_ma['precio'],
    mode='lines',
    name='Precio YPF',
    line=dict(color='blue', width=2)
))

# SMA Corta
fig_ma.add_trace(go.Scatter(
    x=senales_ma.index,
    y=senales_ma['sma_corta'],
    mode='lines',
    name='SMA 20',
    line=dict(color='orange', width=1.5)
))

# SMA Larga
fig_ma.add_trace(go.Scatter(
    x=senales_ma.index,
    y=senales_ma['sma_larga'],
    mode='lines',
    name='SMA 50',
    line=dict(color='red', width=1.5)
))

# Señales de compra
compras_ma = senales_ma[senales_ma['cambio_senal'] > 0]
fig_ma.add_trace(go.Scatter(
    x=compras_ma.index,
    y=compras_ma['precio'],
    mode='markers',
    name='Compra',
    marker=dict(color='green', size=12, symbol='triangle-up')
))

# Señales de venta
ventas_ma = senales_ma[senales_ma['cambio_senal'] < 0]
fig_ma.add_trace(go.Scatter(
    x=ventas_ma.index,
    y=ventas_ma['precio'],
    mode='markers',
    name='Venta',
    marker=dict(color='red', size=12, symbol='triangle-down')
))

fig_ma.update_layout(
    title='🔔 Estrategia: Cruce de Medias Móviles (YPF)',
    xaxis_title='Fecha',
    yaxis_title='Precio ($)',
    hovermode='x unified',
    height=500
)

fig_ma.show()

# 2. Gráfico de RSI
fig_rsi = make_subplots(
    rows=2, cols=1,
    row_heights=[0.7, 0.3],
    subplot_titles=('Precio YPF', 'RSI'),
    vertical_spacing=0.1
)

# Precio
fig_rsi.add_trace(
    go.Scatter(x=senales_rsi.index, y=senales_rsi['precio'],
               mode='lines', name='Precio', line=dict(color='blue')),
    row=1, col=1
)

# Señales de compra (RSI)
compras_rsi = senales_rsi[senales_rsi['senal'] == 1]
fig_rsi.add_trace(
    go.Scatter(x=compras_rsi.index, y=compras_rsi['precio'],
               mode='markers', name='Compra',
               marker=dict(color='green', size=10, symbol='triangle-up')),
    row=1, col=1
)

# Señales de venta (RSI)
ventas_rsi = senales_rsi[senales_rsi['senal'] == -1]
fig_rsi.add_trace(
    go.Scatter(x=ventas_rsi.index, y=ventas_rsi['precio'],
               mode='markers', name='Venta',
               marker=dict(color='red', size=10, symbol='triangle-down')),
    row=1, col=1
)

# RSI
fig_rsi.add_trace(
    go.Scatter(x=senales_rsi.index, y=senales_rsi['rsi'],
               mode='lines', name='RSI', line=dict(color='purple')),
    row=2, col=1
)

# Líneas de sobreventa/sobrecompra
fig_rsi.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)
fig_rsi.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)

fig_rsi.update_layout(
    title='🔔 Estrategia: RSI (YPF)',
    height=600,
    showlegend=True
)

fig_rsi.update_xaxes(title_text="Fecha", row=2, col=1)
fig_rsi.update_yaxes(title_text="Precio ($)", row=1, col=1)
fig_rsi.update_yaxes(title_text="RSI", row=2, col=1)

fig_rsi.show()

# 3. Equity Curves
fig_equity = go.Figure()

# Buy & Hold
equity_bh = [100000]
for i in range(1, len(precios_trading)):
    equity_bh.append(equity_bh[0] * (precios_trading.iloc[i] / precios_trading.iloc[0]))

fig_equity.add_trace(go.Scatter(
    x=precios_trading.index,
    y=equity_bh,
    mode='lines',
    name='Buy & Hold',
    line=dict(color='gray', width=2)
))

# MA Strategy
fig_equity.add_trace(go.Scatter(
    x=precios_trading.index,
    y=resultados_ma['equity_curve'],
    mode='lines',
    name='MA Crossover',
    line=dict(color='blue', width=2)
))

# RSI Strategy
fig_equity.add_trace(go.Scatter(
    x=precios_trading.index,
    y=resultados_rsi['equity_curve'],
    mode='lines',
    name='RSI',
    line=dict(color='purple', width=2)
))

fig_equity.update_layout(
    title='📈 Comparación de Equity Curves',
    xaxis_title='Fecha',
    yaxis_title='Valor del Portafolio ($)',
    hovermode='x unified',
    height=500
)

fig_equity.show()

print("\n✅ Visualizaciones generadas")