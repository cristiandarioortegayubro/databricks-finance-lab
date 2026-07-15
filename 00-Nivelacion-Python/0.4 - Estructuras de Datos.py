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
# MAGIC ### Notebook 0.4: Estructuras de Datos
# MAGIC ### 📊 **LISTAS, TUPLAS, DICCIONARIOS Y SETS**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción
# MAGIC %md
# MAGIC # 📦 Introducción: Estructuras de Datos
# MAGIC
# MAGIC ## 📚 Repaso de Notebooks Anteriores
# MAGIC
# MAGIC Hasta ahora aprendimos:
# MAGIC
# MAGIC ✅ **Notebook 0.1**: Variables, tipos de datos (int, float, str, bool), operadores
# MAGIC ✅ **Notebook 0.2**: Condicionales (if/elif/else), bucles (for/while), list comprehensions
# MAGIC ✅ **Notebook 0.3**: Funciones, parámetros, return, librerías
# MAGIC
# MAGIC **Problema**: Hasta ahora, trabajamos con **datos individuales** (un precio, un nombre, un rendimiento).
# MAGIC
# MAGIC ¿Y si necesitamos manejar **múltiples datos relacionados**?
# MAGIC * Una lista de 100 precios históricos
# MAGIC * Un portafolio con 10 acciones y sus cantidades
# MAGIC * Información completa de cada empresa (ticker, precio, sector, rendimiento)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ¿Qué son las Estructuras de Datos?
# MAGIC
# MAGIC Las **estructuras de datos** son formas de **organizar y almacenar múltiples valores** en una sola variable.
# MAGIC
# MAGIC ### Analogía con el mundo real
# MAGIC
# MAGIC 📊 **Variable simple** = Una nota adhesiva con un número
# MAGIC 📦 **Lista** = Una columna de Excel
# MAGIC 📋 **Diccionario** = Una tabla de Excel con columnas nombradas
# MAGIC 📎 **Tupla** = Una nota adhesiva permanente (no se puede cambiar)
# MAGIC 🎯 **Set** = Una lista sin duplicados
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 💼 ¿Por qué son fundamentales en finanzas?
# MAGIC
# MAGIC ### Sin estructuras de datos:
# MAGIC ```python
# MAGIC precio_dia1 = 5250
# MAGIC precio_dia2 = 5280
# MAGIC precio_dia3 = 5195
# MAGIC # ...
# MAGIC precio_dia100 = 5420
# MAGIC # ❌ Imposible de manejar
# MAGIC ```
# MAGIC
# MAGIC ### Con estructuras de datos:
# MAGIC ```python
# MAGIC precios = [5250, 5280, 5195, ..., 5420]  # ✅ Fácil
# MAGIC ```
# MAGIC
# MAGIC ### Aplicaciones financieras
# MAGIC
# MAGIC ✅ **Listas**: Precios históricos, rendimientos diarios, series temporales
# MAGIC ✅ **Diccionarios**: Portafolios (ticker → cantidad), datos de empresas
# MAGIC ✅ **Tuplas**: Información inmutable (fecha, ticker, exchange)
# MAGIC ✅ **Sets**: Tickers únicos, eliminar duplicados, comparar carteras
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📋 Estructura de Este Notebook
# MAGIC
# MAGIC ### Parte 1: Listas 📋
# MAGIC 1. Crear y acceder
# MAGIC 2. Métodos (append, remove, sort)
# MAGIC 3. Listas anidadas (matrices)
# MAGIC
# MAGIC ### Parte 2: Tuplas 📎
# MAGIC * Inmutables (no cambian)
# MAGIC * Cuándo usarlas
# MAGIC
# MAGIC ### Parte 3: Diccionarios 📚
# MAGIC 1. Básico (clave: valor)
# MAGIC 2. Métodos
# MAGIC 3. Diccionarios anidados
# MAGIC
# MAGIC ### Parte 4: Sets 🎯
# MAGIC * Sin duplicados
# MAGIC * Operaciones de conjuntos
# MAGIC
# MAGIC ### Parte 5: Comparación y Casos
# MAGIC * Cuándo usar cada estructura
# MAGIC * Casos integrados
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⏱️ **Tiempo estimado**: 60 minutos
# MAGIC
# MAGIC ¡Empecemos!

# COMMAND ----------

# DBTITLE 1,Explicación - Listas Parte 1
# MAGIC %md
# MAGIC ## 📋 LISTAS - Parte 1: Crear y Acceder
# MAGIC
# MAGIC ### ¿Qué es una Lista?
# MAGIC
# MAGIC Una **lista** es una colección **ordenada** y **mutable** (se puede modificar) de elementos.
# MAGIC
# MAGIC ### Sintaxis
# MAGIC
# MAGIC ```python
# MAGIC precios = [5250, 5280, 5195, 5310, 5420]
# MAGIC ```
# MAGIC
# MAGIC 👉 Se crean con **corchetes** `[]`
# MAGIC 👉 Los elementos se separan por **comas**
# MAGIC 👉 Pueden contener **cualquier tipo** de dato (int, float, str, bool, incluso otras listas)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Indexación: Acceder a Elementos
# MAGIC
# MAGIC Cada elemento tiene una **posición** (index):
# MAGIC
# MAGIC ```
# MAGIC   Precios:  [5250, 5280, 5195, 5310, 5420]
# MAGIC   Índice:     0     1     2     3     4
# MAGIC   Índice:    -5    -4    -3    -2    -1   (negativo: desde el final)
# MAGIC ```
# MAGIC
# MAGIC **Acceder a un elemento**:
# MAGIC ```python
# MAGIC precios[0]   # 5250 (primer elemento)
# MAGIC precios[2]   # 5195 (tercer elemento)
# MAGIC precios[-1]  # 5420 (último elemento)
# MAGIC precios[-2]  # 5310 (penúltimo)
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Slicing: Extraer Sublistas
# MAGIC
# MAGIC **Sintaxis**: `lista[inicio:fin:paso]`
# MAGIC
# MAGIC * `inicio`: Índice donde empieza (incluido)
# MAGIC * `fin`: Índice donde termina (**NO incluido**)
# MAGIC * `paso`: Saltos (opcional)
# MAGIC
# MAGIC **Ejemplos**:
# MAGIC ```python
# MAGIC precios[1:4]    # [5280, 5195, 5310]  (elementos 1, 2, 3)
# MAGIC precios[:3]     # [5250, 5280, 5195]  (primeros 3)
# MAGIC precios[2:]     # [5195, 5310, 5420]  (desde el 2 hasta el final)
# MAGIC precios[::2]    # [5250, 5195, 5420]  (cada 2 elementos)
# MAGIC precios[::-1]   # [5420, 5310, 5195, 5280, 5250]  (invertir)
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Analogía con Excel
# MAGIC
# MAGIC | Excel | Python |
# MAGIC |-------|--------|
# MAGIC | Columna A1:A5 | `precios = [5250, 5280, 5195, 5310, 5420]` |
# MAGIC | `=A1` | `precios[0]` |
# MAGIC | `=A5` | `precios[-1]` |
# MAGIC | `=A2:A4` | `precios[1:4]` |

# COMMAND ----------

# DBTITLE 1,Código - Listas Parte 1
print("═" * 70)
print("EJEMPLO: Listas - Crear y Acceder")
print("═" * 70)

# 1. CREAR LISTAS
print("\n1️⃣ CREAR LISTAS DE DATOS FINANCIEROS")
print("-" * 70)

# Lista de precios históricos de YPF
precios_ypf = [5250, 5280, 5195, 5310, 5420, 5385, 5450]
print(f"Precios de YPF (7 días): {precios_ypf}")

# Lista de tickers
tickers = ["YPF", "GGAL", "MELI", "COME", "TRAN"]
print(f"Tickers: {tickers}")

# Lista mixta (diferentes tipos)
info_accion = ["YPF", "BYMA", 5250.75, True]
print(f"Info mixta: {info_accion} (tipo: {[type(x).__name__ for x in info_accion]})")

# 2. ACCEDER A ELEMENTOS
print("\n2️⃣ ACCEDER A ELEMENTOS POR ÍNDICE")
print("-" * 70)

print(f"\nPrecios: {precios_ypf}")
print(f"\nÍndices positivos:")
print(f"  Primer precio (precios_ypf[0]): ${precios_ypf[0]:,}")
print(f"  Tercer precio (precios_ypf[2]): ${precios_ypf[2]:,}")
print(f"\nÍndices negativos (desde el final):")
print(f"  Último precio (precios_ypf[-1]): ${precios_ypf[-1]:,}")
print(f"  Penúltimo (precios_ypf[-2]): ${precios_ypf[-2]:,}")

# 3. SLICING - Extraer sublistas
print("\n3️⃣ SLICING: EXTRAER SUBLISTAS")
print("-" * 70)

print(f"\nLista completa: {precios_ypf}")
print(f"\nPrimeros 3 días ([:3]): {precios_ypf[:3]}")
print(f"Últimos 3 días ([-3:]): {precios_ypf[-3:]}")
print(f"Del día 2 al 5 ([1:5]): {precios_ypf[1:5]}")
print(f"Cada 2 días ([::2]): {precios_ypf[::2]}")
print(f"Invertir ([::-1]): {precios_ypf[::-1]}")

# 4. APLICACIÓN PRÁCTICA: Análisis de precios
print("\n4️⃣ APLICACIÓN: ANÁLISIS DE PRECIOS")
print("-" * 70)

precio_inicial = precios_ypf[0]
precio_final = precios_ypf[-1]
variacion = precio_final - precio_inicial
variacion_pct = (variacion / precio_inicial) * 100

print(f"\nPeríodo: 7 días")
print(f"Precio inicial: ${precio_inicial:,}")
print(f"Precio final: ${precio_final:,}")
print(f"Variación: ${variacion:+,.0f} ({variacion_pct:+.2f}%)")

# Precio máximo y mínimo
max_precio = max(precios_ypf)
min_precio = min(precios_ypf)
dia_max = precios_ypf.index(max_precio) + 1
dia_min = precios_ypf.index(min_precio) + 1

print(f"\nPrecio máximo: ${max_precio:,} (Día {dia_max})")
print(f"Precio mínimo: ${min_precio:,} (Día {dia_min})")
print(f"Rango: ${max_precio - min_precio:,}")

# Promedio
promedio = sum(precios_ypf) / len(precios_ypf)
print(f"\nPrecio promedio: ${promedio:,.2f}")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - Listas Parte 2
# MAGIC %md
# MAGIC ## 📋 LISTAS - Parte 2: Métodos
# MAGIC
# MAGIC ### Modificar Listas
# MAGIC
# MAGIC Las listas son **mutables**: podemos cambiarlas después de crearlas.
# MAGIC
# MAGIC ### Métodos Principales
# MAGIC
# MAGIC #### 1. **append(elemento)** - Agregar al final
# MAGIC ```python
# MAGIC precios = [100, 150]
# MAGIC precios.append(200)
# MAGIC # precios = [100, 150, 200]
# MAGIC ```
# MAGIC
# MAGIC #### 2. **insert(posición, elemento)** - Agregar en posición específica
# MAGIC ```python
# MAGIC precios.insert(1, 125)  # Insertar 125 en posición 1
# MAGIC # precios = [100, 125, 150, 200]
# MAGIC ```
# MAGIC
# MAGIC #### 3. **remove(elemento)** - Eliminar la primera ocurrencia
# MAGIC ```python
# MAGIC precios.remove(125)
# MAGIC # precios = [100, 150, 200]
# MAGIC ```
# MAGIC
# MAGIC #### 4. **pop(posición)** - Eliminar y devolver elemento
# MAGIC ```python
# MAGIC ultimo = precios.pop()  # Elimina y devuelve el último
# MAGIC # ultimo = 200, precios = [100, 150]
# MAGIC ```
# MAGIC
# MAGIC #### 5. **sort()** - Ordenar (modifica la lista original)
# MAGIC ```python
# MAGIC precios = [200, 100, 150]
# MAGIC precios.sort()
# MAGIC # precios = [100, 150, 200]
# MAGIC
# MAGIC precios.sort(reverse=True)  # Descendente
# MAGIC # precios = [200, 150, 100]
# MAGIC ```
# MAGIC
# MAGIC #### 6. **reverse()** - Invertir
# MAGIC ```python
# MAGIC precios.reverse()
# MAGIC # Invierte el orden actual
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Funciones Útiles
# MAGIC
# MAGIC * `len(lista)` - Longitud
# MAGIC * `sum(lista)` - Suma de elementos
# MAGIC * `min(lista)` - Mínimo
# MAGIC * `max(lista)` - Máximo
# MAGIC * `sorted(lista)` - Nueva lista ordenada (no modifica original)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Uso en Finanzas
# MAGIC
# MAGIC 💼 **Gestionar portafolio dinámico**: Agregar/quitar acciones según estrategia

# COMMAND ----------

# DBTITLE 1,Código - Listas Parte 2
print("═" * 70)
print("EJEMPLO: Listas - Métodos y Modificaciones")
print("═" * 70)

# 1. APPEND - Agregar al final
print("\n1️⃣ APPEND: AGREGAR ACCIONES AL PORTAFOLIO")
print("-" * 70)

portafolio = ["YPF", "GGAL"]
print(f"Portafolio inicial: {portafolio}")

portafolio.append("MELI")
print(f"Después de append('MELI'): {portafolio}")

portafolio.append("COME")
print(f"Después de append('COME'): {portafolio}")

# 2. INSERT - Agregar en posición específica
print("\n2️⃣ INSERT: AGREGAR EN POSICIÓN ESPECÍFICA")
print("-" * 70)

portafolio.insert(1, "TRAN")  # Insertar en posición 1
print(f"Después de insert(1, 'TRAN'): {portafolio}")

# 3. REMOVE - Eliminar elemento
print("\n3️⃣ REMOVE: VENDER UNA ACCIÓN")
print("-" * 70)

print(f"Antes de vender: {portafolio}")
portafolio.remove("TRAN")
print(f"Después de remove('TRAN'): {portafolio}")

# 4. POP - Eliminar y obtener
print("\n4️⃣ POP: ELIMINAR Y OBTENER ELEMENTO")
print("-" * 70)

venta = portafolio.pop()  # Último elemento
print(f"Acción vendida: {venta}")
print(f"Portafolio después de pop(): {portafolio}")

primera = portafolio.pop(0)  # Primer elemento
print(f"Acción vendida (primera): {primera}")
print(f"Portafolio final: {portafolio}")

# 5. SORT - Ordenar
print("\n5️⃣ SORT: ORDENAR PRECIOS")
print("-" * 70)

precios = [5250, 175, 1450, 850, 2.5]
print(f"Precios desordenados: {precios}")

precios.sort()
print(f"Precios ordenados (ascendente): {precios}")

precios.sort(reverse=True)
print(f"Precios ordenados (descendente): {precios}")

# 6. SORTED - Ordenar sin modificar original
print("\n6️⃣ SORTED: CREAR NUEVA LISTA ORDENADA")
print("-" * 70)

rendimientos = [0.12, -0.03, 0.18, 0.05, -0.08]
print(f"Rendimientos originales: {rendimientos}")

rendimientos_ordenados = sorted(rendimientos)
print(f"Rendimientos ordenados: {rendimientos_ordenados}")
print(f"Originales sin cambios: {rendimientos}")

# 7. APLICACIÓN: Gestionar top performers
print("\n7️⃣ APLICACIÓN: TOP PERFORMERS")
print("-" * 70)

acciones_rendimientos = [
    ("YPF", 0.18),
    ("GGAL", 0.09),
    ("MELI", 0.04),
    ("COME", 0.22),
    ("TRAN", -0.03)
]

# Ordenar por rendimiento (segundo elemento de la tupla)
acciones_ordenadas = sorted(acciones_rendimientos, key=lambda x: x[1], reverse=True)

print("\nRanking de acciones por rendimiento:")
for i, (ticker, rendimiento) in enumerate(acciones_ordenadas, 1):
    print(f"  {i}. {ticker:6s}: {rendimiento:+.1%}")

# Top 3
top_3 = [ticker for ticker, _ in acciones_ordenadas[:3]]
print(f"\n🏆 Top 3 acciones: {top_3}")

# 8. FUNCIONES ÚTILES
print("\n8️⃣ FUNCIONES ÚTILES")
print("-" * 70)

precios_semana = [5250, 5280, 5195, 5310, 5420]

print(f"Precios de la semana: {precios_semana}")
print(f"\nCantidad de días (len): {len(precios_semana)}")
print(f"Suma total (sum): ${sum(precios_semana):,}")
print(f"Precio máximo (max): ${max(precios_semana):,}")
print(f"Precio mínimo (min): ${min(precios_semana):,}")
print(f"Precio promedio: ${sum(precios_semana) / len(precios_semana):,.2f}")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - Diccionarios Parte 1
# MAGIC %md
# MAGIC ## 📚 DICCIONARIOS - Parte 1: Básico
# MAGIC
# MAGIC ### ¿Qué es un Diccionario?
# MAGIC
# MAGIC Un **diccionario** es una colección **no ordenada** de pares **clave: valor**.
# MAGIC
# MAGIC ### Analogía
# MAGIC
# MAGIC 📖 Como un diccionario real:
# MAGIC * **Clave** = Palabra que buscas
# MAGIC * **Valor** = Definición
# MAGIC
# MAGIC 💼 En finanzas:
# MAGIC * **Clave** = Ticker de acción
# MAGIC * **Valor** = Cantidad o precio
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Sintaxis
# MAGIC
# MAGIC ```python
# MAGIC cartera = {"YPF": 50, "GGAL": 100, "MELI": 25}
# MAGIC ```
# MAGIC
# MAGIC 👉 Se crean con **llaves** `{}`
# MAGIC 👉 Formato: `{clave1: valor1, clave2: valor2}`
# MAGIC 👉 Las **claves** deben ser únicas e inmutables (str, int, tupla)
# MAGIC 👉 Los **valores** pueden ser cualquier tipo
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Operaciones Básicas
# MAGIC
# MAGIC #### 1. **Acceder a un valor**
# MAGIC ```python
# MAGIC cartera["YPF"]  # 50
# MAGIC ```
# MAGIC
# MAGIC #### 2. **Agregar o modificar**
# MAGIC ```python
# MAGIC cartera["COME"] = 75   # Agregar nueva
# MAGIC cartera["YPF"] = 60    # Modificar existente
# MAGIC ```
# MAGIC
# MAGIC #### 3. **Eliminar**
# MAGIC ```python
# MAGIC del cartera["YPF"]  # Eliminar par completo
# MAGIC ```
# MAGIC
# MAGIC #### 4. **Verificar si existe una clave**
# MAGIC ```python
# MAGIC if "YPF" in cartera:
# MAGIC     print("YPF está en la cartera")
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ventajas sobre Listas
# MAGIC
# MAGIC ✅ **Acceso por nombre**: `cartera["YPF"]` es más claro que `lista[0]`
# MAGIC ✅ **Datos relacionados**: Ticker → Cantidad
# MAGIC ✅ **Búsqueda rápida**: O(1) vs O(n) en listas
# MAGIC
# MAGIC ### Analogía con Excel
# MAGIC
# MAGIC | Excel | Python |
# MAGIC |-------|--------|
# MAGIC | Tabla con 2 columnas (Ticker, Cantidad) | Diccionario |
# MAGIC | `=BUSCARV("YPF", ...)` | `cartera["YPF"]` |

# COMMAND ----------

# DBTITLE 1,Código - Diccionarios Parte 1
print("═" * 70)
print("EJEMPLO: Diccionarios - Básico")
print("═" * 70)

# 1. CREAR DICCIONARIOS
print("\n1️⃣ CREAR DICCIONARIOS")
print("-" * 70)

# Cartera: ticker → cantidad
cartera = {"YPF": 50, "GGAL": 100, "MELI": 25}
print(f"Cartera de acciones:")
for ticker, cantidad in cartera.items():
    print(f"  {ticker}: {cantidad} acciones")

# Precios: ticker → precio
precios = {"YPF": 5250.75, "GGAL": 175.50, "MELI": 1450.00}
print(f"\nPrecios actuales:")
for ticker, precio in precios.items():
    print(f"  {ticker}: ${precio:,.2f}")

# 2. ACCEDER A VALORES
print("\n2️⃣ ACCEDER A VALORES")
print("-" * 70)

print(f"\n¿Cuántas acciones de YPF tengo?")
print(f"  cartera['YPF'] = {cartera['YPF']}")

print(f"\n¿Cuál es el precio de GGAL?")
print(f"  precios['GGAL'] = ${precios['GGAL']:,.2f}")

# Calcular valor de una posición
ticker = "YPF"
cantidad = cartera[ticker]
precio = precios[ticker]
valor = cantidad * precio
print(f"\nValor de la posición en {ticker}:")
print(f"  {cantidad} acciones × ${precio:,.2f} = ${valor:,.2f}")

# 3. AGREGAR Y MODIFICAR
print("\n3️⃣ AGREGAR Y MODIFICAR")
print("-" * 70)

print(f"\nCartera inicial: {list(cartera.keys())}")

# Agregar nueva acción
cartera["COME"] = 75
precios["COME"] = 2.50
print(f"Después de agregar COME: {list(cartera.keys())}")

# Modificar cantidad existente
print(f"\nYPF antes: {cartera['YPF']} acciones")
cartera["YPF"] = 60  # Compré 10 más
print(f"YPF después: {cartera['YPF']} acciones")

# 4. ELIMINAR
print("\n4️⃣ ELIMINAR ELEMENTOS")
print("-" * 70)

print(f"\nCartera antes de vender: {list(cartera.keys())}")
del cartera["COME"]
print(f"Cartera después de vender COME: {list(cartera.keys())}")

# 5. VERIFICAR EXISTENCIA
print("\n5️⃣ VERIFICAR SI UNA CLAVE EXISTE")
print("-" * 70)

tickers_buscar = ["YPF", "TRAN", "MELI"]
for ticker in tickers_buscar:
    if ticker in cartera:
        print(f"  ✅ {ticker}: {cartera[ticker]} acciones")
    else:
        print(f"  ❌ {ticker}: No está en la cartera")

# 6. APLICACIÓN: Calcular valor total del portafolio
print("\n6️⃣ APLICACIÓN: VALOR TOTAL DEL PORTAFOLIO")
print("-" * 70)

print("\nResumen del portafolio:")
print(f"\n{'Ticker':<8} {'Cantidad':>10} {'Precio':>12} {'Valor':>15}")
print("-" * 70)

total_portafolio = 0
for ticker, cantidad in cartera.items():
    precio = precios[ticker]
    valor = cantidad * precio
    total_portafolio += valor
    print(f"{ticker:<8} {cantidad:>10} ${precio:>11,.2f} ${valor:>14,.2f}")

print("-" * 70)
print(f"{'TOTAL':>31} ${total_portafolio:>14,.2f}")

# 7. MÉTODO GET - Evitar errores
print("\n7️⃣ MÉTODO GET: EVITAR ERRORES")
print("-" * 70)

# Forma peligrosa (puede dar error)
print("\n⚠️ Forma peligrosa:")
try:
    cantidad_tran = cartera["TRAN"]  # Error si no existe
except KeyError:
    print("  ❌ KeyError: 'TRAN' no existe en el diccionario")

# Forma segura con get()
print("\n✅ Forma segura con get():")
cantidad_tran = cartera.get("TRAN", 0)  # Devuelve 0 si no existe
print(f"  Cantidad de TRAN: {cantidad_tran}")

cantidad_ypf = cartera.get("YPF", 0)
print(f"  Cantidad de YPF: {cantidad_ypf}")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - Tuplas
# MAGIC %md
# MAGIC ## 📎 TUPLAS: Inmutables y Seguras
# MAGIC
# MAGIC ### ¿Qué es una Tupla?
# MAGIC
# MAGIC Una **tupla** es similar a una lista, pero **inmutable**: una vez creada, **no se puede modificar**.
# MAGIC
# MAGIC ### Sintaxis
# MAGIC
# MAGIC ```python
# MAGIC info = ("YPF", "BYMA", 5250)
# MAGIC ```
# MAGIC
# MAGIC 👉 Se crean con **paréntesis** `()`
# MAGIC 👉 Los elementos se separan por **comas**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Diferencias con Listas
# MAGIC
# MAGIC | Característica | Lista | Tupla |
# MAGIC |---------------|-------|-------|
# MAGIC | Símbolo | `[]` | `()` |
# MAGIC | Mutable | ✅ Sí | ❌ No |
# MAGIC | Velocidad | Más lenta | Más rápida |
# MAGIC | Uso de memoria | Más | Menos |
# MAGIC | Métodos | Muchos | Pocos |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ¿Cuándo Usar Tuplas?
# MAGIC
# MAGIC ✅ **Datos que NO deben cambiar**:
# MAGIC * Fecha de una transacción
# MAGIC * Ticker y exchange de una acción
# MAGIC * Coordenadas, constantes
# MAGIC
# MAGIC ✅ **Como claves de diccionarios** (las listas no pueden)
# MAGIC
# MAGIC ✅ **Retornar múltiples valores** de una función
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Operaciones
# MAGIC
# MAGIC #### Acceder (igual que listas)
# MAGIC ```python
# MAGIC info = ("YPF", "BYMA", 5250)
# MAGIC info[0]  # "YPF"
# MAGIC info[-1]  # 5250
# MAGIC ```
# MAGIC
# MAGIC #### Desempaquetado
# MAGIC ```python
# MAGIC ticker, exchange, precio = ("YPF", "BYMA", 5250)
# MAGIC # ticker = "YPF"
# MAGIC # exchange = "BYMA"
# MAGIC # precio = 5250
# MAGIC ```
# MAGIC
# MAGIC #### ⚠️ NO se puede modificar
# MAGIC ```python
# MAGIC info[0] = "GGAL"  # ❌ TypeError: 'tuple' object does not support item assignment
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Código - Tuplas
print("═" * 70)
print("EJEMPLO: Tuplas - Datos Inmutables")
print("═" * 70)

# 1. CREAR TUPLAS
print("\n1️⃣ CREAR TUPLAS")
print("-" * 70)

# Información fija de una acción
info_ypf = ("YPF", "BYMA", "AR", "Energía")
print(f"Información de YPF: {info_ypf}")

# Fecha de transacción
transaccion = (2024, 6, 12, "Compra", "YPF", 50, 5250.75)
print(f"Transacción: {transaccion}")

# Coordenadas de precio (día, precio)
precios_historicos = [
    (1, 5250),
    (2, 5280),
    (3, 5195),
    (4, 5310)
]
print(f"\nPrecios históricos (tuplas en lista):")
for dia, precio in precios_historicos:
    print(f"  Día {dia}: ${precio:,}")

# 2. ACCEDER A ELEMENTOS
print("\n2️⃣ ACCEDER A ELEMENTOS")
print("-" * 70)

print(f"\ninfo_ypf = {info_ypf}")
print(f"Ticker (info_ypf[0]): {info_ypf[0]}")
print(f"Exchange (info_ypf[1]): {info_ypf[1]}")
print(f"Último elemento (info_ypf[-1]): {info_ypf[-1]}")

# 3. DESEMPAQUETADO
print("\n3️⃣ DESEMPAQUETADO DE TUPLAS")
print("-" * 70)

ticker, exchange, pais, sector = info_ypf
print(f"\nDesempaquetado:")
print(f"  ticker = '{ticker}'")
print(f"  exchange = '{exchange}'")
print(f"  pais = '{pais}'")
print(f"  sector = '{sector}'")

# Desempaquetar transacción
anio, mes, dia, tipo, ticker_trans, cantidad, precio = transaccion
print(f"\nTransacción:")
print(f"  Fecha: {dia}/{mes}/{anio}")
print(f"  Tipo: {tipo}")
print(f"  Ticker: {ticker_trans}")
print(f"  Cantidad: {cantidad}")
print(f"  Precio: ${precio:,.2f}")

# 4. INMUTABILIDAD
print("\n4️⃣ INMUTABILIDAD: NO SE PUEDE MODIFICAR")
print("-" * 70)

print(f"\nTupla original: {info_ypf}")
print(f"\n⚠️ Intentando modificar info_ypf[0] = 'GGAL'...")

try:
    info_ypf[0] = "GGAL"
except TypeError as e:
    print(f"  ❌ Error: {e}")
    print(f"  ℹ️ Las tuplas NO se pueden modificar")

print(f"\nTupla sin cambios: {info_ypf}")

# 5. VENTAJAS DE TUPLAS
print("\n5️⃣ VENTAJAS: SEGURIDAD Y VELOCIDAD")
print("-" * 70)

import sys
import time

# Comparación de memoria
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)

print(f"\nUso de memoria:")
print(f"  Lista: {sys.getsizeof(lista)} bytes")
print(f"  Tupla: {sys.getsizeof(tupla)} bytes")
print(f"  🚀 Tupla usa {sys.getsizeof(lista) - sys.getsizeof(tupla)} bytes menos")

# 6. USO PRÁCTICO: Retornar múltiples valores
print("\n6️⃣ RETORNAR MÚTIPLES VALORES DE UNA FUNCIÓN")
print("-" * 70)

def analizar_accion(ticker, precio_compra, precio_actual):
    """Retorna (ganancia, rendimiento_pct, recomendacion)"""
    ganancia = precio_actual - precio_compra
    rendimiento_pct = (ganancia / precio_compra) * 100
    
    if rendimiento_pct > 15:
        recomendacion = "Vender (tomar ganancias)"
    elif rendimiento_pct > 0:
        recomendacion = "Mantener"
    else:
        recomendacion = "Analizar venta"
    
    return (ganancia, rendimiento_pct, recomendacion)  # Tupla

# Usar la función
ganancia, rendimiento, recomendacion = analizar_accion("YPF", 5000, 5250)

print(f"\nAnálisis de YPF:")
print(f"  Ganancia: ${ganancia:,.2f}")
print(f"  Rendimiento: {rendimiento:.2f}%")
print(f"  Recomendación: {recomendacion}")

# 7. TUPLAS COMO CLAVES DE DICCIONARIO
print("\n7️⃣ TUPLAS COMO CLAVES DE DICCIONARIO")
print("-" * 70)

# Precios históricos por (ticker, fecha)
precios_dict = {
    ("YPF", "2024-06-10"): 5250,
    ("YPF", "2024-06-11"): 5280,
    ("GGAL", "2024-06-10"): 175,
    ("GGAL", "2024-06-11"): 180
}

print("\nPrecios históricos:")
for (ticker, fecha), precio in precios_dict.items():
    print(f"  {ticker} el {fecha}: ${precio:,}")

# Buscar precio específico
print(f"\nPrecio de YPF el 2024-06-11: ${precios_dict[('YPF', '2024-06-11')]:,}")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - Sets
# MAGIC %md
# MAGIC ## 🎯 SETS (Conjuntos): Sin Duplicados
# MAGIC
# MAGIC ### ¿Qué es un Set?
# MAGIC
# MAGIC Un **set** es una colección **no ordenada** de elementos **únicos** (sin duplicados).
# MAGIC
# MAGIC ### Sintaxis
# MAGIC
# MAGIC ```python
# MAGIC tickers = {"YPF", "GGAL", "YPF", "MELI"}
# MAGIC print(tickers)  # {"YPF", "GGAL", "MELI"}
# MAGIC ```
# MAGIC
# MAGIC 👉 Se crean con **llaves** `{}` (igual que diccionarios, pero sin `:`)
# MAGIC 👉 **Elimina duplicados automáticamente**
# MAGIC 👉 **No está ordenado** (no tiene índices)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ¿Cuándo Usar Sets?
# MAGIC
# MAGIC ✅ **Eliminar duplicados** de una lista
# MAGIC ✅ **Verificar pertenencia** rápidamente (más rápido que listas)
# MAGIC ✅ **Operaciones de conjuntos**: unión, intersección, diferencia
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Operaciones de Conjuntos
# MAGIC
# MAGIC #### 1. **Unión** (|) - Todos los elementos
# MAGIC ```python
# MAGIC A = {"YPF", "GGAL"}
# MAGIC B = {"GGAL", "MELI"}
# MAGIC A | B  # {"YPF", "GGAL", "MELI"}
# MAGIC ```
# MAGIC
# MAGIC #### 2. **Intersección** (&) - Elementos comunes
# MAGIC ```python
# MAGIC A & B  # {"GGAL"}
# MAGIC ```
# MAGIC
# MAGIC #### 3. **Diferencia** (-) - En A pero no en B
# MAGIC ```python
# MAGIC A - B  # {"YPF"}
# MAGIC ```
# MAGIC
# MAGIC #### 4. **Diferencia simétrica** (^) - En A o B, pero no en ambos
# MAGIC ```python
# MAGIC A ^ B  # {"YPF", "MELI"}
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Métodos Útiles
# MAGIC
# MAGIC * `add(elemento)` - Agregar
# MAGIC * `remove(elemento)` - Eliminar (error si no existe)
# MAGIC * `discard(elemento)` - Eliminar (sin error)
# MAGIC * `clear()` - Vaciar
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Uso en Finanzas
# MAGIC
# MAGIC 💼 **Comparar portafolios**: ¿Qué acciones tenemos en común?
# MAGIC 💼 **Encontrar tickers únicos**: De múltiples fuentes
# MAGIC 💼 **Filtrar sectores**: ¿Qué sectores tengo?

# COMMAND ----------

# DBTITLE 1,Código - Sets
print("═" * 70)
print("EJEMPLO: Sets - Conjuntos sin Duplicados")
print("═" * 70)

# 1. CREAR SETS Y ELIMINAR DUPLICADOS
print("\n1️⃣ CREAR SETS: ELIMINAR DUPLICADOS AUTOMÁTICAMENTE")
print("-" * 70)

# Lista con duplicados
operaciones = ["YPF", "GGAL", "YPF", "MELI", "YPF", "GGAL", "COME"]
print(f"Operaciones (con duplicados): {operaciones}")
print(f"Cantidad: {len(operaciones)}")

# Convertir a set para eliminar duplicados
tickers_unicos = set(operaciones)
print(f"\nTickers únicos (set): {tickets_unicos}")
print(f"Cantidad de tickers únicos: {len(tickers_unicos)}")

# 2. OPERACIONES DE CONJUNTOS
print("\n2️⃣ OPERACIONES DE CONJUNTOS")
print("-" * 70)

portafolio_a = {"YPF", "GGAL", "MELI", "COME"}
portafolio_b = {"GGAL", "MELI", "TRAN", "LOMA"}

print(f"Portafolio A: {portafolio_a}")
print(f"Portafolio B: {portafolio_b}")

# Unión: Todos los tickers
union = portafolio_a | portafolio_b
print(f"\nUnión (A | B): {union}")
print(f"  ℹ️ Todos los tickers en ambos portafolios")

# Intersección: Tickers comunes
interseccion = portafolio_a & portafolio_b
print(f"\nIntersección (A & B): {interseccion}")
print(f"  ℹ️ Tickers que están en AMBOS portafolios")

# Diferencia: En A pero no en B
diferencia_a = portafolio_a - portafolio_b
print(f"\nDiferencia (A - B): {diferencia_a}")
print(f"  ℹ️ Tickers solo en Portafolio A")

diferencia_b = portafolio_b - portafolio_a
print(f"\nDiferencia (B - A): {diferencia_b}")
print(f"  ℹ️ Tickers solo en Portafolio B")

# Diferencia simétrica: En A o B, pero no en ambos
dif_simetrica = portafolio_a ^ portafolio_b
print(f"\nDiferencia simétrica (A ^ B): {dif_simetrica}")
print(f"  ℹ️ Tickers en UNO u OTRO, pero no en ambos")

# 3. MÉTODOS
print("\n3️⃣ MÉTODOS: ADD, REMOVE, DISCARD")
print("-" * 70)

cartera = {"YPF", "GGAL", "MELI"}
print(f"Cartera inicial: {cartera}")

# Agregar
cartera.add("COME")
print(f"Después de add('COME'): {cartera}")

# Intentar agregar duplicado (no hace nada)
cartera.add("YPF")
print(f"Después de add('YPF') - duplicado: {cartera}")

# Remove (error si no existe)
cartera.remove("COME")
print(f"Después de remove('COME'): {cartera}")

# Discard (sin error si no existe)
cartera.discard("TRAN")  # No existe, pero no da error
print(f"Después de discard('TRAN') - no existía: {cartera}")

# 4. VERIFICAR PERTENENCIA (MUY RÁPIDO)
print("\n4️⃣ VERIFICAR PERTENENCIA: MUY RÁPIDO")
print("-" * 70)

tickers_grandes = set([f"TICK{i}" for i in range(10000)])
tickers_grandes.add("YPF")

print(f"\nSet con {len(tickers_grandes):,} elementos")
print(f"¿YPF está en el set? {'YPF' in tickers_grandes}")
print(f"¿GGAL está en el set? {'GGAL' in tickers_grandes}")
print(f"\nℹ️ La búsqueda en sets es O(1) - instantánea")

# 5. APLICACIÓN: Comparar múltiples portafolios
print("\n5️⃣ APLICACIÓN: COMPARAR MÚTIPLES PORTAFOLIOS")
print("-" * 70)

portafolio_juan = {"YPF", "GGAL", "MELI", "COME"}
portafolio_maria = {"GGAL", "MELI", "TRAN"}
portafolio_pedro = {"YPF", "MELI", "LOMA"}

print(f"Portafolio Juan: {portafolio_juan}")
print(f"Portafolio María: {portafolio_maria}")
print(f"Portafolio Pedro: {portafolio_pedro}")

# Acciones que tienen TODOS
todos = portafolio_juan & portafolio_maria & portafolio_pedro
print(f"\n👥 Acciones que tienen TODOS: {todos}")

# Todas las acciones entre los 3
todas = portafolio_juan | portafolio_maria | portafolio_pedro
print(f"\n📈 Todas las acciones entre los 3: {todas}")
print(f"   Total de acciones únicas: {len(todas)}")

# Acciones solo de Juan
solo_juan = portafolio_juan - portafolio_maria - portafolio_pedro
print(f"\n👤 Acciones solo de Juan: {solo_juan}")

# 6. CONVERTIR ENTRE LIST Y SET
print("\n6️⃣ CONVERTIR ENTRE LIST Y SET")
print("-" * 70)

# Lista con duplicados
operaciones_list = ["YPF", "YPF", "GGAL", "MELI", "YPF", "GGAL"]
print(f"Lista con duplicados ({len(operaciones_list)} elementos):")
print(f"  {operaciones_list}")

# Convertir a set (elimina duplicados)
tickers_set = set(operaciones_list)
print(f"\nConvertir a set ({len(tickers_set)} elementos):")
print(f"  {tickers_set}")

# Convertir de vuelta a lista
tickers_list_unicos = list(tickers_set)
print(f"\nConvertir de vuelta a lista:")
print(f"  {tickers_list_unicos}")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Comparación de Estructuras
# MAGIC %md
# MAGIC ## 📊 COMPARACIÓN DE ESTRUCTURAS DE DATOS
# MAGIC
# MAGIC ### Tabla Comparativa
# MAGIC
# MAGIC | Característica | Lista | Tupla | Diccionario | Set |
# MAGIC |---------------|-------|-------|-------------|-----|
# MAGIC | **Símbolo** | `[]` | `()` | `{k:v}` | `{v}` |
# MAGIC | **Ordenado** | ✅ Sí | ✅ Sí | ❌ No* | ❌ No |
# MAGIC | **Mutable** | ✅ Sí | ❌ No | ✅ Sí | ✅ Sí |
# MAGIC | **Duplicados** | ✅ Permite | ✅ Permite | Claves únicas | ❌ No |
# MAGIC | **Indexado** | ✅ Por número | ✅ Por número | ✅ Por clave | ❌ No |
# MAGIC | **Velocidad acceso** | O(n) | O(n) | O(1) | O(1) |
# MAGIC | **Uso memoria** | Media | Baja | Alta | Media |
# MAGIC
# MAGIC *Desde Python 3.7, diccionarios mantienen orden de inserción
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ¿Cuándo Usar Cada Una?
# MAGIC
# MAGIC #### 📋 **LISTAS**: Colección ordenada que puede cambiar
# MAGIC **Usar cuando**:
# MAGIC * Necesitas **orden** (precios históricos, series temporales)
# MAGIC * Necesitas **modificar** (agregar/quitar elementos)
# MAGIC * Puedes tener **duplicados**
# MAGIC * Accedes por **posición** (primero, último, etc.)
# MAGIC
# MAGIC **Ejemplos financieros**:
# MAGIC * `precios = [5250, 5280, 5195, ...]`
# MAGIC * `rendimientos_diarios = [0.02, -0.01, 0.03, ...]`
# MAGIC * `fechas = ["2024-01-01", "2024-01-02", ...]`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 📎 **TUPLAS**: Datos fijos que no deben cambiar
# MAGIC **Usar cuando**:
# MAGIC * Los datos **NO deben modificarse** (fechas, constantes)
# MAGIC * Necesitas **velocidad y eficiencia**
# MAGIC * Quieres **prevenir cambios accidentales**
# MAGIC * Retornas **múltiples valores** de una función
# MAGIC
# MAGIC **Ejemplos financieros**:
# MAGIC * `transaccion = ("2024-06-12", "Compra", "YPF", 50)`
# MAGIC * `info_accion = ("YPF", "BYMA", "AR")`
# MAGIC * Retornar: `return (ganancia, rendimiento, riesgo)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 📚 **DICCIONARIOS**: Datos con clave-valor
# MAGIC **Usar cuando**:
# MAGIC * Necesitas **buscar por nombre/clave** en lugar de posición
# MAGIC * Tienes **datos relacionados** (ticker → precio)
# MAGIC * Necesitas **acceso rápido** O(1)
# MAGIC * Organizas **datos estructurados**
# MAGIC
# MAGIC **Ejemplos financieros**:
# MAGIC * `cartera = {"YPF": 50, "GGAL": 100}`
# MAGIC * `precios = {"YPF": 5250, "GGAL": 175}`
# MAGIC * `empresa = {"ticker": "YPF", "precio": 5250, "sector": "Energía"}`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 🎯 **SETS**: Elementos únicos sin orden
# MAGIC **Usar cuando**:
# MAGIC * Necesitas **eliminar duplicados**
# MAGIC * Haces **operaciones de conjuntos** (unión, intersección)
# MAGIC * Verificas **pertenencia rápida** ("in")
# MAGIC * El **orden no importa**
# MAGIC
# MAGIC **Ejemplos financieros**:
# MAGIC * `tickers_unicos = {"YPF", "GGAL", "MELI"}`
# MAGIC * `sectores = {"Energía", "Financiero", "Tecnología"}`
# MAGIC * Comparar portafolios: `comunes = cartera_a & cartera_b`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Combinación de Estructuras
# MAGIC
# MAGIC En finanzas, **frecuentemente combinamos estructuras**:
# MAGIC
# MAGIC ```python
# MAGIC # Lista de diccionarios
# MAGIC acciones = [
# MAGIC     {"ticker": "YPF", "precio": 5250, "sector": "Energía"},
# MAGIC     {"ticker": "GGAL", "precio": 175, "sector": "Financiero"}
# MAGIC ]
# MAGIC
# MAGIC # Diccionario con listas
# MAGIC portafolio = {
# MAGIC     "tickers": ["YPF", "GGAL", "MELI"],
# MAGIC     "cantidades": [50, 100, 25],
# MAGIC     "precios": [5250, 175, 1450]
# MAGIC }
# MAGIC
# MAGIC # Diccionario con sets
# MAGIC portafolios = {
# MAGIC     "Juan": {"YPF", "GGAL"},
# MAGIC     "María": {"GGAL", "MELI"}
# MAGIC }
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Caso Integrado: Gestión Completa de Portafolio
# MAGIC %md
# MAGIC ## 💼 CASO INTEGRADO: Gestión Completa de Portafolio
# MAGIC
# MAGIC Vamos a crear un sistema completo de gestión de portafolio usando **TODAS** las estructuras de datos aprendidas.
# MAGIC
# MAGIC ### Componentes
# MAGIC
# MAGIC 1. **Lista** - Historial de transacciones
# MAGIC 2. **Tuplas** - Información fija de cada transacción
# MAGIC 3. **Diccionario** - Datos completos de cada acción
# MAGIC 4. **Diccionario anidado** - Portafolio con múltiples métricas
# MAGIC 5. **Sets** - Análisis y comparaciones

# COMMAND ----------

# DBTITLE 1,Código - Caso Integrado
print("═" * 80)
print("CASO INTEGRADO: Sistema Completo de Gestión de Portafolio")
print("═" * 80)

# 1. DICCIONARIO ANIDADO: Portafolio completo
portafolio = {
    "YPF": {
        "cantidad": 50,
        "precio_compra": 5000,
        "precio_actual": 5250,
        "sector": "Energía",
        "exchange": "BYMA"
    },
    "GGAL": {
        "cantidad": 100,
        "precio_compra": 150,
        "precio_actual": 175,
        "sector": "Financiero",
        "exchange": "BYMA"
    },
    "MELI": {
        "cantidad": 25,
        "precio_compra": 1500,
        "precio_actual": 1450,
        "sector": "Tecnología",
        "exchange": "NASDAQ"
    },
    "COME": {
        "cantidad": 200,
        "precio_compra": 2.0,
        "precio_actual": 2.5,
        "sector": "Servicios",
        "exchange": "BYMA"
    }
}

# 2. LISTA DE TUPLAS: Historial de transacciones
transacciones = [
    ("2024-01-15", "Compra", "YPF", 30, 4800),
    ("2024-02-10", "Compra", "YPF", 20, 5100),
    ("2024-03-05", "Compra", "GGAL", 100, 150),
    ("2024-04-20", "Compra", "MELI", 25, 1500),
    ("2024-05-12", "Compra", "COME", 200, 2.0)
]

print("\n" + "="*80)
print("1️⃣ PORTAFOLIO ACTUAL")
print("="*80)

print(f"\n{'Ticker':<8} {'Cant':>6} {'P.Compra':>12} {'P.Actual':>12} {'Sector':<15} {'Exchange':<10}")
print("-" * 80)

for ticker, datos in portafolio.items():
    print(f"{ticker:<8} {datos['cantidad']:>6} ${datos['precio_compra']:>11,.2f} ${datos['precio_actual']:>11,.2f} {datos['sector']:<15} {datos['exchange']:<10}")

print("\n" + "="*80)
print("2️⃣ HISTORIAL DE TRANSACCIONES")
print("="*80)

print(f"\n{'Fecha':<12} {'Tipo':<8} {'Ticker':<8} {'Cant':>6} {'Precio':>12}")
print("-" * 80)

for fecha, tipo, ticker, cantidad, precio in transacciones:
    print(f"{fecha:<12} {tipo:<8} {ticker:<8} {cantidad:>6} ${precio:>11,.2f}")

print("\n" + "="*80)
print("3️⃣ ANÁLISIS DE RENDIMIENTOS")
print("="*80)

total_invertido = 0
total_actual = 0

print(f"\n{'Ticker':<8} {'Inversión':>15} {'Valor Actual':>15} {'Ganancia':>15} {'Rend.':>10}")
print("-" * 80)

for ticker, datos in portafolio.items():
    inversion = datos['cantidad'] * datos['precio_compra']
    valor_actual = datos['cantidad'] * datos['precio_actual']
    ganancia = valor_actual - inversion
    rendimiento = (ganancia / inversion) * 100
    
    total_invertido += inversion
    total_actual += valor_actual
    
    simbolo = "✅" if rendimiento > 0 else "❌"
    print(f"{ticker:<8} ${inversion:>14,.2f} ${valor_actual:>14,.2f} ${ganancia:>14,.2f} {simbolo} {rendimiento:>6.2f}%")

ganancia_total = total_actual - total_invertido
rendimiento_total = (ganancia_total / total_invertido) * 100

print("-" * 80)
print(f"{'TOTAL':<8} ${total_invertido:>14,.2f} ${total_actual:>14,.2f} ${ganancia_total:>14,.2f} {'  '} {rendimiento_total:>6.2f}%")

print("\n" + "="*80)
print("4️⃣ ANÁLISIS POR SECTOR (usando SETS)")
print("="*80)

# Obtener sectores únicos
sectores = {datos['sector'] for datos in portafolio.values()}
print(f"\nSectores en portafolio: {sectores}")

# Analizar por sector
print(f"\n{'Sector':<15} {'Inversión':>15} {'% del Total':>12}")
print("-" * 80)

for sector in sorted(sectores):
    inversion_sector = sum(
        datos['cantidad'] * datos['precio_compra']
        for datos in portafolio.values()
        if datos['sector'] == sector
    )
    porcentaje = (inversion_sector / total_invertido) * 100
    print(f"{sector:<15} ${inversion_sector:>14,.2f} {porcentaje:>11.1f}%")

print("\n" + "="*80)
print("5️⃣ COMPARACIÓN DE EXCHANGES")
print("="*80)

# Tickers por exchange (usando sets)
byma = {ticker for ticker, datos in portafolio.items() if datos['exchange'] == 'BYMA'}
nasdaq = {ticker for ticker, datos in portafolio.items() if datos['exchange'] == 'NASDAQ'}

print(f"\nAcciones en BYMA: {byma}")
print(f"Acciones en NASDAQ: {nasdaq}")
print(f"\nTotal BYMA: {len(byma)} acciones")
print(f"Total NASDAQ: {len(nasdaq)} acciones")

print("\n" + "="*80)
print("6️⃣ OPERACIONES: COMPRAR/VENDER")
print("="*80)

def comprar_accion(portafolio, ticker, cantidad, precio):
    """Agregar o aumentar posición"""
    if ticker in portafolio:
        # Ya existe, actualizar cantidad y precio promedio
        datos = portafolio[ticker]
        nueva_cantidad = datos['cantidad'] + cantidad
        precio_promedio = ((datos['cantidad'] * datos['precio_compra']) + (cantidad * precio)) / nueva_cantidad
        datos['cantidad'] = nueva_cantidad
        datos['precio_compra'] = precio_promedio
        return f"Compra agregada: {cantidad} {ticker} a ${precio:,.2f}. Nueva cantidad: {nueva_cantidad}"
    else:
        return f"Ticker {ticker} no encontrado en portafolio"

def vender_accion(portafolio, ticker, cantidad):
    """Vender o reducir posición"""
    if ticker in portafolio:
        if portafolio[ticker]['cantidad'] >= cantidad:
            portafolio[ticker]['cantidad'] -= cantidad
            if portafolio[ticker]['cantidad'] == 0:
                del portafolio[ticker]
                return f"Posición en {ticker} cerrada completamente"
            return f"Vendidas {cantidad} acciones de {ticker}. Restantes: {portafolio[ticker]['cantidad']}"
        else:
            return f"Error: Solo tienes {portafolio[ticker]['cantidad']} acciones de {ticker}"
    else:
        return f"Error: {ticker} no está en el portafolio"

# Simular operaciones
print("\nComprar 10 YPF más a $5300:")
print(comprar_accion(portafolio, "YPF", 10, 5300))

print("\nVender 50 COME:")
print(vender_accion(portafolio, "COME", 50))

print("\n" + "="*80)
print("✅ Sistema de gestión de portafolio completado")
print("="*80)

# COMMAND ----------

# DBTITLE 1,Ejercicios Prácticos
# MAGIC %md
# MAGIC ## ✍️ EJERCICIOS PRÁCTICOS
# MAGIC
# MAGIC ### 📋 LISTAS
# MAGIC
# MAGIC **Ejercicio 1**: Crea una lista de precios históricos de 10 días y muestra el primero, último y promedio.
# MAGIC
# MAGIC **Ejercicio 2**: Dada `precios = [5250, 5280, 5195, 5310, 5420]`, agrega un nuevo precio al final y ordena la lista descendente.
# MAGIC
# MAGIC **Ejercicio 3**: Extrae los primeros 5 elementos y los últimos 3 de una lista de 20 precios.
# MAGIC
# MAGIC **Ejercicio 4**: Crea una función que reciba una lista de rendimientos y retorne solo los positivos.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📎 TUPLAS
# MAGIC
# MAGIC **Ejercicio 5**: Crea una tupla con información de una transacción: (fecha, tipo, ticker, cantidad, precio). Desempaqueta los valores.
# MAGIC
# MAGIC **Ejercicio 6**: Crea una lista de tuplas con 5 acciones y sus precios. Ordena por precio.
# MAGIC
# MAGIC **Ejercicio 7**: ¿Por qué usar tuplas en lugar de listas para fechas de transacciones? Explica.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📚 DICCIONARIOS
# MAGIC
# MAGIC **Ejercicio 8**: Crea un diccionario `cartera` con 4 tickers y sus cantidades. Muestra todas las claves, valores y pares.
# MAGIC
# MAGIC **Ejercicio 9**: Agrega un nuevo ticker al diccionario, modifica la cantidad de uno existente y elimina otro.
# MAGIC
# MAGIC **Ejercicio 10**: Crea un diccionario anidado con información completa de 3 empresas (ticker, precio, cantidad, sector).
# MAGIC
# MAGIC **Ejercicio 11**: Itera sobre el diccionario del ejercicio anterior y calcula el valor de cada posición.
# MAGIC
# MAGIC **Ejercicio 12**: Usa `.get()` para buscar un ticker que no existe sin que de error.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 SETS
# MAGIC
# MAGIC **Ejercicio 13**: Dada una lista con tickers duplicados, crea un set para obtener solo los únicos.
# MAGIC
# MAGIC **Ejercicio 14**: Crea dos sets de portafolios diferentes. Encuentra los tickers comunes, los que solo están en el primero, y la unión de ambos.
# MAGIC
# MAGIC **Ejercicio 15**: ¿Qué ventaja tiene usar `ticker in mi_set` vs `ticker in mi_lista` para verificar existencia?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📊 INTEGRACIÓN
# MAGIC
# MAGIC **Ejercicio 16**: Crea una lista de diccionarios, donde cada diccionario representa una acción con ticker, precio y rendimiento. Filtra solo las rentables.
# MAGIC
# MAGIC **Ejercicio 17**: Dado un diccionario de precios y una lista de tickers, calcula el valor total si compras 1 de cada uno.
# MAGIC
# MAGIC **Ejercicio 18**: Crea un diccionario con listas como valores: `{"precios": [...], "volumenes": [...]}`. Calcula promedios.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 DESAFÍO FINAL
# MAGIC
# MAGIC **Ejercicio 19**: Sistema completo de portafolio
# MAGIC
# MAGIC Crea un sistema que:
# MAGIC 1. Use un diccionario anidado para el portafolio
# MAGIC 2. Una lista de tuplas para historial de transacciones
# MAGIC 3. Funciones para:
# MAGIC    * Agregar nueva compra
# MAGIC    * Vender acciones
# MAGIC    * Calcular valor total
# MAGIC    * Mostrar rendimiento por acción
# MAGIC    * Listar sectores únicos (set)
# MAGIC    * Top 3 mejores rendimientos (sorted + list comprehension)
# MAGIC
# MAGIC Datos iniciales:
# MAGIC * YPF: 50 acciones a $5000, precio actual $5250
# MAGIC * GGAL: 100 acciones a $150, precio actual $175  
# MAGIC * MELI: 25 acciones a $1500, precio actual $1450
# MAGIC * COME: 200 acciones a $2.00, precio actual $2.50

# COMMAND ----------

# DBTITLE 1,Consultas con Genie Code
# MAGIC %md
# MAGIC ## 🤖 CONSULTAS CON GENIE CODE
# MAGIC
# MAGIC ### 📋 LISTAS (20 preguntas)
# MAGIC
# MAGIC 1. ¿Qué diferencia hay entre `lista[2]` y `lista[2:3]`?
# MAGIC 2. ¿Cómo accedo al último elemento sin saber la longitud?
# MAGIC 3. ¿Qué hace `lista[::-1]`?
# MAGIC 4. ¿Cuál es la diferencia entre `append()` y `extend()`?
# MAGIC 5. ¿Qué diferencia hay entre `sort()` y `sorted()`?
# MAGIC 6. ¿Cómo elimino el tercer elemento de una lista?
# MAGIC 7. ¿Puedo tener una lista con diferentes tipos de datos?
# MAGIC 8. ¿Cómo encuentro el índice de un elemento específico?
# MAGIC 9. ¿Qué pasa si hago `lista.remove()` de un elemento que no existe?
# MAGIC 10. ¿Cómo copio una lista sin que los cambios afecten a la original?
# MAGIC 11. ¿Qué es una list comprehension y cuándo usarla?
# MAGIC 12. ¿Cómo invierto una lista sin modificar la original?
# MAGIC 13. ¿Puedo usar listas como claves de un diccionario?
# MAGIC 14. ¿Qué diferencia hay entre `lista.pop()` y `del lista[0]`?
# MAGIC 15. ¿Cómo creo una lista de 100 ceros?
# MAGIC 16. ¿Cómo uno dos listas en una sola?
# MAGIC 17. Dame 5 ejemplos de listas en finanzas
# MAGIC 18. ¿Cómo filtro una lista para quedarme solo con elementos que cumplan una condición?
# MAGIC 19. ¿Qué es el slicing negativo?
# MAGIC 20. ¿Cómo creo una lista de listas (matriz)?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📎 TUPLAS (10 preguntas)
# MAGIC
# MAGIC 21. ¿Qué significa que una tupla es "inmutable"?
# MAGIC 22. ¿Puedo modificar un elemento de una tupla después de crearla?
# MAGIC 23. ¿Cuándo debo usar tuplas en lugar de listas?
# MAGIC 24. ¿Qué ventajas tienen las tuplas sobre las listas?
# MAGIC 25. ¿Qué es el "desempaquetado" de tuplas?
# MAGIC 26. ¿Cómo creo una tupla de un solo elemento?
# MAGIC 27. ¿Puedo usar tuplas como claves de diccionario?
# MAGIC 28. ¿Qué métodos tienen las tuplas?
# MAGIC 29. Dame 5 ejemplos de cuándo usar tuplas en finanzas
# MAGIC 30. ¿Cómo convierto una lista en tupla y viceversa?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📚 DICCIONARIOS (25 preguntas)
# MAGIC
# MAGIC 31. ¿Qué es un diccionario en Python?
# MAGIC 32. ¿Cuál es la diferencia entre listas y diccionarios?
# MAGIC 33. ¿Cómo accedo a un valor si no sé si la clave existe?
# MAGIC 34. ¿Qué diferencia hay entre `.get()` y acceder con `[]`?
# MAGIC 35. ¿Cómo agrego un nuevo par clave-valor?
# MAGIC 36. ¿Cómo elimino una clave de un diccionario?
# MAGIC 37. ¿Qué hacen `.keys()`, `.values()` e `.items()`?
# MAGIC 38. ¿Cómo itero sobre un diccionario?
# MAGIC 39. ¿Puedo usar listas como claves de diccionario?
# MAGIC 40. ¿Qué tipos de datos puedo usar como claves?
# MAGIC 41. ¿Cómo ordeno un diccionario por valores?
# MAGIC 42. ¿Qué es un diccionario anidado?
# MAGIC 43. ¿Cómo accedo a valores en un diccionario anidado?
# MAGIC 44. ¿Qué diferencia hay entre `dict.update()` y `dict[key] = value`?
# MAGIC 45. ¿Cómo verifico si una clave existe en un diccionario?
# MAGIC 46. ¿Puedo tener valores duplicados en un diccionario?
# MAGIC 47. ¿Desde qué versión de Python los diccionarios mantienen el orden?
# MAGIC 48. Dame 10 ejemplos de diccionarios en finanzas
# MAGIC 49. ¿Cómo creo un diccionario con valores por defecto?
# MAGIC 50. ¿Qué es dictionary comprehension?
# MAGIC 51. ¿Cómo fusiono dos diccionarios?
# MAGIC 52. ¿Qué pasa si intento acceder a una clave que no existe?
# MAGIC 53. ¿Cómo copio un diccionario?
# MAGIC 54. ¿Cuál es más rápido: buscar en lista o diccionario?
# MAGIC 55. ¿Cómo obtengo el máximo/mínimo de un diccionario por valores?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 SETS (10 preguntas)
# MAGIC
# MAGIC 56. ¿Qué es un set en Python?
# MAGIC 57. ¿Qué diferencia hay entre sets y listas?
# MAGIC 58. ¿Cómo elimino duplicados de una lista?
# MAGIC 59. ¿Qué operaciones de conjuntos puedo hacer?
# MAGIC 60. ¿Qué diferencia hay entre `.add()` y `.update()`?
# MAGIC 61. ¿Cómo verifico si un elemento está en un set?
# MAGIC 62. ¿Puedo acceder a elementos de un set por índice?
# MAGIC 63. ¿Qué es la unión, intersección y diferencia de sets?
# MAGIC 64. Dame 5 ejemplos de cuándo usar sets en finanzas
# MAGIC 65. ¿Cómo creo un set vacío?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔄 CONVERSIONES (10 preguntas)
# MAGIC
# MAGIC 66. ¿Cómo convierto una lista en set?
# MAGIC 67. ¿Cómo convierto una tupla en lista?
# MAGIC 68. ¿Cómo creo un diccionario a partir de dos listas?
# MAGIC 69. ¿Cómo convierto un diccionario en lista de tuplas?
# MAGIC 70. ¿Qué pasa al convertir un diccionario a set?
# MAGIC 71. ¿Cómo convierto un string en lista de caracteres?
# MAGIC 72. ¿Puedo convertir cualquier estructura a cualquier otra?
# MAGIC 73. ¿Qué información se pierde al convertir lista a set?
# MAGIC 74. ¿Cómo creo una lista de tuplas a partir de un diccionario?
# MAGIC 75. Muéstrame 5 ejemplos de conversiones útiles en finanzas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📊 COMPARACIÓN Y SELECCIÓN (15 preguntas)
# MAGIC
# MAGIC 76. ¿Cuándo debo usar listas vs diccionarios?
# MAGIC 77. ¿Cuándo debo usar tuplas vs listas?
# MAGIC 78. ¿Cuándo debo usar sets vs listas?
# MAGIC 79. ¿Cuál estructura es más rápida para buscar?
# MAGIC 80. ¿Cuál estructura usa menos memoria?
# MAGIC 81. ¿Puedo anidar estructuras? (lista de diccionarios, etc.)
# MAGIC 82. ¿Qué estructura usar para precios históricos?
# MAGIC 83. ¿Qué estructura usar para un portafolio?
# MAGIC 84. ¿Qué estructura usar para tickers únicos?
# MAGIC 85. Muéstrame una comparación de velocidad entre estructuras
# MAGIC 86. ¿Qué es big O notation aplicado a estructuras?
# MAGIC 87. ¿Cómo elijo la estructura correcta para mi problema?
# MAGIC 88. Dame 10 ejemplos de estructuras combinadas en finanzas
# MAGIC 89. ¿Qué estructura usar para datos de series temporales?
# MAGIC 90. ¿Qué estructura usar para configuraciones?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎉 ¡Felicitaciones!
# MAGIC
# MAGIC Has completado el **Notebook 0.4 - Estructuras de Datos**.
# MAGIC
# MAGIC ### ¿Qué aprendiste?
# MAGIC
# MAGIC ✅ **Listas**: Colecciones ordenadas mutables  
# MAGIC ✅ **Tuplas**: Datos inmutables y seguros  
# MAGIC ✅ **Diccionarios**: Pares clave-valor  
# MAGIC ✅ **Sets**: Elementos únicos sin orden  
# MAGIC ✅ **Cuándo usar cada estructura**  
# MAGIC ✅ **Conversiones entre estructuras**  
# MAGIC ✅ **Estructuras anidadas**  
# MAGIC ✅ **Aplicaciones financieras reales**
# MAGIC
# MAGIC ### 👉 Próximo Paso
# MAGIC
# MAGIC Continuar con **Notebook 0.5 - Pandas para Finanzas** donde aprenderás:
# MAGIC * DataFrames: La estructura más poderosa
# MAGIC * Leer y manipular datos tabulares
# MAGIC * Filtrado, agregaciones, group by
# MAGIC * Series temporales
# MAGIC
# MAGIC ¡Nos vemos en el próximo notebook! 🚀