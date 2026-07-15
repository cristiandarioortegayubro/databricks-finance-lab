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
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC # Databricks Finance Lab
# MAGIC ## Analítica Financiera Agéntica
# MAGIC
# MAGIC ### Módulo 00: Nivelación en Python
# MAGIC ### Notebook 0.1: Introducción a Python
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC </div>

# COMMAND ----------

# DBTITLE 1,Bienvenida al Módulo de Nivelación
# MAGIC %md
# MAGIC # 👋 Bienvenida al Módulo de Nivelación en Python
# MAGIC
# MAGIC ## 🎯 Objetivo del Módulo 00
# MAGIC
# MAGIC ¡Bienvenido/a! Este módulo está diseñado para que **cualquier estudiante**, sin importar su experiencia previa en programación, pueda seguir el curso de **Analítica Financiera Agéntica**.
# MAGIC
# MAGIC ### ¿Para quién es este módulo?
# MAGIC
# MAGIC ✅ Estudiantes **sin experiencia en Python**  
# MAGIC ✅ Estudiantes con conocimientos básicos que desean **refrescar conceptos**  
# MAGIC ✅ Estudiantes que vienen de otros lenguajes (Excel, R, etc.)  
# MAGIC ✅ Cualquiera que quiera **aprender Python aplicado a finanzas**
# MAGIC
# MAGIC ### ¿Qué vamos a aprender?
# MAGIC
# MAGIC El Módulo 00 tiene **7 notebooks** que cubren todo lo necesario:
# MAGIC
# MAGIC 1. **0.1 - Introducción a Python** (este notebook)
# MAGIC    * Variables y tipos de datos
# MAGIC    * Operadores aritméticos
# MAGIC    * Strings y formato
# MAGIC    * Print y salida de datos
# MAGIC
# MAGIC 2. **0.2 - Estructuras de Control**
# MAGIC    * Condicionales (if, elif, else)
# MAGIC    * Bucles (for, while)
# MAGIC    * List comprehensions
# MAGIC
# MAGIC 3. **0.3 - Funciones y Módulos**
# MAGIC    * Crear funciones
# MAGIC    * Parámetros y return
# MAGIC    * Importar librerías
# MAGIC
# MAGIC 4. **0.4 - Estructuras de Datos**
# MAGIC    * Listas y tuplas
# MAGIC    * Diccionarios
# MAGIC    * Sets
# MAGIC
# MAGIC 5. **0.5 - Pandas para Finanzas**
# MAGIC    * DataFrames
# MAGIC    * Filtrado y selección
# MAGIC    * Agregaciones
# MAGIC
# MAGIC 6. **0.6 - Visualización de Datos**
# MAGIC    * Matplotlib
# MAGIC    * Seaborn
# MAGIC    * **Plotly** (gráficos interactivos)
# MAGIC
# MAGIC 7. **0.7 - Python Aplicado a Finanzas**
# MAGIC    * Cálculos financieros
# MAGIC    * Manejo de fechas
# MAGIC    * Buenas prácticas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📚 Metodología de Aprendizaje
# MAGIC
# MAGIC 👉 **Aprender haciendo**: Cada concepto viene con ejemplos ejecutables  
# MAGIC 👉 **Contexto financiero**: Todos los ejemplos usan casos financieros reales  
# MAGIC 👉 **Progresión gradual**: De lo más simple a lo más complejo  
# MAGIC 👉 **Ejercicios prácticos**: Al final de cada sección  
# MAGIC 👉 **Genie como tutor**: Preguntas sugeridas para explorar con IA
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ⌚ Tiempo Estimado
# MAGIC
# MAGIC * **Este notebook (0.1)**: 30-45 minutos
# MAGIC * **Módulo completo (0.1-0.7)**: 8-10 horas
# MAGIC
# MAGIC 💡 **Tip**: No te apures. Es mejor entender bien los fundamentos que avanzar rápido.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ✅ ¿Listo/a para empezar?
# MAGIC
# MAGIC ¡Empecemos con lo más básico de Python!

# COMMAND ----------

# DBTITLE 1,Explicación - Qué es Python
# MAGIC %md
# MAGIC ## 🐍 ¿Qué es Python?
# MAGIC
# MAGIC **Python** es un lenguaje de programación:
# MAGIC * 📄 **Fácil de leer**: Su sintaxis es simple y clara (casi como escribir en inglés)
# MAGIC * 🚀 **Poderoso**: Usado por empresas como Google, Netflix, NASA
# MAGIC * 📊 **Popular en finanzas**: Bancos, fondos de inversión, analistas lo usan diariamente
# MAGIC * 🎓 **Ideal para aprender**: Perfecto para principiantes
# MAGIC
# MAGIC ### ¿Por qué Python en Finanzas?
# MAGIC
# MAGIC ✅ **Análisis de datos**: Pandas, NumPy  
# MAGIC ✅ **Visualizaciones**: Matplotlib, Seaborn, Plotly  
# MAGIC ✅ **Modelos financieros**: Cálculo de VAN, TIR, WACC  
# MAGIC ✅ **Automatización**: Descargar precios, generar reportes  
# MAGIC ✅ **Machine Learning**: Predicción de precios, detección de fraudes
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 💻 Tu Primer Programa en Python
# MAGIC
# MAGIC Empecemos con lo más simple: hacer que Python "hable".
# MAGIC
# MAGIC En Python, usamos `print()` para mostrar texto o resultados en la pantalla.

# COMMAND ----------

# DBTITLE 1,Código - Mi Primer Programa
# Mi primer programa en Python
print("¡Hola, mundo financiero!")
print("Bienvenido/a al curso de Analítica Financiera")

# COMMAND ----------

# DBTITLE 1,Explicación - Variables
# MAGIC %md
# MAGIC ## 📦 Variables: Cajas con Etiquetas
# MAGIC
# MAGIC ### ¿Qué es una variable?
# MAGIC
# MAGIC Imagina una **caja** donde guardas un valor, y le pones una **etiqueta** para recordar qué hay dentro.
# MAGIC
# MAGIC ```
# MAGIC ┌─────────────────┐
# MAGIC │  precio_accion  │  ← Etiqueta (nombre de la variable)
# MAGIC ├─────────────────┤
# MAGIC │     150.50      │  ← Contenido (valor)
# MAGIC └─────────────────┘
# MAGIC ```
# MAGIC
# MAGIC En Python, una **variable** es un nombre que usamos para guardar y acceder a un valor.
# MAGIC
# MAGIC ### Crear una variable
# MAGIC
# MAGIC En Python es MUY simple:
# MAGIC
# MAGIC ```python
# MAGIC nombre_variable = valor
# MAGIC ```
# MAGIC
# MAGIC **Ejemplo financiero**:
# MAGIC ```python
# MAGIC precio_accion = 150.50
# MAGIC empresa = "YPF"
# MAGIC cantidad_acciones = 100
# MAGIC ```
# MAGIC
# MAGIC ### Reglas para nombres de variables
# MAGIC
# MAGIC ✅ **Permitido**:
# MAGIC * Letras (a-z, A-Z)
# MAGIC * Números (pero NO al inicio)
# MAGIC * Guión bajo (_)
# MAGIC * Usar minúsculas con guiones bajos: `precio_accion`, `tasa_interes`
# MAGIC
# MAGIC ❌ **NO permitido**:
# MAGIC * Empezar con número: `1precio` ✗
# MAGIC * Espacios: `precio accion` ✗
# MAGIC * Caracteres especiales: `precio@acción` ✗
# MAGIC * Palabras reservadas: `if`, `for`, `class` ✗
# MAGIC
# MAGIC ### ¿Por qué usar variables?
# MAGIC
# MAGIC 1. **Reutilizar valores**: Calculas una vez, usas muchas veces
# MAGIC 2. **Código legible**: `precio_accion` es más claro que `150.50`
# MAGIC 3. **Facilita cambios**: Cambias el valor en un lugar, se actualiza en todos lados
# MAGIC
# MAGIC 💡 **Tip**: Usa nombres descriptivos. `p` no dice nada, pero `precio_cierre` sí.

# COMMAND ----------

# DBTITLE 1,Código - Ejemplo de Variables
# Ejemplo 1: Variables financieras básicas
empresa = "YPF"
precio_accion = 5250.75
cantidad_acciones = 50

print("Empresa:", empresa)
print("Precio por acción:", precio_accion)
print("Cantidad de acciones:", cantidad_acciones)

print("\n" + "="*50)

# Ejemplo 2: Usar variables en cálculos
inversion_total = precio_accion * cantidad_acciones
print("Inversión total: $", inversion_total)

print("\n" + "="*50)

# Ejemplo 3: Cambiar el valor de una variable
print("Precio original:", precio_accion)
precio_accion = 5500.00  # El precio subió
print("Precio actualizado:", precio_accion)

# La inversión se recalcula automáticamente
inversion_actualizada = precio_accion * cantidad_acciones
print("Nueva inversión total: $", inversion_actualizada)

# COMMAND ----------

# DBTITLE 1,Explicación - Tipos de Datos
# MAGIC %md
# MAGIC ## 🔢 Tipos de Datos: ¿Qué tipo de información guardamos?
# MAGIC
# MAGIC En Python, los datos tienen **tipos** diferentes según lo que representan.
# MAGIC
# MAGIC ### Los 4 tipos básicos más importantes
# MAGIC
# MAGIC #### 1. **int** (enteros) - Números sin decimales
# MAGIC
# MAGIC ```python
# MAGIC cantidad_acciones = 100
# MAGIC anio = 2024
# MAGIC clientes = 5000
# MAGIC ```
# MAGIC
# MAGIC **Uso en finanzas**: Cantidades, años, conteos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 2. **float** (decimales) - Números con punto decimal
# MAGIC
# MAGIC ```python
# MAGIC precio = 150.50
# MAGIC tasa_interes = 0.045  # 4.5%
# MAGIC rendimiento = 12.75
# MAGIC ```
# MAGIC
# MAGIC **Uso en finanzas**: Precios, tasas, porcentajes, ratios
# MAGIC
# MAGIC 💡 **Importante**: En Python usamos **punto** (`.`) para decimales, no coma (`,`)
# MAGIC * Correcto: `150.50` ✅
# MAGIC * Incorrecto: `150,50` ❌
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 3. **str** (strings) - Texto
# MAGIC
# MAGIC ```python
# MAGIC empresa = "Mercado Libre"
# MAGIC ticker = "MELI"
# MAGIC reporte = "El mercado está alcista"
# MAGIC ```
# MAGIC
# MAGIC **Uso en finanzas**: Nombres de empresas, tickers, descripciones, reportes
# MAGIC
# MAGIC 💡 **Importante**: El texto va entre comillas:
# MAGIC * Comillas dobles: `"YPF"` ✅
# MAGIC * Comillas simples: `'YPF'` ✅
# MAGIC * Sin comillas: `YPF` ❌ (Python pensará que es una variable)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 4. **bool** (booleanos) - Verdadero o Falso
# MAGIC
# MAGIC ```python
# MAGIC es_rentable = True
# MAGIC mercado_alcista = False
# MAGIC tiene_dividendos = True
# MAGIC ```
# MAGIC
# MAGIC **Uso en finanzas**: Condiciones, flags, estados
# MAGIC
# MAGIC 💡 **Importante**: En Python se escribe con mayúscula inicial:
# MAGIC * `True` ✅
# MAGIC * `False` ✅
# MAGIC * `true` o `false` ❌ (da error)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ¿Cómo saber el tipo de una variable?
# MAGIC
# MAGIC Usa la función `type()`:
# MAGIC
# MAGIC ```python
# MAGIC precio = 150.50
# MAGIC print(type(precio))  # <class 'float'>
# MAGIC ```
# MAGIC
# MAGIC ### Resumen Visual
# MAGIC
# MAGIC | Tipo | Ejemplo | Uso Financiero |
# MAGIC |------|---------|----------------|
# MAGIC | **int** | `100` | Cantidad de acciones, años |
# MAGIC | **float** | `150.50` | Precios, tasas, rendimientos |
# MAGIC | **str** | `"YPF"` | Nombres, tickers, descripciones |
# MAGIC | **bool** | `True` | Condiciones, estados |

# COMMAND ----------

# DBTITLE 1,Código - Tipos de Datos
# Ejemplo de los 4 tipos de datos básicos

print("═" * 60)
print("EJEMPLO: Tipos de Datos en Finanzas")
print("═" * 60)

# 1. int (enteros)
cantidad_acciones = 150
anio_inversion = 2024
print("\n1️⃣ ENTEROS (int):")
print(f"   Cantidad de acciones: {cantidad_acciones}")
print(f"   Año de inversión: {anio_inversion}")
print(f"   Tipo: {type(cantidad_acciones)}")

# 2. float (decimales)
precio_accion = 5250.75
tasa_interes = 0.045  # 4.5%
print("\n2️⃣ DECIMALES (float):")
print(f"   Precio por acción: ${precio_accion}")
print(f"   Tasa de interés: {tasa_interes} (4.5%)")
print(f"   Tipo: {type(precio_accion)}")

# 3. str (strings - texto)
empresa = "Banco Galicia"
ticker = "GGAL"
print("\n3️⃣ TEXTO (str):")
print(f"   Empresa: {empresa}")
print(f"   Ticker: {ticker}")
print(f"   Tipo: {type(empresa)}")

# 4. bool (booleanos)
es_rentable = True
tiene_dividendos = False
print("\n4️⃣ BOOLEANOS (bool):")
print(f"   ¿Es rentable?: {es_rentable}")
print(f"   ¿Tiene dividendos?: {tiene_dividendos}")
print(f"   Tipo: {type(es_rentable)}")

print("\n" + "═" * 60)

# Ejemplo práctico combinado
print("\n💼 ANÁLISIS DE INVERSIÓN:")
print(f"   Invertí en {cantidad_acciones} acciones de {empresa}")
print(f"   Precio por acción: ${precio_accion}")
inversion_total = cantidad_acciones * precio_accion
print(f"   Inversión total: ${inversion_total}")
print(f"   ¿Es rentable? {es_rentable}")

# COMMAND ----------

# DBTITLE 1,Explicación - Operadores Aritméticos
# MAGIC %md
# MAGIC ## ➕ Operadores Aritméticos: Hacer Cálculos
# MAGIC
# MAGIC Python funciona como una **calculadora** muy poderosa. Podemos hacer todas las operaciones matemáticas básicas.
# MAGIC
# MAGIC ### Operadores Básicos
# MAGIC
# MAGIC | Operador | Operación | Ejemplo | Resultado |
# MAGIC |----------|-----------|---------|----------|
# MAGIC | `+` | Suma | `100 + 50` | `150` |
# MAGIC | `-` | Resta | `100 - 30` | `70` |
# MAGIC | `*` | Multiplicación | `50 * 3` | `150` |
# MAGIC | `/` | División | `100 / 4` | `25.0` |
# MAGIC | `**` | Potencia | `2 ** 3` | `8` |
# MAGIC | `//` | División entera | `10 // 3` | `3` |
# MAGIC | `%` | Módulo (resto) | `10 % 3` | `1` |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ejemplos Financieros
# MAGIC
# MAGIC #### 1. Calcular valor total de una inversión
# MAGIC
# MAGIC ```python
# MAGIC precio = 150.50
# MAGIC cantidad = 100
# MAGIC total = precio * cantidad  # 15050.0
# MAGIC ```
# MAGIC
# MAGIC #### 2. Calcular rendimiento porcentual
# MAGIC
# MAGIC ```python
# MAGIC precio_inicial = 100
# MAGIC precio_final = 120
# MAGIC rendimiento = (precio_final - precio_inicial) / precio_inicial
# MAGIC rendimiento_pct = rendimiento * 100  # 20.0%
# MAGIC ```
# MAGIC
# MAGIC #### 3. Calcular interés compuesto
# MAGIC
# MAGIC ```python
# MAGIC capital = 10000
# MAGIC tasa = 0.05  # 5%
# MAGIC anios = 3
# MAGIC monto_final = capital * (1 + tasa) ** anios
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Orden de Operaciones
# MAGIC
# MAGIC Python respeta el orden matemático estándar:
# MAGIC
# MAGIC 1. **Paréntesis** `()`
# MAGIC 2. **Potencias** `**`
# MAGIC 3. **Multiplicación y División** `*` `/` `//` `%`
# MAGIC 4. **Suma y Resta** `+` `-`
# MAGIC
# MAGIC **Ejemplo**:
# MAGIC ```python
# MAGIC resultado = 2 + 3 * 4
# MAGIC print(resultado)  # 14 (no 20)
# MAGIC
# MAGIC resultado = (2 + 3) * 4
# MAGIC print(resultado)  # 20
# MAGIC ```
# MAGIC
# MAGIC 💡 **Tip**: Cuando tengas dudas, usa paréntesis para dejar claro el orden.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### División: `/` vs `//`
# MAGIC
# MAGIC * **`/`** (división normal): Siempre da un float (decimal)
# MAGIC   ```python
# MAGIC   10 / 4  # 2.5
# MAGIC   ```
# MAGIC
# MAGIC * **`//`** (división entera): Solo da la parte entera
# MAGIC   ```python
# MAGIC   10 // 4  # 2
# MAGIC   ```
# MAGIC
# MAGIC **Uso financiero**: 
# MAGIC * `/` para cálculos de rendimiento, ratios
# MAGIC * `//` cuando quieres cantidades enteras (ej: cuántos meses completos)

# COMMAND ----------

# DBTITLE 1,Código - Operadores Aritméticos
print("═" * 70)
print("EJEMPLO: Operadores Aritméticos en Finanzas")
print("═" * 70)

# 1. SUMA: Calcular inversión total
print("\n1️⃣ SUMA (+): Inversión en múltiples activos")
accion_a = 5000
accion_b = 3500
accion_c = 2800
total_invertido = accion_a + accion_b + accion_c
print(f"   Acción A: ${accion_a}")
print(f"   Acción B: ${accion_b}")
print(f"   Acción C: ${accion_c}")
print(f"   Total invertido: ${total_invertido}")

# 2. RESTA: Calcular ganancia o pérdida
print("\n2️⃣ RESTA (-): Calcular ganancia")
precio_compra = 100.00
precio_venta = 125.50
ganancia = precio_venta - precio_compra
print(f"   Precio de compra: ${precio_compra}")
print(f"   Precio de venta: ${precio_venta}")
print(f"   Ganancia por acción: ${ganancia}")

# 3. MULTIPLICACIÓN: Valor total del portafolio
print("\n3️⃣ MULTIPLICACIÓN (*): Valor total")
precio_accion = 150.50
cantidad = 200
valor_total = precio_accion * cantidad
print(f"   Precio por acción: ${precio_accion}")
print(f"   Cantidad: {cantidad}")
print(f"   Valor total: ${valor_total}")

# 4. DIVISIÓN: Calcular precio promedio
print("\n4️⃣ DIVISIÓN (/): Precio promedio")
compra_1 = 100
compra_2 = 110
compra_3 = 105
precio_promedio = (compra_1 + compra_2 + compra_3) / 3
print(f"   Compra 1: ${compra_1}")
print(f"   Compra 2: ${compra_2}")
print(f"   Compra 3: ${compra_3}")
print(f"   Precio promedio: ${precio_promedio:.2f}")

# 5. POTENCIA: Interés compuesto
print("\n5️⃣ POTENCIA (**): Interés compuesto")
capital_inicial = 10000
tasa_anual = 0.05  # 5%
anios = 3
monto_final = capital_inicial * (1 + tasa_anual) ** anios
print(f"   Capital inicial: ${capital_inicial}")
print(f"   Tasa anual: {tasa_anual * 100}%")
print(f"   Años: {anios}")
print(f"   Monto final: ${monto_final:.2f}")
ganancia_total = monto_final - capital_inicial
print(f"   Ganancia por intereses: ${ganancia_total:.2f}")

# 6. MÓDULO: Verificar si un número es par o impar
print("\n6️⃣ MÓDULO (%): Operaciones especiales")
anio = 2024
resto = anio % 4
print(f"   Año: {anio}")
print(f"   Resto de {anio} ÷ 4: {resto}")
if resto == 0:
    print(f"   → {anio} es divisible por 4 (año bisiesto)")

print("\n" + "═" * 70)

# EJEMPLO INTEGRADO: Calcular rendimiento de inversión
print("\n💼 CÁLCULO DE RENDIMIENTO:")
print("-" * 70)
inversion_inicial = 50000
inversion_final = 62500
tiempo_dias = 180

ganancia = inversion_final - inversion_inicial
rendimiento_decimal = ganancia / inversion_inicial
rendimiento_porcentual = rendimiento_decimal * 100
rendimiento_anualizado = rendimiento_porcentual * (365 / tiempo_dias)

print(f"Inversión inicial: ${inversion_inicial:,.2f}")
print(f"Inversión final: ${inversion_final:,.2f}")
print(f"Tiempo: {tiempo_dias} días")
print(f"\nGanancia: ${ganancia:,.2f}")
print(f"Rendimiento: {rendimiento_porcentual:.2f}%")
print(f"Rendimiento anualizado: {rendimiento_anualizado:.2f}%")

# COMMAND ----------

# DBTITLE 1,Explicación - Strings y Formato
# MAGIC %md
# MAGIC ## 📝 Strings: Trabajar con Texto
# MAGIC
# MAGIC En finanzas, no todo son números. Necesitamos **texto** para:
# MAGIC * Nombres de empresas
# MAGIC * Tickers
# MAGIC * Reportes
# MAGIC * Mensajes
# MAGIC
# MAGIC ### Concatenación: Unir Strings
# MAGIC
# MAGIC Podemos **unir** (concatenar) strings con el operador `+`:
# MAGIC
# MAGIC ```python
# MAGIC empresa = "Banco "
# MAGIC banco = "Galicia"
# MAGIC nombre_completo = empresa + banco  # "Banco Galicia"
# MAGIC ```
# MAGIC
# MAGIC ### f-strings: Formato Moderno y Fácil
# MAGIC
# MAGIC La forma **más moderna y recomendada** de combinar texto con variables es usar **f-strings**:
# MAGIC
# MAGIC ```python
# MAGIC empresa = "YPF"
# MAGIC precio = 5250.75
# MAGIC
# MAGIC # F-string: se pone f antes de las comillas
# MAGIC mensaje = f"El precio de {empresa} es ${precio}"
# MAGIC print(mensaje)
# MAGIC # Salida: El precio de YPF es $5250.75
# MAGIC ```
# MAGIC
# MAGIC 👉 **Nota la `f` antes de las comillas**: `f"...{variable}..."`
# MAGIC
# MAGIC ### Formatear Números
# MAGIC
# MAGIC Podemos controlar cómo se muestran los números:
# MAGIC
# MAGIC #### 1. Decimales
# MAGIC
# MAGIC ```python
# MAGIC precio = 5250.75438
# MAGIC print(f"Precio: ${precio:.2f}")  # 2 decimales
# MAGIC # Salida: Precio: $5250.75
# MAGIC ```
# MAGIC
# MAGIC #### 2. Separador de miles
# MAGIC
# MAGIC ```python
# MAGIC monto = 1250000
# MAGIC print(f"Monto: ${monto:,}")
# MAGIC # Salida: Monto: $1,250,000
# MAGIC ```
# MAGIC
# MAGIC #### 3. Porcentajes
# MAGIC
# MAGIC ```python
# MAGIC rendimiento = 0.1245
# MAGIC print(f"Rendimiento: {rendimiento:.2%}")
# MAGIC # Salida: Rendimiento: 12.45%
# MAGIC ```
# MAGIC
# MAGIC ### Operaciones con Strings
# MAGIC
# MAGIC #### Longitud
# MAGIC ```python
# MAGIC ticker = "MELI"
# MAGIC print(len(ticker))  # 4
# MAGIC ```
# MAGIC
# MAGIC #### Mayúsculas y minúsculas
# MAGIC ```python
# MAGIC empresa = "mercado libre"
# MAGIC print(empresa.upper())  # MERCADO LIBRE
# MAGIC print(empresa.lower())  # mercado libre
# MAGIC print(empresa.title())  # Mercado Libre
# MAGIC ```
# MAGIC
# MAGIC #### Verificaciones
# MAGIC ```python
# MAGIC ticker = "AAPL"
# MAGIC print(ticker.isupper())  # True
# MAGIC print(ticker.isdigit())  # False
# MAGIC ```
# MAGIC
# MAGIC ### Ejemplo Práctico: Reporte de Cartera
# MAGIC
# MAGIC ```python
# MAGIC empresa = "Banco Galicia"
# MAGIC ticker = "GGAL"
# MAGIC precio = 175.50
# MAGIC cantidad = 100
# MAGIC total = precio * cantidad
# MAGIC
# MAGIC reporte = f"""
# MAGIC === REPORTE DE INVERSIÓN ===
# MAGIC Empresa: {empresa} ({ticker})
# MAGIC Precio: ${precio:.2f}
# MAGIC Cantidad: {cantidad}
# MAGIC Valor Total: ${total:,.2f}
# MAGIC """
# MAGIC
# MAGIC print(reporte)
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Código - Strings y Formato
print("═" * 70)
print("EJEMPLO: Strings y Formato en Finanzas")
print("═" * 70)

# 1. CONCATENACIÓN BÁSICA
print("\n1️⃣ CONCATENACIÓN:")
empresa_tipo = "Banco "
empresa_nombre = "Galicia"
nombre_completo = empresa_tipo + empresa_nombre
print(f"   {nombre_completo}")

# 2. F-STRINGS: La forma moderna
print("\n2️⃣ F-STRINGS (Recomendado):")
empresa = "YPF"
ticker = "YPFD"
precio = 5250.75
cantidad = 50

# F-string simple
mensaje = f"El precio de {empresa} ({ticker}) es ${precio}"
print(f"   {mensaje}")

# F-string con cálculos
total = precio * cantidad
print(f"   Si compro {cantidad} acciones, pago ${total}")

# 3. FORMATEAR NÚMEROS
print("\n3️⃣ FORMATEAR NÚMEROS:")
monto_grande = 1250000.758
rendimiento = 0.1245
tasa = 0.045

print(f"   2 decimales: ${monto_grande:.2f}")
print(f"   Separador de miles: ${monto_grande:,.2f}")
print(f"   Porcentaje: {rendimiento:.2%}")
print(f"   Tasa: {tasa * 100:.1f}%")

# 4. OPERACIONES CON STRINGS
print("\n4️⃣ OPERACIONES:")
ticker = "MELI"
empresa_full = "mercado libre"

print(f"   Longitud de ticker: {len(ticker)} caracteres")
print(f"   Mayúsculas: {empresa_full.upper()}")
print(f"   Título: {empresa_full.title()}")
print(f"   ¿Es mayúscula?: {ticker.isupper()}")

# 5. REPORTE COMPLETO
print("\n" + "═" * 70)
print("📄 REPORTE DE PORTAFOLIO")
print("═" * 70)

# Datos del portafolio
empresas = [
    {"nombre": "Banco Galicia", "ticker": "GGAL", "precio": 175.50, "cantidad": 100},
    {"nombre": "YPF", "ticker": "YPFD", "precio": 5250.75, "cantidad": 50},
    {"nombre": "Mercado Libre", "ticker": "MELI", "precio": 1450.00, "cantidad": 25}
]

total_portafolio = 0

for accion in empresas:
    valor = accion["precio"] * accion["cantidad"]
    total_portafolio += valor
    
    reporte = f"""
Empresa: {accion['nombre']} ({accion['ticker']})
Precio: ${accion['precio']:,.2f}
Cantidad: {accion['cantidad']}
Valor: ${valor:,.2f}
{'-' * 70}"""
    print(reporte)

print(f"\nVALOR TOTAL DEL PORTAFOLIO: ${total_portafolio:,.2f}")
print("═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - Conversión de Tipos
# MAGIC %md
# MAGIC ## 🔄 Conversión de Tipos (Type Conversion)
# MAGIC
# MAGIC ### ¿Por qué convertir tipos?
# MAGIC
# MAGIC A veces necesitamos **cambiar** el tipo de un dato:
# MAGIC * Convertir texto a número para calcular
# MAGIC * Convertir número a texto para mostrar
# MAGIC * Leer datos de un archivo (siempre vienen como texto)
# MAGIC
# MAGIC ### Funciones de Conversión
# MAGIC
# MAGIC #### 1. `int()` - Convertir a entero
# MAGIC
# MAGIC ```python
# MAGIC # De string a int
# MAGIC texto = "100"
# MAGIC numero = int(texto)
# MAGIC print(numero)  # 100 (como número)
# MAGIC print(type(numero))  # <class 'int'>
# MAGIC
# MAGIC # De float a int (elimina decimales)
# MAGIC precio = 150.75
# MAGIC precio_entero = int(precio)
# MAGIC print(precio_entero)  # 150
# MAGIC ```
# MAGIC
# MAGIC ⚠️ **Cuidado**: Si el string no es un número válido, da error:
# MAGIC ```python
# MAGIC int("hola")  # ❌ ERROR
# MAGIC int("150.5")  # ❌ ERROR (tiene punto decimal)
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 2. `float()` - Convertir a decimal
# MAGIC
# MAGIC ```python
# MAGIC # De string a float
# MAGIC tasa = "0.045"
# MAGIC tasa_numero = float(tasa)
# MAGIC print(tasa_numero)  # 0.045
# MAGIC
# MAGIC # De int a float
# MAGIC cantidad = 100
# MAGIC cantidad_decimal = float(cantidad)
# MAGIC print(cantidad_decimal)  # 100.0
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 3. `str()` - Convertir a texto
# MAGIC
# MAGIC ```python
# MAGIC # De int a string
# MAGIC precio = 150
# MAGIC precio_texto = str(precio)
# MAGIC print(precio_texto)  # "150" (como texto)
# MAGIC print(type(precio_texto))  # <class 'str'>
# MAGIC
# MAGIC # Ahora puedes concatenar
# MAGIC mensaje = "El precio es " + precio_texto
# MAGIC print(mensaje)  # El precio es 150
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ¿Cuándo usar cada una?
# MAGIC
# MAGIC | Conversión | Cuándo usarla | Ejemplo Financiero |
# MAGIC |-------------|----------------|--------------------|
# MAGIC | `int()` | Cantidades exactas | Cantidad de acciones |
# MAGIC | `float()` | Números con decimales | Precios, tasas, rendimientos |
# MAGIC | `str()` | Mostrar en reportes | Concatenar con texto |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Caso Práctico: Leer Entrada del Usuario
# MAGIC
# MAGIC Cuando lees datos del usuario (aunque no lo haremos en este curso), **siempre vienen como string**:
# MAGIC
# MAGIC ```python
# MAGIC # Ejemplo (solo ilustrativo)
# MAGIC precio_input = "150.50"  # Viene como texto
# MAGIC cantidad_input = "100"   # Viene como texto
# MAGIC
# MAGIC # Necesitas convertir para calcular
# MAGIC precio = float(precio_input)
# MAGIC cantidad = int(cantidad_input)
# MAGIC total = precio * cantidad
# MAGIC
# MAGIC print(f"Total: ${total}")
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Truco: Verificar antes de convertir
# MAGIC
# MAGIC ```python
# MAGIC texto = "150"
# MAGIC
# MAGIC # Verificar si es un número
# MAGIC if texto.isdigit():
# MAGIC     numero = int(texto)
# MAGIC     print(f"Convertido: {numero}")
# MAGIC else:
# MAGIC     print("No es un número válido")
# MAGIC ```
# MAGIC
# MAGIC 💡 **Tip**: En finanzas, casi siempre trabajamos con `float()` porque los precios y tasas tienen decimales.

# COMMAND ----------

# DBTITLE 1,Código - Conversión de Tipos
print("═" * 70)
print("EJEMPLO: Conversión de Tipos en Finanzas")
print("═" * 70)

# 1. STRING A NÚMERO
print("\n1️⃣ DE STRING A NÚMERO:")
precio_texto = "5250.75"
cantidad_texto = "50"

print(f"   Antes - precio_texto: '{precio_texto}' (tipo: {type(precio_texto).__name__})")
print(f"   Antes - cantidad_texto: '{cantidad_texto}' (tipo: {type(cantidad_texto).__name__})")

# Convertir
precio = float(precio_texto)
cantidad = int(cantidad_texto)

print(f"\n   Después - precio: {precio} (tipo: {type(precio).__name__})")
print(f"   Después - cantidad: {cantidad} (tipo: {type(cantidad).__name__})")

# Ahora podemos calcular
total = precio * cantidad
print(f"\n   💵 Cálculo: {cantidad} acciones × ${precio} = ${total:,.2f}")

# 2. NÚMERO A STRING (para reportes)
print("\n2️⃣ DE NÚMERO A STRING:")
rendimiento = 0.1245
monto = 150000

print(f"   Antes - rendimiento: {rendimiento} (tipo: {type(rendimiento).__name__})")

# Convertir a string
rendimiento_texto = str(rendimiento)
monto_texto = str(monto)

print(f"   Después - rendimiento_texto: '{rendimiento_texto}' (tipo: {type(rendimiento_texto).__name__})")

# Ahora podemos concatenar
reporte = "El rendimiento fue de " + rendimiento_texto + " sobre " + monto_texto
print(f"\n   Reporte: {reporte}")
print(f"   (Mejor con f-string: El rendimiento fue de {rendimiento} sobre ${monto})")

# 3. FLOAT A INT (elimina decimales)
print("\n3️⃣ DE FLOAT A INT (eliminar decimales):")
precio_decimal = 150.99
precio_entero = int(precio_decimal)

print(f"   Precio original: ${precio_decimal}")
print(f"   Precio sin decimales: ${precio_entero}")
print(f"   ⚠️ Nota: NO redondea, simplemente elimina los decimales")

# 4. CASO PRÁCTICO: Procesar datos de texto
print("\n4️⃣ CASO PRÁCTICO: Procesar datos de un CSV (simulado)")
print("-" * 70)

# Simular datos que vienen de un archivo (siempre como strings)
datos_csv = [
    "YPF,5250.75,50",
    "GGAL,175.50,100",
    "MELI,1450.00,25"
]

total_portafolio = 0

print("\nProcesando datos...\n")
for linea in datos_csv:
    # Separar los valores
    partes = linea.split(",")
    ticker = partes[0]  # Ya es string
    precio = float(partes[1])  # Convertir a float
    cantidad = int(partes[2])  # Convertir a int
    
    valor = precio * cantidad
    total_portafolio += valor
    
    print(f"{ticker:6s} | Precio: ${precio:>8,.2f} | Cant: {cantidad:>3d} | Valor: ${valor:>12,.2f}")

print("-" * 70)
print(f"TOTAL DEL PORTAFOLIO: ${total_portafolio:,.2f}")

# 5. VERIFICAR ANTES DE CONVERTIR
print("\n5️⃣ VERIFICAR ANTES DE CONVERTIR:")
entrada_usuario = "150"

if entrada_usuario.isdigit():
    numero = int(entrada_usuario)
    print(f"   ✅ '{entrada_usuario}' es válido. Convertido a: {numero}")
else:
    print(f"   ❌ '{entrada_usuario}' no es un número válido")

entrada_invalida = "abc123"
if entrada_invalida.isdigit():
    numero = int(entrada_invalida)
    print(f"   ✅ '{entrada_invalida}' convertido a: {numero}")
else:
    print(f"   ❌ '{entrada_invalida}' no es un número válido")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Ejercicios Prácticos
# MAGIC %md
# MAGIC ## ✍️ EJERCICIOS PRÁCTICOS
# MAGIC
# MAGIC Es hora de poner en práctica lo aprendido. Resuelve estos ejercicios usando Python.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 1: Variables Básicas
# MAGIC
# MAGIC **Tarea**: Crea variables para una inversión y muestra la información.
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Crea una variable `empresa` con el nombre "Banco Galicia"
# MAGIC 2. Crea una variable `ticker` con el valor "GGAL"
# MAGIC 3. Crea una variable `precio_accion` con el valor 175.50
# MAGIC 4. Crea una variable `cantidad_acciones` con el valor 150
# MAGIC 5. Usa `print()` para mostrar cada variable
# MAGIC
# MAGIC **Resultado esperado**:
# MAGIC ```
# MAGIC Empresa: Banco Galicia
# MAGIC Ticker: GGAL
# MAGIC Precio: 175.5
# MAGIC Cantidad: 150
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 2: Cálculo de Inversión Total
# MAGIC
# MAGIC **Tarea**: Calcula el valor total de una inversión.
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Usa las variables del Ejercicio 1
# MAGIC 2. Calcula `inversion_total = precio_accion * cantidad_acciones`
# MAGIC 3. Muestra el resultado con un mensaje claro
# MAGIC
# MAGIC **Resultado esperado**:
# MAGIC ```
# MAGIC Inversión total: $26325.0
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 3: Calcular Ganancia
# MAGIC
# MAGIC **Tarea**: Calcula la ganancia de una operación.
# MAGIC
# MAGIC **Datos**:
# MAGIC * Compraste una acción a $100
# MAGIC * La vendiste a $125
# MAGIC * Tenías 50 acciones
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Crea variables: `precio_compra`, `precio_venta`, `cantidad`
# MAGIC 2. Calcula `ganancia_por_accion = precio_venta - precio_compra`
# MAGIC 3. Calcula `ganancia_total = ganancia_por_accion * cantidad`
# MAGIC 4. Muestra ambos resultados
# MAGIC
# MAGIC **Resultado esperado**:
# MAGIC ```
# MAGIC Ganancia por acción: $25
# MAGIC Ganancia total: $1250
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 4: F-strings y Formato
# MAGIC
# MAGIC **Tarea**: Crea un reporte formateado de una inversión.
# MAGIC
# MAGIC **Datos**:
# MAGIC * Empresa: "Mercado Libre"
# MAGIC * Ticker: "MELI"
# MAGIC * Precio: 1450.758 (con muchos decimales)
# MAGIC * Cantidad: 25
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Usa f-strings para crear un reporte
# MAGIC 2. El precio debe mostrarse con solo 2 decimales
# MAGIC 3. El total debe tener separador de miles
# MAGIC
# MAGIC **Resultado esperado**:
# MAGIC ```
# MAGIC REPORTE DE INVERSIÓN
# MAGIC Empresa: Mercado Libre (MELI)
# MAGIC Precio: $1450.76
# MAGIC Cantidad: 25
# MAGIC Total: $36,268.95
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 5: Rendimiento Porcentual
# MAGIC
# MAGIC **Tarea**: Calcula el rendimiento de una inversión.
# MAGIC
# MAGIC **Datos**:
# MAGIC * Inversión inicial: $10,000
# MAGIC * Inversión final: $12,500
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Calcula la ganancia: `ganancia = inversion_final - inversion_inicial`
# MAGIC 2. Calcula el rendimiento decimal: `rendimiento = ganancia / inversion_inicial`
# MAGIC 3. Calcula el rendimiento porcentual: `rendimiento_pct = rendimiento * 100`
# MAGIC 4. Muestra el resultado con 2 decimales
# MAGIC
# MAGIC **Resultado esperado**:
# MAGIC ```
# MAGIC Ganancia: $2500.0
# MAGIC Rendimiento: 25.00%
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 6: Interés Compuesto
# MAGIC
# MAGIC **Tarea**: Calcula el monto final con interés compuesto.
# MAGIC
# MAGIC **Fórmula**: $M = C \times (1 + r)^n$
# MAGIC
# MAGIC Donde:
# MAGIC * M = Monto final
# MAGIC * C = Capital inicial
# MAGIC * r = Tasa de interés (decimal)
# MAGIC * n = Número de períodos
# MAGIC
# MAGIC **Datos**:
# MAGIC * Capital inicial: $50,000
# MAGIC * Tasa anual: 6% (0.06)
# MAGIC * Años: 5
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Crea las variables
# MAGIC 2. Calcula: `monto_final = capital * (1 + tasa) ** anios`
# MAGIC 3. Calcula: `ganancia = monto_final - capital`
# MAGIC 4. Muestra ambos resultados con formato
# MAGIC
# MAGIC **Resultado esperado**:
# MAGIC ```
# MAGIC Monto final: $66,911.28
# MAGIC Ganancia por intereses: $16,911.28
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 7: Conversión de Tipos
# MAGIC
# MAGIC **Tarea**: Procesa datos que vienen como strings.
# MAGIC
# MAGIC **Datos** (como strings):
# MAGIC ```python
# MAGIC precio_texto = "5250.75"
# MAGIC cantidad_texto = "50"
# MAGIC ticker = "YPF"
# MAGIC ```
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Convierte `precio_texto` a float
# MAGIC 2. Convierte `cantidad_texto` a int
# MAGIC 3. Calcula el total
# MAGIC 4. Muestra un reporte con f-string
# MAGIC
# MAGIC **Resultado esperado**:
# MAGIC ```
# MAGIC Ticker: YPF
# MAGIC Precio: $5250.75
# MAGIC Cantidad: 50
# MAGIC Total: $262537.50
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 DESAFÍO FINAL: Portafolio Completo
# MAGIC
# MAGIC **Tarea**: Crea un análisis de un portafolio con 3 acciones.
# MAGIC
# MAGIC **Datos**:
# MAGIC | Empresa | Ticker | Precio | Cantidad |
# MAGIC |---------|--------|--------|----------|
# MAGIC | YPF | YPFD | 5250.75 | 50 |
# MAGIC | Banco Galicia | GGAL | 175.50 | 100 |
# MAGIC | Mercado Libre | MELI | 1450.00 | 25 |
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Crea variables para cada acción
# MAGIC 2. Calcula el valor de cada posición
# MAGIC 3. Calcula el valor total del portafolio
# MAGIC 4. Calcula el % que representa cada acción del total
# MAGIC 5. Crea un reporte bien formateado
# MAGIC
# MAGIC **Resultado esperado**:
# MAGIC ```
# MAGIC PORTAFOLIO DE INVERSIONES
# MAGIC ==========================
# MAGIC
# MAGIC YPF (YPFD)
# MAGIC   Precio: $5,250.75
# MAGIC   Cantidad: 50
# MAGIC   Valor: $262,537.50
# MAGIC   % del portafolio: 73.98%
# MAGIC
# MAGIC Banco Galicia (GGAL)
# MAGIC   Precio: $175.50
# MAGIC   Cantidad: 100
# MAGIC   Valor: $17,550.00
# MAGIC   % del portafolio: 4.95%
# MAGIC
# MAGIC Mercado Libre (MELI)
# MAGIC   Precio: $1,450.00
# MAGIC   Cantidad: 25
# MAGIC   Valor: $36,250.00
# MAGIC   % del portafolio: 10.22%
# MAGIC
# MAGIC ==========================
# MAGIC VALOR TOTAL: $316,337.50
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 💡 **Tip**: Empieza por los ejercicios más simples y avanza gradualmente. Si te atascas, revisa los ejemplos anteriores o pregunta a Genie Code.

# COMMAND ----------

# DBTITLE 1,Consultas con Genie Code
# MAGIC %md
# MAGIC ## 🤖 CONSULTAS CON GENIE CODE
# MAGIC
# MAGIC Usa estas preguntas para explorar y profundizar con la ayuda de Genie Code, tu asistente de IA.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 💻 Conceptos Básicos de Python
# MAGIC
# MAGIC 1. ¿Qué diferencia hay entre Python 2 y Python 3?
# MAGIC 2. ¿Por qué Python es tan popular en finanzas y ciencia de datos?
# MAGIC 3. ¿Qué significa que Python es un lenguaje "interpretado"?
# MAGIC 4. Muéstrame 5 ejemplos de cómo se usa Python en bancos y fondos de inversión
# MAGIC 5. ¿Qué es Databricks y cómo se relaciona con Python?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📦 Variables
# MAGIC
# MAGIC 6. ¿Por qué se llaman "variables"? ¿Qué significa que pueden "variar"?
# MAGIC 7. ¿Cuáles son las mejores prácticas para nombrar variables en Python?
# MAGIC 8. ¿Qué es snake_case y por qué se usa en Python?
# MAGIC 9. Muéstrame ejemplos de nombres de variables BUENOS y MALOS para finanzas
# MAGIC 10. ¿Qué pasa si uso una variable antes de crearla?
# MAGIC 11. ¿Puedo usar acentos o ñ en nombres de variables?
# MAGIC 12. Crea 10 nombres de variables descriptivos para diferentes conceptos financieros
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔢 Tipos de Datos
# MAGIC
# MAGIC 13. ¿Qué diferencia hay entre `int` y `float`? ¿Cuándo usar cada uno?
# MAGIC 14. ¿Qué pasa si divido dos enteros en Python? ¿Da un entero o un float?
# MAGIC 15. ¿Por qué `True` y `False` se escriben con mayúscula en Python?
# MAGIC 16. ¿Qué otros tipos de datos existen en Python además de int, float, str y bool?
# MAGIC 17. Muéstrame cómo verificar el tipo de cualquier variable
# MAGIC 18. ¿Qué es None en Python y cuándo se usa?
# MAGIC 19. Crea un ejemplo que use los 4 tipos básicos en un cálculo financiero
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ➕ Operadores Aritméticos
# MAGIC
# MAGIC 20. ¿Qué es la "precedencia de operadores" y por qué importa?
# MAGIC 21. ¿Cómo funciona el operador `%` (módulo)? Dame 3 ejemplos prácticos
# MAGIC 22. ¿Qué diferencia hay entre `/` y `//`?
# MAGIC 23. Muéstrame cómo calcular potencias de tres formas diferentes
# MAGIC 24. ¿Puedo usar operadores con variables de diferentes tipos (int y float)?
# MAGIC 25. Calcula el valor futuro de una inversión con interés compuesto usando operadores
# MAGIC 26. ¿Cómo redondeo un número en Python?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📝 Strings y Formato
# MAGIC
# MAGIC 27. ¿Qué diferencia hay entre usar comillas simples y dobles?
# MAGIC 28. ¿Cómo puedo incluir comillas dentro de un string?
# MAGIC 29. ¿Qué son los "caracteres de escape" como `\n` y `\t`?
# MAGIC 30. Muéstrame 5 formas diferentes de formatear strings en Python
# MAGIC 31. ¿Qué es mejor: concatenación, .format() o f-strings? ¿Por qué?
# MAGIC 32. ¿Cómo hago para que un número grande tenga separadores de miles?
# MAGIC 33. Muéstrame cómo formatear un número como porcentaje con f-strings
# MAGIC 34. Crea un template de reporte financiero bien formateado con f-strings
# MAGIC 35. ¿Cómo convierto un string a mayúsculas, minúsculas o title case?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔄 Conversión de Tipos
# MAGIC
# MAGIC 36. ¿Qué pasa si intento convertir un string no numérico a int?
# MAGIC 37. ¿Cómo puedo verificar si un string es un número válido antes de convertir?
# MAGIC 38. ¿Qué diferencia hay entre `int("150.5")` y `float("150.5")`?
# MAGIC 39. Muéstrame cómo convertir un número a string de diferentes formas
# MAGIC 40. ¿Por qué necesito convertir tipos cuando leo datos de archivos?
# MAGIC 41. Crea un programa que lea datos de strings y haga cálculos financieros
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📊 Aplicaciones Financieras
# MAGIC
# MAGIC 42. Calcula el VAN (Valor Actual Neto) de un proyecto usando solo lo aprendido
# MAGIC 43. Calcula cuánto necesito invertir hoy para tener $100,000 en 10 años
# MAGIC 44. Crea una calculadora de interés simple usando variables y operadores
# MAGIC 45. Calcula el precio promedio ponderado de compras de acciones
# MAGIC 46. ¿Cómo calculo la tasa de crecimiento anual compuesta (CAGR)?
# MAGIC 47. Crea un reporte de rendimiento de un portafolio con múltiples acciones
# MAGIC 48. Calcula el ratio precio/ganancia (P/E ratio) de una empresa
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚠️ Errores Comunes
# MAGIC
# MAGIC 49. ¿Qué significa el error "NameError: name 'x' is not defined"?
# MAGIC 50. ¿Por qué me da error cuando intento sumar un número y un string?
# MAGIC 51. ¿Qué significa "TypeError" y cómo lo soluciono?
# MAGIC 52. ¿Por qué `print precio` da error pero `print(precio)` funciona?
# MAGIC 53. Muéstrame los 10 errores más comunes que cometen los principiantes en Python
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🚀 Próximos Pasos
# MAGIC
# MAGIC 54. ¿Qué aprenderé en el notebook 0.2 (Estructuras de Control)?
# MAGIC 55. ¿Cómo se relaciona este notebook con el resto del curso de finanzas?
# MAGIC 56. Dame 5 ejercicios adicionales para practicar lo aprendido
# MAGIC 57. ¿Qué recursos adicionales recomiendas para aprender Python?
# MAGIC 58. ¿Cuánto tiempo necesito para dominar estos conceptos básicos?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🇦🇷 Contexto Argentino
# MAGIC
# MAGIC 59. ¿Cómo manejo los puntos y comas en precios argentinos vs Python?
# MAGIC 60. Muéstrame cómo trabajar con precios en pesos argentinos (ARS)
# MAGIC 61. Crea ejemplos financieros con empresas argentinas (YPF, GGAL, MELI)
# MAGIC 62. ¿Cómo calculo el efecto de la inflación argentina en una inversión?
# MAGIC 63. Muéstrame cómo convertir entre USD y ARS con tipos de cambio
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 💡 Consejos de Aprendizaje
# MAGIC
# MAGIC 64. ¿Cuál es la mejor forma de aprender Python? ¿Leer o practicar?
# MAGIC 65. ¿Cuánto tiempo debo dedicar diariamente a aprender Python?
# MAGIC 66. ¿Es necesario memorizar la sintaxis o puedo consultarla?
# MAGIC 67. Dame 5 consejos para no frustrarme cuando aprendo a programar
# MAGIC 68. ¿Cómo puedo practicar Python fuera de este curso?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 💡 **Tip**: No intentes memorizar todo. Enfocáte en entender los conceptos y practicar. Con Genie Code siempre puedes consultar dudas específicas cuando las necesites.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎉 ¡Felicitaciones!
# MAGIC
# MAGIC Has completado el **Notebook 0.1 - Introducción a Python**.
# MAGIC
# MAGIC ### ¿Qué aprendiste?
# MAGIC
# MAGIC ✅ Qué es Python y por qué se usa en finanzas  
# MAGIC ✅ Variables: crear, nombrar y usar  
# MAGIC ✅ Tipos de datos: int, float, str, bool  
# MAGIC ✅ Operadores aritméticos para cálculos  
# MAGIC ✅ Strings y formato con f-strings  
# MAGIC ✅ Conversión entre tipos de datos  
# MAGIC ✅ Aplicaciones financieras prácticas
# MAGIC
# MAGIC ### 👉 Próximo Paso
# MAGIC
# MAGIC Continuar con **Notebook 0.2 - Estructuras de Control** donde aprenderás:
# MAGIC * Condicionales (if, elif, else)
# MAGIC * Bucles (for, while)
# MAGIC * Cómo tomar decisiones en tu código
# MAGIC
# MAGIC ¡Nos vemos en el próximo notebook! 🚀