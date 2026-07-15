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
# MAGIC ### Notebook 0.2: Estructuras de Control
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC </div>

# COMMAND ----------

# DBTITLE 1,Introducción
# MAGIC %md
# MAGIC # 🎯 Introducción: Estructuras de Control
# MAGIC
# MAGIC ## 📚 Repaso del Notebook Anterior (0.1)
# MAGIC
# MAGIC En el notebook 0.1 aprendimos:
# MAGIC ✅ Variables y tipos de datos (int, float, str, bool)
# MAGIC ✅ Operadores aritméticos (+, -, *, /, **, //, %)
# MAGIC ✅ Strings y formato con f-strings
# MAGIC ✅ Conversión de tipos
# MAGIC
# MAGIC **Hasta ahora**, nuestro código se ejecuta línea por línea, de arriba hacia abajo, siempre igual.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🚦 ¿Qué son las Estructuras de Control?
# MAGIC
# MAGIC Las **estructuras de control** nos permiten:
# MAGIC 1. **Tomar decisiones** → Condicionales (if, elif, else)
# MAGIC 2. **Repetir acciones** → Bucles (for, while)
# MAGIC
# MAGIC ### Analogía con Excel
# MAGIC
# MAGIC | Excel | Python |
# MAGIC |-------|--------|
# MAGIC | `=SI(A1>100, "Alto", "Bajo")` | `if precio > 100:` |
# MAGIC | Arrastrar fórmula hacia abajo | `for` o `while` |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 💼 ¿Por qué son importantes en finanzas?
# MAGIC
# MAGIC ### Condicionales
# MAGIC - ✅ **Clasificar inversiones**: Si rendimiento > 10% → "Buena inversión"
# MAGIC - ✅ **Generar alertas**: Si precio < umbral → "Comprar"
# MAGIC - ✅ **Aplicar comisiones**: Si monto > $10,000 → Comisión del 1%
# MAGIC
# MAGIC ### Bucles
# MAGIC - ✅ **Analizar múltiples acciones**: Calcular rendimiento de 100 empresas
# MAGIC - ✅ **Proyecciones**: Simular 30 años de interés compuesto
# MAGIC - ✅ **Reportes**: Generar resumen de todo el portafolio
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📋 ¿Qué aprenderemos hoy?
# MAGIC
# MAGIC ### Parte 1: Condicionales 🔀
# MAGIC 1. `if` básico
# MAGIC 2. `if-else`
# MAGIC 3. `if-elif-else` (múltiples condiciones)
# MAGIC 4. Operadores lógicos (`and`, `or`, `not`)
# MAGIC 5. Condiciones anidadas
# MAGIC
# MAGIC ### Parte 2: Bucles 🔁
# MAGIC 1. `for` con listas
# MAGIC 2. `for` con `range()`
# MAGIC 3. `while`
# MAGIC 4. `break` y `continue`
# MAGIC 5. Bucles anidados
# MAGIC
# MAGIC ### Parte 3: List Comprehensions 🚀
# MAGIC - Sintaxis compacta y eficiente
# MAGIC
# MAGIC ### Parte 4: Casos Integrados 💼
# MAGIC - Aplicaciones reales en finanzas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⏱️ **Tiempo estimado**: 45-60 minutos
# MAGIC
# MAGIC ¡Empecemos!

# COMMAND ----------

# DBTITLE 1,Explicación - If Básico
# MAGIC %md
# MAGIC ## 🔀 CONDICIONALES - Parte 1: if Básico
# MAGIC
# MAGIC ### ¿Qué es un condicional?
# MAGIC
# MAGIC Un **condicional** permite que nuestro código tome **decisiones**.
# MAGIC
# MAGIC ```
# MAGIC SI (condición es verdadera):
# MAGIC     Ejecutar este código
# MAGIC ```
# MAGIC
# MAGIC ### Sintaxis en Python
# MAGIC
# MAGIC ```python
# MAGIC if condicion:
# MAGIC     # Código que se ejecuta SI la condición es True
# MAGIC     print("La condición se cumplió")
# MAGIC ```
# MAGIC
# MAGIC ⚠️ **Importante**:
# MAGIC 1. El `if` termina con dos puntos `:`
# MAGIC 2. El código dentro del `if` está **indentado** (4 espacios o 1 tab)
# MAGIC 3. La indentación indica qué código pertenece al `if`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Operadores de Comparación
# MAGIC
# MAGIC Para crear condiciones, usamos estos operadores:
# MAGIC
# MAGIC | Operador | Significado | Ejemplo | Resultado |
# MAGIC |----------|-------------|---------|----------|
# MAGIC | `==` | Igual a | `5 == 5` | `True` |
# MAGIC | `!=` | Diferente de | `5 != 3` | `True` |
# MAGIC | `>` | Mayor que | `10 > 5` | `True` |
# MAGIC | `<` | Menor que | `3 < 10` | `True` |
# MAGIC | `>=` | Mayor o igual | `5 >= 5` | `True` |
# MAGIC | `<=` | Menor o igual | `3 <= 5` | `True` |
# MAGIC
# MAGIC ⚠️ **Cuidado**: `=` (asignación) vs `==` (comparación)
# MAGIC ```python
# MAGIC precio = 100  # Asignación: guardamos el valor 100
# MAGIC if precio == 100:  # Comparación: ¿precio es igual a 100?
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ejemplos Financieros
# MAGIC
# MAGIC #### Ejemplo 1: Detectar si una acción subió
# MAGIC ```python
# MAGIC precio_hoy = 110
# MAGIC precio_ayer = 100
# MAGIC
# MAGIC if precio_hoy > precio_ayer:
# MAGIC     print("¡La acción subió!")
# MAGIC ```
# MAGIC
# MAGIC #### Ejemplo 2: Alerta de precio bajo
# MAGIC ```python
# MAGIC precio_accion = 85
# MAGIC umbral_compra = 90
# MAGIC
# MAGIC if precio_accion < umbral_compra:
# MAGIC     print("🚨 Precio bajo. Considerar compra.")
# MAGIC ```
# MAGIC
# MAGIC #### Ejemplo 3: Verificar rentabilidad
# MAGIC ```python
# MAGIC rendimiento = 0.12  # 12%
# MAGIC
# MAGIC if rendimiento > 0.10:
# MAGIC     print("✅ Inversión rentable (>10%)")
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ¿Qué pasa si la condición es False?
# MAGIC
# MAGIC Si la condición NO se cumple, el código dentro del `if` **se salta** completamente.
# MAGIC
# MAGIC ```python
# MAGIC precio = 80
# MAGIC
# MAGIC if precio > 100:
# MAGIC     print("Precio alto")  # Esto NO se ejecuta
# MAGIC
# MAGIC print("Fin del programa")  # Esto SÍ se ejecuta
# MAGIC ```
# MAGIC
# MAGIC **Salida**:
# MAGIC ```
# MAGIC Fin del programa
# MAGIC ```
# MAGIC
# MAGIC (El mensaje "Precio alto" no aparece porque la condición es False)

# COMMAND ----------

# DBTITLE 1,Código - If Básico
print("═" * 70)
print("EJEMPLO: Condicional IF Básico en Finanzas")
print("═" * 70)

# Ejemplo 1: Detectar si una acción subió
print("\n1️⃣ DETECTAR SI UNA ACCIÓN SUBIÓ:")
print("-" * 70)

empresa = "YPF"
precio_ayer = 5250.00
precio_hoy = 5380.50

print(f"Empresa: {empresa}")
print(f"Precio ayer: ${precio_ayer:,.2f}")
print(f"Precio hoy: ${precio_hoy:,.2f}")
print()

if precio_hoy > precio_ayer:
    diferencia = precio_hoy - precio_ayer
    variacion_pct = (diferencia / precio_ayer) * 100
    print(f"✅ ¡La acción SUBIÓ!")
    print(f"   Variación: ${diferencia:,.2f} (+{variacion_pct:.2f}%)")

# Ejemplo 2: Alerta de precio bajo (oportunidad de compra)
print("\n2️⃣ SISTEMA DE ALERTAS - PRECIO BAJO:")
print("-" * 70)

empresa = "Banco Galicia"
precio_actual = 165.50
umbral_compra = 170.00

print(f"Empresa: {empresa}")
print(f"Precio actual: ${precio_actual:,.2f}")
print(f"Umbral de compra: ${umbral_compra:,.2f}")
print()

if precio_actual < umbral_compra:
    descuento = umbral_compra - precio_actual
    descuento_pct = (descuento / umbral_compra) * 100
    print(f"🚨 ALERTA: Precio bajo detectado!")
    print(f"   Está ${descuento:.2f} por debajo del umbral ({descuento_pct:.1f}%)")
    print(f"   💡 Considerar COMPRA")

# Ejemplo 3: Verificar si una inversión es rentable
print("\n3️⃣ VERIFICAR RENTABILIDAD:")
print("-" * 70)

inversion_inicial = 100000
inversion_final = 112500
rendimiento = (inversion_final - inversion_inicial) / inversion_inicial
rendimiento_pct = rendimiento * 100
rendimiento_minimo = 10  # 10%

print(f"Inversión inicial: ${inversion_inicial:,.2f}")
print(f"Inversión final: ${inversion_final:,.2f}")
print(f"Rendimiento: {rendimiento_pct:.2f}%")
print(f"Rendimiento mínimo aceptable: {rendimiento_minimo}%")
print()

if rendimiento_pct > rendimiento_minimo:
    print(f"✅ INVERSIÓN RENTABLE")
    print(f"   Supera el rendimiento mínimo por {rendimiento_pct - rendimiento_minimo:.2f} puntos")

if rendimiento_pct > 15:
    print(f"🌟 EXCELENTE rendimiento (>{rendimiento_pct:.0f}%)")

# Ejemplo 4: Comisión especial para grandes montos
print("\n4️⃣ APLICAR COMISIÓN ESPECIAL:")
print("-" * 70)

monto_operacion = 50000
comision_normal = 0.015  # 1.5%
comision_especial = 0.010  # 1.0%
umbral_descuento = 30000

print(f"Monto de operación: ${monto_operacion:,.2f}")
print(f"Umbral para descuento: ${umbral_descuento:,.2f}")
print()

# Inicialmente usamos comisión normal
comision_aplicada = comision_normal

if monto_operacion > umbral_descuento:
    comision_aplicada = comision_especial
    print(f"🎁 Cliente califica para comisión especial")

monto_comision = monto_operacion * comision_aplicada
print(f"\nComisión aplicada: {comision_aplicada * 100}%")
print(f"Monto de comisión: ${monto_comision:,.2f}")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - If-Else
# MAGIC %md
# MAGIC ## 🔀 CONDICIONALES - Parte 2: if-else
# MAGIC
# MAGIC ### Limitación del if simple
# MAGIC
# MAGIC Con `if` solo, si la condición es False, no pasa nada. ¿Y si queremos hacer algo **cuando NO se cumple**?
# MAGIC
# MAGIC ### Sintaxis if-else
# MAGIC
# MAGIC ```python
# MAGIC if condicion:
# MAGIC     # Código si es True
# MAGIC else:
# MAGIC     # Código si es False
# MAGIC ```
# MAGIC
# MAGIC 👉 **Siempre se ejecuta UNA de las dos opciones**, nunca ambas.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Diagrama de Flujo
# MAGIC
# MAGIC ```
# MAGIC           ┌─────────────┐
# MAGIC           │ ¿Condición? │
# MAGIC           └─────┬───────┘
# MAGIC               │
# MAGIC      ┌─────┼─────┐
# MAGIC      │          │
# MAGIC    True         False
# MAGIC      │          │
# MAGIC  ┌──┴──┐    ┌──┴──┐
# MAGIC  │ if  │    │else│
# MAGIC  └─────┘    └─────┘
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ejemplos Financieros
# MAGIC
# MAGIC #### Ejemplo 1: Decisión de compra/venta
# MAGIC
# MAGIC ```python
# MAGIC precio_actual = 150
# MAGIC precio_objetivo = 140
# MAGIC
# MAGIC if precio_actual < precio_objetivo:
# MAGIC     print("Comprar")
# MAGIC else:
# MAGIC     print("Esperar o vender")
# MAGIC ```
# MAGIC
# MAGIC #### Ejemplo 2: Clasificar inversión
# MAGIC
# MAGIC ```python
# MAGIC rendimiento = 0.08  # 8%
# MAGIC
# MAGIC if rendimiento >= 0:
# MAGIC     print("Ganancia")
# MAGIC else:
# MAGIC     print("Pérdida")
# MAGIC ```
# MAGIC
# MAGIC #### Ejemplo 3: Aplicar o no comisión
# MAGIC
# MAGIC ```python
# MAGIC monto = 5000
# MAGIC
# MAGIC if monto > 10000:
# MAGIC     comision = monto * 0.01
# MAGIC else:
# MAGIC     comision = 0
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ventaja del else
# MAGIC
# MAGIC **Sin else** (necesitamos dos ifs):
# MAGIC ```python
# MAGIC if precio > 100:
# MAGIC     print("Caro")
# MAGIC if precio <= 100:  # Repetimos la condición
# MAGIC     print("Barato")
# MAGIC ```
# MAGIC
# MAGIC **Con else** (más limpio):
# MAGIC ```python
# MAGIC if precio > 100:
# MAGIC     print("Caro")
# MAGIC else:
# MAGIC     print("Barato")
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Código - If-Else
print("═" * 70)
print("EJEMPLO: if-else en Finanzas")
print("═" * 70)

# Ejemplo 1: Decisión de compra o venta
print("\n1️⃣ DECISIÓN: COMPRAR O VENDER")
print("-" * 70)

empresa = "Mercado Libre"
precio_actual = 1420.00
precio_objetivo = 1450.00

print(f"Empresa: {empresa}")
print(f"Precio actual: ${precio_actual:,.2f}")
print(f"Precio objetivo: ${precio_objetivo:,.2f}")
print()

if precio_actual < precio_objetivo:
    diferencia = precio_objetivo - precio_actual
    potencial = (diferencia / precio_actual) * 100
    print(f"🟢 RECOMENDACIÓN: COMPRAR")
    print(f"   Aún está ${diferencia:.2f} por debajo del objetivo")
    print(f"   Potencial de subida: {potencial:.1f}%")
else:
    diferencia = precio_actual - precio_objetivo
    print(f"🔴 RECOMENDACIÓN: NO COMPRAR (o vender si ya tienes)")
    print(f"   Ya superó el precio objetivo por ${diferencia:.2f}")

# Ejemplo 2: Clasificar resultado de inversión
print("\n2️⃣ CLASIFICAR RESULTADO")
print("-" * 70)

inversion_inicial = 100000
inversion_final = 95000
rendimiento = ((inversion_final - inversion_inicial) / inversion_inicial) * 100

print(f"Inversión inicial: ${inversion_inicial:,.2f}")
print(f"Inversión final: ${inversion_final:,.2f}")
print(f"Rendimiento: {rendimiento:.2f}%")
print()

if rendimiento >= 0:
    print(f"✅ GANANCIA de {abs(rendimiento):.2f}%")
    ganancia = inversion_final - inversion_inicial
    print(f"   Ganaste: ${abs(ganancia):,.2f}")
else:
    print(f"❌ PÉRDIDA de {abs(rendimiento):.2f}%")
    perdida = inversion_inicial - inversion_final
    print(f"   Perdiste: ${perdida:,.2f}")

# Ejemplo 3: Sistema de comisiones
print("\n3️⃣ SISTEMA DE COMISIONES")
print("-" * 70)

monto_operacion = 8500
umbral_sin_comision = 10000

print(f"Monto de operación: ${monto_operacion:,.2f}")
print(f"Umbral sin comisión: ${umbral_sin_comision:,.2f}")
print()

if monto_operacion >= umbral_sin_comision:
    comision = 0
    print(f"🎉 Operación sin comisión")
    print(f"   Monto final: ${monto_operacion:,.2f}")
else:
    tasa_comision = 0.02  # 2%
    comision = monto_operacion * tasa_comision
    monto_final = monto_operacion - comision
    print(f"💳 Se aplica comisión de {tasa_comision * 100}%")
    print(f"   Comisión: ${comision:,.2f}")
    print(f"   Monto final: ${monto_final:,.2f}")

# Ejemplo 4: Alerta de precio
print("\n4️⃣ SISTEMA DE ALERTAS")
print("-" * 70)

for ticker, precio in [("YPF", 5250), ("GGAL", 180), ("MELI", 1380)]:
    precio_referencia = 5000 if ticker == "YPF" else (175 if ticker == "GGAL" else 1400)
    
    print(f"\n{ticker}: ${precio:,.2f} (Referencia: ${precio_referencia:,.2f})")
    
    if precio < precio_referencia:
        descuento = ((precio_referencia - precio) / precio_referencia) * 100
        print(f"  🟢 Precio BAJO (-{descuento:.1f}%) - Oportunidad de compra")
    else:
        sobreprecio = ((precio - precio_referencia) / precio_referencia) * 100
        print(f"  🔴 Precio ALTO (+{sobreprecio:.1f}%) - Considerar venta")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - If-Elif-Else
# MAGIC %md
# MAGIC ## 🔀 CONDICIONALES - Parte 3: if-elif-else (Múltiples Condiciones)
# MAGIC
# MAGIC ### Limitación de if-else
# MAGIC
# MAGIC Con `if-else` solo podemos manejar **dos casos**: verdadero o falso. ¿Y si necesitamos **3, 4 o más opciones**?
# MAGIC
# MAGIC **Ejemplo**: Clasificar rendimiento como "Bajo", "Medio" o "Alto"
# MAGIC
# MAGIC ### Sintaxis if-elif-else
# MAGIC
# MAGIC ```python
# MAGIC if condicion1:
# MAGIC     # Código si condicion1 es True
# MAGIC elif condicion2:
# MAGIC     # Código si condicion1 es False y condicion2 es True
# MAGIC elif condicion3:
# MAGIC     # Código si condicion1 y condicion2 son False, pero condicion3 es True
# MAGIC else:
# MAGIC     # Código si TODAS las condiciones anteriores son False
# MAGIC ```
# MAGIC
# MAGIC 👉 `elif` significa "else if" (sino, si...)
# MAGIC
# MAGIC 👉 Se evalúan **en orden**, de arriba hacia abajo
# MAGIC
# MAGIC 👉 Se ejecuta **solo el primer bloque** cuya condición sea True
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Diagrama de Flujo
# MAGIC
# MAGIC ```
# MAGIC ¿Condición 1?
# MAGIC     │
# MAGIC     ├── True → Ejecutar bloque 1 → FIN
# MAGIC     │
# MAGIC     └── False
# MAGIC         │
# MAGIC         ¿Condición 2?
# MAGIC             │
# MAGIC             ├── True → Ejecutar bloque 2 → FIN
# MAGIC             │
# MAGIC             └── False
# MAGIC                 │
# MAGIC                 ¿Condición 3?
# MAGIC                     │
# MAGIC                     ├── True → Ejecutar bloque 3 → FIN
# MAGIC                     │
# MAGIC                     └── False → Ejecutar else → FIN
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ejemplos Financieros
# MAGIC
# MAGIC #### Ejemplo 1: Clasificar rendimiento
# MAGIC
# MAGIC ```python
# MAGIC rendimiento = 0.12  # 12%
# MAGIC
# MAGIC if rendimiento > 0.15:
# MAGIC     print("Rendimiento ALTO")
# MAGIC elif rendimiento > 0.08:
# MAGIC     print("Rendimiento MEDIO")
# MAGIC elif rendimiento > 0:
# MAGIC     print("Rendimiento BAJO")
# MAGIC else:
# MAGIC     print("PÉRDIDA")
# MAGIC ```
# MAGIC
# MAGIC #### Ejemplo 2: Sistema de calificación crediticia
# MAGIC
# MAGIC ```python
# MAGIC score = 750
# MAGIC
# MAGIC if score >= 800:
# MAGIC     print("Excelente - Tasa 5%")
# MAGIC elif score >= 700:
# MAGIC     print("Bueno - Tasa 7%")
# MAGIC elif score >= 600:
# MAGIC     print("Regular - Tasa 10%")
# MAGIC else:
# MAGIC     print("Malo - Préstamo rechazado")
# MAGIC ```
# MAGIC
# MAGIC #### Ejemplo 3: Rangos de precio
# MAGIC
# MAGIC ```python
# MAGIC precio = 5500
# MAGIC
# MAGIC if precio > 10000:
# MAGIC     categoria = "Premium"
# MAGIC elif precio > 5000:
# MAGIC     categoria = "Intermedio"
# MAGIC elif precio > 1000:
# MAGIC     categoria = "Básico"
# MAGIC else:
# MAGIC     categoria = "Económico"
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚠️ Orden Importa
# MAGIC
# MAGIC **MAL** (orden incorrecto):
# MAGIC ```python
# MAGIC rendimiento = 0.20  # 20%
# MAGIC
# MAGIC if rendimiento > 0:      # Esta se cumple primero
# MAGIC     print("Bajo")
# MAGIC elif rendimiento > 0.15:  # Nunca se evaluará
# MAGIC     print("Alto")
# MAGIC ```
# MAGIC Salida: "Bajo" (incorrecto)
# MAGIC
# MAGIC **BIEN** (orden correcto):
# MAGIC ```python
# MAGIC if rendimiento > 0.15:   # Más restrictiva primero
# MAGIC     print("Alto")
# MAGIC elif rendimiento > 0:
# MAGIC     print("Bajo")
# MAGIC ```
# MAGIC Salida: "Alto" (correcto)
# MAGIC
# MAGIC 💡 **Regla**: Pon las condiciones **más específicas primero**, las generales después.

# COMMAND ----------

# DBTITLE 1,Código - If-Elif-Else
print("═" * 70)
print("EJEMPLO: if-elif-else - Múltiples Condiciones")
print("═" * 70)

# Ejemplo 1: Clasificar rendimiento de inversiones
print("\n1️⃣ CLASIFICAR RENDIMIENTO")
print("-" * 70)

empresas = [
    ("YPF", 0.18),
    ("Banco Galicia", 0.09),
    ("Mercado Libre", 0.04),
    ("Telecom", -0.03)
]

for empresa, rendimiento in empresas:
    rendimiento_pct = rendimiento * 100
    print(f"\n{empresa}: {rendimiento_pct:+.1f}%")
    
    if rendimiento > 0.15:
        clasificacion = "🟢 EXCELENTE"
        recomendacion = "Mantener posición"
    elif rendimiento > 0.08:
        clasificacion = "🟡 BUENO"
        recomendacion = "Rendimiento sólido"
    elif rendimiento > 0:
        clasificacion = "🟠 MODERADO"
        recomendacion = "Bajo pero positivo"
    else:
        clasificacion = "🔴 NEGATIVO"
        recomendacion = "Considerar venta"
    
    print(f"  {clasificacion}")
    print(f"  💡 {recomendacion}")

# Ejemplo 2: Sistema de calificación crediticia
print("\n\n2️⃣ SISTEMA DE CALIFICACIÓN CREDITICIA")
print("-" * 70)

clientes = [
    ("Juan Pérez", 850),
    ("María García", 720),
    ("Carlos López", 650),
    ("Ana Martínez", 580)
]

for nombre, score in clientes:
    print(f"\n{nombre} - Score: {score}")
    
    if score >= 800:
        calificacion = "Excelente"
        tasa = 5.0
        limite = 500000
    elif score >= 700:
        calificacion = "Bueno"
        tasa = 7.5
        limite = 300000
    elif score >= 600:
        calificacion = "Regular"
        tasa = 12.0
        limite = 100000
    else:
        calificacion = "Malo"
        tasa = None
        limite = 0
    
    print(f"  Calificación: {calificacion}")
    if tasa:
        print(f"  Tasa ofrecida: {tasa}% anual")
        print(f"  Límite de crédito: ${limite:,}")
    else:
        print(f"  ❌ Préstamo RECHAZADO")

# Ejemplo 3: Categorías de precio de acciones
print("\n\n3️⃣ CATEGORÍAS DE PRECIO")
print("-" * 70)

acciones = [
    ("MELI", 1450.00),
    ("YPF", 5250.75),
    ("GGAL", 175.50),
    ("COME", 2.35)
]

for ticker, precio in acciones:
    print(f"\n{ticker}: ${precio:,.2f}")
    
    if precio > 5000:
        categoria = "💎 Premium"
        descripcion = "Acción de alto valor"
    elif precio > 1000:
        categoria = "💛 Intermedia"
        descripcion = "Acción de valor medio"
    elif precio > 100:
        categoria = "💚 Básica"
        descripcion = "Acción accesible"
    else:
        categoria = "💙 Económica"
        descripcion = "Acción de bajo valor"
    
    print(f"  Categoría: {categoria}")
    print(f"  {descripcion}")

# Ejemplo 4: Alertas de volatilidad
print("\n\n4️⃣ ALERTAS DE VOLATILIDAD")
print("-" * 70)

volatilidades = [
    ("Bitcoin", 0.45),
    ("YPF", 0.12),
    ("Bonos argentinos", 0.08),
    ("Plazo fijo", 0.01)
]

for activo, volatilidad in volatilidades:
    volatilidad_pct = volatilidad * 100
    print(f"\n{activo}: {volatilidad_pct:.1f}% de volatilidad")
    
    if volatilidad > 0.30:
        nivel = "🔴 MUY ALTA"
        perfil = "Solo para inversores agresivos"
    elif volatilidad > 0.15:
        nivel = "🟠 ALTA"
        perfil = "Para inversores con tolerancia al riesgo"
    elif volatilidad > 0.05:
        nivel = "🟡 MODERADA"
        perfil = "Apto para perfil balanceado"
    else:
        nivel = "🟢 BAJA"
        perfil = "Apto para perfil conservador"
    
    print(f"  Nivel de riesgo: {nivel}")
    print(f"  🎯 {perfil}")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - Operadores Lógicos
# MAGIC %md
# MAGIC ## 🔀 CONDICIONALES - Parte 4: Operadores Lógicos
# MAGIC
# MAGIC ### Combinar Múltiples Condiciones
# MAGIC
# MAGIC Hasta ahora, cada `if` evaluaba **una sola condición**. ¿Y si necesitamos que **dos o más condiciones** se cumplan simultáneamente?
# MAGIC
# MAGIC **Ejemplo**: Comprar acción SI precio < $100 **Y** rendimiento > 10%
# MAGIC
# MAGIC ### Los 3 Operadores Lógicos
# MAGIC
# MAGIC | Operador | Significado | Resultado True cuando... |
# MAGIC |----------|-------------|-------------------------|
# MAGIC | `and` | Y (conjunción) | **AMBAS** condiciones son True |
# MAGIC | `or` | O (disyunción) | **AL MENOS UNA** condición es True |
# MAGIC | `not` | NO (negación) | **INVIERTE** el resultado (True → False, False → True) |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 1. Operador `and`
# MAGIC
# MAGIC Ambas condiciones **deben** ser True.
# MAGIC
# MAGIC ```python
# MAGIC if condicion1 and condicion2:
# MAGIC     # Se ejecuta solo si AMBAS son True
# MAGIC ```
# MAGIC
# MAGIC **Tabla de verdad**:
# MAGIC
# MAGIC | Condición 1 | Condición 2 | Resultado |
# MAGIC |-------------|-------------|----------|
# MAGIC | True | True | **True** |
# MAGIC | True | False | False |
# MAGIC | False | True | False |
# MAGIC | False | False | False |
# MAGIC
# MAGIC **Ejemplo financiero**:
# MAGIC ```python
# MAGIC precio = 95
# MAGIC rendimiento = 0.12
# MAGIC
# MAGIC if precio < 100 and rendimiento > 0.10:
# MAGIC     print("Comprar")  # Solo si AMBAS se cumplen
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 2. Operador `or`
# MAGIC
# MAGIC Al menos **una** condición debe ser True.
# MAGIC
# MAGIC ```python
# MAGIC if condicion1 or condicion2:
# MAGIC     # Se ejecuta si AL MENOS UNA es True
# MAGIC ```
# MAGIC
# MAGIC **Tabla de verdad**:
# MAGIC
# MAGIC | Condición 1 | Condición 2 | Resultado |
# MAGIC |-------------|-------------|----------|
# MAGIC | True | True | **True** |
# MAGIC | True | False | **True** |
# MAGIC | False | True | **True** |
# MAGIC | False | False | False |
# MAGIC
# MAGIC **Ejemplo financiero**:
# MAGIC ```python
# MAGIC rendimiento = 0.15
# MAGIC volumen = 1200000
# MAGIC
# MAGIC if rendimiento > 0.12 or volumen > 1000000:
# MAGIC     print("Acción interesante")  # Con que UNA se cumpla
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 3. Operador `not`
# MAGIC
# MAGIC Invierte el resultado.
# MAGIC
# MAGIC ```python
# MAGIC if not condicion:
# MAGIC     # Se ejecuta si la condición es False
# MAGIC ```
# MAGIC
# MAGIC **Tabla de verdad**:
# MAGIC
# MAGIC | Condición | Resultado |
# MAGIC |-----------|----------|
# MAGIC | True | **False** |
# MAGIC | False | **True** |
# MAGIC
# MAGIC **Ejemplo financiero**:
# MAGIC ```python
# MAGIC esta_en_cartera = False
# MAGIC
# MAGIC if not esta_en_cartera:
# MAGIC     print("Añadir a la cartera")
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Combinar Múltiples Operadores
# MAGIC
# MAGIC Puedes combinar `and`, `or` y `not`:
# MAGIC
# MAGIC ```python
# MAGIC if (precio < 100 and rendimiento > 0.10) or volumen > 2000000:
# MAGIC     print("Comprar")
# MAGIC ```
# MAGIC
# MAGIC 👉 Usa **paréntesis** para dejar claro el orden de evaluación.
# MAGIC
# MAGIC **Precedencia** (orden de evaluación):
# MAGIC 1. `not`
# MAGIC 2. `and`
# MAGIC 3. `or`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ejemplos Prácticos
# MAGIC
# MAGIC #### Filtrar acciones "Blue Chip"
# MAGIC ```python
# MAGIC liquidez_alta = volumen > 1000000
# MAGIC precio_estable = volatilidad < 0.15
# MAGIC rentable = rendimiento > 0.08
# MAGIC
# MAGIC if liquidez_alta and precio_estable and rentable:
# MAGIC     print("Blue Chip - Inversión segura")
# MAGIC ```
# MAGIC
# MAGIC #### Alerta de oportunidad
# MAGIC ```python
# MAGIC if (precio < precio_minimo_historico) or (rendimiento > 0.20):
# MAGIC     print("🚨 Oportunidad detectada")
# MAGIC ```
# MAGIC
# MAGIC #### Excluir de análisis
# MAGIC ```python
# MAGIC if not (empresa == "Excluida" or sector == "Prohibido"):
# MAGIC     # Analizar empresa
# MAGIC     pass
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Código - Operadores Lógicos
print("═" * 70)
print("EJEMPLO: Operadores Lógicos (and, or, not)")
print("═" * 70)

# Ejemplo 1: Filtrar acciones con operador AND
print("\n1️⃣ FILTRO CON 'AND' - Todas las condiciones deben cumplirse")
print("-" * 70)

acciones = [
    {"ticker": "YPF", "precio": 5200, "rendimiento": 0.15, "volumen": 1500000},
    {"ticker": "GGAL", "precio": 175, "rendimiento": 0.09, "volumen": 2000000},
    {"ticker": "MELI", "precio": 1450, "rendimiento": 0.04, "volumen": 800000},
    {"ticker": "COME", "precio": 2.5, "rendimiento": 0.18, "volumen": 500000}
]

print("\nBuscando acciones que cumplan:")
print("  • Precio < $2000")
print("  • Rendimiento > 10%")
print("  • Volumen > 1M")
print()

for accion in acciones:
    if accion["precio"] < 2000 and accion["rendimiento"] > 0.10 and accion["volumen"] > 1000000:
        print(f"✅ {accion['ticker']}: Cumple TODOS los criterios")
        print(f"   Precio: ${accion['precio']:,.2f}")
        print(f"   Rendimiento: {accion['rendimiento']*100:.1f}%")
        print(f"   Volumen: {accion['volumen']:,}")

# Ejemplo 2: Oportunidades con operador OR
print("\n\n2️⃣ FILTRO CON 'OR' - Al menos una condición debe cumplirse")
print("-" * 70)

print("\nBuscando acciones que cumplan AL MENOS UNA de:")
print("  • Rendimiento > 15% (alto rendimiento)")
print("  • Volumen > 1.8M (alta liquidez)")
print()

for accion in acciones:
    if accion["rendimiento"] > 0.15 or accion["volumen"] > 1800000:
        razones = []
        if accion["rendimiento"] > 0.15:
            razones.append(f"Alto rendimiento ({accion['rendimiento']*100:.1f}%)")
        if accion["volumen"] > 1800000:
            razones.append(f"Alta liquidez ({accion['volumen']:,})")
        
        print(f"✅ {accion['ticker']}: {', '.join(razones)}")

# Ejemplo 3: Excluir con operador NOT
print("\n\n3️⃣ FILTRO CON 'NOT' - Excluir acciones")
print("-" * 70)

excluidas = ["COME", "TRAN"]

print(f"\nAnalizar todas las acciones EXCEPTO: {', '.join(excluidas)}")
print()

for accion in acciones:
    if not accion["ticker"] in excluidas:
        print(f"✅ {accion['ticker']}: Incluida en el análisis")
        print(f"   Precio: ${accion['precio']:,.2f}")
    else:
        print(f"❌ {accion['ticker']}: Excluida del análisis")

# Ejemplo 4: Combinar múltiples operadores
print("\n\n4️⃣ COMBINAR MÚTIPLES OPERADORES")
print("-" * 70)

print("\nEstrategia compleja:")
print("  Comprar SI:")
print("    (Precio < $1000 AND Rendimiento > 10%)")
print("    O")
print("    (Volumen > 1.5M AND NOT en lista de excluidas)")
print()

for accion in acciones:
    # Condición compleja
    condicion1 = accion["precio"] < 1000 and accion["rendimiento"] > 0.10
    condicion2 = accion["volumen"] > 1500000 and not accion["ticker"] in excluidas
    
    if condicion1 or condicion2:
        print(f"🟢 COMPRAR {accion['ticker']}")
        
        # Explicar por qué
        if condicion1:
            print(f"   ✓ Precio accesible (${accion['precio']:,.2f}) con buen rendimiento ({accion['rendimiento']*100:.1f}%)")
        if condicion2:
            print(f"   ✓ Alta liquidez ({accion['volumen']:,}) y no excluida")
    else:
        print(f"🔴 NO COMPRAR {accion['ticker']}")

# Ejemplo 5: Clasificación avanzada
print("\n\n5️⃣ CLASIFICACIÓN AVANZADA DE INVERSIONES")
print("-" * 70)

for accion in acciones:
    ticker = accion["ticker"]
    precio = accion["precio"]
    rendimiento = accion["rendimiento"]
    volumen = accion["volumen"]
    
    print(f"\n{ticker}:")
    
    # Blue Chip: alta liquidez, rendimiento sólido, no volatil
    if volumen > 1500000 and rendimiento > 0.08 and precio < 6000:
        print("  💎 BLUE CHIP - Inversión sólida y segura")
    
    # Growth: alto rendimiento aunque baja liquidez
    elif rendimiento > 0.15 and precio < 10000:
        print("  🚀 GROWTH - Alto potencial de crecimiento")
    
    # Value: precio bajo, esperar mejora
    elif precio < 100 and rendimiento >= 0:
        print("  💰 VALUE - Precio atractivo, potencial recuperación")
    
    # Especulativa: alta volatilidad
    else:
        print("  ⚠️ ESPECULATIVA - Mayor riesgo")
    
    # Alerta adicional
    if rendimiento < 0.05 and volumen < 1000000:
        print("  🚨 ADVERTENCIA: Bajo rendimiento Y baja liquidez")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - Bucles For
# MAGIC %md
# MAGIC ## 🔁 BUCLES - Parte 1: for con Listas
# MAGIC
# MAGIC ### ¿Qué es un bucle?
# MAGIC
# MAGIC Un **bucle** permite **repetir** una acción múltiples veces sin escribir el mismo código una y otra vez.
# MAGIC
# MAGIC **Sin bucle** (repetitivo):
# MAGIC ```python
# MAGIC print("YPF")
# MAGIC print("GGAL")
# MAGIC print("MELI")
# MAGIC print("COME")
# MAGIC ```
# MAGIC
# MAGIC **Con bucle** (eficiente):
# MAGIC ```python
# MAGIC for ticker in ["YPF", "GGAL", "MELI", "COME"]:
# MAGIC     print(ticker)
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Sintaxis del for
# MAGIC
# MAGIC ```python
# MAGIC for variable in secuencia:
# MAGIC     # Código que se repite
# MAGIC     # 'variable' toma cada valor de la secuencia, uno por uno
# MAGIC ```
# MAGIC
# MAGIC 👉 La **variable** cambia en cada iteración (ciclo del bucle)
# MAGIC
# MAGIC 👉 El código **indentado** se ejecuta para cada elemento
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ejemplo Básico
# MAGIC
# MAGIC ```python
# MAGIC precios = [100, 150, 200, 175]
# MAGIC
# MAGIC for precio in precios:
# MAGIC     print(f"El precio es ${precio}")
# MAGIC ```
# MAGIC
# MAGIC **Salida**:
# MAGIC ```
# MAGIC El precio es $100
# MAGIC El precio es $150
# MAGIC El precio es $200
# MAGIC El precio es $175
# MAGIC ```
# MAGIC
# MAGIC **¿Qué pasó?**
# MAGIC 1. Primera vuelta: `precio = 100` → ejecuta el print
# MAGIC 2. Segunda vuelta: `precio = 150` → ejecuta el print
# MAGIC 3. Tercera vuelta: `precio = 200` → ejecuta el print
# MAGIC 4. Cuarta vuelta: `precio = 175` → ejecuta el print
# MAGIC 5. Fin de la lista → termina el bucle
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Aplicaciones Financieras
# MAGIC
# MAGIC #### 1. Procesar múltiples precios
# MAGIC ```python
# MAGIC precios = [5250, 175, 1450, 2.5]
# MAGIC
# MAGIC for precio in precios:
# MAGIC     if precio > 1000:
# MAGIC         print(f"${precio} - Acción de alto valor")
# MAGIC     else:
# MAGIC         print(f"${precio} - Acción accesible")
# MAGIC ```
# MAGIC
# MAGIC #### 2. Calcular totales
# MAGIC ```python
# MAGIC inversiones = [10000, 5000, 7500, 12000]
# MAGIC total = 0
# MAGIC
# MAGIC for monto in inversiones:
# MAGIC     total += monto  # total = total + monto
# MAGIC
# MAGIC print(f"Inversión total: ${total}")
# MAGIC ```
# MAGIC
# MAGIC #### 3. Iterar sobre diccionarios
# MAGIC ```python
# MAGIC cartera = {
# MAGIC     "YPF": 50,
# MAGIC     "GGAL": 100,
# MAGIC     "MELI": 25
# MAGIC }
# MAGIC
# MAGIC for ticker, cantidad in cartera.items():
# MAGIC     print(f"{ticker}: {cantidad} acciones")
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ventajas del for
# MAGIC
# MAGIC ✅ **Código más corto**: 3 líneas en lugar de 100
# MAGIC ✅ **Más fácil de mantener**: Cambias una vez, afecta todo
# MAGIC ✅ **Flexible**: Funciona con listas de cualquier tamaño
# MAGIC ✅ **Legible**: Queda claro que estás procesando cada elemento

# COMMAND ----------

# DBTITLE 1,Código - Bucles For
print("═" * 70)
print("EJEMPLO: Bucles for en Finanzas")
print("═" * 70)

# Ejemplo 1: Iterar sobre lista de precios
print("\n1️⃣ PROCESAR LISTA DE PRECIOS")
print("-" * 70)

empresas = ["YPF", "Banco Galicia", "Mercado Libre", "Telecom"]
precios = [5250.75, 175.50, 1450.00, 850.25]

for i in range(len(empresas)):
    empresa = empresas[i]
    precio = precios[i]
    print(f"{empresa:20s} | ${precio:>10,.2f}")

# Ejemplo 2: Calcular total de portafolio
print("\n2️⃣ CALCULAR VALOR TOTAL DEL PORTAFOLIO")
print("-" * 70)

cartera = {
    "YPF": {"cantidad": 50, "precio": 5250.75},
    "GGAL": {"cantidad": 100, "precio": 175.50},
    "MELI": {"cantidad": 25, "precio": 1450.00}
}

total_portafolio = 0

print("\nPosiciones:")
for ticker, datos in cartera.items():
    valor = datos["cantidad"] * datos["precio"]
    total_portafolio += valor
    
    print(f"\n{ticker}:")
    print(f"  Cantidad: {datos['cantidad']}")
    print(f"  Precio: ${datos['precio']:,.2f}")
    print(f"  Valor: ${valor:,.2f}")

print(f"\n{'=' * 70}")
print(f"VALOR TOTAL DEL PORTAFOLIO: ${total_portafolio:,.2f}")

# Ejemplo 3: Calcular rendimientos
print("\n\n3️⃣ CALCULAR RENDIMIENTOS")
print("-" * 70)

operaciones = [
    {"empresa": "YPF", "compra": 5000, "venta": 5250},
    {"empresa": "GGAL", "compra": 150, "venta": 175},
    {"empresa": "MELI", "compra": 1500, "venta": 1450},
    {"empresa": "COME", "compra": 2.0, "venta": 2.5}
]

print(f"\n{'Empresa':<15} {'Compra':>10} {'Venta':>10} {'Rendimiento':>12}")
print("-" * 70)

for op in operaciones:
    rendimiento = ((op["venta"] - op["compra"]) / op["compra"]) * 100
    simbolo = "✅" if rendimiento > 0 else "❌"
    
    print(f"{op['empresa']:<15} ${op['compra']:>9,.2f} ${op['venta']:>9,.2f} {simbolo} {rendimiento:>8.2f}%")

# Ejemplo 4: Filtrar y clasificar
print("\n\n4️⃣ FILTRAR Y CLASIFICAR INVERSIONES")
print("-" * 70)

acciones = [
    {"ticker": "YPF", "rendimiento": 0.18, "sector": "Energía"},
    {"ticker": "GGAL", "rendimiento": 0.09, "sector": "Financiero"},
    {"ticker": "MELI", "rendimiento": 0.04, "sector": "Tecnología"},
    {"ticker": "LOMA", "rendimiento": 0.15, "sector": "Energía"},
    {"ticker": "TRAN", "rendimiento": -0.03, "sector": "Transporte"}
]

rendimiento_minimo = 0.10

print(f"\nAcciones con rendimiento > {rendimiento_minimo * 100}%:\n")

for accion in acciones:
    if accion["rendimiento"] > rendimiento_minimo:
        print(f"✅ {accion['ticker']} ({accion['sector']})")
        print(f"   Rendimiento: {accion['rendimiento'] * 100:.1f}%")

# Ejemplo 5: Acumular promedios
print("\n\n5️⃣ CALCULAR PROMEDIOS")
print("-" * 70)

rendimientos_mensuales = [0.05, 0.03, -0.02, 0.07, 0.04, 0.06, 0.02, 0.08, -0.01, 0.05, 0.04, 0.03]
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

print("\nRendimientos mensuales:")
total_rendimiento = 0
meses_positivos = 0
meses_negativos = 0

for i in range(len(rendimientos_mensuales)):
    rendimiento = rendimientos_mensuales[i]
    mes = meses[i]
    total_rendimiento += rendimiento
    
    if rendimiento > 0:
        meses_positivos += 1
        simbolo = "🟢"
    else:
        meses_negativos += 1
        simbolo = "🔴"
    
    print(f"  {mes}: {simbolo} {rendimiento:+.1%}")

promedio = total_rendimiento / len(rendimientos_mensuales)

print(f"\n{'=' * 70}")
print(f"Rendimiento promedio mensual: {promedio:.2%}")
print(f"Meses positivos: {meses_positivos}")
print(f"Meses negativos: {meses_negativos}")
print(f"Rendimiento anual acumulado: {total_rendimiento:.2%}")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - For con Range
# MAGIC %md
# MAGIC ## 🔁 BUCLES - Parte 2: for con range()
# MAGIC
# MAGIC ### ¿Qué es range()?
# MAGIC
# MAGIC `range()` genera una **secuencia de números** que podemos usar en un `for`.
# MAGIC
# MAGIC ### Sintaxis
# MAGIC
# MAGIC #### 1. `range(n)` - Del 0 al n-1
# MAGIC
# MAGIC ```python
# MAGIC for i in range(5):
# MAGIC     print(i)
# MAGIC ```
# MAGIC
# MAGIC **Salida**: `0, 1, 2, 3, 4` (5 números, empieza en 0)
# MAGIC
# MAGIC #### 2. `range(inicio, fin)` - Desde inicio hasta fin-1
# MAGIC
# MAGIC ```python
# MAGIC for i in range(2, 7):
# MAGIC     print(i)
# MAGIC ```
# MAGIC
# MAGIC **Salida**: `2, 3, 4, 5, 6`
# MAGIC
# MAGIC #### 3. `range(inicio, fin, paso)` - Con saltos
# MAGIC
# MAGIC ```python
# MAGIC for i in range(0, 10, 2):
# MAGIC     print(i)
# MAGIC ```
# MAGIC
# MAGIC **Salida**: `0, 2, 4, 6, 8`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ¿Cuándo usar range()?
# MAGIC
# MAGIC ✅ Cuando necesitas repetir algo **N veces**
# MAGIC ✅ Cuando necesitas el **índice** (posición) de los elementos
# MAGIC ✅ Cuando quieres generar **secuencias numéricas**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ejemplos Financieros
# MAGIC
# MAGIC #### 1. Proyección de interés compuesto
# MAGIC
# MAGIC ```python
# MAGIC capital = 10000
# MAGIC tasa = 0.05
# MAGIC
# MAGIC for anio in range(1, 6):  # Años 1 al 5
# MAGIC     capital = capital * (1 + tasa)
# MAGIC     print(f"Año {anio}: ${capital:.2f}")
# MAGIC ```
# MAGIC
# MAGIC #### 2. Acceder a elementos por índice
# MAGIC
# MAGIC ```python
# MAGIC empresas = ["YPF", "GGAL", "MELI"]
# MAGIC precios = [5250, 175, 1450]
# MAGIC
# MAGIC for i in range(len(empresas)):
# MAGIC     print(f"{empresas[i]}: ${precios[i]}")
# MAGIC ```
# MAGIC
# MAGIC #### 3. Simular escenarios
# MAGIC
# MAGIC ```python
# MAGIC for tasa in range(5, 16, 2):  # 5%, 7%, 9%, 11%, 13%, 15%
# MAGIC     tasa_decimal = tasa / 100
# MAGIC     monto_final = 10000 * (1 + tasa_decimal) ** 5
# MAGIC     print(f"Tasa {tasa}%: ${monto_final:.2f}")
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Código - For con Range
print("═" * 70)
print("EJEMPLO: for con range()")
print("═" * 70)

# Ejemplo 1: Proyección de interés compuesto
print("\n1️⃣ PROYECCIÓN DE INTERÉS COMPUESTO (5 años)")
print("-" * 70)

capital_inicial = 100000
tasa_anual = 0.055  # 5.5%
capital = capital_inicial

print(f"\nCapital inicial: ${capital_inicial:,.2f}")
print(f"Tasa anual: {tasa_anual * 100}%\n")

for anio in range(1, 6):
    capital = capital * (1 + tasa_anual)
    ganancia = capital - capital_inicial
    print(f"Año {anio}: ${capital:>12,.2f} | Ganancia: ${ganancia:>12,.2f}")

# Ejemplo 2: Simular múltiples escenarios de tasa
print("\n\n2️⃣ COMPARAR MÚTIPLES TASAS DE INTERÉS")
print("-" * 70)

capital_base = 50000
anios = 10

print(f"\nCapital inicial: ${capital_base:,.2f}")
print(f"Plazo: {anios} años\n")
print(f"{'Tasa':>6} | {'Monto Final':>15} | {'Ganancia':>15}")
print("-" * 70)

for tasa_pct in range(4, 13, 2):  # 4%, 6%, 8%, 10%, 12%
    tasa = tasa_pct / 100
    monto_final = capital_base * (1 + tasa) ** anios
    ganancia = monto_final - capital_base
    
    print(f"{tasa_pct:>5}% | ${monto_final:>14,.2f} | ${ganancia:>14,.2f}")

# Ejemplo 3: Generar tabla de amortización
print("\n\n3️⃣ TABLA DE AMORTIZACIÓN - PRÉSTAMO")
print("-" * 70)

prestamo = 100000
tasa_mensual = 0.015  # 1.5% mensual
cuotas = 6
cuota_fija = prestamo / cuotas

print(f"\nPréstamo: ${prestamo:,.2f}")
print(f"Tasa mensual: {tasa_mensual * 100}%")
print(f"Cuotas: {cuotas}\n")
print(f"{'Mes':>3} | {'Saldo Inicial':>15} | {'Interés':>12} | {'Amort.':>12} | {'Cuota':>12} | {'Saldo Final':>15}")
print("-" * 95)

saldo = prestamo

for mes in range(1, cuotas + 1):
    interes = saldo * tasa_mensual
    amortizacion = cuota_fija
    cuota_total = amortizacion + interes
    saldo_nuevo = saldo - amortizacion
    
    print(f"{mes:>3} | ${saldo:>14,.2f} | ${interes:>11,.2f} | ${amortizacion:>11,.2f} | ${cuota_total:>11,.2f} | ${saldo_nuevo:>14,.2f}")
    
    saldo = saldo_nuevo

# Ejemplo 4: Contador de días hábiles
print("\n\n4️⃣ CALCULAR RENDIMIENTO DIARIO COMPUESTO")
print("-" * 70)

inversion_inicial = 10000
rendimiento_diario = 0.001  # 0.1% diario
dias_habiles = 252  # Días de trading en un año

print(f"\nInversión inicial: ${inversion_inicial:,.2f}")
print(f"Rendimiento diario: {rendimiento_diario * 100}%")
print(f"Días hábiles al año: {dias_habiles}\n")

inversion = inversion_inicial

# Mostrar progreso cada 50 días
for dia in range(1, dias_habiles + 1):
    inversion = inversion * (1 + rendimiento_diario)
    
    if dia % 50 == 0 or dia == dias_habiles:
        ganancia = inversion - inversion_inicial
        rendimiento_acum = ((inversion / inversion_inicial) - 1) * 100
        print(f"Día {dia:>3}: ${inversion:>12,.2f} | Ganancia: ${ganancia:>10,.2f} | Rend: {rendimiento_acum:>6.2f}%")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - While y Break/Continue
# MAGIC %md
# MAGIC ## 🔁 BUCLES - Parte 3: while, break y continue
# MAGIC
# MAGIC ### Bucle while
# MAGIC
# MAGIC El bucle `while` repite **mientras** una condición sea True.
# MAGIC
# MAGIC ```python
# MAGIC while condicion:
# MAGIC     # Código que se repite
# MAGIC     # IMPORTANTE: La condición debe volverse False en algún momento
# MAGIC ```
# MAGIC
# MAGIC **Diferencia con for**:
# MAGIC * `for`: Sabes cuántas veces repetir
# MAGIC * `while`: No sabes cuántas veces, depende de una condición
# MAGIC
# MAGIC **Ejemplo**: ¿Cuántos años para duplicar una inversión?
# MAGIC
# MAGIC ```python
# MAGIC capital = 10000
# MAGIC objetivo = 20000
# MAGIC anios = 0
# MAGIC tasa = 0.07
# MAGIC
# MAGIC while capital < objetivo:
# MAGIC     capital = capital * (1 + tasa)
# MAGIC     anios += 1
# MAGIC
# MAGIC print(f"Duplicarás tu dinero en {anios} años")
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### break - Salir del bucle
# MAGIC
# MAGIC `break` **termina** el bucle inmediatamente.
# MAGIC
# MAGIC ```python
# MAGIC for precio in [100, 150, 80, 200]:
# MAGIC     if precio < 90:
# MAGIC         print("Precio muy bajo, deteniendo análisis")
# MAGIC         break
# MAGIC     print(f"Precio: ${precio}")
# MAGIC ```
# MAGIC
# MAGIC **Salida**:
# MAGIC ```
# MAGIC Precio: $100
# MAGIC Precio: $150
# MAGIC Precio muy bajo, deteniendo análisis
# MAGIC ```
# MAGIC (No procesa el 200)
# MAGIC
# MAGIC **Uso financiero**: Buscar la primera acción que cumpla un criterio
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### continue - Saltar a la siguiente iteración
# MAGIC
# MAGIC `continue` **salta** el resto del código y va a la siguiente vuelta del bucle.
# MAGIC
# MAGIC ```python
# MAGIC for precio in [100, -5, 150, 0, 200]:
# MAGIC     if precio <= 0:
# MAGIC         continue  # Saltar precios inválidos
# MAGIC     print(f"Precio válido: ${precio}")
# MAGIC ```
# MAGIC
# MAGIC **Salida**:
# MAGIC ```
# MAGIC Precio válido: $100
# MAGIC Precio válido: $150
# MAGIC Precio válido: $200
# MAGIC ```
# MAGIC (Omite -5 y 0)
# MAGIC
# MAGIC **Uso financiero**: Filtrar datos inválidos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Comparación: break vs continue
# MAGIC
# MAGIC ```python
# MAGIC print("CON BREAK:")
# MAGIC for i in range(1, 6):
# MAGIC     if i == 3:
# MAGIC         break  # Para TODO
# MAGIC     print(i)
# MAGIC # Salida: 1, 2
# MAGIC
# MAGIC print("\nCON CONTINUE:")
# MAGIC for i in range(1, 6):
# MAGIC     if i == 3:
# MAGIC         continue  # Salta solo el 3
# MAGIC     print(i)
# MAGIC # Salida: 1, 2, 4, 5
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚠️ Cuidado con while infinito
# MAGIC
# MAGIC **MAL** (bucle infinito):
# MAGIC ```python
# MAGIC while True:
# MAGIC     print("Esto nunca termina")  # ❌
# MAGIC ```
# MAGIC
# MAGIC **BIEN** (con condición de salida):
# MAGIC ```python
# MAGIC contador = 0
# MAGIC while contador < 10:
# MAGIC     print(contador)
# MAGIC     contador += 1  # IMPORTANTE: Cambiar la condición
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Código - While, Break, Continue
print("═" * 70)
print("EJEMPLO: while, break y continue")
print("═" * 70)

# Ejemplo 1: While - Cuántos años para alcanzar objetivo
print("\n1️⃣ WHILE: ¿CUÁNTOS AÑOS PARA ALCANZAR OBJETIVO?")
print("-" * 70)

inversion_inicial = 100000
objetivo = 250000
tasa_anual = 0.08  # 8%

inversion = inversion_inicial
anios = 0

print(f"Inversión inicial: ${inversion_inicial:,.2f}")
print(f"Objetivo: ${objetivo:,.2f}")
print(f"Tasa: {tasa_anual * 100}%\n")

while inversion < objetivo:
    anios += 1
    inversion = inversion * (1 + tasa_anual)
    print(f"Año {anios}: ${inversion:,.2f}")

print(f"\n✅ Alcanzarás tu objetivo en {anios} años")

# Ejemplo 2: Break - Buscar primera acción rentable
print("\n\n2️⃣ BREAK: BUSCAR PRIMERA ACCIÓN MUY RENTABLE")
print("-" * 70)

acciones = [
    {"ticker": "COME", "rendimiento": 0.05},
    {"ticker": "TRAN", "rendimiento": 0.08},
    {"ticker": "YPF", "rendimiento": 0.22},
    {"ticker": "MELI", "rendimiento": 0.18},
    {"ticker": "GGAL", "rendimiento": 0.09}
]

rendimiento_objetivo = 0.20

print(f"Buscando primera acción con rendimiento > {rendimiento_objetivo * 100}%\n")

for accion in acciones:
    print(f"Analizando {accion['ticker']}: {accion['rendimiento'] * 100:.1f}%")
    
    if accion["rendimiento"] > rendimiento_objetivo:
        print(f"\n✅ ¡ENCONTRADA! {accion['ticker']} con {accion['rendimiento'] * 100:.1f}%")
        print("Deteniendo búsqueda (break)")
        break
else:
    print("\n❌ No se encontró ninguna acción que cumpla el criterio")

# Ejemplo 3: Continue - Omitir datos inválidos
print("\n\n3️⃣ CONTINUE: OMITIR PRECIOS INVÁLIDOS")
print("-" * 70)

precios_raw = [5250.75, -10, 175.50, 0, 1450.00, None, 850.25]

print("Procesando lista de precios (algunos inválidos):\n")

precios_validos = []
total = 0

for precio in precios_raw:
    # Verificar si es inválido
    if precio is None or precio <= 0:
        print(f"⚠️  Precio inválido: {precio} - OMITIENDO (continue)")
        continue  # Saltar al siguiente
    
    # Si llegamos aquí, el precio es válido
    print(f"✅ Precio válido: ${precio:,.2f}")
    precios_validos.append(precio)
    total += precio

promedio = total / len(precios_validos) if precios_validos else 0

print(f"\nPrecios válidos: {len(precios_validos)}")
print(f"Promedio: ${promedio:,.2f}")

# Ejemplo 4: Combinar while con break
print("\n\n4️⃣ WHILE + BREAK: SIMULAR RETIROS HASTA AGOTAR FONDO")
print("-" * 70)

fondo = 50000
retiro_mensual = 3500
mes = 0
max_meses = 20  # Límite de seguridad

print(f"Fondo inicial: ${fondo:,.2f}")
print(f"Retiro mensual: ${retiro_mensual:,.2f}\n")

while fondo > 0:
    mes += 1
    
    if mes > max_meses:
        print(f"\n⚠️ Límite de {max_meses} meses alcanzado (break de seguridad)")
        break
    
    if fondo < retiro_mensual:
        print(f"Mes {mes}: Retiro final de ${fondo:,.2f} (insuficiente para retiro completo)")
        fondo = 0
    else:
        fondo -= retiro_mensual
        print(f"Mes {mes}: Retiro ${retiro_mensual:,.2f} | Saldo: ${fondo:,.2f}")

print(f"\n🚨 Fondo agotado en {mes} meses")

# Ejemplo 5: Continue con múltiples condiciones
print("\n\n5️⃣ CONTINUE: FILTRAR ACCIONES POR MÚTIPLES CRITERIOS")
print("-" * 70)

acciones_completas = [
    {"ticker": "YPF", "precio": 5250, "volumen": 1500000, "sector": "Energía"},
    {"ticker": "GGAL", "precio": 175, "volumen": 2500000, "sector": "Financiero"},
    {"ticker": "MELI", "precio": 1450, "volumen": 800000, "sector": "Tecnología"},
    {"ticker": "COME", "precio": 2, "volumen": 500000, "sector": "Servicios"},
    {"ticker": "TRAN", "precio": 850, "volumen": 300000, "sector": "Transporte"}
]

print("Filtros:")
print("  • Precio entre $100 y $6000")
print("  • Volumen > 1M")
print("  • Sector NO sea 'Transporte'\n")

acciones_seleccionadas = []

for accion in acciones_completas:
    # Filtro 1: Precio
    if accion["precio"] < 100 or accion["precio"] > 6000:
        print(f"❌ {accion['ticker']}: Precio fuera de rango (${accion['precio']:,})")
        continue
    
    # Filtro 2: Volumen
    if accion["volumen"] < 1000000:
        print(f"❌ {accion['ticker']}: Volumen bajo ({accion['volumen']:,})")
        continue
    
    # Filtro 3: Sector
    if accion["sector"] == "Transporte":
        print(f"❌ {accion['ticker']}: Sector excluido ({accion['sector']})")
        continue
    
    # Si pasó todos los filtros
    print(f"✅ {accion['ticker']}: CUMPLE todos los criterios")
    acciones_seleccionadas.append(accion["ticker"])

print(f"\n🎯 Acciones seleccionadas: {', '.join(acciones_seleccionadas)}")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Explicación - List Comprehensions
# MAGIC %md
# MAGIC ## 🚀 LIST COMPREHENSIONS: Sintaxis Compacta
# MAGIC
# MAGIC ### ¿Qué son?
# MAGIC
# MAGIC Una **list comprehension** es una forma **compacta** de crear listas usando un `for` en una sola línea.
# MAGIC
# MAGIC ### Forma Tradicional vs List Comprehension
# MAGIC
# MAGIC #### Forma tradicional (4 líneas)
# MAGIC ```python
# MAGIC precios = [100, 150, 200, 175]
# MAGIC precios_con_iva = []
# MAGIC
# MAGIC for precio in precios:
# MAGIC     precios_con_iva.append(precio * 1.21)
# MAGIC ```
# MAGIC
# MAGIC #### List comprehension (1 línea)
# MAGIC ```python
# MAGIC precios = [100, 150, 200, 175]
# MAGIC precios_con_iva = [precio * 1.21 for precio in precios]
# MAGIC ```
# MAGIC
# MAGIC ¡El resultado es el mismo!
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Sintaxis
# MAGIC
# MAGIC ```python
# MAGIC [expresion for elemento in secuencia]
# MAGIC ```
# MAGIC
# MAGIC **Partes**:
# MAGIC 1. **Expresión**: Qué hacer con cada elemento
# MAGIC 2. **for elemento in secuencia**: Recorrer la secuencia
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Con Condicional (Filtro)
# MAGIC
# MAGIC Puedes **filtrar** elementos con `if`:
# MAGIC
# MAGIC ```python
# MAGIC [expresion for elemento in secuencia if condicion]
# MAGIC ```
# MAGIC
# MAGIC **Ejemplo**: Solo precios mayores a 100
# MAGIC
# MAGIC #### Forma tradicional:
# MAGIC ```python
# MAGIC precios = [80, 150, 200, 90, 175]
# MAGIC precios_altos = []
# MAGIC
# MAGIC for precio in precios:
# MAGIC     if precio > 100:
# MAGIC         precios_altos.append(precio)
# MAGIC ```
# MAGIC
# MAGIC #### List comprehension:
# MAGIC ```python
# MAGIC precios = [80, 150, 200, 90, 175]
# MAGIC precios_altos = [precio for precio in precios if precio > 100]
# MAGIC ```
# MAGIC
# MAGIC Resultado: `[150, 200, 175]`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Ejemplos Financieros
# MAGIC
# MAGIC #### 1. Aplicar descuento
# MAGIC ```python
# MAGIC precios = [100, 150, 200]
# MAGIC con_descuento = [p * 0.9 for p in precios]
# MAGIC # [90.0, 135.0, 180.0]
# MAGIC ```
# MAGIC
# MAGIC #### 2. Calcular rendimientos
# MAGIC ```python
# MAGIC compras = [100, 150, 200]
# MAGIC ventas = [120, 140, 230]
# MAGIC rendimientos = [(v - c) / c for c, v in zip(compras, ventas)]
# MAGIC # [0.2, -0.067, 0.15]
# MAGIC ```
# MAGIC
# MAGIC #### 3. Filtrar acciones rentables
# MAGIC ```python
# MAGIC rendimientos = [0.12, -0.03, 0.08, 0.15]
# MAGIC rentables = [r for r in rendimientos if r > 0.10]
# MAGIC # [0.12, 0.15]
# MAGIC ```
# MAGIC
# MAGIC #### 4. Extraer tickers de un diccionario
# MAGIC ```python
# MAGIC cartera = {
# MAGIC     "YPF": 50,
# MAGIC     "GGAL": 100,
# MAGIC     "MELI": 25
# MAGIC }
# MAGIC tickers = [t for t in cartera.keys()]
# MAGIC # ['YPF', 'GGAL', 'MELI']
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ¿Cuándo usar List Comprehensions?
# MAGIC
# MAGIC ✅ **Transformar** cada elemento de una lista
# MAGIC ✅ **Filtrar** elementos de una lista
# MAGIC ✅ **Código más legible** (cuando es simple)
# MAGIC
# MAGIC ❌ **NO usar** si:
# MAGIC * La lógica es muy compleja
# MAGIC * Necesitas hacer múltiples operaciones
# MAGIC * El código se vuelve difícil de leer
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Comparación de Legibilidad
# MAGIC
# MAGIC **Simple** (list comprehension es mejor):
# MAGIC ```python
# MAGIC # ✅ Claro
# MAGIC cuadrados = [x**2 for x in range(10)]
# MAGIC
# MAGIC # ❌ Más verboso
# MAGIC cuadrados = []
# MAGIC for x in range(10):
# MAGIC     cuadrados.append(x**2)
# MAGIC ```
# MAGIC
# MAGIC **Complejo** (bucle tradicional es mejor):
# MAGIC ```python
# MAGIC # ❌ Difícil de leer
# MAGIC resultado = [x*2 if x > 10 else x/2 if x > 5 else x for x in datos if x > 0]
# MAGIC
# MAGIC # ✅ Más claro
# MAGIC resultado = []
# MAGIC for x in datos:
# MAGIC     if x > 0:
# MAGIC         if x > 10:
# MAGIC             resultado.append(x * 2)
# MAGIC         elif x > 5:
# MAGIC             resultado.append(x / 2)
# MAGIC         else:
# MAGIC             resultado.append(x)
# MAGIC ```
# MAGIC
# MAGIC 💡 **Regla**: Si tu list comprehension ocupa más de una línea o es difícil de entender, usa un `for` tradicional.

# COMMAND ----------

# DBTITLE 1,Código - List Comprehensions
print("═" * 70)
print("EJEMPLO: List Comprehensions en Finanzas")
print("═" * 70)

# Ejemplo 1: Aplicar IVA a lista de precios
print("\n1️⃣ APLICAR IVA (21%)")
print("-" * 70)

precios = [5250.75, 175.50, 1450.00, 850.25, 2.35]

print("Forma tradicional (con bucle):")
precios_con_iva_tradicional = []
for precio in precios:
    precios_con_iva_tradicional.append(precio * 1.21)

print("\nForma moderna (list comprehension):")
precios_con_iva = [precio * 1.21 for precio in precios]

print(f"\nPrecios originales: {precios}")
print(f"Precios con IVA:    {[round(p, 2) for p in precios_con_iva]}")

# Ejemplo 2: Filtrar acciones rentables
print("\n\n2️⃣ FILTRAR ACCIONES RENTABLES (>10%)")
print("-" * 70)

acciones_rendimientos = [
    ("YPF", 0.18),
    ("GGAL", 0.09),
    ("MELI", 0.04),
    ("LOMA", 0.15),
    ("TRAN", -0.03)
]

print("Todas las acciones:")
for ticker, rend in acciones_rendimientos:
    print(f"  {ticker}: {rend:+.1%}")

# Filtrar con list comprehension
rentables = [(ticker, rend) for ticker, rend in acciones_rendimientos if rend > 0.10]

print(f"\nAcciones rentables (>10%):")
for ticker, rend in rentables:
    print(f"  ✅ {ticker}: {rend:+.1%}")

# Ejemplo 3: Calcular rendimientos de múltiples operaciones
print("\n\n3️⃣ CALCULAR RENDIMIENTOS")
print("-" * 70)

operaciones = [
    {"ticker": "YPF", "compra": 5000, "venta": 5250},
    {"ticker": "GGAL", "compra": 150, "venta": 175},
    {"ticker": "MELI", "compra": 1500, "venta": 1450},
    {"ticker": "COME", "compra": 2.0, "venta": 2.5}
]

# Calcular rendimiento de cada operación
rendimientos = [((op["venta"] - op["compra"]) / op["compra"]) * 100 for op in operaciones]

for i, op in enumerate(operaciones):
    simbolo = "✅" if rendimientos[i] > 0 else "❌"
    print(f"{simbolo} {op['ticker']:6s}: Compra ${op['compra']:>8,.2f} | Venta ${op['venta']:>8,.2f} | Rend: {rendimientos[i]:+6.2f}%")

# Ejemplo 4: Extraer solo los tickers
print("\n\n4️⃣ EXTRAER TICKERS DE CARTERA")
print("-" * 70)

cartera = {
    "YPF": {"cantidad": 50, "precio": 5250.75},
    "GGAL": {"cantidad": 100, "precio": 175.50},
    "MELI": {"cantidad": 25, "precio": 1450.00}
}

# Extraer solo los tickers
tickers = [ticker for ticker in cartera.keys()]
print(f"Tickers en cartera: {', '.join(tickers)}")

# Calcular valor de cada posición
valores = [datos["cantidad"] * datos["precio"] for datos in cartera.values()]
print(f"Valores: {[f'${v:,.2f}' for v in valores]}")

# Ejemplo 5: Transformaciones complejas
print("\n\n5️⃣ CLASIFICAR PRECIOS CON CONDICIÓN")
print("-" * 70)

precios_acciones = [5250, 175, 1450, 2.5, 850, 12500]

print("Clasificación:")
print("  • > $5000: Premium")
print("  • > $1000: Alto")
print("  • > $100: Medio")
print("  • ≤ $100: Bajo\n")

# Con list comprehension (puede ser complejo)
clasificaciones = [
    "Premium" if p > 5000 else "Alto" if p > 1000 else "Medio" if p > 100 else "Bajo"
    for p in precios_acciones
]

for precio, clasificacion in zip(precios_acciones, clasificaciones):
    print(f"${precio:>8,.2f} → {clasificacion}")

# Ejemplo 6: Filtrar y transformar simultáneamente
print("\n\n6️⃣ FILTRAR Y TRANSFORMAR")
print("-" * 70)

precios_usd = [100, 45, 200, 30, 150, 15, 175]
tipo_cambio = 350  # USD a ARS

print(f"Precios en USD (solo > $50):\n{[p for p in precios_usd if p > 50]}")

# Convertir a ARS solo los que son > $50
precios_ars = [p * tipo_cambio for p in precios_usd if p > 50]
print(f"\nConvertidos a ARS:\n{[f'${p:,.0f}' for p in precios_ars]}")

# Ejemplo 7: Crear diccionario con comprehension
print("\n\n7️⃣ DICTIONARY COMPREHENSION")
print("-" * 70)

tickers = ["YPF", "GGAL", "MELI"]
precios = [5250.75, 175.50, 1450.00]

# Crear diccionario ticker: precio
diccionario_precios = {ticker: precio for ticker, precio in zip(tickers, precios)}

print("Diccionario de precios:")
for ticker, precio in diccionario_precios.items():
    print(f"  {ticker}: ${precio:,.2f}")

# Ejemplo 8: Comparación de rendimiento
print("\n\n8️⃣ COMPARACIÓN: FOR vs LIST COMPREHENSION")
print("-" * 70)

import time

precios_grandes = list(range(1, 100001))  # 100,000 precios

# Método 1: For tradicional
inicio = time.time()
con_iva_for = []
for p in precios_grandes:
    con_iva_for.append(p * 1.21)
tiempo_for = time.time() - inicio

# Método 2: List comprehension
inicio = time.time()
con_iva_comp = [p * 1.21 for p in precios_grandes]
tiempo_comp = time.time() - inicio

print(f"Procesar 100,000 precios:")
print(f"  For tradicional:      {tiempo_for:.4f} segundos")
print(f"  List comprehension:   {tiempo_comp:.4f} segundos")
print(f"  Diferencia:           {abs(tiempo_for - tiempo_comp):.4f} segundos")
print(f"  🚀 List comprehension es {tiempo_for/tiempo_comp:.1f}x más rápida")

print("\n" + "═" * 70)

# COMMAND ----------

# DBTITLE 1,Ejercicios Prácticos
# MAGIC %md
# MAGIC ## ✍️ EJERCICIOS PRÁCTICOS
# MAGIC
# MAGIC ### 🔹 Ejercicio 1: Condicional Básico
# MAGIC
# MAGIC **Tarea**: Crear un sistema de clasificación de precios.
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Crea una variable `precio_accion = 175.50`
# MAGIC 2. Si el precio es mayor a 1000, muestra "Acción de alto valor"
# MAGIC 3. Si no, muestra "Acción accesible"
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 2: If-Elif-Else
# MAGIC
# MAGIC **Tarea**: Clasificar rendimiento de una inversión.
# MAGIC
# MAGIC **Dato**: `rendimiento = 0.08` (8%)
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Si rendimiento > 15%: "Excelente"
# MAGIC 2. Si rendimiento > 10%: "Bueno"
# MAGIC 3. Si rendimiento > 5%: "Moderado"
# MAGIC 4. Si rendimiento > 0%: "Bajo"
# MAGIC 5. Si no: "Pérdida"
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 3: Operadores Lógicos
# MAGIC
# MAGIC **Tarea**: Filtrar una acción "Blue Chip".
# MAGIC
# MAGIC **Datos**:
# MAGIC ```python
# MAGIC precio = 5200
# MAGIC volumen = 1500000
# MAGIC rendimiento = 0.12
# MAGIC ```
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Es Blue Chip SI: precio < 10000 AND volumen > 1000000 AND rendimiento > 0.08
# MAGIC 2. Mostrar si cumple o no
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 4: Bucle For con Lista
# MAGIC
# MAGIC **Tarea**: Calcular el total de un portafolio.
# MAGIC
# MAGIC **Datos**:
# MAGIC ```python
# MAGIC valores = [10000, 5500, 7200, 12000, 3500]
# MAGIC ```
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Usa un bucle `for` para sumar todos los valores
# MAGIC 2. Muestra el total
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 5: For con Range
# MAGIC
# MAGIC **Tarea**: Proyección de interés compuesto.
# MAGIC
# MAGIC **Datos**:
# MAGIC * Capital inicial: $50,000
# MAGIC * Tasa: 6% anual
# MAGIC * Plazo: 5 años
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Usa `for anio in range(1, 6):`
# MAGIC 2. Calcula y muestra el capital al final de cada año
# MAGIC 3. Fórmula: `capital = capital * (1 + tasa)`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 6: While
# MAGIC
# MAGIC **Tarea**: ¿Cuántos años para duplicar?
# MAGIC
# MAGIC **Datos**:
# MAGIC * Capital inicial: $100,000
# MAGIC * Tasa: 8% anual
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Usa `while capital < 200000:`
# MAGIC 2. Cuenta los años
# MAGIC 3. Muestra el resultado
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 7: Break
# MAGIC
# MAGIC **Tarea**: Buscar la primera acción con rendimiento negativo.
# MAGIC
# MAGIC **Datos**:
# MAGIC ```python
# MAGIC acciones = [
# MAGIC     ("YPF", 0.15),
# MAGIC     ("GGAL", 0.08),
# MAGIC     ("MELI", -0.05),
# MAGIC     ("COME", 0.12)
# MAGIC ]
# MAGIC ```
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Usa un bucle `for`
# MAGIC 2. Cuando encuentres un rendimiento < 0, usa `break`
# MAGIC 3. Muestra cuál es la primera acción negativa
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 8: Continue
# MAGIC
# MAGIC **Tarea**: Procesar solo precios válidos.
# MAGIC
# MAGIC **Datos**:
# MAGIC ```python
# MAGIC precios = [5250, -10, 175, 0, 1450, None, 850]
# MAGIC ```
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Usa un bucle `for`
# MAGIC 2. Si el precio es `None` o <= 0, usa `continue`
# MAGIC 3. Suma solo los precios válidos
# MAGIC 4. Muestra el total
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 9: List Comprehension
# MAGIC
# MAGIC **Tarea**: Aplicar comisión a todas las operaciones.
# MAGIC
# MAGIC **Datos**:
# MAGIC ```python
# MAGIC montos = [10000, 5000, 15000, 7500, 20000]
# MAGIC comision = 0.015  # 1.5%
# MAGIC ```
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Usa list comprehension para calcular la comisión de cada monto
# MAGIC 2. Fórmula: `monto * comision`
# MAGIC 3. Muestra la lista de comisiones
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 10: List Comprehension con Filtro
# MAGIC
# MAGIC **Tarea**: Extraer solo rendimientos positivos.
# MAGIC
# MAGIC **Datos**:
# MAGIC ```python
# MAGIC rendimientos = [0.12, -0.03, 0.08, 0.15, -0.05, 0.04]
# MAGIC ```
# MAGIC
# MAGIC **Requisitos**:
# MAGIC 1. Usa list comprehension con `if`
# MAGIC 2. Filtra solo los rendimientos > 0
# MAGIC 3. Muestra la lista resultante
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 DESAFÍO FINAL: Sistema Completo de Análisis
# MAGIC
# MAGIC **Tarea**: Analizar un portafolio completo con todas las estructuras aprendidas.
# MAGIC
# MAGIC **Datos**:
# MAGIC ```python
# MAGIC cartera = [
# MAGIC     {"ticker": "YPF", "cantidad": 50, "precio_compra": 5000, "precio_actual": 5250},
# MAGIC     {"ticker": "GGAL", "cantidad": 100, "precio_compra": 150, "precio_actual": 175},
# MAGIC     {"ticker": "MELI", "cantidad": 25, "precio_compra": 1500, "precio_actual": 1450},
# MAGIC     {"ticker": "COME", "cantidad": 500, "precio_compra": 2.0, "precio_actual": 2.5}
# MAGIC ]
# MAGIC ```
# MAGIC
# MAGIC **Requisitos**:
# MAGIC
# MAGIC 1. **Calcular valor de cada posición** (cantidad * precio_actual)
# MAGIC
# MAGIC 2. **Calcular rendimiento** de cada acción:
# MAGIC    * Fórmula: `(precio_actual - precio_compra) / precio_compra`
# MAGIC
# MAGIC 3. **Clasificar cada acción**:
# MAGIC    * Si rendimiento > 10%: "Excelente"
# MAGIC    * Si rendimiento > 0%: "Positivo"
# MAGIC    * Si no: "Negativo"
# MAGIC
# MAGIC 4. **Usar continue** para saltar acciones con precio_actual = 0 o None
# MAGIC
# MAGIC 5. **Calcular totales**:
# MAGIC    * Inversión total (suma de cantidad * precio_compra)
# MAGIC    * Valor actual total (suma de cantidad * precio_actual)
# MAGIC    * Ganancia/Pérdida total
# MAGIC
# MAGIC 6. **Crear reporte** con:
# MAGIC    * Detalle de cada acción
# MAGIC    * Clasificación
# MAGIC    * Totales finales
# MAGIC    * Rendimiento total del portafolio en %
# MAGIC
# MAGIC **Resultado esperado**:
# MAGIC ```
# MAGIC === REPORTE DE PORTAFOLIO ===
# MAGIC
# MAGIC YPF:
# MAGIC   Cantidad: 50
# MAGIC   Inversión: $250,000.00
# MAGIC   Valor actual: $262,500.00
# MAGIC   Ganancia: $12,500.00 (+5.00%)
# MAGIC   Clasificación: Positivo
# MAGIC
# MAGIC ... (continuar con las demás)
# MAGIC
# MAGIC === TOTALES ===
# MAGIC Inversión total: $XXX,XXX.XX
# MAGIC Valor actual: $XXX,XXX.XX
# MAGIC Ganancia/Pérdida: $X,XXX.XX
# MAGIC Rendimiento: X.XX%
# MAGIC ```
# MAGIC
# MAGIC 💡 **Tip**: Usa todas las estructuras aprendidas: if-elif-else, for, continue, y list comprehensions.

# COMMAND ----------

# DBTITLE 1,Consultas con Genie Code
# MAGIC %md
# MAGIC ## 🤖 CONSULTAS CON GENIE CODE
# MAGIC
# MAGIC ### 🔀 Condicionales (if, elif, else)
# MAGIC
# MAGIC 1. ¿Qué diferencia hay entre `=` y `==` en Python?
# MAGIC 2. ¿Por qué es importante la indentación en los bloques if?
# MAGIC 3. ¿Puedo tener un `else` sin un `if`?
# MAGIC 4. ¿Cuántos `elif` puedo usar en una estructura condicional?
# MAGIC 5. ¿Qué pasa si ninguna condición se cumple y no hay `else`?
# MAGIC 6. Muéstrame 5 ejemplos de condicionales complejos en finanzas
# MAGIC 7. ¿Cómo escribo "si x está entre 10 y 20"?
# MAGIC 8. ¿Qué es un "condicional ternario" (inline if)?
# MAGIC 9. ¿Cómo verifico si una variable es None?
# MAGIC 10. ¿Qué valores se consideran "falsy" en Python?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔗 Operadores Lógicos (and, or, not)
# MAGIC
# MAGIC 11. ¿Cuál es la diferencia entre `and` y `or`?
# MAGIC 12. ¿Qué hace el operador `not`?
# MAGIC 13. ¿Cómo evaluar "si x NO está en una lista"?
# MAGIC 14. ¿Qué es "short-circuit evaluation" en Python?
# MAGIC 15. ¿Puedo combinar `and`, `or` y `not` en una sola condición?
# MAGIC 16. ¿Cuál es la precedencia entre `and`, `or` y `not`?
# MAGIC 17. Muéstrame ejemplos de filtros complejos con múltiples operadores
# MAGIC 18. ¿Cómo verifico si una variable está en un rango con `and`?
# MAGIC 19. ¿Qué es más eficiente: `and` o `or`?
# MAGIC 20. Crea un filtro complejo para acciones "Blue Chip" con 5 criterios
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔁 Bucles For
# MAGIC
# MAGIC 21. ¿Qué diferencia hay entre `for` y `while`?
# MAGIC 22. ¿Cómo itero sobre un diccionario en Python?
# MAGIC 23. ¿Qué es la función `enumerate()` y cuándo usarla?
# MAGIC 24. ¿Qué hace la función `zip()`?
# MAGIC 25. ¿Puedo modificar una lista mientras itero sobre ella?
# MAGIC 26. ¿Cómo itero sobre dos listas simultáneamente?
# MAGIC 27. ¿Qué es un "bucle anidado" y cuándo usarlo?
# MAGIC 28. Muéstrame cómo crear una matriz con bucles anidados
# MAGIC 29. ¿Cómo itero sobre los valores de un diccionario?
# MAGIC 30. ¿Cómo itero sobre los pares clave-valor de un diccionario?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔢 Range()
# MAGIC
# MAGIC 31. ¿Qué hace `range(10)`? ¿Empez a en 0 o en 1?
# MAGIC 32. ¿Cómo creo una secuencia de 5 a 15?
# MAGIC 33. ¿Cómo creo una secuencia de números pares del 0 al 20?
# MAGIC 34. ¿Puedo usar `range()` con números negativos?
# MAGIC 35. ¿Cómo creo una secuencia descendente (de 10 a 1)?
# MAGIC 36. ¿Qué diferencia hay entre `range(5)` y `list(range(5))`?
# MAGIC 37. ¿Puedo usar `range()` con floats (decimales)?
# MAGIC 38. Muéstrame cómo simular 30 años de inversión con range
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔄 While
# MAGIC
# MAGIC 39. ¿Cuándo debo usar `while` en lugar de `for`?
# MAGIC 40. ¿Qué es un "bucle infinito" y cómo evitarlo?
# MAGIC 41. ¿Cómo salir de un while con break?
# MAGIC 42. Dame un ejemplo de while en finanzas (ej: alcanzar un objetivo)
# MAGIC 43. ¿Qué pasa si la condición del while es siempre False?
# MAGIC 44. ¿Puedo usar `else` con un `while`?
# MAGIC 45. Muéstrame cómo simular un retiro mensual hasta agotar un fondo
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⛔ Break y Continue
# MAGIC
# MAGIC 46. ¿Qué diferencia hay entre `break` y `continue`?
# MAGIC 47. ¿Puedo usar `break` fuera de un bucle?
# MAGIC 48. ¿En qué situaciones financieras usaría `break`?
# MAGIC 49. ¿Cuándo es mejor usar `continue` que un `if`?
# MAGIC 50. ¿Qué pasa si uso `break` en un bucle anidado?
# MAGIC 51. Muéstrame cómo usar `break` para buscar un elemento específico
# MAGIC 52. Muéstrame cómo usar `continue` para saltar datos inválidos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🚀 List Comprehensions
# MAGIC
# MAGIC 53. ¿Qué ventajas tienen las list comprehensions sobre bucles for?
# MAGIC 54. ¿Son más rápidas las list comprehensions?
# MAGIC 55. ¿Cómo convierto un for tradicional a list comprehension?
# MAGIC 56. ¿Puedo usar if-else en una list comprehension?
# MAGIC 57. ¿Qué es una "dictionary comprehension"?
# MAGIC 58. ¿Qué es una "set comprehension"?
# MAGIC 59. ¿Cuándo NO debo usar list comprehensions?
# MAGIC 60. Muéstrame 10 ejemplos de list comprehensions en finanzas
# MAGIC 61. ¿Puedo anidar list comprehensions?
# MAGIC 62. ¿Cómo filtro y transformo simultáneamente con list comprehension?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📊 Aplicaciones Financieras
# MAGIC
# MAGIC 63. Crea un sistema de clasificación de riesgo con if-elif-else
# MAGIC 64. Calcula el VAN de un proyecto usando bucles
# MAGIC 65. Simula una tabla de amortización con for
# MAGIC 66. Encuentra la tasa de interés necesaria para un objetivo (while)
# MAGIC 67. Filtra acciones por múltiples criterios (operadores lógicos)
# MAGIC 68. Calcula promedios móviles con bucles
# MAGIC 69. Genera reportes automáticos de portafolio
# MAGIC 70. Crea un sistema de alertas de precios
# MAGIC 71. Simula escenarios de inversión (Monte Carlo básico)
# MAGIC 72. Calcula ratios financieros de múltiples empresas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚠️ Errores Comunes
# MAGIC
# MAGIC 73. ¿Qué significa "IndentationError"?
# MAGIC 74. ¿Por qué me da error "SyntaxError: invalid syntax" en un if?
# MAGIC 75. ¿Qué es "NameError" en un bucle?
# MAGIC 76. ¿Qué significa "UnboundLocalError"?
# MAGIC 77. ¿Por qué mi while no termina nunca?
# MAGIC 78. ¿Por qué mi list comprehension da resultados incorrectos?
# MAGIC 79. Muéstrame los 10 errores más comunes con estructuras de control
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🛠️ Comparación con Excel
# MAGIC
# MAGIC 80. ¿Cómo es `if` de Python vs `=SI()` de Excel?
# MAGIC 81. ¿Cómo replicar una fórmula de Excel arrastrada hacia abajo?
# MAGIC 82. ¿Cómo es un bucle `for` vs copiar una fórmula?
# MAGIC 83. Muéstrame equivalencias entre funciones Excel y Python
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🚀 Próximos Pasos
# MAGIC
# MAGIC 84. ¿Qué aprenderé en el notebook 0.3 (Funciones)?
# MAGIC 85. ¿Cómo puedo practicar más estructuras de control?
# MAGIC 86. Dame 10 ejercicios adicionales de dificultad media
# MAGIC 87. ¿Qué conceptos avanzados existen sobre bucles?
# MAGIC 88. ¿Qué es la "complejidad computacional" de un bucle?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🇦🇷 Contexto Argentino
# MAGIC
# MAGIC 89. Crea un sistema de clasificación de bonos argentinos
# MAGIC 90. Calcula el impacto de la inflación en una inversión (bucle)
# MAGIC 91. Simula la evolución del tipo de cambio USD/ARS
# MAGIC 92. Analiza rendimientos de CEDEARs con estructuras de control
# MAGIC 93. Crea alertas para acciones del Merval
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎉 ¡Felicitaciones!
# MAGIC
# MAGIC Has completado el **Notebook 0.2 - Estructuras de Control**.
# MAGIC
# MAGIC ### ¿Qué aprendiste?
# MAGIC
# MAGIC ✅ **Condicionales**: if, elif, else  
# MAGIC ✅ **Operadores lógicos**: and, or, not  
# MAGIC ✅ **Bucles for**: Iterar sobre listas, diccionarios  
# MAGIC ✅ **Range()**: Generar secuencias numéricas  
# MAGIC ✅ **While**: Repetir hasta que se cumpla una condición  
# MAGIC ✅ **Break y continue**: Controlar el flujo de bucles  
# MAGIC ✅ **List comprehensions**: Sintaxis compacta  
# MAGIC ✅ **Aplicaciones financieras**: Análisis de portafolios, proyecciones, filtros
# MAGIC
# MAGIC ### 👉 Próximo Paso
# MAGIC
# MAGIC Continuar con **Notebook 0.3 - Funciones y Módulos** donde aprenderás:
# MAGIC * Crear tus propias funciones
# MAGIC * Parámetros y valores de retorno
# MAGIC * Funciones reutilizables para finanzas
# MAGIC * Importar librerías (math, datetime)
# MAGIC
# MAGIC ¡Nos vemos en el próximo notebook! 🚀