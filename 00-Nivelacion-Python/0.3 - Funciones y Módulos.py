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
# MAGIC ### Notebook 0.3: Funciones y Módulos para Finanzas
# MAGIC ### 🔧 **MODULARIDAD Y REUTILIZACIÓN DE CÓDIGO**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción - Funciones
# MAGIC %md
# MAGIC
# MAGIC # 🔧 Introducción: Funciones en Finanzas
# MAGIC
# MAGIC ## ¿Qué son las Funciones?
# MAGIC
# MAGIC Una **función** es un bloque de código reutilizable que realiza una tarea específica.
# MAGIC
# MAGIC ### Analogía Financiera
# MAGIC
# MAGIC Piensa en una función como una **calculadora financiera**:
# MAGIC
# MAGIC * ✅ **Input**: Datos que ingresan (precio inicial, precio final, tasa)
# MAGIC * ✅ **Proceso**: Cálculo interno (fórmula matemática)
# MAGIC * ✅ **Output**: Resultado (rendimiento, valor presente, TIR)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ¿Por qué son CRÍTICAS en Finanzas?
# MAGIC
# MAGIC ### 1. **Reutilización** 🔄
# MAGIC Escribe una vez, usa mil veces. Calcula VAN en todos tus proyectos.
# MAGIC
# MAGIC ### 2. **Consistencia** ✅
# MAGIC La misma fórmula siempre da el mismo resultado. Elimina errores.
# MAGIC
# MAGIC ### 3. **Mantenimiento** 🛠️
# MAGIC Si cambias una fórmula, actualizas UN solo lugar.
# MAGIC
# MAGIC ### 4. **Profesionalismo** 💼
# MAGIC Código modular = código profesional.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Estructura del Notebook
# MAGIC
# MAGIC 1. **Funciones Básicas**: def, parámetros, return, docstrings
# MAGIC 2. **Parámetros**: posicionales, por defecto, *args, **kwargs
# MAGIC 3. **Funciones Lambda**: map(), filter(), lambda
# MAGIC 4. **Scope**: variables locales y globales
# MAGIC 5. **Biblioteca Financiera**: 10+ funciones útiles
# MAGIC 6. **Módulos Built-in**: math, random, datetime
# MAGIC 7. **Crear Módulos**: tu propia librería
# MAGIC 8. **Caso Integrado**: análisis completo de cartera
# MAGIC 9. **Ejercicios**: práctica con bonos y opciones
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Objetivos de Aprendizaje
# MAGIC
# MAGIC Al finalizar este notebook podrás:
# MAGIC
# MAGIC * ✅ Crear funciones con parámetros y valores de retorno
# MAGIC * ✅ Documentar funciones con docstrings profesionales
# MAGIC * ✅ Usar funciones lambda para operaciones rápidas
# MAGIC * ✅ Construir tu propia biblioteca de funciones financieras
# MAGIC * ✅ Importar y usar módulos de Python
# MAGIC * ✅ Aplicar funciones en análisis financiero real
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⏱️ **Tiempo estimado**: 60-75 minutos
# MAGIC
# MAGIC 💡 **Tip**: Las funciones son el corazón de Python. Domínalas y tu código será 10x más poderoso.
# MAGIC
# MAGIC ¡Empecemos!

# COMMAND ----------

# DBTITLE 1,Sección - Funciones Básicas
# MAGIC %md
# MAGIC
# MAGIC # 📝 PARTE 1: Funciones Básicas
# MAGIC
# MAGIC ## Sintaxis de una Función
# MAGIC
# MAGIC ```python
# MAGIC def nombre_funcion(parametro1, parametro2):
# MAGIC     """
# MAGIC     Docstring: descripción de la función
# MAGIC     """
# MAGIC     # Código de la función
# MAGIC     resultado = parametro1 + parametro2
# MAGIC     return resultado
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Componentes Clave
# MAGIC
# MAGIC ### 1. `def` - Palabra Clave
# MAGIC Define que estás creando una función
# MAGIC
# MAGIC ### 2. Nombre de la Función
# MAGIC Descriptivo, en minúsculas, con guiones bajos (`calcular_van`, `valor_presente`)
# MAGIC
# MAGIC ### 3. Parámetros
# MAGIC Datos que la función necesita para trabajar
# MAGIC
# MAGIC ### 4. Docstring
# MAGIC Documentación de la función (entre triple comillas)
# MAGIC
# MAGIC ### 5. Cuerpo
# MAGIC Código que realiza la tarea
# MAGIC
# MAGIC ### 6. `return`
# MAGIC Devuelve el resultado
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Ejemplo Financiero
# MAGIC
# MAGIC Vamos a crear funciones para cálculos financieros comunes:
# MAGIC
# MAGIC 1. **Rendimiento simple** de una acción
# MAGIC 2. **Valor presente** de un flujo futuro
# MAGIC 3. **Conversión** pesos → dólares
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Creemos nuestras primeras funciones financieras.

# COMMAND ----------

# DBTITLE 1,Código - Funciones Básicas
print("═" * 70)
print("            FUNCIONES FINANCIERAS BÁSICAS")
print("═" * 70)

# ===== FUNCIÓN 1: RENDIMIENTO SIMPLE =====

def calcular_rendimiento_simple(precio_inicial, precio_final):
    """
    Calcula el rendimiento simple de una acción.
    
    Parámetros:
    -----------
    precio_inicial : float
        Precio de compra de la acción
    precio_final : float
        Precio de venta de la acción
    
    Retorna:
    --------
    float : Rendimiento como decimal (ej: 0.15 para 15%)
    
    Ejemplo:
    --------
    >>> calcular_rendimiento_simple(1000, 1150)
    0.15  # 15% de rendimiento
    """
    rendimiento = (precio_final - precio_inicial) / precio_inicial
    return rendimiento


# ===== FUNCIÓN 2: VALOR PRESENTE =====

def valor_presente(flujo_futuro, tasa, periodos):
    """
    Calcula el valor presente de un flujo de efectivo futuro.
    
    Fórmula: VP = VF / (1 + r)^n
    
    Parámetros:
    -----------
    flujo_futuro : float
        Monto que se recibirá en el futuro
    tasa : float
        Tasa de descuento por período (decimal, ej: 0.10 para 10%)
    periodos : int
        Número de períodos hasta recibir el flujo
    
    Retorna:
    --------
    float : Valor presente del flujo futuro
    
    Ejemplo:
    --------
    >>> valor_presente(100000, 0.10, 5)
    62092.13  # Un flujo de $100k en 5 años vale $62k hoy al 10%
    """
    vp = flujo_futuro / ((1 + tasa) ** periodos)
    return vp


# ===== FUNCIÓN 3: CONVERSIÓN PESOS → DÓLARES =====

def convertir_pesos_dolares(pesos, tipo_cambio):
    """
    Convierte pesos argentinos a dólares.
    
    Parámetros:
    -----------
    pesos : float
        Monto en pesos argentinos
    tipo_cambio : float
        Tipo de cambio (pesos por dólar)
    
    Retorna:
    --------
    float : Monto en dólares
    
    Ejemplo:
    --------
    >>> convertir_pesos_dolares(1000000, 350)
    2857.14  # $1M pesos = USD 2,857
    """
    dolares = pesos / tipo_cambio
    return dolares


print("\n✅ Funciones creadas:")
print("   • calcular_rendimiento_simple()")
print("   • valor_presente()")
print("   • convertir_pesos_dolares()")

# ===== PROBAR LAS FUNCIONES =====

print("\n" + "═" * 70)
print("EJEMPLOS DE USO")
print("═" * 70)

# Ejemplo 1: Rendimiento de YPF
precio_compra_ypf = 4500
precio_venta_ypf = 5200
rendimiento = calcular_rendimiento_simple(precio_compra_ypf, precio_venta_ypf)

print(f"\n📈 1. Rendimiento de YPF:")
print(f"   Precio compra: ${precio_compra_ypf:,.0f}")
print(f"   Precio venta: ${precio_venta_ypf:,.0f}")
print(f"   Rendimiento: {rendimiento:.2%}")

if rendimiento > 0:
    print(f"   ✅ Ganaste ${precio_venta_ypf - precio_compra_ypf:,.0f}")
else:
    print(f"   ❌ Perdiste ${abs(precio_venta_ypf - precio_compra_ypf):,.0f}")

# Ejemplo 2: Valor presente de inversión
flujo_futuro = 1_000_000  # $1M en 3 años
tasa_descuento = 0.12  # 12% anual
periodos = 3

vp = valor_presente(flujo_futuro, tasa_descuento, periodos)

print(f"\n💰 2. Valor Presente:")
print(f"   Flujo futuro (3 años): ${flujo_futuro:,.0f}")
print(f"   Tasa de descuento: {tasa_descuento:.0%}")
print(f"   Valor presente HOY: ${vp:,.2f}")
print(f"   Descuento aplicado: ${flujo_futuro - vp:,.2f}")

# Ejemplo 3: Conversión pesos → dólares
ahorros_pesos = 5_000_000  # $5M pesos
tipo_cambio_blue = 1100  # Dólar blue

dolares = convertir_pesos_dolares(ahorros_pesos, tipo_cambio_blue)

print(f"\n💵 3. Conversión Pesos → Dólares:")
print(f"   Ahorros en pesos: ${ahorros_pesos:,.0f}")
print(f"   Tipo de cambio (blue): ${tipo_cambio_blue:,.0f}")
print(f"   Equivalente en USD: ${dolares:,.2f}")

print("\n" + "═" * 70)
print("✅ Funciones básicas dominadas!")
print("═" * 70)

# COMMAND ----------

# DBTITLE 1,Sección - Parámetros
# MAGIC %md
# MAGIC
# MAGIC # 🎯 PARTE 2: Parámetros y Argumentos
# MAGIC
# MAGIC ## Tipos de Parámetros
# MAGIC
# MAGIC Python ofrece **flexibilidad total** para definir cómo una función recibe datos.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 1. Parámetros Posicionales
# MAGIC
# MAGIC El orden importa:
# MAGIC
# MAGIC ```python
# MAGIC def calcular_rendimiento(precio_inicial, precio_final):
# MAGIC     return (precio_final - precio_inicial) / precio_inicial
# MAGIC
# MAGIC # Llamada: orden específico
# MAGIC rendimiento = calcular_rendimiento(1000, 1150)
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 2. Parámetros por Nombre (Keyword Arguments)
# MAGIC
# MAGIC El orden NO importa:
# MAGIC
# MAGIC ```python
# MAGIC # Llamada: especificando nombres
# MAGIC rendimiento = calcular_rendimiento(precio_final=1150, precio_inicial=1000)
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 3. Parámetros por Defecto
# MAGIC
# MAGIC Valores predefinidos si no se especifican:
# MAGIC
# MAGIC ```python
# MAGIC def calcular_interes(capital, tasa=0.05, periodos=1):
# MAGIC     return capital * tasa * periodos
# MAGIC
# MAGIC # Llamadas válidas:
# MAGIC calcular_interes(10000)  # Usa tasa=0.05, periodos=1
# MAGIC calcular_interes(10000, 0.08)  # Usa tasa=0.08, periodos=1
# MAGIC calcular_interes(10000, tasa=0.10, periodos=3)
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 4. *args - Número Variable de Argumentos
# MAGIC
# MAGIC Recibe **cualquier cantidad** de argumentos posicionales:
# MAGIC
# MAGIC ```python
# MAGIC def sumar_inversiones(*montos):
# MAGIC     return sum(montos)
# MAGIC
# MAGIC sumar_inversiones(1000, 2000, 3000)  # 6000
# MAGIC sumar_inversiones(500, 1500)  # 2000
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 5. **kwargs - Argumentos con Nombre Variables
# MAGIC
# MAGIC Recibe **cualquier cantidad** de argumentos con nombre:
# MAGIC
# MAGIC ```python
# MAGIC def crear_portafolio(**acciones):
# MAGIC     for ticker, cantidad in acciones.items():
# MAGIC         print(f"{ticker}: {cantidad} acciones")
# MAGIC
# MAGIC crear_portafolio(YPF=100, GGAL=200, MELI=50)
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Veamos ejemplos prácticos financieros.

# COMMAND ----------

# DBTITLE 1,Código - Parámetros Avanzados
print("═" * 70)
print("            PARÁMETROS AVANZADOS EN FUNCIONES")
print("═" * 70)

# ===== FUNCIÓN CON PARÁMETROS POR DEFECTO =====

def calcular_valor_futuro(capital, tasa=0.10, periodos=1):
    """
    Calcula el valor futuro de un capital con interés compuesto.
    
    Parámetros:
    -----------
    capital : float
        Capital inicial
    tasa : float, opcional
        Tasa de interés por período (default: 0.10 = 10%)
    periodos : int, opcional
        Número de períodos (default: 1)
    
    Retorna:
    --------
    float : Valor futuro del capital
    """
    vf = capital * ((1 + tasa) ** periodos)
    return vf


print("\n🔹 1. Parámetros por Defecto:")
print("-" * 70)

# Diferentes formas de llamar la función
capital_inicial = 100000

# Solo capital (usa defaults)
vf1 = calcular_valor_futuro(capital_inicial)
print(f"Inversión: ${capital_inicial:,.0f}")
print(f"Con defaults (10%, 1 año): ${vf1:,.2f}")

# Capital + tasa
vf2 = calcular_valor_futuro(capital_inicial, 0.15)
print(f"Con tasa 15%, 1 año: ${vf2:,.2f}")

# Capital + tasa + períodos
vf3 = calcular_valor_futuro(capital_inicial, 0.15, 5)
print(f"Con tasa 15%, 5 años: ${vf3:,.2f}")

# Usando nombres (cualquier orden)
vf4 = calcular_valor_futuro(periodos=3, capital=capital_inicial, tasa=0.12)
print(f"Con tasa 12%, 3 años: ${vf4:,.2f}")


# ===== FUNCIÓN CON *args =====

def sumar_inversiones(*montos):
    """
    Suma cualquier cantidad de montos de inversiones.
    
    Parámetros:
    -----------
    *montos : float
        Número variable de montos a sumar
    
    Retorna:
    --------
    float : Suma total de inversiones
    """
    total = sum(montos)
    return total


def calcular_promedio_inversiones(*montos):
    """
    Calcula el promedio de inversiones.
    """
    if len(montos) == 0:
        return 0
    return sum(montos) / len(montos)


print("\n\n🔹 2. *args - Número Variable de Argumentos:")
print("-" * 70)

# Diferentes cantidades de inversiones
inversion_1 = sumar_inversiones(50000, 30000, 20000)
print(f"Cartera 1 (3 acciones): ${inversion_1:,.0f}")

inversion_2 = sumar_inversiones(10000, 15000, 25000, 30000, 20000)
print(f"Cartera 2 (5 acciones): ${inversion_2:,.0f}")

inversion_3 = sumar_inversiones(100000, 50000)
print(f"Cartera 3 (2 acciones): ${inversion_3:,.0f}")

# Promedio
promedio = calcular_promedio_inversiones(50000, 30000, 20000, 40000)
print(f"\nPromedio de inversión: ${promedio:,.0f}")


# ===== FUNCIÓN CON **kwargs =====

def crear_portafolio(**acciones):
    """
    Crea un portafolio con tickers y cantidades variables.
    
    Parámetros:
    -----------
    **acciones : int
        Pares ticker=cantidad
    
    Retorna:
    --------
    dict : Portafolio con valor total calculado
    """
    print("\n▶️ Portafolio creado:")
    
    # Precios de ejemplo (en un caso real vendrían de API)
    precios = {
        'YPF': 5200,
        'GGAL': 175,
        'MELI': 1450,
        'PAMP': 850,
        'TGSU2': 320
    }
    
    portafolio = {}
    valor_total = 0
    
    for ticker, cantidad in acciones.items():
        precio = precios.get(ticker, 0)
        valor = precio * cantidad
        valor_total += valor
        portafolio[ticker] = {
            'cantidad': cantidad,
            'precio': precio,
            'valor': valor
        }
        print(f"   {ticker:6s}: {cantidad:3d} acciones x ${precio:6,.0f} = ${valor:10,.0f}")
    
    print(f"   {'='*50}")
    print(f"   {'TOTAL':6s}: {' '*15} ${valor_total:10,.0f}")
    
    return portafolio


print("\n\n🔹 3. **kwargs - Argumentos con Nombre Variables:")
print("-" * 70)

# Crear portafolios con diferentes acciones
portafolio_1 = crear_portafolio(YPF=100, GGAL=500, MELI=50)

portafolio_2 = crear_portafolio(PAMP=200, TGSU2=300)

portafolio_3 = crear_portafolio(YPF=150, GGAL=300, MELI=80, PAMP=100, TGSU2=200)

print("\n" + "═" * 70)
print("✅ Parámetros avanzados dominados!")
print("═" * 70)

# COMMAND ----------

# DBTITLE 1,Sección - Funciones Lambda
# MAGIC %md
# MAGIC
# MAGIC # ⚡ PARTE 3: Funciones Lambda
# MAGIC
# MAGIC ## ¿Qué son las Funciones Lambda?
# MAGIC
# MAGIC Funciones **anónimas** (sin nombre) para operaciones **rápidas** y **simples**.
# MAGIC
# MAGIC ### Sintaxis
# MAGIC
# MAGIC ```python
# MAGIC lambda parametros: expresion
# MAGIC ```
# MAGIC
# MAGIC ### Comparación
# MAGIC
# MAGIC **Función tradicional**:
# MAGIC ```python
# MAGIC def duplicar(x):
# MAGIC     return x * 2
# MAGIC ```
# MAGIC
# MAGIC **Función lambda equivalente**:
# MAGIC ```python
# MAGIC duplicar = lambda x: x * 2
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ¿Cuándo Usar Lambda?
# MAGIC
# MAGIC * ✅ **Operaciones simples** de una línea
# MAGIC * ✅ **Callbacks** en funciones como `map()`, `filter()`, `sorted()`
# MAGIC * ✅ **Uso único**: no necesitas reutilizar la función
# MAGIC
# MAGIC ❌ **NO usar** para lógica compleja (usa `def`)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Funciones Útiles con Lambda
# MAGIC
# MAGIC ### 1. `map()` - Aplicar Función a Todos los Elementos
# MAGIC
# MAGIC ```python
# MAGIC precios = [1000, 2000, 3000]
# MAGIC descuento = list(map(lambda x: x * 0.9, precios))
# MAGIC # [900, 1800, 2700]
# MAGIC ```
# MAGIC
# MAGIC ### 2. `filter()` - Filtrar Elementos
# MAGIC
# MAGIC ```python
# MAGIC precios = [500, 1500, 3000, 800, 2000]
# MAGIC caros = list(filter(lambda x: x > 1000, precios))
# MAGIC # [1500, 3000, 2000]
# MAGIC ```
# MAGIC
# MAGIC ### 3. `sorted()` - Ordenar con Clave Personalizada
# MAGIC
# MAGIC ```python
# MAGIC acciones = [('YPF', 5200), ('GGAL', 175), ('MELI', 1450)]
# MAGIC ordenado = sorted(acciones, key=lambda x: x[1])
# MAGIC # Ordena por precio
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Veamos ejemplos financieros con lambda.

# COMMAND ----------

# DBTITLE 1,Código - Funciones Lambda
print("═" * 70)
print("            FUNCIONES LAMBDA EN FINANZAS")
print("═" * 70)

# ===== EJEMPLO 1: CALCULAR COMISIONES CON LAMBDA =====

print("\n🔹 1. Calcular Comisiones con Lambda:")
print("-" * 70)

# Lista de operaciones (montos)
operaciones = [10000, 25000, 50000, 15000, 30000]

# Lambda para calcular comisión del 1.5%
calcular_comision = lambda monto: monto * 0.015

print("Operaciones y sus comisiones:")
for i, monto in enumerate(operaciones, 1):
    comision = calcular_comision(monto)
    print(f"   Operación {i}: ${monto:8,.0f} → Comisión: ${comision:6,.2f}")


# ===== EJEMPLO 2: MAP() - APLICAR DESCUENTO A LISTA DE PRECIOS =====

print("\n\n🔹 2. map() - Aplicar Descuento a Lista de Precios:")
print("-" * 70)

# Precios de acciones
precios_acciones = {
    'YPF': 5200,
    'GGAL': 175,
    'MELI': 1450,
    'PAMP': 850,
    'TGSU2': 320
}

precios = list(precios_acciones.values())

print(f"Precios originales: {precios}")

# Aplicar descuento del 10% con lambda + map
descuento_10 = list(map(lambda x: x * 0.90, precios))

print(f"Con descuento 10%:  {[round(p, 2) for p in descuento_10]}")

# Aplicar incremento del 15% (ajuste por inflación)
ajuste_inflacion = list(map(lambda x: x * 1.15, precios))

print(f"Ajuste inflación:  {[round(p, 2) for p in ajuste_inflacion]}")


# ===== EJEMPLO 3: FILTER() - FILTRAR ACCIONES POR PRECIO =====

print("\n\n🔹 3. filter() - Filtrar Acciones por Criterios:")
print("-" * 70)

# Lista de acciones con precios
acciones = [
    ('YPF', 5200),
    ('GGAL', 175),
    ('MELI', 1450),
    ('PAMP', 850),
    ('TGSU2', 320),
    ('COME', 2.35),
    ('ALUA', 3.15)
]

print("\nAcciones disponibles:")
for ticker, precio in acciones:
    print(f"   {ticker:6s}: ${precio:8,.2f}")

# Filtrar acciones caras (precio > $500)
acciones_caras = list(filter(lambda x: x[1] > 500, acciones))

print("\n▶️ Acciones CARAS (precio > $500):")
for ticker, precio in acciones_caras:
    print(f"   {ticker:6s}: ${precio:8,.2f}")

# Filtrar acciones baratas (precio < $100)
acciones_baratas = list(filter(lambda x: x[1] < 100, acciones))

print("\n▶️ Acciones BARATAS (precio < $100):")
for ticker, precio in acciones_baratas:
    print(f"   {ticker:6s}: ${precio:8,.2f}")

# Filtrar acciones en rango medio ($100 - $1000)
acciones_medias = list(filter(lambda x: 100 <= x[1] <= 1000, acciones))

print("\n▶️ Acciones RANGO MEDIO ($100 - $1000):")
for ticker, precio in acciones_medias:
    print(f"   {ticker:6s}: ${precio:8,.2f}")


# ===== EJEMPLO 4: SORTED() CON KEY LAMBDA =====

print("\n\n🔹 4. sorted() - Ordenar Acciones:")
print("-" * 70)

# Ordenar por precio (ascendente)
acciones_ordenadas_asc = sorted(acciones, key=lambda x: x[1])

print("\nAcciones ordenadas por precio (MENOR a MAYOR):")
for i, (ticker, precio) in enumerate(acciones_ordenadas_asc, 1):
    print(f"   {i}. {ticker:6s}: ${precio:8,.2f}")

# Ordenar por precio (descendente)
acciones_ordenadas_desc = sorted(acciones, key=lambda x: x[1], reverse=True)

print("\nAcciones ordenadas por precio (MAYOR a MENOR):")
for i, (ticker, precio) in enumerate(acciones_ordenadas_desc, 1):
    print(f"   {i}. {ticker:6s}: ${precio:8,.2f}")


# ===== EJEMPLO 5: COMBINAR MAP + FILTER =====

print("\n\n🔹 5. Combinar map() + filter():")
print("-" * 70)

# Calcular rendimiento y filtrar los que superan 10%
rendimientos = [
    ('YPF', 0.156),
    ('GGAL', 0.097),
    ('MELI', 0.116),
    ('PAMP', 0.082),
    ('TGSU2', 0.095)
]

print("Rendimientos:")
for ticker, rend in rendimientos:
    print(f"   {ticker:6s}: {rend:6.2%}")

# Filtrar rendimientos > 10% y convertir a porcentaje
buenos_rendimientos = list(
    map(
        lambda x: (x[0], x[1] * 100),  # Convertir a porcentaje
        filter(lambda x: x[1] > 0.10, rendimientos)  # Filtrar > 10%
    )
)

print("\n▶️ Acciones con rendimiento > 10%:")
for ticker, rend_pct in buenos_rendimientos:
    print(f"   {ticker:6s}: {rend_pct:5.2f}%")

print("\n" + "═" * 70)
print("✅ Funciones lambda dominadas!")
print("═" * 70)

# COMMAND ----------

# DBTITLE 1,Sección - Scope de Variables
# MAGIC %md
# MAGIC
# MAGIC # 🔍 PARTE 4: Scope de Variables
# MAGIC
# MAGIC ## ¿Qué es el Scope?
# MAGIC
# MAGIC El **scope** (alcance) define **dónde** una variable es visible y puede ser usada.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Tipos de Scope
# MAGIC
# MAGIC ### 1. **Local Scope** 🟢
# MAGIC
# MAGIC Variables definidas **dentro** de una función.
# MAGIC
# MAGIC ```python
# MAGIC def calcular():
# MAGIC     x = 10  # Variable LOCAL
# MAGIC     return x
# MAGIC
# MAGIC print(x)  # ERROR: x no existe fuera de la función
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 2. **Global Scope** 🔵
# MAGIC
# MAGIC Variables definidas **fuera** de funciones.
# MAGIC
# MAGIC ```python
# MAGIC tasa_impuesto = 0.15  # Variable GLOBAL
# MAGIC
# MAGIC def calcular_impuesto(ganancia):
# MAGIC     return ganancia * tasa_impuesto  # Puede leer la variable global
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 3. **Modificar Variables Globales**
# MAGIC
# MAGIC Usa la palabra clave `global`:
# MAGIC
# MAGIC ```python
# MAGIC contador = 0
# MAGIC
# MAGIC def incrementar():
# MAGIC     global contador  # Declarar que usamos la variable global
# MAGIC     contador += 1
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Regla LEGB
# MAGIC
# MAGIC Python busca variables en este orden:
# MAGIC
# MAGIC 1. **L**ocal: Dentro de la función
# MAGIC 2. **E**nclosing: En funciones contenedoras
# MAGIC 3. **G**lobal: En el módulo
# MAGIC 4. **B**uilt-in: Funciones integradas de Python
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Veamos ejemplos prácticos con variables financieras.

# COMMAND ----------

# DBTITLE 1,Código - Scope Variables
print("═" * 70)
print("            SCOPE DE VARIABLES")
print("═" * 70)

# ===== EJEMPLO 1: VARIABLE LOCAL =====

print("\n🔹 1. Variable Local:")
print("-" * 70)

def calcular_comision():
    # Variable LOCAL - solo existe dentro de esta función
    tasa_comision = 0.015  # 1.5%
    monto = 100000
    comision = monto * tasa_comision
    return comision

resultado = calcular_comision()
print(f"Comisión calculada: ${resultado:,.2f}")

# Intentar acceder a tasa_comision aquí daría error:
# print(tasa_comision)  # NameError: name 'tasa_comision' is not defined

print("✅ Variable 'tasa_comision' solo existe dentro de la función")


# ===== EJEMPLO 2: VARIABLE GLOBAL =====

print("\n\n🔹 2. Variable Global:")
print("-" * 70)

# Variable GLOBAL - accesible desde cualquier lugar
TASA_IMPUESTO_GANANCIAS = 0.15  # 15% (constante)
TASA_IVA = 0.21  # 21%

def calcular_impuesto_ganancias(ganancia):
    # Puede LEER la variable global
    impuesto = ganancia * TASA_IMPUESTO_GANANCIAS
    return impuesto

def calcular_iva(monto):
    # También puede leer variables globales
    iva = monto * TASA_IVA
    return iva

ganancia_anual = 500000
impuesto = calcular_impuesto_ganancias(ganancia_anual)
print(f"Ganancia: ${ganancia_anual:,.0f}")
print(f"Impuesto a las Ganancias ({TASA_IMPUESTO_GANANCIAS:.0%}): ${impuesto:,.2f}")

monto_operacion = 100000
iva = calcular_iva(monto_operacion)
print(f"\nOperación: ${monto_operacion:,.0f}")
print(f"IVA ({TASA_IVA:.0%}): ${iva:,.2f}")


# ===== EJEMPLO 3: MODIFICAR VARIABLE GLOBAL =====

print("\n\n🔹 3. Modificar Variable Global:")
print("-" * 70)

# Contador global de operaciones
operaciones_realizadas = 0

def registrar_operacion(ticker, cantidad):
    global operaciones_realizadas  # Declarar que modificaremos la variable global
    operaciones_realizadas += 1
    print(f"Operación #{operaciones_realizadas}: Compra de {cantidad} acciones de {ticker}")

print(f"Operaciones iniciales: {operaciones_realizadas}")

registrar_operacion('YPF', 100)
registrar_operacion('GGAL', 200)
registrar_operacion('MELI', 50)

print(f"\nTotal de operaciones realizadas: {operaciones_realizadas}")


# ===== EJEMPLO 4: VARIABLE GLOBAL VS LOCAL =====

print("\n\n🔹 4. Conflicto Local vs Global:")
print("-" * 70)

# Variable global
tipo_cambio = 1000  # Dólar oficial

def convertir_oficial(pesos):
    # Usa la variable global
    dolares = pesos / tipo_cambio
    return dolares

def convertir_blue(pesos):
    # Variable LOCAL con el mismo nombre (NO modifica la global)
    tipo_cambio = 1100  # Dólar blue
    dolares = pesos / tipo_cambio
    return dolares

monto_pesos = 100000

print(f"Monto: ${monto_pesos:,.0f}")
print(f"Tipo de cambio GLOBAL: ${tipo_cambio:,.0f}")

oficial = convertir_oficial(monto_pesos)
print(f"\nConversión oficial: USD {oficial:,.2f}")

blue = convertir_blue(monto_pesos)
print(f"Conversión blue: USD {blue:,.2f}")

print(f"\nTipo de cambio GLOBAL después: ${tipo_cambio:,.0f} (sin cambios)")
print("✅ La variable local NO modificó la global")


# ===== EJEMPLO 5: BUENA PRÁCTICA - CONSTANTES GLOBALES =====

print("\n\n🔹 5. Buena Práctica: Constantes Globales:")
print("-" * 70)

# Constantes financieras argentinas (MAYUSCULAS por convención)
TASA_BONOS_ARGENTINA = 0.25  # 25%
TASA_PLAZO_FIJO = 0.10  # 10% mensual
COMISION_BROKER = 0.015  # 1.5%
IMPUESTO_SELLOS = 0.005  # 0.5%

def calcular_costo_total_operacion(monto):
    """
    Calcula el costo total de una operación incluyendo comisiones e impuestos.
    """
    comision = monto * COMISION_BROKER
    impuesto = monto * IMPUESTO_SELLOS
    costo_total = monto + comision + impuesto
    
    return {
        'monto': monto,
        'comision': comision,
        'impuesto': impuesto,
        'total': costo_total
    }

monto_operacion = 1_000_000
resultado = calcular_costo_total_operacion(monto_operacion)

print(f"Operación:")
print(f"   Monto:            ${resultado['monto']:10,.0f}")
print(f"   Comisión ({COMISION_BROKER:.2%}): ${resultado['comision']:10,.2f}")
print(f"   Imp. Sellos ({IMPUESTO_SELLOS:.2%}):  ${resultado['impuesto']:10,.2f}")
print(f"   {'-'*40}")
print(f"   TOTAL:            ${resultado['total']:10,.2f}")

print("\n✅ Constantes globales mantienen valores consistentes")

print("\n" + "═" * 70)
print("✅ Scope de variables dominado!")
print("═" * 70)

# COMMAND ----------

# DBTITLE 1,Sección - Biblioteca Financiera
# MAGIC %md
# MAGIC
# MAGIC # 📚 PARTE 5: Biblioteca Personal de Funciones Financieras
# MAGIC
# MAGIC ## Tu Caja de Herramientas
# MAGIC
# MAGIC Vamos a crear una **biblioteca de funciones financieras** reutilizables.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ¿Por qué Crear una Biblioteca?
# MAGIC
# MAGIC * ✅ **Reutilización**: Escribe una vez, usa mil veces
# MAGIC * ✅ **Consistencia**: Mismos cálculos en todos tus proyectos
# MAGIC * ✅ **Mantenibilidad**: Corrige un bug en un solo lugar
# MAGIC * ✅ **Profesionalismo**: Código modular y documentado
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Funciones que Vamos a Crear
# MAGIC
# MAGIC ### 🔹 CATEGORÍA 1: RENDIMIENTO
# MAGIC 1. `calcular_rendimiento_simple()` - Rendimiento de una acción
# MAGIC 2. `calcular_rendimiento_compuesto()` - CAGR (Tasa de crecimiento anual compuesta)
# MAGIC 3. `calcular_volatilidad()` - Volatilidad de rendimientos
# MAGIC
# MAGIC ### 🔹 CATEGORÍA 2: VALUACIÓN
# MAGIC 4. `valor_presente()` - Descontar flujos futuros
# MAGIC 5. `valor_futuro()` - Proyectar valor futuro
# MAGIC 6. `calcular_van()` - Valor Actual Neto de proyecto
# MAGIC
# MAGIC ### 🔹 CATEGORÍA 3: RIESGO
# MAGIC 7. `calcular_sharpe_ratio()` - Rendimiento ajustado por riesgo
# MAGIC 8. `calcular_beta()` - Riesgo sistemático
# MAGIC
# MAGIC ### 🔹 CATEGORÍA 4: OPERATORIA
# MAGIC 9. `convertir_pesos_dolares()` - Conversión de divisas
# MAGIC 10. `calcular_comision()` - Comisiones de broker
# MAGIC 11. `calcular_impuesto_ganancias()` - Impuestos sobre ganancias
# MAGIC
# MAGIC ### 🔹 CATEGORÍA 5: PORTAFOLIO
# MAGIC 12. `diversificacion_cartera()` - Métrica de diversificación
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Creemos la biblioteca completa.

# COMMAND ----------

# DBTITLE 1,Código - Biblioteca Financiera
print("═" * 70)
print("            BIBLIOTECA FINANCIERA PERSONAL")
print("═" * 70)
print("\n📚 Creando biblioteca de 12 funciones financieras...\n")

import math
import numpy as np

# =============================================================================
# CATEGORÍA 1: RENDIMIENTO
# =============================================================================

def calcular_rendimiento_simple(precio_inicial, precio_final):
    """
    Calcula el rendimiento simple de una inversión.
    
    Fórmula: R = (Pf - Pi) / Pi
    
    Parámetros:
    -----------
    precio_inicial : float
        Precio de compra
    precio_final : float
        Precio de venta
    
    Retorna:
    --------
    float : Rendimiento (decimal)
    """
    return (precio_final - precio_inicial) / precio_inicial


def calcular_rendimiento_compuesto(precio_inicial, precio_final, periodos):
    """
    Calcula la tasa de crecimiento anual compuesta (CAGR).
    
    Fórmula: CAGR = (Vf / Vi)^(1/n) - 1
    
    Parámetros:
    -----------
    precio_inicial : float
        Valor inicial
    precio_final : float
        Valor final
    periodos : int
        Número de períodos (generalmente años)
    
    Retorna:
    --------
    float : CAGR (decimal)
    """
    return (precio_final / precio_inicial) ** (1 / periodos) - 1


def calcular_volatilidad(rendimientos):
    """
    Calcula la volatilidad (desviación estándar) de una serie de rendimientos.
    
    Parámetros:
    -----------
    rendimientos : list o array
        Serie de rendimientos (decimales)
    
    Retorna:
    --------
    float : Volatilidad (desviación estándar)
    """
    return np.std(rendimientos, ddof=1)  # ddof=1 para muestra


# =============================================================================
# CATEGORÍA 2: VALUACIÓN
# =============================================================================

def valor_presente(flujo_futuro, tasa, periodos):
    """
    Calcula el valor presente de un flujo futuro.
    
    Fórmula: VP = VF / (1 + r)^n
    
    Parámetros:
    -----------
    flujo_futuro : float
        Flujo de efectivo futuro
    tasa : float
        Tasa de descuento (decimal)
    periodos : int
        Número de períodos
    
    Retorna:
    --------
    float : Valor presente
    """
    return flujo_futuro / ((1 + tasa) ** periodos)


def valor_futuro(monto_inicial, tasa, periodos):
    """
    Calcula el valor futuro de una inversión.
    
    Fórmula: VF = VP * (1 + r)^n
    
    Parámetros:
    -----------
    monto_inicial : float
        Capital inicial
    tasa : float
        Tasa de interés (decimal)
    periodos : int
        Número de períodos
    
    Retorna:
    --------
    float : Valor futuro
    """
    return monto_inicial * ((1 + tasa) ** periodos)


def calcular_van(flujos, tasa):
    """
    Calcula el Valor Actual Neto (VAN) de un proyecto.
    
    Parámetros:
    -----------
    flujos : list
        Lista de flujos de efectivo (primer elemento = inversión inicial negativa)
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


# =============================================================================
# CATEGORÍA 3: RIESGO
# =============================================================================

def calcular_sharpe_ratio(rendimientos, tasa_libre_riesgo=0.05):
    """
    Calcula el ratio de Sharpe (rendimiento ajustado por riesgo).
    
    Fórmula: Sharpe = (Rp - Rf) / σp
    
    Parámetros:
    -----------
    rendimientos : list o array
        Serie de rendimientos del portafolio
    tasa_libre_riesgo : float, opcional
        Tasa libre de riesgo anualizada (default: 0.05 = 5%)
    
    Retorna:
    --------
    float : Ratio de Sharpe
    """
    rendimiento_promedio = np.mean(rendimientos)
    volatilidad = np.std(rendimientos, ddof=1)
    
    if volatilidad == 0:
        return 0
    
    return (rendimiento_promedio - tasa_libre_riesgo) / volatilidad


def calcular_beta(rendimientos_activo, rendimientos_mercado):
    """
    Calcula el Beta (riesgo sistemático) de un activo.
    
    Fórmula: β = Cov(Ra, Rm) / Var(Rm)
    
    Parámetros:
    -----------
    rendimientos_activo : list o array
        Rendimientos del activo
    rendimientos_mercado : list o array
        Rendimientos del mercado (ej: Merval)
    
    Retorna:
    --------
    float : Beta del activo
    """
    covarianza = np.cov(rendimientos_activo, rendimientos_mercado)[0, 1]
    varianza_mercado = np.var(rendimientos_mercado, ddof=1)
    
    if varianza_mercado == 0:
        return 0
    
    return covarianza / varianza_mercado


# =============================================================================
# CATEGORÍA 4: OPERATORIA
# =============================================================================

def convertir_pesos_dolares(pesos, tipo_cambio):
    """
    Convierte pesos argentinos a dólares.
    
    Parámetros:
    -----------
    pesos : float
        Monto en pesos
    tipo_cambio : float
        Tipo de cambio (pesos por dólar)
    
    Retorna:
    --------
    float : Monto en dólares
    """
    return pesos / tipo_cambio


def calcular_comision(monto, porcentaje_comision=0.015):
    """
    Calcula la comisión de una operación.
    
    Parámetros:
    -----------
    monto : float
        Monto de la operación
    porcentaje_comision : float, opcional
        Porcentaje de comisión (default: 0.015 = 1.5%)
    
    Retorna:
    --------
    float : Comisión a pagar
    """
    return monto * porcentaje_comision


def calcular_impuesto_ganancias(ganancia, tasa_impuesto=0.15):
    """
    Calcula el impuesto a las ganancias.
    
    Parámetros:
    -----------
    ganancia : float
        Ganancia obtenida
    tasa_impuesto : float, opcional
        Tasa del impuesto (default: 0.15 = 15%)
    
    Retorna:
    --------
    float : Impuesto a pagar
    """
    if ganancia <= 0:
        return 0
    return ganancia * tasa_impuesto


# =============================================================================
# CATEGORÍA 5: PORTAFOLIO
# =============================================================================

def diversificacion_cartera(pesos_por_activo):
    """
    Calcula el índice de Herfindahl-Hirschman de concentración/diversificación.
    
    Un valor cercano a 1 indica alta concentración.
    Un valor cercano a 0 indica alta diversificación.
    
    Parámetros:
    -----------
    pesos_por_activo : list
        Lista de pesos/porcentajes de cada activo (deben sumar 1.0)
    
    Retorna:
    --------
    float : Índice HHI (0 = diversificado, 1 = concentrado)
    """
    return sum([peso**2 for peso in pesos_por_activo])


print("✅ Biblioteca creada exitosamente!\n")
print("Funciones disponibles:")
print("\n🔹 RENDIMIENTO:")
print("   1. calcular_rendimiento_simple()")
print("   2. calcular_rendimiento_compuesto()")
print("   3. calcular_volatilidad()")

print("\n🔹 VALUACIÓN:")
print("   4. valor_presente()")
print("   5. valor_futuro()")
print("   6. calcular_van()")

print("\n🔹 RIESGO:")
print("   7. calcular_sharpe_ratio()")
print("   8. calcular_beta()")

print("\n🔹 OPERATORIA:")
print("   9. convertir_pesos_dolares()")
print("   10. calcular_comision()")
print("   11. calcular_impuesto_ganancias()")

print("\n🔹 PORTAFOLIO:")
print("   12. diversificacion_cartera()")

print("\n" + "═" * 70)
print("✅ Biblioteca financiera personal lista para usar!")
print("═" * 70)

# COMMAND ----------

# DBTITLE 1,Sección - Módulos Built-in
# MAGIC %md
# MAGIC
# MAGIC # 📦 PARTE 6: Módulos Built-in de Python
# MAGIC
# MAGIC ## ¿Qué son los Módulos?
# MAGIC
# MAGIC Un **módulo** es un archivo de Python con funciones, clases y variables que puedes **importar** y usar.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Módulos Útiles para Finanzas
# MAGIC
# MAGIC ### 1. `math` - Funciones Matemáticas
# MAGIC
# MAGIC ```python
# MAGIC import math
# MAGIC
# MAGIC math.log(1.10)  # Logaritmo natural (para rendimientos logarítmicos)
# MAGIC math.exp(0.05)  # Exponencial
# MAGIC math.sqrt(0.04)  # Raíz cuadrada (volatilidad)
# MAGIC ```
# MAGIC
# MAGIC ### 2. `random` - Números Aleatorios
# MAGIC
# MAGIC ```python
# MAGIC import random
# MAGIC
# MAGIC random.random()  # Número entre 0 y 1
# MAGIC random.uniform(1000, 5000)  # Número entre 1000 y 5000
# MAGIC random.gauss(0, 0.02)  # Distribución normal (para simular rendimientos)
# MAGIC ```
# MAGIC
# MAGIC ### 3. `datetime` - Fechas y Tiempos
# MAGIC
# MAGIC ```python
# MAGIC from datetime import datetime, timedelta
# MAGIC
# MAGIC hoy = datetime.now()
# MAGIC vencimiento = datetime(2030, 12, 31)
# MAGIC dias_restantes = (vencimiento - hoy).days
# MAGIC ```
# MAGIC
# MAGIC ### 4. `collections` - Estructuras de Datos
# MAGIC
# MAGIC ```python
# MAGIC from collections import Counter, defaultdict
# MAGIC
# MAGIC # Contar frecuencias
# MAGIC acciones = ['YPF', 'GGAL', 'YPF', 'MELI', 'YPF']
# MAGIC contador = Counter(acciones)  # Counter({'YPF': 3, 'GGAL': 1, 'MELI': 1})
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Usemos estos módulos en casos financieros.

# COMMAND ----------

# DBTITLE 1,Código - Módulos Built-in
print("═" * 70)
print("            MÓDULOS BUILT-IN PARA FINANZAS")
print("═" * 70)

import math
import random
from datetime import datetime, timedelta, date
from collections import Counter, defaultdict

# ===== 1. MATH - RENDIMIENTOS LOGARÍTMICOS =====

print("\n🔹 1. math - Rendimientos Logarítmicos:")
print("-" * 70)

precio_inicial = 1000
precio_final = 1150

# Rendimiento simple
rendimiento_simple = (precio_final / precio_inicial) - 1

# Rendimiento logarítmico (mejor para periodos largos)
rendimiento_log = math.log(precio_final / precio_inicial)

print(f"Precio inicial: ${precio_inicial:,.0f}")
print(f"Precio final: ${precio_final:,.0f}")
print(f"\nRendimiento simple: {rendimiento_simple:.4f} ({rendimiento_simple * 100:.2f}%)")
print(f"Rendimiento logarítmico: {rendimiento_log:.4f} ({rendimiento_log * 100:.2f}%)")

# Ventaja de log: son aditivos
print("\n✅ Ventaja: Los rendimientos log se pueden SUMAR")

# Volatilidad usando raíz cuadrada
varianza = 0.04  # 4% de varianza
volatilidad = math.sqrt(varianza)
print(f"\nVarianza: {varianza:.4f}")
print(f"Volatilidad (√varianza): {volatilidad:.4f} ({volatilidad * 100:.2f}%)")


# ===== 2. RANDOM - SIMULACIÓN DE PRECIOS =====

print("\n\n🔹 2. random - Simulación Monte Carlo de Precios:")
print("-" * 70)

random.seed(42)  # Reproducibilidad

precio_inicial = 5000
rendimiento_esperado = 0.001  # 0.1% diario
volatilidad_diaria = 0.02  # 2% diario
dias_simulados = 30

print(f"Simulando {dias_simulados} días de precios YPF...\n")
print(f"Precio inicial: ${precio_inicial:,.0f}")
print(f"Rendimiento esperado: {rendimiento_esperado:.2%} diario")
print(f"Volatilidad: {volatilidad_diaria:.1%} diaria\n")

precios_simulados = [precio_inicial]
precio_actual = precio_inicial

for dia in range(1, dias_simulados + 1):
    # Generar rendimiento aleatorio con distribución normal
    rendimiento_dia = random.gauss(rendimiento_esperado, volatilidad_diaria)
    precio_actual = precio_actual * (1 + rendimiento_dia)
    precios_simulados.append(precio_actual)
    
    if dia <= 5 or dia > (dias_simulados - 5):
        print(f"Día {dia:2d}: ${precio_actual:7,.2f} ({rendimiento_dia:+.2%})")
    elif dia == 6:
        print("   ...")

precio_final_sim = precios_simulados[-1]
rendimiento_total = (precio_final_sim / precio_inicial) - 1

print(f"\nPrecio final simulado: ${precio_final_sim:,.2f}")
print(f"Rendimiento total: {rendimiento_total:+.2%}")
print(f"Precio máximo: ${max(precios_simulados):,.2f}")
print(f"Precio mínimo: ${min(precios_simulados):,.2f}")


# ===== 3. DATETIME - ANÁLISIS DE VENCIMIENTOS =====

print("\n\n🔹 3. datetime - Análisis de Vencimientos de Bonos:")
print("-" * 70)

# Fecha de hoy
hoy = datetime.now()

# Bonos argentinos con diferentes vencimientos
bonos = [
    {'ticker': 'AL30', 'vencimiento': datetime(2030, 7, 9)},
    {'ticker': 'AL35', 'vencimiento': datetime(2035, 7, 9)},
    {'ticker': 'GD30', 'vencimiento': datetime(2030, 7, 9)},
    {'ticker': 'AE38', 'vencimiento': datetime(2038, 12, 31)}
]

print(f"Fecha actual: {hoy.strftime('%d/%m/%Y')}\n")
print("Análisis de vencimientos:\n")

for bono in bonos:
    vencimiento = bono['vencimiento']
    dias_restantes = (vencimiento - hoy).days
    anios_restantes = dias_restantes / 365.25
    
    print(f"{bono['ticker']}:")
    print(f"   Vencimiento: {vencimiento.strftime('%d/%m/%Y')}")
    print(f"   Días restantes: {dias_restantes:,}")
    print(f"   Años restantes: {anios_restantes:.2f}")
    print()

# Calcular días hábiles (aproximado)
print("Días hábiles aproximados (excl. sáb/dom):")
bono_30 = bonos[0]
dias_totales = (bono_30['vencimiento'] - hoy).days
dias_habiles = dias_totales * 5 / 7  # Aproximación
print(f"{bono_30['ticker']}: {dias_habiles:,.0f} días hábiles")


# ===== 4. COLLECTIONS - ANÁLISIS DE PORTAFOLIO =====

print("\n\n🔹 4. collections - Análisis de Operaciones:")
print("-" * 70)

# Operaciones realizadas en el día
operaciones = [
    'YPF', 'GGAL', 'YPF', 'MELI', 'YPF', 'GGAL', 'PAMP', 
    'YPF', 'MELI', 'YPF', 'TGSU2', 'YPF'
]

# Contar frecuencia de cada acción
contador = Counter(operaciones)

print(f"Total de operaciones: {len(operaciones)}\n")
print("Frecuencia por ticker:")

for ticker, cantidad in contador.most_common():
    porcentaje = (cantidad / len(operaciones)) * 100
    barra = '█' * int(porcentaje / 2)
    print(f"{ticker:6s}: {cantidad:2d} operaciones ({porcentaje:5.1f}%) {barra}")

print(f"\nAcciones más operadas: {contador.most_common(1)[0][0]}")

# defaultdict para agrupar por sector
print("\n\n🔹 5. defaultdict - Agrupar por Sector:")
print("-" * 70)

portafolio = [
    ('YPF', 'Energía', 520000),
    ('GGAL', 'Bancario', 87500),
    ('MELI', 'Tecnología', 72500),
    ('PAMP', 'Energía', 127500),
    ('TGSU2', 'Energía', 96000)
]

# Agrupar valores por sector
sector_valores = defaultdict(float)

for ticker, sector, valor in portafolio:
    sector_valores[sector] += valor

print("Valor invertido por sector:\n")
for sector, valor in sorted(sector_valores.items(), key=lambda x: x[1], reverse=True):
    print(f"{sector:12s}: ${valor:10,.0f}")

total = sum(sector_valores.values())
print(f"{'-'*25}")
print(f"{'TOTAL':12s}: ${total:10,.0f}")

print("\n" + "═" * 70)
print("✅ Módulos built-in dominados!")
print("═" * 70)

# COMMAND ----------

# DBTITLE 1,Sección - Caso Integrado
# MAGIC %md
# MAGIC
# MAGIC # 🎯 CASO INTEGRADO: Análisis Completo de Cartera
# MAGIC
# MAGIC ## Objetivo
# MAGIC
# MAGIC **Integrar TODAS las funciones** que creamos en un análisis profesional completo.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Escenario
# MAGIC
# MAGIC **Juan Inversor** tiene un portafolio argentino con 5 acciones.
# MAGIC
# MAGIC Quiere saber:
# MAGIC 1. ¿Cuál es el **rendimiento** de cada acción?
# MAGIC 2. ¿Cuál es el **rendimiento del portafolio**?
# MAGIC 3. ¿Cuál es la **volatilidad** (riesgo)?
# MAGIC 4. ¿El portafolio está bien **diversificado**?
# MAGIC 5. ¿Cuánto pagó en **comisiones**?
# MAGIC 6. ¿Cuánto debe pagar de **impuestos**?
# MAGIC 7. ¿Cuánto valdrá su inversión en **5 años**?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Datos del Portafolio
# MAGIC
# MAGIC | Ticker | Precio Compra | Precio Actual | Cantidad | Peso |
# MAGIC |--------|---------------|---------------|----------|------|
# MAGIC | YPF    | $4,500        | $5,200        | 100      | 35%  |
# MAGIC | GGAL   | $150          | $175          | 500      | 25%  |
# MAGIC | MELI   | $1,300        | $1,450        | 50       | 20%  |
# MAGIC | PAMP   | $700          | $850          | 150      | 15%  |
# MAGIC | TGSU2  | $280          | $320          | 300      | 5%   |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Usemos nuestra biblioteca de funciones para el análisis completo.

# COMMAND ----------

# DBTITLE 1,Código - Caso Integrado
print("═" * 80)
print("                 CASO INTEGRADO: ANÁLISIS DE CARTERA")
print("═" * 80)
print("\n💼 Cliente: Juan Inversor")
print("📅 Fecha de análisis: {}".format(datetime.now().strftime('%d/%m/%Y')))

# ===== DATOS DEL PORTAFOLIO =====

portafolio = [
    {'ticker': 'YPF', 'precio_compra': 4500, 'precio_actual': 5200, 'cantidad': 100, 'peso': 0.35},
    {'ticker': 'GGAL', 'precio_compra': 150, 'precio_actual': 175, 'cantidad': 500, 'peso': 0.25},
    {'ticker': 'MELI', 'precio_compra': 1300, 'precio_actual': 1450, 'cantidad': 50, 'peso': 0.20},
    {'ticker': 'PAMP', 'precio_compra': 700, 'precio_actual': 850, 'cantidad': 150, 'peso': 0.15},
    {'ticker': 'TGSU2', 'precio_compra': 280, 'precio_actual': 320, 'cantidad': 300, 'peso': 0.05}
]

print("\n" + "=" * 80)
print("1️⃣ COMPOSICIÓN DEL PORTAFOLIO")
print("=" * 80)

inversion_total = 0
valor_actual_total = 0

for accion in portafolio:
    inversion = accion['precio_compra'] * accion['cantidad']
    valor_actual = accion['precio_actual'] * accion['cantidad']
    
    accion['inversion'] = inversion
    accion['valor_actual'] = valor_actual
    
    inversion_total += inversion
    valor_actual_total += valor_actual
    
    print(f"\n{accion['ticker']:6s}:")
    print(f"   Cantidad:       {accion['cantidad']:4d} acciones")
    print(f"   Precio compra:  ${accion['precio_compra']:7,.2f}")
    print(f"   Precio actual:  ${accion['precio_actual']:7,.2f}")
    print(f"   Inversión:      ${inversion:10,.0f}")
    print(f"   Valor actual:   ${valor_actual:10,.0f}")
    print(f"   Peso:           {accion['peso']:5.1%}")

print(f"\n{'='*80}")
print(f"TOTALES:")
print(f"   Inversión total:  ${inversion_total:12,.0f}")
print(f"   Valor actual:     ${valor_actual_total:12,.0f}")
print(f"   Ganancia bruta:   ${valor_actual_total - inversion_total:12,.0f}")


# ===== 2. RENDIMIENTOS INDIVIDUALES =====

print("\n\n" + "=" * 80)
print("2️⃣ RENDIMIENTOS INDIVIDUALES")
print("=" * 80)

rendimientos = []

for accion in portafolio:
    # Usar nuestra función calcular_rendimiento_simple()
    rendimiento = calcular_rendimiento_simple(accion['precio_compra'], accion['precio_actual'])
    accion['rendimiento'] = rendimiento
    rendimientos.append(rendimiento)
    
    ganancia = accion['valor_actual'] - accion['inversion']
    
    print(f"\n{accion['ticker']:6s}: {rendimiento:+7.2%}")
    print(f"   Ganancia: ${ganancia:10,.0f}")
    
    if rendimiento > 0.15:
        print(f"   ✅ ¡Excelente rendimiento!")
    elif rendimiento > 0.05:
        print(f"   🟢 Buen rendimiento")
    else:
        print(f"   🟡 Rendimiento moderado")


# ===== 3. RENDIMIENTO DEL PORTAFOLIO =====

print("\n\n" + "=" * 80)
print("3️⃣ RENDIMIENTO DEL PORTAFOLIO")
print("=" * 80)

# Calcular rendimiento ponderado
rendimiento_portafolio = sum([accion['rendimiento'] * accion['peso'] for accion in portafolio])

print(f"\nRendimiento del portafolio (ponderado): {rendimiento_portafolio:+.2%}")
print(f"\nGanancia total: ${valor_actual_total - inversion_total:,.0f}")

if rendimiento_portafolio > 0.10:
    print(f"✅ El portafolio superó el 10% de rendimiento objetivo")
else:
    print(f"🟡 El portafolio está por debajo del 10% objetivo")


# ===== 4. VOLATILIDAD (RIESGO) =====

print("\n\n" + "=" * 80)
print("4️⃣ VOLATILIDAD Y RIESGO")
print("=" * 80)

# Usar nuestra función calcular_volatilidad()
volatilidad = calcular_volatilidad(rendimientos)

print(f"\nVolatilidad del portafolio: {volatilidad:.2%}")

if volatilidad < 0.10:
    print("✅ Riesgo BAJO - Portafolio conservador")
elif volatilidad < 0.20:
    print("🟡 Riesgo MODERADO - Portafolio balanceado")
else:
    print("⚠️ Riesgo ALTO - Portafolio agresivo")


# ===== 5. RATIO DE SHARPE =====

print("\n\n" + "=" * 80)
print("5️⃣ RATIO DE SHARPE (Rendimiento Ajustado por Riesgo)")
print("=" * 80)

# Usar nuestra función calcular_sharpe_ratio()
tasa_libre_riesgo = 0.05  # 5% anual (bonos del tesoro)
sharpe = calcular_sharpe_ratio(rendimientos, tasa_libre_riesgo)

print(f"\nRatio de Sharpe: {sharpe:.3f}")
print(f"Tasa libre de riesgo: {tasa_libre_riesgo:.0%}")

if sharpe > 1.0:
    print("✅ EXCELENTE - El portafolio ofrece buen rendimiento por unidad de riesgo")
elif sharpe > 0.5:
    print("🟢 BUENO - Rendimiento aceptable ajustado por riesgo")
else:
    print("⚠️ BAJO - Considerar rebalanceo")


# ===== 6. DIVERSIFICACIÓN =====

print("\n\n" + "=" * 80)
print("6️⃣ ANÁLISIS DE DIVERSIFICACIÓN")
print("=" * 80)

# Usar nuestra función diversificacion_cartera()
pesos = [accion['peso'] for accion in portafolio]
hhi = diversificacion_cartera(pesos)

print(f"\nÍndice Herfindahl-Hirschman (HHI): {hhi:.4f}")
print(f"Número de activos: {len(portafolio)}")

if hhi < 0.15:
    print("✅ ALTA diversificación - Riesgo bien distribuido")
elif hhi < 0.25:
    print("🟡 MODERADA diversificación - Aceptable")
else:
    print("⚠️ BAJA diversificación - Portafolio concentrado")

print(f"\nDistribución de pesos:")
for accion in sorted(portafolio, key=lambda x: x['peso'], reverse=True):
    barra = '█' * int(accion['peso'] * 100 / 2)
    print(f"   {accion['ticker']:6s}: {accion['peso']:5.1%} {barra}")


# ===== 7. COSTOS DE OPERACIÓN =====

print("\n\n" + "=" * 80)
print("7️⃣ COSTOS DE OPERACIÓN")
print("=" * 80)

# Calcular comisiones usando nuestra función calcular_comision()
total_operado = valor_actual_total
comision_total = calcular_comision(total_operado, 0.015)  # 1.5%

print(f"\nMonto operado: ${total_operado:,.0f}")
print(f"Comisión (1.5%): ${comision_total:,.2f}")


# ===== 8. IMPUESTOS =====

print("\n\n" + "=" * 80)
print("8️⃣ IMPUESTOS A LAS GANANCIAS")
print("=" * 80)

ganancia_bruta = valor_actual_total - inversion_total

# Calcular impuesto usando nuestra función calcular_impuesto_ganancias()
impuesto = calcular_impuesto_ganancias(ganancia_bruta, 0.15)  # 15%

ganancia_neta = ganancia_bruta - impuesto - comision_total

print(f"\nGanancia bruta:     ${ganancia_bruta:10,.0f}")
print(f"Impuestos (15%):    ${impuesto:10,.2f}")
print(f"Comisiones:         ${comision_total:10,.2f}")
print(f"{'-'*40}")
print(f"Ganancia NETA:      ${ganancia_neta:10,.2f}")

rendimiento_neto = ganancia_neta / inversion_total
print(f"\nRendimiento NETO (después de costos): {rendimiento_neto:+.2%}")


# ===== 9. PROYECCIÓN FUTURA =====

print("\n\n" + "=" * 80)
print("9️⃣ PROYECCIÓN A 5 AÑOS")
print("=" * 80)

# Usar nuestra función valor_futuro()
tasa_crecimiento_esperado = 0.12  # 12% anual
periodos = 5

valor_futuro_proyectado = valor_futuro(valor_actual_total, tasa_crecimiento_esperado, periodos)

print(f"\nValor actual del portafolio: ${valor_actual_total:,.0f}")
print(f"Tasa de crecimiento esperado: {tasa_crecimiento_esperado:.0%} anual")
print(f"Período: {periodos} años")
print(f"\nValor proyectado (5 años): ${valor_futuro_proyectado:,.0f}")

ganancia_proyectada = valor_futuro_proyectado - valor_actual_total
print(f"Ganancia proyectada: ${ganancia_proyectada:,.0f}")


# ===== RESUMEN EJECUTIVO =====

print("\n\n" + "═" * 80)
print("                           RESUMEN EJECUTIVO")
print("═" * 80)

print(f"""\n📈 PORTAFOLIO DE JUAN INVERSOR

💰 INVERSIÓN Y VALOR:
   Inversión inicial:        ${inversion_total:12,.0f}
   Valor actual:             ${valor_actual_total:12,.0f}
   Ganancia bruta:           ${ganancia_bruta:12,.0f}
   Ganancia neta:            ${ganancia_neta:12,.2f}

📉 RENDIMIENTO:
   Rendimiento bruto:        {rendimiento_portafolio:+13.2%}
   Rendimiento neto:         {rendimiento_neto:+13.2%}
   Volatilidad:              {volatilidad:14.2%}
   Ratio Sharpe:             {sharpe:14.3f}

🎯 DIVERSIFICACIÓN:
   Número de activos:        {len(portafolio):14d}
   Índice HHI:               {hhi:14.4f}
   Evaluación:               {'ALTA diversificación' if hhi < 0.15 else 'MODERADA' if hhi < 0.25 else 'BAJA'}

💸 COSTOS:
   Comisiones:               ${comision_total:12,.2f}
   Impuestos:                ${impuesto:12,.2f}
   Costos totales:           ${comision_total + impuesto:12,.2f}

🔮 PROYECCIÓN (5 años al {tasa_crecimiento_esperado:.0%}):
   Valor proyectado:         ${valor_futuro_proyectado:12,.0f}
   Ganancia proyectada:      ${ganancia_proyectada:12,.0f}
""")

print("═" * 80)
print("✅ Análisis completo finalizado usando TODAS nuestras funciones!")
print("═" * 80)

# COMMAND ----------

# DBTITLE 1,Sección - Ejercicios Prácticos
# MAGIC %md
# MAGIC
# MAGIC # 🏋️ EJERCICIOS PRÁCTICOS
# MAGIC
# MAGIC ¡Hora de practicar! Resuelve estos ejercicios usando las funciones que aprendiste.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Ejercicio 1: Función de Duración de Bonos 📊
# MAGIC
# MAGIC **Objetivo**: Crear una función que calcule la duración de Macaulay de un bono.
# MAGIC
# MAGIC **Fórmula**:
# MAGIC $$Duration = \frac{\sum_{t=1}^{n} t \times \frac{C_t}{(1+r)^t}}{Precio}$$
# MAGIC
# MAGIC **Requisitos**:
# MAGIC - Función: `calcular_duracion_bono(cupon, valor_nominal, tasa, periodos)`
# MAGIC - Parámetros:
# MAGIC   * `cupon`: Pago de cupón anual
# MAGIC   * `valor_nominal`: Valor nominal del bono
# MAGIC   * `tasa`: Tasa de descuento
# MAGIC   * `periodos`: Número de períodos hasta vencimiento
# MAGIC - Retorna: Duración en años
# MAGIC
# MAGIC **Ejemplo**:
# MAGIC ```python
# MAGIC duracion = calcular_duracion_bono(cupon=50, valor_nominal=1000, tasa=0.05, periodos=5)
# MAGIC print(f"Duración: {duracion:.2f} años")
# MAGIC ```
# MAGIC
# MAGIC **Ayuda**: La duración mide la sensibilidad del precio del bono a cambios en tasas.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Ejercicio 2: TIR de Flujos de Caja 💵
# MAGIC
# MAGIC **Objetivo**: Crear una función que calcule la Tasa Interna de Retorno (TIR) iterativamente.
# MAGIC
# MAGIC **Requisitos**:
# MAGIC - Función: `calcular_tir(flujos, aproximacion=0.1, max_iteraciones=1000)`
# MAGIC - Parámetros:
# MAGIC   * `flujos`: Lista de flujos (primer elemento = inversión inicial negativa)
# MAGIC   * `aproximacion`: Valor inicial para iterar
# MAGIC   * `max_iteraciones`: Máximo de intentos
# MAGIC - Retorna: TIR como decimal
# MAGIC
# MAGIC **Ejemplo**:
# MAGIC ```python
# MAGIC flujos = [-10000, 3000, 4000, 5000, 3000]
# MAGIC tir = calcular_tir(flujos)
# MAGIC print(f"TIR: {tir:.2%}")
# MAGIC ```
# MAGIC
# MAGIC **Ayuda**: Usa un bucle `while` para encontrar la tasa donde VAN = 0.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Ejercicio 3: Simulación Monte Carlo 🎲
# MAGIC
# MAGIC **Objetivo**: Crear una función que simule precios futuros con Monte Carlo.
# MAGIC
# MAGIC **Requisitos**:
# MAGIC - Función: `simular_precios_monte_carlo(precio_inicial, rendimiento, volatilidad, dias, simulaciones)`
# MAGIC - Parámetros:
# MAGIC   * `precio_inicial`: Precio de partida
# MAGIC   * `rendimiento`: Rendimiento esperado diario
# MAGIC   * `volatilidad`: Volatilidad diaria
# MAGIC   * `dias`: Días a simular
# MAGIC   * `simulaciones`: Número de trayectorias
# MAGIC - Retorna: Lista de precios finales de cada simulación
# MAGIC
# MAGIC **Ejemplo**:
# MAGIC ```python
# MAGIC resultados = simular_precios_monte_carlo(
# MAGIC     precio_inicial=5000,
# MAGIC     rendimiento=0.001,
# MAGIC     volatilidad=0.02,
# MAGIC     dias=30,
# MAGIC     simulaciones=1000
# MAGIC )
# MAGIC
# MAGIC precio_promedio = sum(resultados) / len(resultados)
# MAGIC print(f"Precio promedio: ${precio_promedio:,.2f}")
# MAGIC ```
# MAGIC
# MAGIC **Ayuda**: Usa `random.gauss()` para generar rendimientos aleatorios.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Ejercicio 4: Value at Risk (VaR) ⚠️
# MAGIC
# MAGIC **Objetivo**: Crear una función que calcule el VaR de un portafolio.
# MAGIC
# MAGIC **Requisitos**:
# MAGIC - Función: `calcular_var(rendimientos, nivel_confianza=0.95, valor_portafolio=1000000)`
# MAGIC - Parámetros:
# MAGIC   * `rendimientos`: Lista de rendimientos históricos
# MAGIC   * `nivel_confianza`: Nivel de confianza (0.90, 0.95, 0.99)
# MAGIC   * `valor_portafolio`: Valor actual del portafolio
# MAGIC - Retorna: VaR en pesos
# MAGIC
# MAGIC **Ejemplo**:
# MAGIC ```python
# MAGIC rendimientos = [0.02, -0.01, 0.03, -0.02, 0.01, -0.03, 0.02]
# MAGIC var = calcular_var(rendimientos, nivel_confianza=0.95, valor_portafolio=1000000)
# MAGIC print(f"VaR (95%): ${var:,.0f}")
# MAGIC ```
# MAGIC
# MAGIC **Ayuda**: El VaR es el percentil correspondiente al nivel de confianza.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Ejercicio 5: Biblioteca de Funciones de Bonos 📚
# MAGIC
# MAGIC **Objetivo**: Crear un módulo completo con funciones para análisis de bonos.
# MAGIC
# MAGIC **Funciones a implementar**:
# MAGIC
# MAGIC 1. `precio_bono(cupon, valor_nominal, tasa, periodos)`
# MAGIC    - Calcula el precio de un bono
# MAGIC
# MAGIC 2. `ytm_bono(precio, cupon, valor_nominal, periodos)`
# MAGIC    - Calcula el Yield to Maturity (YTM)
# MAGIC
# MAGIC 3. `convexidad_bono(cupon, valor_nominal, tasa, periodos)`
# MAGIC    - Calcula la convexidad del bono
# MAGIC
# MAGIC 4. `precio_modificado_tasa(precio, duracion, cambio_tasa)`
# MAGIC    - Estima cambio de precio por cambio en tasas
# MAGIC
# MAGIC 5. `analisis_completo_bono(cupon, valor_nominal, tasa, periodos)`
# MAGIC    - Retorna diccionario con precio, duración, convexidad, YTM
# MAGIC
# MAGIC **Ejemplo de uso**:
# MAGIC ```python
# MAGIC analisis = analisis_completo_bono(
# MAGIC     cupon=50,
# MAGIC     valor_nominal=1000,
# MAGIC     tasa=0.05,
# MAGIC     periodos=10
# MAGIC )
# MAGIC
# MAGIC print("Análisis del Bono:")
# MAGIC for metrica, valor in analisis.items():
# MAGIC     print(f"   {metrica}: {valor}")
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎯 Consejo
# MAGIC
# MAGIC Recuerda:
# MAGIC 1. Usa **docstrings** para documentar
# MAGIC 2. Valida **parámetros** (ej: tasa no negativa)
# MAGIC 3. Maneja **excepciones** (ej: división por cero)
# MAGIC 4. Escribe **ejemplos** de uso
# MAGIC 5. Prueba con **datos reales**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ¡Éxito con los ejercicios! 🚀

# COMMAND ----------

# DBTITLE 1,Sección - Consultas Genie
# MAGIC %md
# MAGIC
# MAGIC # 🤖 PRÁCTICA CON GENIE
# MAGIC
# MAGIC ## ¿Qué es Genie?
# MAGIC
# MAGIC **Genie** es el asistente conversacional de Databricks que te permite hacer preguntas en **lenguaje natural** sobre tus datos.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Consultas de Ejemplo sobre Funciones y Módulos
# MAGIC
# MAGIC Prueba estas consultas en Genie para profundizar tu entendimiento:
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Consulta 1: Documentación de Funciones
# MAGIC
# MAGIC **Pregunta a Genie**:
# MAGIC
# MAGIC > "¿Cómo crear una función en Python que calcule el valor presente de flujos futuros con diferentes tasas de descuento por período?"
# MAGIC
# MAGIC **Lo que aprenderás**:
# MAGIC - Sintaxis de funciones con múltiples parámetros
# MAGIC - Cómo manejar listas de tasas variables
# MAGIC - Buenas prácticas de documentación
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Consulta 2: Módulos Financieros
# MAGIC
# MAGIC **Pregunta a Genie**:
# MAGIC
# MAGIC > "¿Qué módulos de Python son útiles para análisis financiero y cómo puedo usarlos para calcular rendimientos logarítmicos y volatilidad?"
# MAGIC
# MAGIC **Lo que aprenderás**:
# MAGIC - Módulos como `math`, `numpy`, `pandas`
# MAGIC - Diferencia entre rendimientos simples y logarítmicos
# MAGIC - Cálculo de volatilidad histórica
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Consulta 3: Funciones Lambda en Finanzas
# MAGIC
# MAGIC **Pregunta a Genie**:
# MAGIC
# MAGIC > "¿Cómo usar funciones lambda junto con map() y filter() para procesar una lista de operaciones bursátiles y calcular comisiones?"
# MAGIC
# MAGIC **Lo que aprenderás**:
# MAGIC - Cuándo usar lambda vs def
# MAGIC - Programación funcional en finanzas
# MAGIC - Procesamiento eficiente de listas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Consulta 4: Scope de Variables
# MAGIC
# MAGIC **Pregunta a Genie**:
# MAGIC
# MAGIC > "¿Cuál es la diferencia entre variables locales y globales en Python y cuándo debería usar `global` en funciones financieras?"
# MAGIC
# MAGIC **Lo que aprenderás**:
# MAGIC - Regla LEGB
# MAGIC - Buenas prácticas con variables globales
# MAGIC - Cuándo usar constantes globales (tasas, impuestos)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Consulta 5: Biblioteca Personalizada
# MAGIC
# MAGIC **Pregunta a Genie**:
# MAGIC
# MAGIC > "¿Cómo crear y organizar una biblioteca personal de funciones financieras en Python para reutilizar en múltiples proyectos?"
# MAGIC
# MAGIC **Lo que aprenderás**:
# MAGIC - Estructura de módulos
# MAGIC - Import de funciones personalizadas
# MAGIC - Organización por categorías (rendimiento, riesgo, valuación)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Consulta 6: Optimización de Funciones
# MAGIC
# MAGIC **Pregunta a Genie**:
# MAGIC
# MAGIC > "¿Cómo optimizar funciones financieras en Python para que sean más rápidas cuando proceso miles de cálculos?"
# MAGIC
# MAGIC **Lo que aprenderás**:
# MAGIC - Vectorización con NumPy
# MAGIC - Evitar bucles innecesarios
# MAGIC - Caché de resultados
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 💡 Tips para Consultas Efectivas
# MAGIC
# MAGIC * ✅ **Sé específico**: Menciona el contexto (finanzas, bonos, acciones)
# MAGIC * ✅ **Incluye ejemplos**: "dame un ejemplo con YPF"
# MAGIC * ✅ **Pide código**: "muéstrame el código completo"
# MAGIC * ✅ **Pregunta por buenas prácticas**: "¿cuál es la mejor forma de..."
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ¡Prueba estas consultas y continúa aprendiendo! 🚀

# COMMAND ----------

# DBTITLE 1,Sección - Conclusión
# MAGIC %md
# MAGIC
# MAGIC # 🎓 ¡Felicitaciones!
# MAGIC
# MAGIC ## Has Completado el Notebook 0.3
# MAGIC
# MAGIC * ✅ **Funciones básicas**: def, parámetros, return, docstrings
# MAGIC * ✅ **Parámetros avanzados**: posicionales, por defecto, *args, **kwargs
# MAGIC * ✅ **Funciones lambda**: map(), filter(), sorted()
# MAGIC * ✅ **Scope**: variables locales y globales
# MAGIC * ✅ **Biblioteca financiera**: 12 funciones reutilizables
# MAGIC * ✅ **Módulos built-in**: math, random, datetime, collections
# MAGIC * ✅ **Caso integrado**: análisis completo de cartera
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🚀 Próximos Pasos
# MAGIC
# MAGIC ### Notebook 0.4: Estructuras de Datos
# MAGIC - Listas, tuplas, sets, diccionarios
# MAGIC - Métodos de estructuras
# MAGIC - Comprehensions avanzadas
# MAGIC
# MAGIC ### Notebook 0.5: Pandas para Finanzas
# MAGIC - DataFrames y Series
# MAGIC - Manipulación de datos
# MAGIC - Series temporales
# MAGIC
# MAGIC ### Notebook 0.6: Visualización de Datos
# MAGIC - Matplotlib, Seaborn, Plotly
# MAGIC - Gráficos financieros
# MAGIC - Dashboards interactivos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📚 Recursos Adicionales
# MAGIC
# MAGIC * **Python Official Docs**: https://docs.python.org/3/
# MAGIC * **Real Python**: https://realpython.com/
# MAGIC * **QuantLib**: Biblioteca para finanzas cuantitativas
# MAGIC * **PyAlgoTrade**: Framework para backtesting
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 💬 Feedback
# MAGIC
# MAGIC ¿Te resultó útil este notebook?
# MAGIC
# MAGIC Comparte tu experiencia en el foro del curso o con tu instructor.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 💪 **Recuerda**: Las funciones son la base de todo código profesional. Domínalas y tu código será 10x más poderoso.
# MAGIC
# MAGIC ¡Nos vemos en el siguiente notebook! 🚀