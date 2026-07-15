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
# MAGIC ### Notebook 0.5: Pandas para Finanzas
# MAGIC ### 🐼 **LA LIBRERÍA MÁS IMPORTANTE PARA ANÁLISIS DE DATOS**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción a Pandas
# MAGIC %md
# MAGIC # 🐼 Introducción: ¿Qué es Pandas?
# MAGIC
# MAGIC ## 🌟 La Librería MÁS Importante en Finanzas
# MAGIC
# MAGIC **Pandas** es la librería de Python para **manipular y analizar datos**. Es **INDISPENSABLE** en finanzas.
# MAGIC
# MAGIC ### ¿Por qué Pandas es TAN importante?
# MAGIC
# MAGIC ✅ **Maneja datos tabulares**: Como Excel, pero con superpoderes
# MAGIC ✅ **Lee cualquier formato**: CSV, Excel, JSON, SQL, APIs
# MAGIC ✅ **Operaciones rápidas**: Millones de filas en 
# MAGIC ✅ **Series temporales**: Ideal para precios históricos
# MAGIC ✅ **Agregaciones potentes**: GROUP BY como en SQL
# MAGIC ✅ **Integración perfecta**: Con NumPy, Matplotlib, y más
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📚 Origen del Nombre
# MAGIC
# MAGIC **Pan**el **Da**ta = Datos en panel (series temporales multidimensionales)
# MAGIC
# MAGIC 🐼 También: el logo es un panda, porque es "adorable pero poderoso"
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📦 Las 2 Estructuras Principales
# MAGIC
# MAGIC ### 1. **Series** - Una columna
# MAGIC ```python
# MAGIC precios = pd.Series([5000, 5200, 5100])
# MAGIC ```
# MAGIC * Como una lista mejorada
# MAGIC * Tiene índice
# MAGIC * Una sola columna
# MAGIC
# MAGIC ### 2. **DataFrame** - Una tabla completa
# MAGIC ```python
# MAGIC df = pd.DataFrame({
# MAGIC     'fecha': ['2024-01-01', '2024-01-02'],
# MAGIC     'precio': [5000, 5200],
# MAGIC     'volumen': [1000000, 1200000]
# MAGIC })
# MAGIC ```
# MAGIC * Como una hoja de Excel
# MAGIC * Múltiples columnas
# MAGIC * Cada columna es una Series
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎯 Objetivos de Este Notebook
# MAGIC
# MAGIC Al finalizar, podrás:
# MAGIC
# MAGIC ✅ Crear y manipular Series y DataFrames
# MAGIC ✅ Leer archivos CSV y Excel
# MAGIC ✅ Filtrar y seleccionar datos
# MAGIC ✅ Hacer agregaciones (sum, mean, groupby)
# MAGIC ✅ Manejar valores faltantes
# MAGIC ✅ Combinar datasets (merge, join)
# MAGIC ✅ Trabajar con fechas y series temporales
# MAGIC ✅ Aplicar todo esto a datos financieros argentinos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📈 Casos que Veremos
# MAGIC
# MAGIC 1. 💹 Precios de acciones argentinas (YPF, GGAL, MELI)
# MAGIC 2. 📊 Rendimientos y volatilidad
# MAGIC 3. 📉 Volumen de operaciones
# MAGIC 4. 💰 Balances de empresas
# MAGIC 5. 📆 Series temporales financieras
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⏱️ **Tiempo estimado**: 75-90 minutos
# MAGIC
# MAGIC ¡Empecemos!

# COMMAND ----------

# DBTITLE 1,Explicación - Importar Pandas
# MAGIC %md
# MAGIC ## 📦 Importar Pandas
# MAGIC
# MAGIC La **convención universal** es importar Pandas como `pd`:
# MAGIC
# MAGIC ```python
# MAGIC import pandas as pd
# MAGIC ```
# MAGIC
# MAGIC También importaremos NumPy (para generar datos) y datetime (para fechas).

# COMMAND ----------

# DBTITLE 1,Código - Importar Librerías
# Importar librerías
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

print("═" * 70)
print("            PANDAS PARA FINANZAS - NOTEBOOK 0.5")
print("═" * 70)
print(f"\n✅ Pandas importado correctamente")
print(f"   Versión: {pd.__version__}")
print(f"\n✅ NumPy versión: {np.__version__}")
print(f"\n🐼 ¡Pandas listo para analizar datos financieros!")

# COMMAND ----------

# DBTITLE 1,Sección - Series de Pandas
# MAGIC %md
# MAGIC # 📊 PARTE 1: Series de Pandas
# MAGIC
# MAGIC ## ¿Qué es una Series?
# MAGIC
# MAGIC Una **Series** es una **columna de datos** con un índice.
# MAGIC
# MAGIC ### Diferencias con una lista
# MAGIC
# MAGIC | Característica | Lista Python | Pandas Series |
# MAGIC |---------------|--------------|---------------|
# MAGIC | Estructura | Secuencia simple | Columna con índice |
# MAGIC | Operaciones | Básicas | Avanzadas (sum, mean, std) |
# MAGIC | Índice | Numérico (0, 1, 2...) | Personalizable |
# MAGIC | Velocidad | Lenta | Rápida (NumPy) |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Crear una Series
# MAGIC
# MAGIC ### 1. Desde una lista
# MAGIC ```python
# MAGIC precios = pd.Series([5000, 5200, 5100, 5300])
# MAGIC ```
# MAGIC
# MAGIC ### 2. Con índice personalizado
# MAGIC ```python
# MAGIC precios = pd.Series(
# MAGIC     [5000, 5200, 5100, 5300],
# MAGIC     index=['Lunes', 'Martes', 'Miércoles', 'Jueves']
# MAGIC )
# MAGIC ```
# MAGIC
# MAGIC ### 3. Desde un diccionario
# MAGIC ```python
# MAGIC precios = pd.Series({
# MAGIC     'YPF': 5000,
# MAGIC     'GGAL': 175,
# MAGIC     'MELI': 1450
# MAGIC })
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Veamos ejemplos prácticos.

# COMMAND ----------

# DBTITLE 1,Código - Series Ejemplos
# 1. Series simple de precios
precios_ypf = pd.Series([5000, 5200, 5100, 5300, 5400])

print("💹 1. Series Simple de Precios:")
print(precios_ypf)
print(f"\nTipo: {type(precios_ypf)}")
print(f"Índice por defecto: {list(precios_ypf.index)}")

# 2. Series con índice personalizado (fechas)
fechas = pd.date_range(start='2024-06-10', periods=5, freq='D')
precios_ypf_fechas = pd.Series(
    [5000, 5200, 5100, 5300, 5400],
    index=fechas,
    name='YPF'
)

print("\n" + "="*70)
print("📅 2. Series con Fechas como Índice:")
print(precios_ypf_fechas)

# 3. Series desde diccionario (acciones argentinas)
precios_merval = pd.Series({
    'YPF': 5200,
    'GGAL': 175.50,
    'MELI': 1450.80,
    'COME': 2.35,
    'TRAN': 1150.00,
    'LOMA': 920.00
})

print("\n" + "="*70)
print("🏆 3. Series de Precios del Merval (Hoy):")
print(precios_merval)

# 4. Operaciones con Series
print("\n" + "="*70)
print("📊 4. Estadísticas Básicas:")
print(f"   Máximo: ${precios_ypf_fechas.max():,.2f}")
print(f"   Mínimo: ${precios_ypf_fechas.min():,.2f}")
print(f"   Media: ${precios_ypf_fechas.mean():,.2f}")
print(f"   Desv. Estándar: ${precios_ypf_fechas.std():,.2f}")
print(f"   Suma Total: ${precios_ypf_fechas.sum():,.2f}")

# 5. Acceder a elementos
print("\n" + "="*70)
print("🔍 5. Acceder a Elementos:")
print(f"   Precio de YPF: ${precios_merval['YPF']:,.2f}")
print(f"   Precio de MELI: ${precios_merval['MELI']:,.2f}")
print(f"   Precio del primer día: ${precios_ypf_fechas.iloc[0]:,.2f}")
print(f"   Precio del último día: ${precios_ypf_fechas.iloc[-1]:,.2f}")

print("\n✅ Series creadas y exploradas exitosamente")

# COMMAND ----------

# DBTITLE 1,Sección - DataFrames Básicos
# MAGIC %md
# MAGIC
# MAGIC # 📊 PARTE 2: DataFrames - La Estructura Principal
# MAGIC
# MAGIC ## ¿Qué es un DataFrame?
# MAGIC
# MAGIC Un **DataFrame** es una **tabla completa** con múltiples columnas.
# MAGIC
# MAGIC ### Piensa en Excel
# MAGIC
# MAGIC ✅ Filas y columnas
# MAGIC ✅ Cada columna puede tener un tipo diferente (números, texto, fechas)
# MAGIC ✅ Cada columna es una Series
# MAGIC ✅ Tiene índice para las filas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Crear un DataFrame
# MAGIC
# MAGIC ### 1. Desde un diccionario
# MAGIC ```python
# MAGIC df = pd.DataFrame({
# MAGIC     'ticker': ['YPF', 'GGAL', 'MELI'],
# MAGIC     'precio': [5200, 175.50, 1450.80],
# MAGIC     'sector': ['Energía', 'Bancario', 'Tecnología']
# MAGIC })
# MAGIC ```
# MAGIC
# MAGIC ### 2. Desde listas de listas
# MAGIC ```python
# MAGIC data = [
# MAGIC     ['YPF', 5200, 'Energía'],
# MAGIC     ['GGAL', 175.50, 'Bancario'],
# MAGIC     ['MELI', 1450.80, 'Tecnología']
# MAGIC ]
# MAGIC df = pd.DataFrame(data, columns=['ticker', 'precio', 'sector'])
# MAGIC ```
# MAGIC
# MAGIC ### 3. Desde archivos (CSV, Excel)
# MAGIC ```python
# MAGIC df = pd.read_csv('precios.csv')
# MAGIC df = pd.read_excel('cartera.xlsx')
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Creemos una cartera de acciones argentinas.

# COMMAND ----------

# DBTITLE 1,Código - DataFrame Cartera Argentina
# Crear DataFrame con cartera de acciones argentinas
cartera = pd.DataFrame({
    'ticker': ['YPF', 'GGAL', 'MELI', 'COME', 'TRAN', 'LOMA', 'ALUA', 'CRES'],
    'precio': [5200.00, 175.50, 1450.80, 2.35, 1150.00, 920.00, 3.15, 18.50],
    'sector': ['Energía', 'Bancario', 'Tecnología', 'Alimentos', 'Transporte', 'Energía', 'Industrial', 'Bancario'],
    'cantidad': [100, 500, 50, 10000, 80, 200, 5000, 1000],
    'pais': ['Argentina', 'Argentina', 'LATAM', 'Argentina', 'Argentina', 'Argentina', 'Argentina', 'Argentina']
})

print("📊 CARTERA DE ACCIONES ARGENTINAS")
print("=" * 70)
print("\n🔹 DataFrame creado:")
display(cartera)

# Información básica
print("\n📋 Información del DataFrame:")
print(f"   Dimensiones: {cartera.shape[0]} filas × {cartera.shape[1]} columnas")
print(f"   Columnas: {list(cartera.columns)}")
print(f"   Tipos de datos:\n{cartera.dtypes}")

# Calcular valor de inversión
cartera['valor_total'] = cartera['precio'] * cartera['cantidad']

print("\n💰 Cartera con Valor Total:")
display(cartera)

print(f"\n💵 Inversión Total: ${cartera['valor_total'].sum():,.2f}")
print("\n✅ DataFrame creado exitosamente")

# COMMAND ----------

# DBTITLE 1,Sección - Exploración de Datos
# MAGIC %md
# MAGIC
# MAGIC # 🔍 PARTE 3: Exploración de Datos
# MAGIC
# MAGIC ## Métodos Esenciales para Explorar
# MAGIC
# MAGIC ### 1. `.head()` y `.tail()`
# MAGIC Ver las primeras o últimas filas:
# MAGIC ```python
# MAGIC df.head()      # Primeras 5 filas
# MAGIC df.head(10)    # Primeras 10 filas
# MAGIC df.tail()      # Últimas 5 filas
# MAGIC ```
# MAGIC
# MAGIC ### 2. `.info()`
# MAGIC Resumen completo del DataFrame:
# MAGIC - Número de filas
# MAGIC - Tipos de datos
# MAGIC - Memoria utilizada
# MAGIC - Valores no nulos
# MAGIC
# MAGIC ### 3. `.describe()`
# MAGIC Estadísticas de columnas numéricas:
# MAGIC - count, mean, std
# MAGIC - min, 25%, 50%, 75%, max
# MAGIC
# MAGIC ### 4. `.shape`, `.columns`, `.index`
# MAGIC Atributos básicos del DataFrame
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Exploremos nuestra cartera.

# COMMAND ----------

# DBTITLE 1,Código - Exploración de Cartera
print("🔍 EXPLORACIÓN DE LA CARTERA")
print("=" * 70)

# 1. Primeras filas
print("\n📋 1. Primeras 3 acciones:")
display(cartera.head(3))

# 2. Últimas filas
print("\n📋 2. Últimas 3 acciones:")
display(cartera.tail(3))

# 3. Información del DataFrame
print("\n📊 3. Información Completa:")
cartera.info()

# 4. Estadísticas descriptivas
print("\n📈 4. Estadísticas de Columnas Numéricas:")
display(cartera.describe())

# 5. Análisis por columna
print("\n💹 5. Análisis Específico por Columna:")
print(f"   Precio promedio: ${cartera['precio'].mean():,.2f}")
print(f"   Precio máximo: ${cartera['precio'].max():,.2f} ({cartera[cartera['precio'] == cartera['precio'].max()]['ticker'].values[0]})")
print(f"   Precio mínimo: ${cartera['precio'].min():,.2f} ({cartera[cartera['precio'] == cartera['precio'].min()]['ticker'].values[0]})")
print(f"   Inversión total: ${cartera['valor_total'].sum():,.2f}")

# 6. Conteo por sector
print("\n🏢 6. Distribución por Sector:")
display(cartera['sector'].value_counts())

# 7. Columnas y tipos
print("\n📑 7. Columnas del DataFrame:")
for col, dtype in cartera.dtypes.items():
    print(f"   {col}: {dtype}")

print("\n✅ Exploración completada")

# COMMAND ----------

# DBTITLE 1,Sección - Filtrado de Datos
# MAGIC %md
# MAGIC
# MAGIC # 🔎 PARTE 4: Filtrado de Datos
# MAGIC
# MAGIC ## Filtrado Booleano
# MAGIC
# MAGIC Pandas usa **máscaras booleanas** para filtrar filas.
# MAGIC
# MAGIC ### Sintaxis Básica
# MAGIC ```python
# MAGIC # Filtro simple
# MAGIC df[df['precio'] > 1000]
# MAGIC
# MAGIC # Múltiples condiciones con &, |, ~
# MAGIC df[(df['precio'] > 1000) & (df['sector'] == 'Energía')]
# MAGIC ```
# MAGIC
# MAGIC ⚠️ **IMPORTANTE**: 
# MAGIC - Usa `&` para AND (no `and`)
# MAGIC - Usa `|` para OR (no `or`)
# MAGIC - Usa `~` para NOT (no `not`)
# MAGIC - **Siempre** usa paréntesis en cada condición
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Métodos de Filtrado
# MAGIC
# MAGIC ### 1. Por valor exacto
# MAGIC ```python
# MAGIC df[df['sector'] == 'Energía']
# MAGIC ```
# MAGIC
# MAGIC ### 2. Por rango
# MAGIC ```python
# MAGIC df[(df['precio'] >= 100) & (df['precio'] <= 1000)]
# MAGIC ```
# MAGIC
# MAGIC ### 3. Por lista de valores (`.isin()`)
# MAGIC ```python
# MAGIC df[df['ticker'].isin(['YPF', 'GGAL', 'MELI'])]
# MAGIC ```
# MAGIC
# MAGIC ### 4. Por texto (`.str.contains()`)
# MAGIC ```python
# MAGIC df[df['ticker'].str.contains('ME')]
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Filtremos nuestra cartera.

# COMMAND ----------

# DBTITLE 1,Código - Filtrado de Cartera
print("🔎 FILTRADO DE CARTERA")
print("=" * 70)

# 1. Filtro simple: Acciones con precio > $500
print("\n💵 1. Acciones con precio > $500:")
acciones_caras = cartera[cartera['precio'] > 500]
display(acciones_caras[['ticker', 'precio', 'sector']])

# 2. Filtro por sector: Solo Energía
print("\n⚡ 2. Acciones del Sector Energía:")
energia = cartera[cartera['sector'] == 'Energía']
display(energia[['ticker', 'precio', 'valor_total']])

# 3. Múltiples condiciones: Energía O Bancario
print("\n🏦 3. Acciones de Energía O Bancario:")
energia_bancario = cartera[(cartera['sector'] == 'Energía') | (cartera['sector'] == 'Bancario')]
display(energia_bancario[['ticker', 'sector', 'precio']])

# 4. Filtro con AND: Precio < $200 Y Cantidad > 200
print("\n🔹 4. Acciones baratas con alta tenencia (precio < $200 Y cantidad > 200):")
baratas_alta_tenencia = cartera[(cartera['precio'] < 200) & (cartera['cantidad'] > 200)]
display(baratas_alta_tenencia[['ticker', 'precio', 'cantidad', 'valor_total']])

# 5. Filtro con .isin(): Tickers específicos
print("\n🎯 5. Acciones específicas (YPF, MELI, GGAL):")
top_3 = cartera[cartera['ticker'].isin(['YPF', 'MELI', 'GGAL'])]
display(top_3[['ticker', 'precio', 'valor_total']])

# 6. Negación: Todo EXCEPTO Energía
print("\n❌ 6. Acciones que NO son de Energía:")
no_energia = cartera[~(cartera['sector'] == 'Energía')]
display(no_energia[['ticker', 'sector', 'precio']])

# 7. Filtro por valor de inversión
print("\n📈 7. Top 3 inversiones por valor:")
top_inversiones = cartera.nlargest(3, 'valor_total')
display(top_inversiones[['ticker', 'sector', 'valor_total']])

# 8. Estadísticas de subconjuntos
print("\n📊 8. Comparación por Sectores:")
print(f"   Inversión en Energía: ${energia['valor_total'].sum():,.2f}")
print(f"   Inversión en Bancario: ${cartera[cartera['sector'] == 'Bancario']['valor_total'].sum():,.2f}")
print(f"   Inversión en Tecnología: ${cartera[cartera['sector'] == 'Tecnología']['valor_total'].sum():,.2f}")

print("\n✅ Filtrado completado")

# COMMAND ----------

# DBTITLE 1,Sección - GroupBy y Agregaciones
# MAGIC %md
# MAGIC
# MAGIC # 📦 PARTE 5: GroupBy y Agregaciones
# MAGIC
# MAGIC ## ¿Qué es GroupBy?
# MAGIC
# MAGIC **GroupBy** agrupa filas que tienen el mismo valor en una columna y aplica operaciones a cada grupo.
# MAGIC
# MAGIC ### Concepto: "Split-Apply-Combine"
# MAGIC
# MAGIC 1. **Split**: Dividir datos en grupos
# MAGIC 2. **Apply**: Aplicar función a cada grupo
# MAGIC 3. **Combine**: Combinar resultados
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Sintaxis Básica
# MAGIC
# MAGIC ```python
# MAGIC df.groupby('columna').sum()
# MAGIC df.groupby('columna').mean()
# MAGIC df.groupby('columna').count()
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Funciones de Agregación
# MAGIC
# MAGIC | Función | Descripción | Uso Financiero |
# MAGIC |---------|-------------|----------------|
# MAGIC | `.sum()` | Suma total | Inversión por sector |
# MAGIC | `.mean()` | Promedio | Precio promedio |
# MAGIC | `.count()` | Conteo | Número de acciones |
# MAGIC | `.min()` | Mínimo | Precio más bajo |
# MAGIC | `.max()` | Máximo | Precio más alto |
# MAGIC | `.std()` | Desviación estándar | Volatilidad |
# MAGIC | `.agg()` | Múltiples funciones | Análisis completo |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Agrupar por Múltiples Columnas
# MAGIC
# MAGIC ```python
# MAGIC df.groupby(['sector', 'pais']).sum()
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Agrupemos la cartera por sector.

# COMMAND ----------

# DBTITLE 1,Código - GroupBy en Cartera
print("📦 GROUPBY Y AGREGACIONES")
print("=" * 70)

# 1. Agrupar por sector: Suma de inversiones
print("\n💰 1. Inversión Total por Sector:")
inversion_sector = cartera.groupby('sector')['valor_total'].sum().sort_values(ascending=False)
display(inversion_sector.to_frame())

# 2. Múltiples estadísticas por sector
print("\n📈 2. Estadísticas Completas por Sector:")
estadisticas_sector = cartera.groupby('sector').agg({
    'ticker': 'count',  # Cantidad de acciones
    'precio': 'mean',   # Precio promedio
    'cantidad': 'sum',  # Cantidad total de acciones
    'valor_total': ['sum', 'mean', 'max']  # Múltiples operaciones
})
display(estadisticas_sector)

# 3. Agrupar y redondear
print("\n📊 3. Resumen por Sector (redondeado):")
resumen = cartera.groupby('sector').agg({
    'ticker': 'count',
    'precio': 'mean',
    'valor_total': 'sum'
}).round(2)
resumen.columns = ['Num_Acciones', 'Precio_Promedio', 'Inversion_Total']
display(resumen)

# 4. Porcentaje de inversión por sector
print("\n🧩 4. Porcentaje de Inversión por Sector:")
inversion_total = cartera['valor_total'].sum()
porcentaje_sector = (inversion_sector / inversion_total * 100).round(2)
porcentaje_sector = porcentaje_sector.sort_values(ascending=False)
for sector, pct in porcentaje_sector.items():
    print(f"   {sector}: {pct}%")

# 5. Top ticker por sector (precio más alto)
print("\n🏆 5. Acción Más Cara por Sector:")
top_por_sector = cartera.loc[cartera.groupby('sector')['precio'].idxmax()]
display(top_por_sector[['sector', 'ticker', 'precio']])

# 6. Agrupar por múltiples columnas
print("\n🌎 6. Inversión por Sector y País:")
inversion_sector_pais = cartera.groupby(['sector', 'pais'])['valor_total'].sum()
display(inversion_sector_pais.to_frame())

# 7. Filtrar grupos: Sectores con inversión > $100,000
print("\n🔹 7. Sectores con Inversión > $100,000:")
sectores_grandes = inversion_sector[inversion_sector > 100000]
display(sectores_grandes.to_frame())

print("\n✅ Agregaciones completadas")

# COMMAND ----------

# DBTITLE 1,Sección - Series Temporales
# MAGIC %md
# MAGIC
# MAGIC # 📅 PARTE 6: Series Temporales Financieras
# MAGIC
# MAGIC ## ¿Qué son Series Temporales?
# MAGIC
# MAGIC Una **serie temporal** es un conjunto de datos ordenados cronológicamente.
# MAGIC
# MAGIC ### Ejemplos financieros:
# MAGIC - Precios históricos de acciones
# MAGIC - Cotizaciones del dólar
# MAGIC - Volumen de operaciones diario
# MAGIC - Rendimientos mensuales
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Herramientas de Pandas para Series Temporales
# MAGIC
# MAGIC ### 1. `.pct_change()` - Calcular Rendimientos
# MAGIC ```python
# MAGIC rendimientos = precios.pct_change()
# MAGIC ```
# MAGIC * Calcula el cambio porcentual entre valores consecutivos
# MAGIC * **Esencial** para análisis de retornos
# MAGIC
# MAGIC ### 2. `.shift()` - Desplazar Valores
# MAGIC ```python
# MAGIC precios_ayer = precios.shift(1)
# MAGIC ```
# MAGIC * Mueve los datos hacia adelante o atrás
# MAGIC * Útil para comparaciones temporales
# MAGIC
# MAGIC ### 3. `.rolling()` - Ventanas Móviles
# MAGIC ```python
# MAGIC media_movil_7 = precios.rolling(window=7).mean()
# MAGIC ```
# MAGIC * Calcula estadísticas en ventanas deslizantes
# MAGIC * **Medias móviles**: indicador técnico clave
# MAGIC
# MAGIC ### 4. `.resample()` - Cambiar Frecuencia
# MAGIC ```python
# MAGIC precios_semanales = precios.resample('W').last()
# MAGIC ```
# MAGIC * Cambia de frecuencia (diario → semanal → mensual)
# MAGIC * Útil para análisis agregados
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Frecuencias en Pandas
# MAGIC
# MAGIC | Código | Frecuencia |
# MAGIC |--------|------------|
# MAGIC | `'D'` | Diario |
# MAGIC | `'W'` | Semanal |
# MAGIC | `'M'` | Mensual |
# MAGIC | `'Q'` | Trimestral |
# MAGIC | `'Y'` | Anual |
# MAGIC | `'H'` | Horario |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Creemos series temporales de YPF.

# COMMAND ----------

# DBTITLE 1,Código - Series Temporales YPF
print("📅 SERIES TEMPORALES - YPF")
print("=" * 70)

# 1. Crear fechas de 60 días
fechas = pd.date_range(start='2024-04-13', periods=60, freq='D')

# 2. Simular precios históricos de YPF (partiendo de $5000)
np.random.seed(42)  # Para reproducibilidad
rendimientos_diarios = np.random.normal(0.001, 0.025, 60)  # Media 0.1%, volatilidad 2.5%
precios_ypf = pd.Series(index=fechas, dtype=float)
precios_ypf.iloc[0] = 5000  # Precio inicial

# Generar precios con paseo aleatorio
for i in range(1, 60):
    precios_ypf.iloc[i] = precios_ypf.iloc[i-1] * (1 + rendimientos_diarios[i])

print("\n📈 1. Precios Históricos de YPF (primeros 10 días):")
print(precios_ypf.head(10))

# 3. Calcular rendimientos diarios
rendimientos = precios_ypf.pct_change() * 100  # En porcentaje

print("\n💹 2. Rendimientos Diarios (últimos 10 días):")
print(rendimientos.tail(10).round(2))

# 4. Media móvil de 7 y 30 días
ma_7 = precios_ypf.rolling(window=7).mean()
ma_30 = precios_ypf.rolling(window=30).mean()

print("\n📊 3. Precios con Medias Móviles (últimos 5 días):")
df_ma = pd.DataFrame({
    'Precio': precios_ypf,
    'MA_7': ma_7,
    'MA_30': ma_30
})
display(df_ma.tail())

# 5. Resample a frecuencia semanal
precios_semanales = precios_ypf.resample('W').last()

print("\n📅 4. Precios Semanales (cierre de cada semana):")
print(precios_semanales)

# 6. Volatilidad rodante (ventana de 10 días)
volatilidad_10d = rendimientos.rolling(window=10).std()

print("\n📉 5. Volatilidad Rodante (10 días, últimos 5 días):")
print(volatilidad_10d.tail().round(3))

# 7. Estadísticas del período
print("\n📊 6. Estadísticas del Período (60 días):")
print(f"   Precio Inicial: ${precios_ypf.iloc[0]:,.2f}")
print(f"   Precio Final: ${precios_ypf.iloc[-1]:,.2f}")
print(f"   Retorno Total: {((precios_ypf.iloc[-1] / precios_ypf.iloc[0]) - 1) * 100:.2f}%")
print(f"   Rendimiento Diario Promedio: {rendimientos.mean():.2f}%")
print(f"   Volatilidad Diaria: {rendimientos.std():.2f}%")
print(f"   Precio Máximo: ${precios_ypf.max():,.2f} ({precios_ypf.idxmax().strftime('%d/%m/%Y')})") 
print(f"   Precio Mínimo: ${precios_ypf.min():,.2f} ({precios_ypf.idxmin().strftime('%d/%m/%Y')})")

print("\n✅ Análisis de series temporales completado")

# COMMAND ----------

# DBTITLE 1,Sección - Manipulación Avanzada
# MAGIC %md
# MAGIC
# MAGIC # 🔗 PARTE 7: Manipulación Avanzada de DataFrames
# MAGIC
# MAGIC ## Combinar DataFrames
# MAGIC
# MAGIC ### 1. `.merge()` - SQL-style Joins
# MAGIC
# MAGIC Combina dos DataFrames basándose en columnas comunes.
# MAGIC
# MAGIC #### Tipos de Joins:
# MAGIC
# MAGIC | Tipo | Descripción | SQL Equivalente |
# MAGIC |------|-------------|------------------|
# MAGIC | `inner` | Solo filas que coinciden en ambos | INNER JOIN |
# MAGIC | `left` | Todas las filas del izquierdo | LEFT JOIN |
# MAGIC | `right` | Todas las filas del derecho | RIGHT JOIN |
# MAGIC | `outer` | Todas las filas de ambos | FULL OUTER JOIN |
# MAGIC
# MAGIC #### Sintaxis:
# MAGIC ```python
# MAGIC df_combined = df1.merge(df2, on='ticker', how='inner')
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 2. `.concat()` - Concatenar DataFrames
# MAGIC
# MAGIC Apila DataFrames verticalmente (agregar filas) u horizontalmente (agregar columnas).
# MAGIC
# MAGIC ```python
# MAGIC # Vertical (apilar filas)
# MAGIC df_total = pd.concat([df1, df2], axis=0)
# MAGIC
# MAGIC # Horizontal (agregar columnas)
# MAGIC df_wide = pd.concat([df1, df2], axis=1)
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 3. `.pivot_table()` - Tabla Dinámica
# MAGIC
# MAGIC Crea tablas dinámicas como en Excel.
# MAGIC
# MAGIC ```python
# MAGIC pivot = df.pivot_table(
# MAGIC     values='precio',
# MAGIC     index='sector',
# MAGIC     columns='fecha',
# MAGIC     aggfunc='mean'
# MAGIC )
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 4. `.apply()` - Aplicar Funciones Personalizadas
# MAGIC
# MAGIC Aplica una función a cada fila o columna.
# MAGIC
# MAGIC ```python
# MAGIC # Por columna
# MAGIC df['nueva_col'] = df['precio'].apply(lambda x: x * 1.21)  # Agregar IVA
# MAGIC
# MAGIC # Por fila
# MAGIC df['categoria'] = df.apply(lambda row: 'Cara' if row['precio'] > 1000 else 'Barata', axis=1)
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Veamos ejemplos prácticos de combinación.

# COMMAND ----------

# DBTITLE 1,Código - Manipulación Avanzada
print("🔗 MANIPULACIÓN AVANZADA DE DATAFRAMES")
print("=" * 70)

# 1. Crear 3 DataFrames para combinar

# DataFrame 1: Precios actuales
precios_hoy = pd.DataFrame({
    'ticker': ['YPF', 'GGAL', 'MELI', 'COME', 'TRAN'],
    'precio_hoy': [5200.00, 175.50, 1450.80, 2.35, 1150.00]
})

# DataFrame 2: Precios hace 1 mes
precios_mes_anterior = pd.DataFrame({
    'ticker': ['YPF', 'GGAL', 'MELI', 'LOMA', 'TRAN'],  # LOMA no está en hoy, COME no está aquí
    'precio_mes_anterior': [4800.00, 165.00, 1380.00, 880.00, 1100.00]
})

# DataFrame 3: Información de empresas
info_empresas = pd.DataFrame({
    'ticker': ['YPF', 'GGAL', 'MELI', 'COME', 'TRAN', 'LOMA'],
    'sector': ['Energía', 'Bancario', 'Tecnología', 'Alimentos', 'Transporte', 'Energía'],
    'empleados': [50000, 8000, 15000, 12000, 5000, 7500]
})

print("\n📋 DataFrames Originales:")
print("\n1. Precios Hoy:")
display(precios_hoy)
print("\n2. Precios Mes Anterior:")
display(precios_mes_anterior)
print("\n3. Información de Empresas:")
display(info_empresas)

# 2. MERGE - Inner Join (solo tickers que están en ambos)
print("\n" + "=" * 70)
print("🔀 2. INNER JOIN - Solo tickers en ambos DataFrames:")
inner_merge = precios_hoy.merge(precios_mes_anterior, on='ticker', how='inner')
inner_merge['variacion_%'] = ((inner_merge['precio_hoy'] / inner_merge['precio_mes_anterior']) - 1) * 100
display(inner_merge)

# 3. MERGE - Left Join (todos de precios_hoy)
print("\n" + "=" * 70)
print("🔀 3. LEFT JOIN - Todos los tickers de hoy (NaN si no hay precio anterior):")
left_merge = precios_hoy.merge(precios_mes_anterior, on='ticker', how='left')
display(left_merge)

# 4. MERGE - Outer Join (todos los tickers)
print("\n" + "=" * 70)
print("🔀 4. OUTER JOIN - Todos los tickers de ambos DataFrames:")
outer_merge = precios_hoy.merge(precios_mes_anterior, on='ticker', how='outer')
display(outer_merge)

# 5. MERGE - Multiple DataFrames (encadenado)
print("\n" + "=" * 70)
print("🔗 5. MERGE Múltiple - Combinar los 3 DataFrames:")
df_completo = precios_hoy.merge(precios_mes_anterior, on='ticker', how='outer') \
                        .merge(info_empresas, on='ticker', how='left')
display(df_completo)

# 6. CONCAT - Apilar verticalmente (agregar filas)
print("\n" + "=" * 70)
print("⬇️ 6. CONCAT Vertical - Apilar DataFrames:")

# Crear dos DataFrames para apilar
cartera_1 = pd.DataFrame({
    'ticker': ['YPF', 'GGAL'],
    'cantidad': [100, 500],
    'origen': ['Cartera A', 'Cartera A']
})

cartera_2 = pd.DataFrame({
    'ticker': ['MELI', 'COME'],
    'cantidad': [50, 10000],
    'origen': ['Cartera B', 'Cartera B']
})

cartera_total = pd.concat([cartera_1, cartera_2], axis=0, ignore_index=True)
display(cartera_total)

# 7. PIVOT TABLE - Crear tabla dinámica
print("\n" + "=" * 70)
print("📊 7. PIVOT TABLE - Resumen por Sector:")

# Crear datos para pivot
operaciones = pd.DataFrame({
    'fecha': ['2024-06-10', '2024-06-10', '2024-06-11', '2024-06-11', '2024-06-12', '2024-06-12'],
    'sector': ['Energía', 'Bancario', 'Energía', 'Bancario', 'Energía', 'Bancario'],
    'volumen': [1000000, 500000, 1200000, 600000, 900000, 550000],
    'operaciones': [150, 200, 180, 220, 140, 210]
})

pivot = operaciones.pivot_table(
    values='volumen',
    index='sector',
    columns='fecha',
    aggfunc='sum'
)

display(pivot)

# 8. APPLY - Aplicar función personalizada
print("\n" + "=" * 70)
print("🔧 8. APPLY - Clasificar acciones por precio:")

# Función de clasificación
def clasificar_precio(precio):
    if pd.isna(precio):
        return 'Sin Datos'
    elif precio < 100:
        return 'Muy Barata'
    elif precio < 500:
        return 'Barata'
    elif precio < 1000:
        return 'Media'
    else:
        return 'Cara'

precios_hoy['clasificacion'] = precios_hoy['precio_hoy'].apply(clasificar_precio)
display(precios_hoy)

# 9. APPLY por fila - Cálculo condicional
print("\n" + "=" * 70)
print("🔧 9. APPLY por Fila - Recomendación de Inversión:")

df_completo['recomendacion'] = df_completo.apply(
    lambda row: 'COMPRAR' if pd.notna(row['precio_hoy']) and pd.notna(row['precio_mes_anterior']) and row['precio_hoy'] < row['precio_mes_anterior']
                else 'VENDER' if pd.notna(row['precio_hoy']) and pd.notna(row['precio_mes_anterior']) and row['precio_hoy'] > row['precio_mes_anterior']
                else 'MANTENER',
    axis=1
)

display(df_completo[['ticker', 'precio_hoy', 'precio_mes_anterior', 'sector', 'recomendacion']])

print("\n✅ Manipulación avanzada completada")

# COMMAND ----------

# DBTITLE 1,Caso Integrado - Análisis de Cartera
# MAGIC %md
# MAGIC
# MAGIC # 💼 CASO INTEGRADO: Análisis Completo de Cartera
# MAGIC
# MAGIC ## 🎯 Escenario
# MAGIC
# MAGIC Eres analista en una **casa de bolsa argentina** y debes preparar un **reporte ejecutivo** de la cartera de inversión de un cliente.
# MAGIC
# MAGIC ### 📋 Datos Disponibles:
# MAGIC
# MAGIC 1. **Cartera del cliente**: 8 acciones argentinas
# MAGIC 2. **Precios históricos**: 30 días de cotizaciones
# MAGIC 3. **Objetivo**: Entregar un reporte con:
# MAGIC    - Rendimientos individuales y de cartera
# MAGIC    - Análisis por sector
# MAGIC    - Identificación de mejores y peores performers
# MAGIC    - Métricas de riesgo (volatilidad)
# MAGIC    - Recomendaciones de rebalanceo
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🔍 Tareas del Análisis:
# MAGIC
# MAGIC 1. ✅ Crear dataset de cartera
# MAGIC 2. ✅ Simular precios históricos 30 días
# MAGIC 3. ✅ Calcular rendimientos y volatilidad
# MAGIC 4. ✅ Análisis por sector
# MAGIC 5. ✅ Identificar top/bottom performers
# MAGIC 6. ✅ Calcular métricas de riesgo
# MAGIC 7. ✅ Generar reporte ejecutivo
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Analicemos la cartera completa.

# COMMAND ----------

# DBTITLE 1,Código - Caso Integrado Completo
print("💼 CASO INTEGRADO: ANÁLISIS COMPLETO DE CARTERA")
print("=" * 70)
print("🏢 Casa de Bolsa: Merval Inversiones")
print("👤 Cliente: Juan Pérez")
print("📅 Fecha de Análisis: 12 de Junio de 2024")
print("=" * 70)

# ========== PASO 1: CARGAR DATOS DE LA CARTERA ==========
print("\n📊 PASO 1: Cartera del Cliente")
print("-" * 70)

cartera_cliente = pd.DataFrame({
    'ticker': ['YPF', 'GGAL', 'MELI', 'COME', 'TRAN', 'LOMA', 'ALUA', 'CRES'],
    'cantidad': [200, 1000, 80, 15000, 150, 400, 8000, 2000],
    'precio_compra': [4500, 160, 1300, 2.10, 1050, 850, 2.80, 16.50],
    'precio_actual': [5200, 175.50, 1450.80, 2.35, 1150, 920, 3.15, 18.50],
    'sector': ['Energía', 'Bancario', 'Tecnología', 'Alimentos', 'Transporte', 'Energía', 'Industrial', 'Bancario']
})

# Calcular valores
cartera_cliente['inversion_inicial'] = cartera_cliente['cantidad'] * cartera_cliente['precio_compra']
cartera_cliente['valor_actual'] = cartera_cliente['cantidad'] * cartera_cliente['precio_actual']
cartera_cliente['ganancia_perdida'] = cartera_cliente['valor_actual'] - cartera_cliente['inversion_inicial']
cartera_cliente['rendimiento_%'] = ((cartera_cliente['precio_actual'] / cartera_cliente['precio_compra']) - 1) * 100

display(cartera_cliente)

# ========== PASO 2: MÉTRICAS GENERALES ==========
print("\n💰 PASO 2: Resumen Ejecutivo")
print("-" * 70)

inversion_total = cartera_cliente['inversion_inicial'].sum()
valor_actual_total = cartera_cliente['valor_actual'].sum()
ganancia_total = cartera_cliente['ganancia_perdida'].sum()
rendimiento_cartera = ((valor_actual_total / inversion_total) - 1) * 100

print(f"   Inversión Inicial: ${inversion_total:,.2f}")
print(f"   Valor Actual: ${valor_actual_total:,.2f}")
print(f"   Ganancia/Pérdida: ${ganancia_total:,.2f}")
print(f"   Rendimiento Total: {rendimiento_cartera:.2f}%")

if rendimiento_cartera > 0:
    print(f"   ✅ Estado: GANANCIA (${ganancia_total:,.2f})")
else:
    print(f"   ⚠️ Estado: PÉRDIDA (${ganancia_total:,.2f})")

# ========== PASO 3: ANÁLISIS POR SECTOR ==========
print("\n🏢 PASO 3: Análisis por Sector")
print("-" * 70)

sector_analisis = cartera_cliente.groupby('sector').agg({
    'ticker': 'count',
    'inversion_inicial': 'sum',
    'valor_actual': 'sum',
    'ganancia_perdida': 'sum',
    'rendimiento_%': 'mean'
}).round(2)

sector_analisis.columns = ['Num_Acciones', 'Inversion_Inicial', 'Valor_Actual', 'Ganancia_Perdida', 'Rendimiento_Promedio_%']
sector_analisis = sector_analisis.sort_values('Ganancia_Perdida', ascending=False)

display(sector_analisis)

# Porcentaje de cartera por sector
print("\n📊 Distribución de Cartera por Sector:")
porcentaje_sector = (cartera_cliente.groupby('sector')['valor_actual'].sum() / valor_actual_total * 100).sort_values(ascending=False)
for sector, pct in porcentaje_sector.items():
    print(f"   {sector}: {pct:.2f}%")

# ========== PASO 4: TOP Y BOTTOM PERFORMERS ==========
print("\n🏆 PASO 4: Top y Bottom Performers")
print("-" * 70)

# Top 3 mejores
top_3 = cartera_cliente.nlargest(3, 'rendimiento_%')[['ticker', 'sector', 'rendimiento_%', 'ganancia_perdida']]
print("\n✅ Top 3 Mejores Acciones:")
for idx, row in top_3.iterrows():
    print(f"   {row['ticker']} ({row['sector']}): +{row['rendimiento_%']:.2f}% (${row['ganancia_perdida']:,.2f})")

# Bottom 3 peores
bottom_3 = cartera_cliente.nsmallest(3, 'rendimiento_%')[['ticker', 'sector', 'rendimiento_%', 'ganancia_perdida']]
print("\n⚠️ Bottom 3 Peores Acciones:")
for idx, row in bottom_3.iterrows():
    print(f"   {row['ticker']} ({row['sector']}): {row['rendimiento_%']:.2f}% (${row['ganancia_perdida']:,.2f})")

# ========== PASO 5: SIMULAR VOLATILIDAD (ÚLTIMOS 30 DÍAS) ==========
print("\n📉 PASO 5: Análisis de Riesgo (Volatilidad)")
print("-" * 70)

# Simular rendimientos diarios para cada acción
np.random.seed(123)
volatilidades = {}  # Volatilidad anualizada

for ticker in cartera_cliente['ticker']:
    # Simular 30 días de rendimientos (distribución normal)
    rendimientos_diarios = np.random.normal(0.001, 0.02, 30)  # Media 0.1%, vol 2%
    volatilidad_diaria = np.std(rendimientos_diarios)
    volatilidad_anualizada = volatilidad_diaria * np.sqrt(252) * 100  # 252 días hábiles
    volatilidades[ticker] = volatilidad_anualizada

# Agregar volatilidad al DataFrame
cartera_cliente['volatilidad_anual_%'] = cartera_cliente['ticker'].map(volatilidades)

print("\n📊 Volatilidad Anualizada por Acción:")
volatilidad_df = cartera_cliente[['ticker', 'sector', 'rendimiento_%', 'volatilidad_anual_%']].sort_values('volatilidad_anual_%', ascending=False)
display(volatilidad_df)

# Clasificación de riesgo
print("\n⚠️ Clasificación de Riesgo:")
for idx, row in volatilidad_df.iterrows():
    if row['volatilidad_anual_%'] < 20:
        riesgo = "BAJO"
    elif row['volatilidad_anual_%'] < 35:
        riesgo = "MEDIO"
    else:
        riesgo = "ALTO"
    print(f"   {row['ticker']}: {row['volatilidad_anual_%']:.2f}% → Riesgo {riesgo}")

# ========== PASO 6: CONCENTRACIÓN DE CARTERA ==========
print("\n🎯 PASO 6: Análisis de Concentración")
print("-" * 70)

cartera_cliente['peso_cartera_%'] = (cartera_cliente['valor_actual'] / valor_actual_total * 100)

print("\n📊 Peso de cada Acción en la Cartera:")
for idx, row in cartera_cliente.sort_values('peso_cartera_%', ascending=False).iterrows():
    print(f"   {row['ticker']}: {row['peso_cartera_%']:.2f}%")

# Alertas de concentración
print("\n⚠️ Alertas de Concentración:")
for idx, row in cartera_cliente.iterrows():
    if row['peso_cartera_%'] > 25:
        print(f"   🔴 {row['ticker']}: {row['peso_cartera_%']:.2f}% - ALTA CONCENTRACIÓN (riesgo de sobre-exposición)")
    elif row['peso_cartera_%'] > 15:
        print(f"   🟡 {row['ticker']}: {row['peso_cartera_%']:.2f}% - Concentración moderada")

# ========== PASO 7: REPORTE FINAL ==========
print("\n" + "=" * 70)
print("📋 REPORTE EJECUTIVO FINAL")
print("=" * 70)

print(f"\n💼 RESUMEN DE CARTERA:")
print(f"   • Total Invertido: ${inversion_total:,.2f}")
print(f"   • Valor Actual: ${valor_actual_total:,.2f}")
print(f"   • Ganancia Neta: ${ganancia_total:,.2f}")
print(f"   • Rendimiento: {rendimiento_cartera:.2f}%")

print(f"\n🏆 MEJOR INVERSIÓN:")
mejor = cartera_cliente.loc[cartera_cliente['rendimiento_%'].idxmax()]
print(f"   {mejor['ticker']} ({mejor['sector']}): +{mejor['rendimiento_%']:.2f}% (${mejor['ganancia_perdida']:,.2f})")

print(f"\n⚠️ PEOR INVERSIÓN:")
peor = cartera_cliente.loc[cartera_cliente['rendimiento_%'].idxmin()]
print(f"   {peor['ticker']} ({peor['sector']}): {peor['rendimiento_%']:.2f}% (${peor['ganancia_perdida']:,.2f})")

print(f"\n🏢 MEJOR SECTOR:")
mejor_sector = sector_analisis['Ganancia_Perdida'].idxmax()
print(f"   {mejor_sector}: ${sector_analisis.loc[mejor_sector, 'Ganancia_Perdida']:,.2f}")

print(f"\n📊 RECOMENDACIONES:")
if rendimiento_cartera > 10:
    print("   ✅ Cartera con excelente desempeño")
    print("   ✅ Considerar tomar ganancias en acciones con alta volatilidad")
elif rendimiento_cartera > 0:
    print("   ✅ Cartera con desempeño positivo")
    print("   ⚠️ Monitorear acciones con rendimiento negativo")
else:
    print("   ⚠️ Cartera con pérdidas")
    print("   🔄 Considerar rebalanceo hacia sectores más rentables")

# Recomendaciones de diversificación
if (cartera_cliente['peso_cartera_%'] > 25).any():
    print("   🔴 ALERTA: Alta concentración - Diversificar posiciones")

if sector_analisis['Num_Acciones'].max() > 3:
    print("   🟡 Considerar mayor diversificación sectorial")

print("\n" + "=" * 70)
print("✅ ANÁLISIS COMPLETO DE CARTERA FINALIZADO")
print("=" * 70)

# COMMAND ----------

# DBTITLE 1,Ejercicios Prácticos
# MAGIC %md
# MAGIC
# MAGIC # 🎓 EJERCICIOS PRÁCTICOS
# MAGIC
# MAGIC ## 📝 5 Ejercicios sobre Bonos Argentinos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 💡 Ejercicio 1: Crear DataFrame de Bonos
# MAGIC
# MAGIC **Objetivo**: Crear un DataFrame con bonos del Tesoro argentino.
# MAGIC
# MAGIC **Datos**:
# MAGIC ```python
# MAGIC bonos = pd.DataFrame({
# MAGIC     'ticker': ['AL30', 'AL35', 'GD30', 'GD35', 'AE38'],
# MAGIC     'vencimiento': ['2030-07-09', '2035-07-09', '2030-07-09', '2035-07-09', '2038-12-31'],
# MAGIC     'tasa_cupon': [1.00, 3.875, 1.00, 2.50, 1.00],
# MAGIC     'precio': [35.50, 42.30, 36.20, 38.50, 28.75],
# MAGIC     'rating': ['B-', 'B-', 'B-', 'B-', 'B-'],
# MAGIC     'moneda': ['USD', 'USD', 'USD', 'USD', 'USD']
# MAGIC })
# MAGIC ```
# MAGIC
# MAGIC **Tareas**:
# MAGIC 1. Convertir la columna `vencimiento` a tipo fecha
# MAGIC 2. Calcular días hasta el vencimiento
# MAGIC 3. Agregar columna `valor_nominal` (100 para todos)
# MAGIC 4. Calcular el rendimiento implícito: `(valor_nominal / precio - 1) * 100`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 💡 Ejercicio 2: Calcular Duración
# MAGIC
# MAGIC **Objetivo**: Calcular la duración aproximada de cada bono.
# MAGIC
# MAGIC **Fórmula Simplificada**:
# MAGIC ```
# MAGIC Duración ≈ Años hasta vencimiento / (1 + tasa_cupon)
# MAGIC ```
# MAGIC
# MAGIC **Tareas**:
# MAGIC 1. Calcular años hasta el vencimiento desde hoy
# MAGIC 2. Aplicar la fórmula de duración
# MAGIC 3. Identificar el bono con mayor duración (mayor sensibilidad a tasas)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 💡 Ejercicio 3: Filtrar por Rating y Precio
# MAGIC
# MAGIC **Objetivo**: Filtrar bonos según criterios de inversión.
# MAGIC
# MAGIC **Tareas**:
# MAGIC 1. Filtrar bonos con rating 'B-' o mejor
# MAGIC 2. Filtrar bonos con precio < $40 (oportunidad de compra)
# MAGIC 3. Combinar ambos filtros con operador AND
# MAGIC 4. Ordenar por rendimiento descendente
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 💡 Ejercicio 4: Agrupar por Emisor
# MAGIC
# MAGIC **Objetivo**: Analizar bonos por tipo de emisor.
# MAGIC
# MAGIC **Datos adicionales**:
# MAGIC ```python
# MAGIC # Agregar columna de emisor
# MAGIC bonos['emisor'] = bonos['ticker'].apply(lambda x: 'Ley Argentina' if x.startswith('AL') else 'Ley Extranjera')
# MAGIC ```
# MAGIC
# MAGIC **Tareas**:
# MAGIC 1. Agrupar por `emisor`
# MAGIC 2. Calcular precio promedio, tasa de cupón promedio
# MAGIC 3. Contar cantidad de bonos por emisor
# MAGIC 4. Identificar qué emisor tiene mejores condiciones
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 💡 Ejercicio 5: Calcular TIR Aproximada
# MAGIC
# MAGIC **Objetivo**: Estimar la Tasa Interna de Retorno (TIR) de los bonos.
# MAGIC
# MAGIC **Fórmula Simplificada**:
# MAGIC ```
# MAGIC TIR ≈ (Cupón Anual + (Valor Nominal - Precio) / Años al Vencimiento) / ((Valor Nominal + Precio) / 2) * 100
# MAGIC ```
# MAGIC
# MAGIC **Tareas**:
# MAGIC 1. Calcular cupón anual: `tasa_cupon * valor_nominal / 100`
# MAGIC 2. Calcular años al vencimiento
# MAGIC 3. Aplicar fórmula de TIR aproximada
# MAGIC 4. Crear columna con clasificación:
# MAGIC    - TIR > 10%: "Alta Rentabilidad"
# MAGIC    - TIR 5-10%: "Rentabilidad Media"
# MAGIC    - TIR < 5%: "Baja Rentabilidad"
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎯 Desafío Extra
# MAGIC
# MAGIC Combina todos los análisis anteriores en un **reporte ejecutivo de bonos** que incluya:
# MAGIC - Resumen de cartera de bonos
# MAGIC - Bonos recomendados para compra
# MAGIC - Análisis de riesgo por duración
# MAGIC - Comparación entre emisores
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 💪 ¡Practica estos ejercicios para dominar Pandas!
# MAGIC
# MAGIC 🔍 **Pista**: Usa `.apply()`, `.groupby()`, y filtros booleanos.

# COMMAND ----------

# DBTITLE 1,Consultas con Genie
# MAGIC %md
# MAGIC
# MAGIC # 🤖 CONSULTAS CON GENIE
# MAGIC
# MAGIC ## ¿Qué es Genie?
# MAGIC
# MAGIC **Genie** es el asistente de IA de Databricks que te ayuda a analizar datos usando **lenguaje natural**.
# MAGIC
# MAGIC ### ¿Cómo funciona?
# MAGIC
# MAGIC 1. Escribes tu pregunta en español
# MAGIC 2. Genie genera el código Python/SQL necesario
# MAGIC 3. Ejecuta el análisis
# MAGIC 4. Muestra los resultados
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📝 3 Consultas Ejemplo para Practicar
# MAGIC
# MAGIC ### 🔹 Consulta 1: Rendimiento Promedio por Sector
# MAGIC
# MAGIC **Pregunta para Genie**:
# MAGIC > *"¿Cuál es el rendimiento promedio de las acciones del sector Energía en la cartera?"*
# MAGIC
# MAGIC **Qué hace**:
# MAGIC - Filtra acciones del sector Energía
# MAGIC - Calcula el promedio de rendimientos
# MAGIC - Muestra el resultado
# MAGIC
# MAGIC **Resultado esperado**: Número con rendimiento % del sector
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Consulta 2: Top 3 Acciones por Volumen
# MAGIC
# MAGIC **Pregunta para Genie**:
# MAGIC > *"Mostrar las 3 acciones con mayor volumen de operaciones en los últimos 30 días"*
# MAGIC
# MAGIC **Qué hace**:
# MAGIC - Ordena acciones por volumen
# MAGIC - Selecciona las top 3
# MAGIC - Muestra ticker, volumen y sector
# MAGIC
# MAGIC **Resultado esperado**: Tabla con 3 filas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Consulta 3: Correlación entre Acciones
# MAGIC
# MAGIC **Pregunta para Genie**:
# MAGIC > *"Calcular la correlación entre los rendimientos de YPF y GGAL en los últimos 60 días"*
# MAGIC
# MAGIC **Qué hace**:
# MAGIC - Obtiene precios históricos de ambas acciones
# MAGIC - Calcula rendimientos diarios
# MAGIC - Calcula correlación (coeficiente entre -1 y 1)
# MAGIC
# MAGIC **Resultado esperado**: Número entre -1 y 1
# MAGIC - **+1**: Perfecta correlación positiva
# MAGIC - **0**: Sin correlación
# MAGIC - **-1**: Perfecta correlación negativa
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 💡 Más Ideas de Consultas
# MAGIC
# MAGIC Practica con Genie preguntándole:
# MAGIC
# MAGIC ✅ "¿Cuál es la acción más volátil de la cartera?"
# MAGIC ✅ "Crear un gráfico de líneas con los precios de MELI en los últimos 90 días"
# MAGIC ✅ "¿Qué porcentaje de la cartera está invertido en el sector Bancario?"
# MAGIC ✅ "Mostrar las acciones que tuvieron rendimiento negativo en el último mes"
# MAGIC ✅ "Calcular la matriz de correlación entre todas las acciones de la cartera"
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎯 Ventajas de Usar Genie
# MAGIC
# MAGIC ✅ **Rápido**: No necesitas escribir código
# MAGIC ✅ **Educativo**: Aprendes viendo el código generado
# MAGIC ✅ **Versátil**: Análisis + visualizaciones
# MAGIC ✅ **Iterativo**: Puedes refinar tu pregunta
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **Tip**: Después de que Genie genere el código, **revísalo** para entender qué hizo. ¡Es la mejor forma de aprender!
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC # 🎉 ¡FELICITACIONES!
# MAGIC
# MAGIC Has completado el **Notebook 0.5 - Pandas para Finanzas**.
# MAGIC
# MAGIC ## 🎓 Lo que Aprendiste:
# MAGIC
# MAGIC ✅ **Series y DataFrames** - Estructuras básicas de Pandas
# MAGIC ✅ **Exploración de datos** - `.head()`, `.info()`, `.describe()`
# MAGIC ✅ **Filtrado booleano** - Condiciones múltiples con `&`, `|`, `~`
# MAGIC ✅ **GroupBy y agregaciones** - Análisis por grupos
# MAGIC ✅ **Series temporales** - `.pct_change()`, `.rolling()`, `.resample()`
# MAGIC ✅ **Manipulación avanzada** - `.merge()`, `.concat()`, `.pivot_table()`
# MAGIC ✅ **Caso integrado** - Análisis completo de cartera
# MAGIC ✅ **Ejercicios prácticos** - Bonos argentinos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📚 Próximo Paso
# MAGIC
# MAGIC **Notebook 0.6**: Visualización de Datos con Matplotlib, Seaborn y Plotly
# MAGIC
# MAGIC 🔗 Continúa tu aprendizaje para crear gráficos profesionales.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🐼 Recuerda
# MAGIC
# MAGIC > "Pandas es la herramienta más importante para análisis de datos en Python. Domínala y abrirás infinitas posibilidades en finanzas."
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **🎯 ¡Ahora estás listo para analizar cualquier dataset financiero!**