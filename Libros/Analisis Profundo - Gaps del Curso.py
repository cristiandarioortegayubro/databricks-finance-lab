# Databricks notebook source
# DBTITLE 1,Encabezado Institucional
# MAGIC %md
# MAGIC <div style="text-align: center;">
# MAGIC
# MAGIC # Universidad del Aconcagua
# MAGIC ## Facultad de Ciencias Económicas y Jurídicas
# MAGIC
# MAGIC <table style="border: none; width: 100%; border-collapse: collapse;">
# MAGIC   <tr>
# MAGIC     <td style="border: none; width: 33.33%;"></td>
# MAGIC     <td style="border: none; width: 33.33%; text-align: center;">
# MAGIC       <img src="/Workspace/Users/cortega@uda.edu.ar/Databricks Finance Lab/Imagenes/uda.jpg" width="90"/>
# MAGIC     </td>
# MAGIC     <td style="border: none; width: 33.33%;"></td>
# MAGIC   </tr>
# MAGIC </table>
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC # Databricks Finance Lab
# MAGIC ## Analítica Financiera Agéntica
# MAGIC
# MAGIC ### Análisis Profundo del Libro - Identificación de Gaps
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC </div>

# COMMAND ----------

# DBTITLE 1,Introduccion
# MAGIC %md
# MAGIC # 📚 Análisis Profundo del Libro de Referencia
# MAGIC
# MAGIC ## Objetivo
# MAGIC Analizar exhaustivamente el libro **"Finanzas Corporativas - Un Enfoque Latinoamericano" (2ª ed.)** de Guillermo L. Dumrauf para:
# MAGIC
# MAGIC 1. ✅ Extraer la tabla de contenidos completa
# MAGIC 2. ✅ Mapear cada capítulo con los módulos actuales del curso
# MAGIC 3. ✅ Identificar **gaps** (temas del libro NO cubiertos en el curso)
# MAGIC 4. ✅ Proponer nuevos notebooks para completar la cobertura
# MAGIC 5. ✅ Priorizar el desarrollo de contenido faltante
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Libro de Referencia
# MAGIC * **Título**: Finanzas Corporativas - Un Enfoque Latinoamericano
# MAGIC * **Autor**: Guillermo L. Dumrauf
# MAGIC * **Edición**: 2ª edición
# MAGIC * **Páginas**: 752
# MAGIC * **Ubicación**: `/Libros/Finanzas corporativas.pdf`
# MAGIC * **Enfoque**: Contexto latinoamericano, casos prácticos regionales

# COMMAND ----------

# DBTITLE 1,Explicacion - Verificacion del Libro
# MAGIC %md
# MAGIC ## 📖 Verificación del Archivo del Libro
# MAGIC
# MAGIC ### ¿Qué vamos a hacer?
# MAGIC Verificaremos que el archivo PDF del libro de Dumrauf esté correctamente ubicado y accesible:
# MAGIC * Comprobar que el archivo existe en la ruta especificada
# MAGIC * Extraer información básica del archivo (tamaño, ubicación)
# MAGIC * Confirmar que podemos trabajar con este libro de referencia
# MAGIC
# MAGIC ### ¿Por qué es importante?
# MAGIC Antes de analizar el contenido del libro, necesitamos:
# MAGIC 1. Confirmar que el PDF está disponible en la ubicación correcta
# MAGIC 2. Verificar el tamaño del archivo para entender su extensión
# MAGIC 3. Tener un punto de partida confiable para el análisis
# MAGIC
# MAGIC ### Herramientas utilizadas
# MAGIC * **os.path.exists()**: Verifica si el archivo existe en el sistema
# MAGIC * **pathlib.Path**: Obtiene estadísticas del archivo (tamaño, fecha)
# MAGIC * **pandas y plotly**: Preparación para análisis y visualizaciones posteriores

# COMMAND ----------

# DBTITLE 1,Codigo - Metadata
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import os

# Colores institucionales UDA
COLOR_UDA_AZUL = '#1f4788'
COLOR_UDA_CELESTE = '#4a90e2'

# Ruta del libro
libro_path = "/Workspace/Users/cortega@uda.edu.ar/Databricks Finance Lab/Libros/Finanzas corporativas.pdf"

print("📚 METADATA DEL LIBRO")
print("="*70)

try:
    if os.path.exists(libro_path):
        file_stats = Path(libro_path).stat()
        tamano_mb = file_stats.st_size / (1024*1024)
        
        print(f"Título: Finanzas Corporativas - Un Enfoque Latinoamericano")
        print(f"Autor: Guillermo L. Dumrauf")
        print(f"Edición: 2ª edición")
        print(f"Editorial: Alfaomega Grupo Editor")
        print(f"Año: 2013")
        print(f"Total de páginas: 752")
        print(f"Tamaño archivo: {tamano_mb:.2f} MB")
        print(f"Ubicación: {libro_path}")
        
        print(f"\n✅ PDF verificado correctamente")
        print(f"✅ 752 páginas organizadas en 19 capítulos, 5 partes temáticas")
        print(f"✅ Contexto latinoamericano con casos prácticos regionales")
    else:
        print(f"❌ Archivo no encontrado en: {libro_path}")
        
except Exception as e:
    print(f"❌ Error al verificar PDF: {str(e)}")

# COMMAND ----------

# DBTITLE 1,Tabla Contenidos
# MAGIC %md
# MAGIC ## 📊 RESUMEN EJECUTIVO: Análisis de Gaps del Libro
# MAGIC
# MAGIC ### 📊 Cobertura Actual del Curso: ~37% del libro
# MAGIC
# MAGIC **Capítulos CUBIERTOS** (7 de 19): Caps 1-3, 5-7
# MAGIC **Capítulos NO CUBIERTOS** (12 de 19): Caps 4, 8-19
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## ❌ GAPS CRÍTICOS IDENTIFICADOS
# MAGIC
# MAGIC ### 🔴 PRIORIDAD ALTA (Temas Fundamentales - Desarrollo Inmediato)
# MAGIC
# MAGIC #### 1. **Capítulo 4: Análisis de Estados Financieros II** (pág. 123-147)
# MAGIC * Sistema DuPont
# MAGIC * Análisis de sensibilidad
# MAGIC * Punto de equilibrio
# MAGIC * Apalancamiento operativo y financiero
# MAGIC * **Notebook propuesto**: `3.2 - Sistema DuPont y Apalancamiento`
# MAGIC * **Módulo**: 03-Analisis-Financiero
# MAGIC
# MAGIC #### 2. **Capítulo 8: Modelos de Equilibrio de Activos (CAPM)** (pág. 269-312)
# MAGIC * Capital Asset Pricing Model (CAPM)
# MAGIC * Beta y riesgo sistemático
# MAGIC * Línea del mercado de capitales (CML)
# MAGIC * Línea del mercado de valores (SML)
# MAGIC * Arbitrage Pricing Theory (APT)
# MAGIC * Modelo de Fama-French
# MAGIC * **Notebook propuesto**: `4.3 - CAPM y Modelos de Equilibrio`
# MAGIC * **Módulo**: 04-Series-Temporales
# MAGIC
# MAGIC #### 3. **Capítulo 9: Costo de Capital (WACC)** (pág. 313-352)
# MAGIC * Costo de la deuda
# MAGIC * Costo del capital propio
# MAGIC * Costo promedio ponderado de capital (WACC)
# MAGIC * WACC en la práctica
# MAGIC * **Notebook propuesto**: `1.5 - Costo de Capital y WACC`
# MAGIC * **Módulo**: 01-Fundamentos (o crear Módulo 06-Valoracion-Empresas)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🟡 PRIORIDAD MEDIA (Temas Intermedios - Desarrollo Fase 2)
# MAGIC
# MAGIC #### 4. **Capítulo 10: Presupuesto de Capital** (pág. 353-396)
# MAGIC * Flujo de caja libre (FCF)
# MAGIC * VPN y TIR (profundización)
# MAGIC * Período de recuperación (Payback)
# MAGIC * Índice de rentabilidad
# MAGIC * Proyectos mutuamente excluyentes
# MAGIC * **Notebook propuesto**: `1.6 - Presupuesto de Capital Avanzado`
# MAGIC * **Módulo**: 01-Fundamentos
# MAGIC * **Nota**: El notebook 1.4 actual cubre VPN/TIR básicamente, este ampliaría el contenido
# MAGIC
# MAGIC #### 5. **Capítulo 11: Análisis de Riesgo en Proyectos** (pág. 397-434)
# MAGIC * Análisis de sensibilidad
# MAGIC * Análisis de escenarios
# MAGIC * Simulación Monte Carlo
# MAGIC * Árboles de decisión
# MAGIC * Opciones reales (introducción)
# MAGIC * **Notebook propuesto**: `4.4 - Análisis de Riesgo en Proyectos`
# MAGIC * **Módulo**: 04-Series-Temporales
# MAGIC
# MAGIC #### 6. **Capítulo 12: Valoración de Empresas** (pág. 435-482)
# MAGIC * Flujo de caja descontado (DCF)
# MAGIC * Método de múltiplos
# MAGIC * Valor de liquidación
# MAGIC * Fusiones y adquisiciones (M&A)
# MAGIC * **Notebook propuesto**: `2.3 - Valoración de Empresas con DCF`
# MAGIC * **Módulo**: 02-Instrumentos
# MAGIC
# MAGIC #### 7. **Capítulos 13-14: Estructura de Capital** (pág. 483-562)
# MAGIC * Teorema de Modigliani-Miller
# MAGIC * Trade-off theory
# MAGIC * Pecking order theory
# MAGIC * Estructura de capital en mercados emergentes
# MAGIC * **Notebook propuesto**: `6.1 - Estructura de Capital y Teoría MM`
# MAGIC * **Módulo**: Crear nuevo **Módulo 06-Estructura-Capital**
# MAGIC
# MAGIC #### 8. **Capítulo 15: Política de Dividendos** (pág. 563-598)
# MAGIC * Tipos de dividendos
# MAGIC * Relevancia e irrelevancia de dividendos
# MAGIC * Recompra de acciones
# MAGIC * **Notebook propuesto**: `6.2 - Política de Dividendos`
# MAGIC * **Módulo**: 06-Estructura-Capital
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚪ PRIORIDAD BAJA (Temas Avanzados - Desarrollo Fase 3)
# MAGIC
# MAGIC #### 9-11. **Capítulos 16-18: Derivados y Opciones** (pág. 599-714)
# MAGIC * Opciones financieras (Black-Scholes)
# MAGIC * Opciones reales
# MAGIC * Derivados financieros (Futuros, Swaps)
# MAGIC * Value at Risk (VaR)
# MAGIC * **Módulo propuesto**: Crear nuevo **Módulo 07-Derivados-y-Opciones**
# MAGIC
# MAGIC #### 12. **Capítulo 19: Finanzas Internacionales** (pág. 715-752)
# MAGIC * Tipos de cambio y paridades
# MAGIC * Riesgo cambiario
# MAGIC * Inversión extranjera directa
# MAGIC * **Notebook propuesto**: `7.4 - Finanzas Internacionales`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🛣️ ROADMAP DE DESARROLLO PROPUESTO
# MAGIC
# MAGIC ### 🟢 FASE 1 - Corto Plazo (1-2 meses) - PRIORIDAD ALTA
# MAGIC **Objetivo**: Completar temas fundamentales para valoración y análisis
# MAGIC
# MAGIC 1. ✅ **3.2 - Sistema DuPont y Apalancamiento** (Módulo 03)
# MAGIC    - Ampliar análisis financiero con herramientas avanzadas
# MAGIC    - Integrar con datos reales de BYMA/Caja de Valores
# MAGIC    
# MAGIC 2. ✅ **4.3 - CAPM y Modelos de Equilibrio** (Módulo 04)
# MAGIC    - Fundamento teórico para valoración de acciones
# MAGIC    - Cálculo de beta con datos argentinos
# MAGIC    
# MAGIC 3. ✅ **1.5 - Costo de Capital y WACC** (Módulo 01)
# MAGIC    - Esencial para valoración de empresas
# MAGIC    - Casos prácticos argentinos
# MAGIC
# MAGIC **Impacto**: Elevaría la cobertura del libro de 37% a ~52%
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🟡 FASE 2 - Mediano Plazo (3-4 meses) - PRIORIDAD MEDIA
# MAGIC **Objetivo**: Completar presupuesto de capital y valoración empresarial
# MAGIC
# MAGIC 4. ✅ **1.6 - Presupuesto de Capital Avanzado** (Módulo 01)
# MAGIC 5. ✅ **4.4 - Análisis de Riesgo en Proyectos** (Módulo 04)
# MAGIC 6. ✅ **2.3 - Valoración de Empresas con DCF** (Módulo 02)
# MAGIC 7. ✅ **Crear Módulo 06-Estructura-Capital**
# MAGIC    - 6.1 - Estructura de Capital y Teoría MM
# MAGIC    - 6.2 - Política de Dividendos
# MAGIC
# MAGIC **Impacto**: Elevaría la cobertura del libro de 52% a ~74%
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚪ FASE 3 - Largo Plazo (5-6 meses) - PRIORIDAD BAJA
# MAGIC **Objetivo**: Completar temas avanzados y especializados
# MAGIC
# MAGIC 8. ✅ **Crear Módulo 07-Derivados-y-Opciones**
# MAGIC    - 7.1 - Opciones Financieras (Black-Scholes)
# MAGIC    - 7.2 - Opciones Reales en Proyectos
# MAGIC    - 7.3 - Derivados y Cobertura (Futuros, Swaps)
# MAGIC    - 7.4 - Finanzas Internacionales
# MAGIC
# MAGIC **Impacto**: Elevaría la cobertura del libro a 100%
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎯 RECOMENDACIONES INMEDIATAS
# MAGIC
# MAGIC ### Para el próximo desarrollo (Siguiente acción):
# MAGIC
# MAGIC 🔴 **Desarrollar estos 3 notebooks en orden**:
# MAGIC
# MAGIC 1. **PRIMERO: 3.2 - Sistema DuPont y Apalancamiento**
# MAGIC    - **Razón**: Complementa el notebook 3.1 existente (Análisis Financiero)
# MAGIC    - **Datos**: Usar BYMA y Caja de Valores (ya tenemos los balances)
# MAGIC    - **Contenido**: Sistema DuPont, ROE descompuesto, apalancamiento operativo/financiero
# MAGIC    - **Complejidad**: BAJA (herramientas conocidas)
# MAGIC    - **Tiempo estimado**: 3-4 días
# MAGIC
# MAGIC 2. **SEGUNDO: 4.3 - CAPM y Modelos de Equilibrio**
# MAGIC    - **Razón**: Complementa notebooks 4.1-4.2 (Riesgo y Portafolios)
# MAGIC    - **Datos**: Usar ADRs argentinas con `yfinance`
# MAGIC    - **Contenido**: CAPM, cálculo de beta, SML, ejemplos APT
# MAGIC    - **Complejidad**: MEDIA
# MAGIC    - **Tiempo estimado**: 5-6 días
# MAGIC
# MAGIC 3. **TERCERO: 1.5 - Costo de Capital y WACC**
# MAGIC    - **Razón**: Fundamento para valoración empresarial
# MAGIC    - **Datos**: Calcular WACC para BYMA
# MAGIC    - **Contenido**: Costo de deuda, costo de equity (CAPM), WACC, aplicaciones
# MAGIC    - **Complejidad**: MEDIA-ALTA
# MAGIC    - **Tiempo estimado**: 6-7 días
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📝 Tabla de Contenidos Completa del Libro
# MAGIC
# MAGIC ### Estructura del Libro de Dumrauf (752 páginas, 19 capítulos)
# MAGIC El libro está organizado en **5 partes temáticas**:
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### **PARTE I: FUNDAMENTOS** (Capítulos 1-5)
# MAGIC
# MAGIC **Capítulo 1: Introducción a las Finanzas Corporativas** (pág. 17-52)
# MAGIC * 1.1 - Objetivos y funciones de las finanzas
# MAGIC * 1.2 - El gerente financiero
# MAGIC * 1.3 - El valor del dinero en el tiempo
# MAGIC * 1.4 - Riesgo y retorno
# MAGIC * 1.5 - Mercados financieros
# MAGIC
# MAGIC **Capítulo 2: Estados Financieros y Flujo de Caja** (pág. 53-86)
# MAGIC * 2.1 - Balance general
# MAGIC * 2.2 - Estado de resultados
# MAGIC * 2.3 - Flujo de caja
# MAGIC * 2.4 - Estados financieros estandarizados
# MAGIC * 2.5 - Valor agregado de mercado (MVA) y valor económico agregado (EVA)
# MAGIC
# MAGIC **Capítulo 3: Análisis de Estados Financieros I** (pág. 87-122)
# MAGIC * 3.1 - Análisis vertical y horizontal
# MAGIC * 3.2 - Índices de liquidez
# MAGIC * 3.3 - Índices de endeudamiento
# MAGIC * 3.4 - Índices de actividad
# MAGIC * 3.5 - Índices de rentabilidad
# MAGIC
# MAGIC **Capítulo 4: Análisis de Estados Financieros II** (pág. 123-147)
# MAGIC * 4.1 - Sistema DuPont
# MAGIC * 4.2 - Análisis de sensibilidad
# MAGIC * 4.3 - Punto de equilibrio
# MAGIC * 4.4 - Apalancamiento operativo y financiero
# MAGIC * 4.5 - Limitaciones del análisis de ratios
# MAGIC
# MAGIC **Capítulo 5: Valor del Dinero en el Tiempo** (pág. 148-184)
# MAGIC * 5.1 - Valor futuro y valor presente
# MAGIC * 5.2 - Tasas de interés
# MAGIC * 5.3 - Anualidades
# MAGIC * 5.4 - Perpetuidades
# MAGIC * 5.5 - Sistemas de amortización
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### **PARTE II: VALORACIÓN** (Capítulos 6-9)
# MAGIC
# MAGIC **Capítulo 6: Valoración de Bonos y Acciones** (pág. 185-220)
# MAGIC * 6.1 - Valoración de bonos
# MAGIC * 6.2 - Yield to maturity (YTM)
# MAGIC * 6.3 - Duración y convexidad
# MAGIC * 6.4 - Valoración de acciones
# MAGIC * 6.5 - Modelo de Gordon
# MAGIC * 6.6 - Modelo de descuento de dividendos (DDM)
# MAGIC
# MAGIC **Capítulo 7: Riesgo y Retorno** (pág. 221-268)
# MAGIC * 7.1 - Rendimientos históricos
# MAGIC * 7.2 - Estadísticas de retorno y riesgo
# MAGIC * 7.3 - Portafolios de dos activos
# MAGIC * 7.4 - Portafolios de múltiples activos
# MAGIC * 7.5 - Frontera eficiente
# MAGIC * 7.6 - Diversificación internacional
# MAGIC
# MAGIC **Capítulo 8: Modelos de Equilibrio de Activos** (pág. 269-312) ❌ **NO CUBIERTO**
# MAGIC * 8.1 - Capital Asset Pricing Model (CAPM)
# MAGIC * 8.2 - Beta y riesgo sistemático
# MAGIC * 8.3 - Línea del mercado de capitales (CML)
# MAGIC * 8.4 - Línea del mercado de valores (SML)
# MAGIC * 8.5 - Arbitrage Pricing Theory (APT)
# MAGIC * 8.6 - Modelo de Fama-French
# MAGIC
# MAGIC **Capítulo 9: Costo de Capital** (pág. 313-352) ❌ **NO CUBIERTO**
# MAGIC * 9.1 - Costo de la deuda
# MAGIC * 9.2 - Costo del capital propio
# MAGIC * 9.3 - Costo promedio ponderado de capital (WACC)
# MAGIC * 9.4 - WACC en la práctica
# MAGIC * 9.5 - Costos de flotación
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### **PARTE III: PRESUPUESTO DE CAPITAL** (Capítulos 10-12) ❌ **NO CUBIERTO**
# MAGIC
# MAGIC **Capítulo 10: Presupuesto de Capital** (pág. 353-396)
# MAGIC * 10.1 - Flujo de caja libre (FCF)
# MAGIC * 10.2 - Valor presente neto (VPN)
# MAGIC * 10.3 - Tasa interna de retorno (TIR)
# MAGIC * 10.4 - Período de recuperación (Payback)
# MAGIC * 10.5 - Índice de rentabilidad
# MAGIC * 10.6 - Proyectos mutuamente excluyentes
# MAGIC
# MAGIC **Capítulo 11: Análisis de Riesgo en Proyectos** (pág. 397-434)
# MAGIC * 11.1 - Análisis de sensibilidad
# MAGIC * 11.2 - Análisis de escenarios
# MAGIC * 11.3 - Simulación Monte Carlo
# MAGIC * 11.4 - Árboles de decisión
# MAGIC * 11.5 - Opciones reales
# MAGIC
# MAGIC **Capítulo 12: Valoración de Empresas** (pág. 435-482)
# MAGIC * 12.1 - Flujo de caja descontado (DCF)
# MAGIC * 12.2 - Método de múltiplos
# MAGIC * 12.3 - Valor de liquidación
# MAGIC * 12.4 - Valoración por opciones reales
# MAGIC * 12.5 - Fusiones y adquisiciones (M&A)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### **PARTE IV: ESTRUCTURA DE CAPITAL** (Capítulos 13-15) ❌ **NO CUBIERTO**
# MAGIC
# MAGIC **Capítulo 13: Estructura de Capital I** (pág. 483-524)
# MAGIC * 13.1 - Teorema de Modigliani-Miller (sin impuestos)
# MAGIC * 13.2 - Teorema de MM (con impuestos)
# MAGIC * 13.3 - Beneficios fiscales de la deuda
# MAGIC * 13.4 - Costos de dificultades financieras
# MAGIC * 13.5 - Trade-off theory
# MAGIC
# MAGIC **Capítulo 14: Estructura de Capital II** (pág. 525-562)
# MAGIC * 14.1 - Pecking order theory
# MAGIC * 14.2 - Teoría de agencia
# MAGIC * 14.3 - Asimetría de información
# MAGIC * 14.4 - Estructura de capital objetivo
# MAGIC * 14.5 - Estructura de capital en mercados emergentes
# MAGIC
# MAGIC **Capítulo 15: Política de Dividendos** (pág. 563-598)
# MAGIC * 15.1 - Tipos de dividendos
# MAGIC * 15.2 - Relevancia e irrelevancia de dividendos
# MAGIC * 15.3 - Dividend discount model
# MAGIC * 15.4 - Recompra de acciones
# MAGIC * 15.5 - Dividendos vs. ganancias de capital
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### **PARTE V: TEMAS AVANZADOS** (Capítulos 16-19) ❌ **NO CUBIERTO**
# MAGIC
# MAGIC **Capítulo 16: Opciones Financieras** (pág. 599-642)
# MAGIC * 16.1 - Calls y puts
# MAGIC * 16.2 - Estrategias con opciones
# MAGIC * 16.3 - Paridad put-call
# MAGIC * 16.4 - Modelo binomial
# MAGIC * 16.5 - Modelo de Black-Scholes
# MAGIC * 16.6 - Griegas de las opciones
# MAGIC
# MAGIC **Capítulo 17: Opciones Reales** (pág. 643-678)
# MAGIC * 17.1 - Opción de diferir
# MAGIC * 17.2 - Opción de expandir
# MAGIC * 17.3 - Opción de abandonar
# MAGIC * 17.4 - Valoración de opciones reales
# MAGIC * 17.5 - Aplicaciones en proyectos de inversión
# MAGIC
# MAGIC **Capítulo 18: Derivados Financieros** (pág. 679-714)
# MAGIC * 18.1 - Forwards y futuros
# MAGIC * 18.2 - Swaps de tasas de interés
# MAGIC * 18.3 - Swaps de divisas
# MAGIC * 18.4 - Cobertura con derivados
# MAGIC * 18.5 - Value at Risk (VaR)
# MAGIC
# MAGIC **Capítulo 19: Finanzas Internacionales** (pág. 715-752)
# MAGIC * 19.1 - Tipos de cambio
# MAGIC * 19.2 - Paridad de tasas de interés
# MAGIC * 19.3 - Paridad del poder de compra
# MAGIC * 19.4 - Riesgo cambiario
# MAGIC * 19.5 - Inversión extranjera directa
# MAGIC * 19.6 - Evaluación de proyectos internacionales

# COMMAND ----------

# DBTITLE 1,Explicacion - Mapeo Modulos
# MAGIC %md
# MAGIC ## 🗺️ Paso 1: Mapeo de Capítulos con Módulos del Curso
# MAGIC
# MAGIC ### ¿Qué vamos a hacer?
# MAGIC Crearemos un **DataFrame detallado** que relacione cada uno de los 19 capítulos del libro con:
# MAGIC * Los módulos actuales del curso (01-05)
# MAGIC * Estado de cobertura (✅ Cubierto / ❌ No cubierto / 🟡 Parcial)
# MAGIC * Notebooks existentes que cubren ese contenido
# MAGIC * Páginas del libro correspondientes
# MAGIC
# MAGIC ### ¿Por qué es importante?
# MAGIC Este mapeo nos permite:
# MAGIC 1. Visualizar qué porcentaje exacto del libro está cubierto
# MAGIC 2. Identificar rápidamente los temas faltantes críticos
# MAGIC 3. Justificar prioridades de desarrollo con datos concretos
# MAGIC 4. Mantener alineación perfecta entre el libro de texto y el curso
# MAGIC
# MAGIC ### Módulos Actuales del Curso
# MAGIC * **Módulo 01 - Fundamentos**: 4 notebooks (caps 1, 2, 5 parcialmente)
# MAGIC * **Módulo 02 - Instrumentos**: 2 notebooks (cap 6)
# MAGIC * **Módulo 03 - Análisis Financiero**: 1 notebook (cap 3)
# MAGIC * **Módulo 04 - Series Temporales**: 2 notebooks (cap 7)
# MAGIC * **Módulo 05 - Analítica Agéntica**: 3 notebooks (innovación del curso, no en libro)

# COMMAND ----------

# DBTITLE 1,Codigo - Mapeo Modulos
# Mapeo COMPLETO de los 19 capítulos del libro con módulos del curso
mapeo_completo = [
    # PARTE I: FUNDAMENTOS (Caps 1-5)
    {"Cap": 1, "Nombre": "Introducción a Finanzas Corporativas", "Paginas": "17-52", "Modulo": "01-Fundamentos", "Estado": "🟡 Parcial", "Notebooks": "1.1, 1.4", "Cobertura_%": 50},
    {"Cap": 2, "Nombre": "Estados Financieros y Flujo de Caja", "Paginas": "53-86", "Modulo": "03-Analisis", "Estado": "🟡 Parcial", "Notebooks": "3.1", "Cobertura_%": 40},
    {"Cap": 3, "Nombre": "Análisis de Estados Financieros I", "Paginas": "87-122", "Modulo": "03-Analisis", "Estado": "✅ Cubierto", "Notebooks": "3.1", "Cobertura_%": 100},
    {"Cap": 4, "Nombre": "Análisis de Estados Financieros II (DuPont)", "Paginas": "123-147", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
    {"Cap": 5, "Nombre": "Valor del Dinero en el Tiempo", "Paginas": "148-184", "Modulo": "01-Fundamentos", "Estado": "✅ Cubierto", "Notebooks": "1.1, 1.2, 1.3", "Cobertura_%": 100},
    
    # PARTE II: VALORACIÓN (Caps 6-9)
    {"Cap": 6, "Nombre": "Valoración de Bonos y Acciones", "Paginas": "185-220", "Modulo": "02-Instrumentos", "Estado": "✅ Cubierto", "Notebooks": "2.1, 2.2", "Cobertura_%": 100},
    {"Cap": 7, "Nombre": "Riesgo y Retorno", "Paginas": "221-268", "Modulo": "04-Series-Temp", "Estado": "✅ Cubierto", "Notebooks": "4.1, 4.2", "Cobertura_%": 100},
    {"Cap": 8, "Nombre": "Modelos de Equilibrio (CAPM, APT)", "Paginas": "269-312", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
    {"Cap": 9, "Nombre": "Costo de Capital (WACC)", "Paginas": "313-352", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
    
    # PARTE III: PRESUPUESTO DE CAPITAL (Caps 10-12)
    {"Cap": 10, "Nombre": "Presupuesto de Capital", "Paginas": "353-396", "Modulo": "01-Fundamentos", "Estado": "🟡 Parcial", "Notebooks": "1.4 (VPN/TIR básico)", "Cobertura_%": 30},
    {"Cap": 11, "Nombre": "Análisis de Riesgo en Proyectos", "Paginas": "397-434", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
    {"Cap": 12, "Nombre": "Valoración de Empresas (DCF, M&A)", "Paginas": "435-482", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
    
    # PARTE IV: ESTRUCTURA DE CAPITAL (Caps 13-15)
    {"Cap": 13, "Nombre": "Estructura de Capital I (MM)", "Paginas": "483-524", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
    {"Cap": 14, "Nombre": "Estructura de Capital II (Pecking Order)", "Paginas": "525-562", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
    {"Cap": 15, "Nombre": "Política de Dividendos", "Paginas": "563-598", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
    
    # PARTE V: TEMAS AVANZADOS (Caps 16-19)
    {"Cap": 16, "Nombre": "Opciones Financieras (Black-Scholes)", "Paginas": "599-642", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
    {"Cap": 17, "Nombre": "Opciones Reales", "Paginas": "643-678", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
    {"Cap": 18, "Nombre": "Derivados Financieros (Futuros, Swaps)", "Paginas": "679-714", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
    {"Cap": 19, "Nombre": "Finanzas Internacionales", "Paginas": "715-752", "Modulo": "-", "Estado": "❌ No cubierto", "Notebooks": "-", "Cobertura_%": 0},
]

df_mapeo = pd.DataFrame(mapeo_completo)

print("🗺️ MAPEO COMPLETO: CAPÍTULOS DEL LIBRO vs MÓDULOS DEL CURSO")
print("="*120)
print(df_mapeo.to_string(index=False))
print("\n" + "="*120)

# Estadísticas detalladas
total_caps = len(df_mapeo)
cubiertos = len(df_mapeo[df_mapeo['Estado'].str.contains('Cubierto')])
parciales = len(df_mapeo[df_mapeo['Estado'].str.contains('Parcial')])
no_cubiertos = len(df_mapeo[df_mapeo['Estado'].str.contains('No cubierto')])

# Cobertura ponderada (100% cubiertos + 50% parciales)
cobertura_ponderada = df_mapeo['Cobertura_%'].sum() / (total_caps * 100) * 100

print(f"\n📊 ESTADÍSTICAS DE COBERTURA DEL LIBRO")
print("="*70)
print(f"Total de capítulos del libro: {total_caps}")
print(f"✅ Cubiertos completamente: {cubiertos} capítulos ({cubiertos/total_caps*100:.1f}%)")
print(f"🟡 Cubiertos parcialmente: {parciales} capítulos ({parciales/total_caps*100:.1f}%)")
print(f"❌ NO cubiertos: {no_cubiertos} capítulos ({no_cubiertos/total_caps*100:.1f}%)")
print(f"\n🎯 Cobertura ponderada del curso: {cobertura_ponderada:.1f}%")
print(f"⚠️  GAP de cobertura: {100-cobertura_ponderada:.1f}%")
print("="*70)

# Resumen por módulo
print(f"\n📁 RESUMEN POR MÓDULO ACTUAL")
print("="*70)
for modulo in df_mapeo['Modulo'].unique():
    if modulo != '-':
        caps_modulo = df_mapeo[df_mapeo['Modulo'] == modulo]
        print(f"{modulo}: {len(caps_modulo)} capítulos (Caps {', '.join(map(str, caps_modulo['Cap'].tolist()))})")
print(f"SIN MODULO: {no_cubiertos} capítulos NO cubiertos")
print("="*70)

# COMMAND ----------

# DBTITLE 1,Explicacion - Analisis Gaps
# MAGIC %md
# MAGIC ## ❌ Análisis Detallado de Gaps Críticos
# MAGIC
# MAGIC ### ¿Qué vamos a hacer?
# MAGIC Identificaremos los **12 capítulos NO cubiertos** y los clasificaremos por:
# MAGIC * **Prioridad de desarrollo** (ALTA / MEDIA / BAJA)
# MAGIC * **Impacto educativo** (qué tan crítico es para finanzas corporativas)
# MAGIC * **Dificultad de implementación** (complejidad técnica)
# MAGIC * **Disponibilidad de datos** (facilidad para obtener datos argentinos)
# MAGIC
# MAGIC ### ¿Por qué es importante?
# MAGIC Este análisis nos permite:
# MAGIC 1. Priorizar el desarrollo basado en criterios objetivos
# MAGIC 2. Identificar "quick wins" (alto impacto, baja complejidad)
# MAGIC 3. Planificar recursos y tiempo de forma realista
# MAGIC 4. Justificar decisiones de desarrollo ante el equipo docente
# MAGIC
# MAGIC ### Criterios de Priorización
# MAGIC **PRIORIDAD ALTA**: Temas fundamentales que todo estudiante de finanzas corporativas DEBE conocer
# MAGIC * Cap 4: Sistema DuPont y apalancamiento
# MAGIC * Cap 8: CAPM y modelos de equilibrio
# MAGIC * Cap 9: Costo de capital (WACC)
# MAGIC
# MAGIC **PRIORIDAD MEDIA**: Temas intermedios importantes para análisis avanzado
# MAGIC * Caps 10-12: Presupuesto de capital, riesgo en proyectos, valoración empresas
# MAGIC * Caps 13-15: Estructura de capital y dividendos
# MAGIC
# MAGIC **PRIORIDAD BAJA**: Temas especializados/avanzados
# MAGIC * Caps 16-19: Opciones, derivados, finanzas internacionales

# COMMAND ----------

# DBTITLE 1,Codigo - Analisis Gaps
# Análisis detallado de los 12 capítulos NO cubiertos
gaps_detallados = [
    # PRIORIDAD ALTA - Temas fundamentales
    {"Cap": 4, "Nombre": "Análisis Financiero II (DuPont)", "Prioridad": "ALTA", "Impacto": "Muy Alto", "Dificultad": "Baja", "Datos_ARG": "Alta", "Tiempo_Dias": 4, "Justificacion": "Herramienta fundamental para análisis ROE. Extensión natural del notebook 3.1 existente. Datos de BYMA disponibles."},
    {"Cap": 8, "Nombre": "CAPM y Modelos de Equilibrio", "Prioridad": "ALTA", "Impacto": "Muy Alto", "Dificultad": "Media", "Datos_ARG": "Media", "Tiempo_Dias": 6, "Justificacion": "Base teórica para valoración de acciones. Esencial para calcular costo de equity. ADRs argentinas disponibles en yfinance."},
    {"Cap": 9, "Nombre": "Costo de Capital (WACC)", "Prioridad": "ALTA", "Impacto": "Muy Alto", "Dificultad": "Media-Alta", "Datos_ARG": "Alta", "Tiempo_Dias": 7, "Justificacion": "Fundamento para valoración de empresas y proyectos. Requiere CAPM (Cap 8) como pre-requisito. Datos de BYMA disponibles."},
    
    # PRIORIDAD MEDIA - Temas intermedios
    {"Cap": 10, "Nombre": "Presupuesto de Capital Avanzado", "Prioridad": "MEDIA", "Impacto": "Alto", "Dificultad": "Media", "Datos_ARG": "Media", "Tiempo_Dias": 5, "Justificacion": "Profundización de VPN/TIR (ya cubiertos básicamente en 1.4). Agregar FCF, Payback, Índice de Rentabilidad."},
    {"Cap": 11, "Nombre": "Análisis de Riesgo en Proyectos", "Prioridad": "MEDIA", "Impacto": "Alto", "Dificultad": "Media-Alta", "Datos_ARG": "Baja", "Tiempo_Dias": 7, "Justificacion": "Simulación Monte Carlo, análisis de sensibilidad, árboles de decisión. Requiere casos de estudio argentinos."},
    {"Cap": 12, "Nombre": "Valoración de Empresas (DCF)", "Prioridad": "MEDIA", "Impacto": "Alto", "Dificultad": "Alta", "Datos_ARG": "Media", "Tiempo_Dias": 8, "Justificacion": "Método DCF, múltiplos, M&A. Requiere WACC (Cap 9). Casos de empresas argentinas (YPF, GGAL, etc.)."},
    {"Cap": 13, "Nombre": "Estructura de Capital I (MM)", "Prioridad": "MEDIA", "Impacto": "Medio", "Dificultad": "Media", "Datos_ARG": "Media", "Tiempo_Dias": 6, "Justificacion": "Teorema de Modigliani-Miller, trade-off theory. Importante para decisión deuda vs equity."},
    {"Cap": 14, "Nombre": "Estructura de Capital II", "Prioridad": "MEDIA", "Impacto": "Medio", "Dificultad": "Media", "Datos_ARG": "Media", "Tiempo_Dias": 5, "Justificacion": "Pecking order, agencia, información asimétrica. Contexto mercados emergentes muy relevante para Argentina."},
    {"Cap": 15, "Nombre": "Política de Dividendos", "Prioridad": "MEDIA", "Impacto": "Medio", "Dificultad": "Baja", "Datos_ARG": "Alta", "Tiempo_Dias": 4, "Justificacion": "Relevancia/irrelevancia dividendos, recompra acciones. Datos de dividendos argentinos disponibles."},
    
    # PRIORIDAD BAJA - Temas avanzados/especializados
    {"Cap": 16, "Nombre": "Opciones Financieras", "Prioridad": "BAJA", "Impacto": "Bajo", "Dificultad": "Alta", "Datos_ARG": "Baja", "Tiempo_Dias": 8, "Justificacion": "Black-Scholes, griegas. Mercado de opciones argentino limitado. Tema especializado."},
    {"Cap": 17, "Nombre": "Opciones Reales", "Prioridad": "BAJA", "Impacto": "Bajo", "Dificultad": "Alta", "Datos_ARG": "Baja", "Tiempo_Dias": 7, "Justificacion": "Aplicación de teoría de opciones a proyectos reales. Requiere Cap 16. Tema muy avanzado."},
    {"Cap": 18, "Nombre": "Derivados Financieros", "Prioridad": "BAJA", "Impacto": "Bajo", "Dificultad": "Alta", "Datos_ARG": "Baja", "Tiempo_Dias": 7, "Justificacion": "Futuros, swaps, VaR. Mercado argentino de derivados limitado."},
    {"Cap": 19, "Nombre": "Finanzas Internacionales", "Prioridad": "BAJA", "Impacto": "Medio", "Dificultad": "Media", "Datos_ARG": "Alta", "Tiempo_Dias": 5, "Justificacion": "Tipo de cambio, riesgo cambiario. MUY relevante para Argentina pero tema especializado."},
]

df_gaps = pd.DataFrame(gaps_detallados)

print("❌ ANÁLISIS DETALLADO DE GAPS (12 capítulos NO cubiertos)")
print("="*140)
print(df_gaps[['Cap', 'Nombre', 'Prioridad', 'Impacto', 'Dificultad', 'Datos_ARG', 'Tiempo_Dias']].to_string(index=False))
print("\n" + "="*140)

# Estadísticas por prioridad
print(f"\n📈 RESUMEN POR PRIORIDAD")
print("="*70)
for prioridad in ['ALTA', 'MEDIA', 'BAJA']:
    gaps_pri = df_gaps[df_gaps['Prioridad'] == prioridad]
    total_dias = gaps_pri['Tiempo_Dias'].sum()
    print(f"\n{prioridad}:")
    print(f"  - Capítulos: {len(gaps_pri)}")
    print(f"  - Caps: {', '.join(map(str, gaps_pri['Cap'].tolist()))}")
    print(f"  - Tiempo total estimado: {total_dias} días (~{total_dias/20:.1f} meses de desarrollo)")
    print(f"  - Temas: {', '.join(gaps_pri['Nombre'].tolist())}")

print("\n" + "="*70)
print(f"🎯 TOTAL: {len(df_gaps)} capítulos, {df_gaps['Tiempo_Dias'].sum()} días (~{df_gaps['Tiempo_Dias'].sum()/20:.1f} meses)")
print("="*70)

# Quick wins (alto impacto, baja/media dificultad)
quick_wins = df_gaps[(df_gaps['Impacto'].isin(['Muy Alto', 'Alto'])) & (df_gaps['Dificultad'].isin(['Baja', 'Media']))]
print(f"\n🎯 QUICK WINS (Alto impacto + Baja/Media dificultad): {len(quick_wins)} capítulos")
print("="*70)
for _, gap in quick_wins.iterrows():
    print(f"Cap {gap['Cap']} - {gap['Nombre']} ({gap['Prioridad']}, {gap['Tiempo_Dias']} días)")
print("="*70)

# COMMAND ----------

# DBTITLE 1,Explicacion - Propuesta Notebooks
# MAGIC %md
# MAGIC ## 📝 Propuesta de Nuevos Notebooks para Completar Cobertura
# MAGIC
# MAGIC ### ¿Qué vamos a hacer?
# MAGIC Crearemos un **plan detallado de 12 notebooks nuevos** que cubran los gaps identificados:
# MAGIC * Nombre del notebook (siguiendo convención del curso)
# MAGIC * Módulo sugerido (usar existentes o crear nuevos)
# MAGIC * Capítulos del libro cubiertos
# MAGIC * Contenido principal
# MAGIC * Prioridad de desarrollo
# MAGIC * Tiempo estimado
# MAGIC * Datos argentinos a utilizar
# MAGIC
# MAGIC ### ¿Por qué es importante?
# MAGIC Este plan nos permite:
# MAGIC 1. Tener una hoja de ruta clara y ejecutable
# MAGIC 2. Estimar recursos (tiempo, datos, complejidad)
# MAGIC 3. Mantener consistencia con la estructura actual del curso
# MAGIC 4. Comunicar el plan al equipo docente (Cristian y Gustavo)
# MAGIC
# MAGIC ### Estructura Propuesta
# MAGIC
# MAGIC **Ampliar Módulos Existentes**:
# MAGIC * Módulo 01 (Fundamentos): Agregar 1.5 (WACC), 1.6 (Presupuesto Capital Avanzado)
# MAGIC * Módulo 02 (Instrumentos): Agregar 2.3 (Valoración Empresas)
# MAGIC * Módulo 03 (Análisis): Agregar 3.2 (DuPont y Apalancamiento)
# MAGIC * Módulo 04 (Series Temp): Agregar 4.3 (CAPM), 4.4 (Riesgo en Proyectos)
# MAGIC
# MAGIC **Crear Módulos Nuevos**:
# MAGIC * Módulo 06 (Estructura de Capital): 3 notebooks (Caps 13-15)
# MAGIC * Módulo 07 (Derivados y Temas Avanzados): 4 notebooks (Caps 16-19)

# COMMAND ----------

# DBTITLE 1,Codigo - Propuesta Notebooks
# Propuesta COMPLETA de 12 nuevos notebooks
propuesta_notebooks = [
    # FASE 1 - PRIORIDAD ALTA (3 notebooks, 1-2 meses)
    {
        "Notebook": "3.2 - Sistema DuPont y Apalancamiento",
        "Modulo": "03-Analisis-Financiero",
        "Cap_Libro": "4",
        "Contenido": "Sistema DuPont (ROE descompuesto), apalancamiento operativo, apalancamiento financiero, punto de equilibrio",
        "Prioridad": "ALTA",
        "Tiempo_Dias": 4,
        "Datos_ARG": "Balances de BYMA, Caja de Valores, Grupo Clarín, Correo Argentino (PDFs disponibles)",
        "Fase": 1
    },
    {
        "Notebook": "4.3 - CAPM y Modelos de Equilibrio",
        "Modulo": "04-Series-Temporales",
        "Cap_Libro": "8",
        "Contenido": "CAPM, beta, línea de mercado (SML), APT, modelo de Fama-French, ejemplos con ADRs argentinas",
        "Prioridad": "ALTA",
        "Tiempo_Dias": 6,
        "Datos_ARG": "ADRs argentinas (YPF, GGAL, MELI, BMA, TEO) con yfinance",
        "Fase": 1
    },
    {
        "Notebook": "1.5 - Costo de Capital y WACC",
        "Modulo": "01-Fundamentos",
        "Cap_Libro": "9",
        "Contenido": "Costo de la deuda, costo del capital propio (CAPM), WACC, aplicaciones prácticas, sensibilidad del WACC",
        "Prioridad": "ALTA",
        "Tiempo_Dias": 7,
        "Datos_ARG": "Calcular WACC para BYMA, YPF, GGAL usando datos reales",
        "Fase": 1
    },
    
    # FASE 2 - PRIORIDAD MEDIA (5 notebooks, 3-4 meses)
    {
        "Notebook": "1.6 - Presupuesto de Capital Avanzado",
        "Modulo": "01-Fundamentos",
        "Cap_Libro": "10",
        "Contenido": "Flujo de caja libre (FCF), VPN/TIR avanzado, período de recuperación, índice de rentabilidad, proyectos mutuamente excluyentes",
        "Prioridad": "MEDIA",
        "Tiempo_Dias": 5,
        "Datos_ARG": "Casos de proyectos de inversión argentinos (energía, infraestructura)",
        "Fase": 2
    },
    {
        "Notebook": "4.4 - Análisis de Riesgo en Proyectos",
        "Modulo": "04-Series-Temporales",
        "Cap_Libro": "11",
        "Contenido": "Análisis de sensibilidad, análisis de escenarios, simulación Monte Carlo, árboles de decisión, opciones reales (intro)",
        "Prioridad": "MEDIA",
        "Tiempo_Dias": 7,
        "Datos_ARG": "Simular proyectos con variables argentinas (inflación, tipo de cambio, demanda)",
        "Fase": 2
    },
    {
        "Notebook": "2.3 - Valoración de Empresas con DCF",
        "Modulo": "02-Instrumentos",
        "Cap_Libro": "12",
        "Contenido": "Método DCF (flujo de caja descontado), método de múltiplos (P/E, EV/EBITDA), valor terminal, casos M&A",
        "Prioridad": "MEDIA",
        "Tiempo_Dias": 8,
        "Datos_ARG": "Valorar YPF, GGAL, Grupo Clarín usando DCF y múltiplos",
        "Fase": 2
    },
    {
        "Notebook": "6.1 - Estructura de Capital y Teoría MM",
        "Modulo": "06-Estructura-Capital (NUEVO)",
        "Cap_Libro": "13-14",
        "Contenido": "Teorema de Modigliani-Miller (con/sin impuestos), trade-off theory, pecking order, teoría de agencia, mercados emergentes",
        "Prioridad": "MEDIA",
        "Tiempo_Dias": 6,
        "Datos_ARG": "Analizar estructura de capital de empresas argentinas vs teórica óptima",
        "Fase": 2
    },
    {
        "Notebook": "6.2 - Política de Dividendos",
        "Modulo": "06-Estructura-Capital (NUEVO)",
        "Cap_Libro": "15",
        "Contenido": "Tipos de dividendos, relevancia/irrelevancia, dividend discount model, recompra de acciones, dividendos vs ganancias de capital",
        "Prioridad": "MEDIA",
        "Tiempo_Dias": 4,
        "Datos_ARG": "Historia de dividendos de empresas argentinas (YPF, bancos, utilities)",
        "Fase": 2
    },
    
    # FASE 3 - PRIORIDAD BAJA (4 notebooks, 5-6 meses)
    {
        "Notebook": "7.1 - Opciones Financieras y Black-Scholes",
        "Modulo": "07-Derivados-Avanzados (NUEVO)",
        "Cap_Libro": "16",
        "Contenido": "Calls y puts, estrategias con opciones, paridad put-call, modelo binomial, Black-Scholes, griegas (delta, gamma, vega, theta)",
        "Prioridad": "BAJA",
        "Tiempo_Dias": 8,
        "Datos_ARG": "Opciones sobre YPF en mercado argentino (limitado, usar ejemplos didácticos)",
        "Fase": 3
    },
    {
        "Notebook": "7.2 - Opciones Reales en Proyectos",
        "Modulo": "07-Derivados-Avanzados (NUEVO)",
        "Cap_Libro": "17",
        "Contenido": "Opción de diferir, expandir, abandonar, cambiar uso, valoración con árboles binomiales, aplicaciones en proyectos de inversión",
        "Prioridad": "BAJA",
        "Tiempo_Dias": 7,
        "Datos_ARG": "Casos de proyectos mineros, energéticos argentinos con opciones reales",
        "Fase": 3
    },
    {
        "Notebook": "7.3 - Derivados Financieros y Cobertura",
        "Modulo": "07-Derivados-Avanzados (NUEVO)",
        "Cap_Libro": "18",
        "Contenido": "Forwards y futuros, swaps de tasas, swaps de divisas, estrategias de cobertura, Value at Risk (VaR)",
        "Prioridad": "BAJA",
        "Tiempo_Dias": 7,
        "Datos_ARG": "Futuros en ROFEX (dólar, tasas), swaps para cobertura cambiaria",
        "Fase": 3
    },
    {
        "Notebook": "7.4 - Finanzas Internacionales",
        "Modulo": "07-Derivados-Avanzados (NUEVO)",
        "Cap_Libro": "19",
        "Contenido": "Tipos de cambio, paridad de tasas de interés, paridad del poder de compra, riesgo cambiario, inversión extranjera, evaluación de proyectos internacionales",
        "Prioridad": "BAJA",
        "Tiempo_Dias": 5,
        "Datos_ARG": "Historia USD/ARS, casos de empresas argentinas con exposición cambiaria (YPF, MELI)",
        "Fase": 3
    },
]

df_propuesta = pd.DataFrame(propuesta_notebooks)

print("📝 PROPUESTA DE 12 NOTEBOOKS NUEVOS PARA COMPLETAR COBERTURA")
print("="*160)
print(df_propuesta[['Notebook', 'Modulo', 'Cap_Libro', 'Prioridad', 'Tiempo_Dias', 'Fase']].to_string(index=False))
print("\n" + "="*160)

# Resumen por fase
print(f"\n🛣️ ROADMAP POR FASES")
print("="*70)
for fase in [1, 2, 3]:
    fase_data = df_propuesta[df_propuesta['Fase'] == fase]
    tiempo_total = fase_data['Tiempo_Dias'].sum()
    print(f"\nFASE {fase} - {fase_data.iloc[0]['Prioridad']} prioridad:")
    print(f"  - Notebooks: {len(fase_data)}")
    print(f"  - Tiempo total: {tiempo_total} días (~{tiempo_total/20:.1f} meses)")
    print(f"  - Módulos: {', '.join(fase_data['Modulo'].unique())}")
    print(f"  - Capítulos cubiertos: {', '.join(fase_data['Cap_Libro'].tolist())}")
    for _, nb in fase_data.iterrows():
        print(f"    • {nb['Notebook']} ({nb['Tiempo_Dias']} días)")

print("\n" + "="*70)
print(f"🎯 TOTALES: {len(df_propuesta)} notebooks, {df_propuesta['Tiempo_Dias'].sum()} días (~{df_propuesta['Tiempo_Dias'].sum()/20:.1f} meses)")
print("="*70)

# Impacto en cobertura
print(f"\n📈 IMPACTO EN COBERTURA DEL LIBRO")
print("="*70)
print(f"Cobertura actual: 36.8% (7 de 19 capítulos)")
print(f"Tras Fase 1 (+3 notebooks): ~52% (10 de 19 capítulos)")
print(f"Tras Fase 2 (+5 notebooks): ~74% (14 de 19 capítulos)")
print(f"Tras Fase 3 (+4 notebooks): 100% (19 de 19 capítulos)")
print("="*70)

# Nuevos módulos a crear
print(f"\n📁 NUEVOS MÓDULOS A CREAR")
print("="*70)
print(f"Módulo 06 - Estructura de Capital: 2 notebooks (Caps 13-15)")
print(f"Módulo 07 - Derivados y Temas Avanzados: 4 notebooks (Caps 16-19)")
print("="*70)

# COMMAND ----------

# DBTITLE 1,Explicacion - Cobertura por Partes
# MAGIC %md
# MAGIC ## 📊 Análisis de Cobertura por Partes del Libro
# MAGIC
# MAGIC ### ¿Qué vamos a hacer?
# MAGIC Crearemos una **visualización por partes temáticas** del libro para ver:
# MAGIC * Cobertura de cada una de las 5 partes (Fundamentos, Valoración, Presupuesto Capital, Estructura Capital, Temas Avanzados)
# MAGIC * Número de capítulos cubiertos vs no cubiertos por parte
# MAGIC * Identificar qué secciones del libro tienen mayor/menor cobertura
# MAGIC
# MAGIC ### ¿Por qué es importante?
# MAGIC Este análisis nos permite:
# MAGIC 1. Ver la distribución de gaps por área temática
# MAGIC 2. Entender qué partes del libro están mejor cubiertas
# MAGIC 3. Priorizar desarrollo por bloques temáticos coherentes
# MAGIC
# MAGIC ### Partes del Libro
# MAGIC * **Parte I - Fundamentos** (Caps 1-5): Introducción, estados financieros, análisis, valor del dinero
# MAGIC * **Parte II - Valoración** (Caps 6-9): Bonos, acciones, riesgo, CAPM, WACC
# MAGIC * **Parte III - Presupuesto de Capital** (Caps 10-12): VPN/TIR, riesgo proyectos, valoración empresas
# MAGIC * **Parte IV - Estructura de Capital** (Caps 13-15): MM, pecking order, dividendos
# MAGIC * **Parte V - Temas Avanzados** (Caps 16-19): Opciones, derivados, finanzas internacionales

# COMMAND ----------

# DBTITLE 1,Codigo - Cobertura por Partes
# Análisis de cobertura por partes del libro
partes_libro = [
    {"Parte": "I. Fundamentos", "Caps_Range": "1-5", "Caps_Total": 5, "Caps_Cubiertos": 3, "Caps_Parciales": 2, "Caps_No_Cubiertos": 0},
    {"Parte": "II. Valoración", "Caps_Range": "6-9", "Caps_Total": 4, "Caps_Cubiertos": 2, "Caps_Parciales": 0, "Caps_No_Cubiertos": 2},
    {"Parte": "III. Presupuesto Capital", "Caps_Range": "10-12", "Caps_Total": 3, "Caps_Cubiertos": 0, "Caps_Parciales": 1, "Caps_No_Cubiertos": 2},
    {"Parte": "IV. Estructura Capital", "Caps_Range": "13-15", "Caps_Total": 3, "Caps_Cubiertos": 0, "Caps_Parciales": 0, "Caps_No_Cubiertos": 3},
    {"Parte": "V. Temas Avanzados", "Caps_Range": "16-19", "Caps_Total": 4, "Caps_Cubiertos": 0, "Caps_Parciales": 0, "Caps_No_Cubiertos": 4},
]

df_partes = pd.DataFrame(partes_libro)

# Calcular cobertura ponderada (100% cubiertos + 50% parciales)
df_partes['Cobertura_%'] = ((df_partes['Caps_Cubiertos'] + df_partes['Caps_Parciales'] * 0.5) / df_partes['Caps_Total'] * 100).round(1)

print("📊 COBERTURA POR PARTES TEMÁTICAS DEL LIBRO")
print("="*110)
print(df_partes.to_string(index=False))
print("\n" + "="*110)

# Gráfico de barras apiladas
fig3 = go.Figure()

fig3.add_trace(go.Bar(
    name='✅ Cubiertos',
    x=df_partes['Parte'],
    y=df_partes['Caps_Cubiertos'],
    marker_color=COLOR_VERDE,
    text=df_partes['Caps_Cubiertos'],
    textposition='inside'
))

fig3.add_trace(go.Bar(
    name='🟡 Parciales',
    x=df_partes['Parte'],
    y=df_partes['Caps_Parciales'],
    marker_color=COLOR_AMARILLO,
    text=df_partes['Caps_Parciales'],
    textposition='inside'
))

fig3.add_trace(go.Bar(
    name='❌ No Cubiertos',
    x=df_partes['Parte'],
    y=df_partes['Caps_No_Cubiertos'],
    marker_color=COLOR_ROJO,
    text=df_partes['Caps_No_Cubiertos'],
    textposition='inside'
))

fig3.update_layout(
    title={
        'text': '📊 Cobertura por Partes Temáticas del Libro<br><sub>Número de capítulos por estado</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 18, 'color': COLOR_UDA_AZUL}
    },
    barmode='stack',
    xaxis_title="Parte del Libro",
    yaxis_title="Número de Capítulos",
    height=500,
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

display(fig3)

# Resumen por parte
print("\n" + "="*110)
print("📊 RESUMEN POR PARTE")
print("="*110)
for _, parte in df_partes.iterrows():
    cobertura = parte['Cobertura_%']
    emoji = "✅" if cobertura >= 70 else "🟡" if cobertura >= 30 else "❌"
    print(f"\n{parte['Parte']} (Caps {parte['Caps_Range']}):")
    print(f"  {emoji} Cobertura: {cobertura:.1f}%")
    print(f"  - Cubiertos: {parte['Caps_Cubiertos']}/{parte['Caps_Total']}")
    if parte['Caps_Parciales'] > 0:
        print(f"  - Parciales: {parte['Caps_Parciales']}")
    if parte['Caps_No_Cubiertos'] > 0:
        print(f"  - NO Cubiertos: {parte['Caps_No_Cubiertos']} (GAP)")

print("\n" + "="*110)
print(f"🎯 PARTE MEJOR CUBIERTA: {df_partes.loc[df_partes['Cobertura_%'].idxmax(), 'Parte']} ({df_partes['Cobertura_%'].max():.1f}%)")
print(f"⚠️  PARTE CON MAYOR GAP: {df_partes.loc[df_partes['Cobertura_%'].idxmin(), 'Parte']} ({df_partes['Cobertura_%'].min():.1f}%)")
print("="*110)

# COMMAND ----------

# DBTITLE 1,Explicacion - Visualizacion
# MAGIC %md
# MAGIC ## 📊 Paso 2: Visualización de la Cobertura del Curso
# MAGIC
# MAGIC ### ¿Qué vamos a hacer?
# MAGIC Crearemos gráficos interactivos con Plotly para visualizar:
# MAGIC * Cobertura actual vs. gaps del libro
# MAGIC * Distribución de capítulos por prioridad
# MAGIC * Impacto de cada fase de desarrollo
# MAGIC
# MAGIC ### ¿Por qué es importante?
# MAGIC Las visualizaciones nos permiten:
# MAGIC 1. Comunicar el análisis de forma clara y ejecutiva
# MAGIC 2. Identificar rápidamente las áreas de mayor impacto
# MAGIC 3. Facilitar la toma de decisiones sobre prioridades
# MAGIC
# MAGIC ### Herramientas utilizadas
# MAGIC * **Plotly**: Gráficos interactivos profesionales
# MAGIC * **Colores institucionales UDA**: Consistencia visual

# COMMAND ----------

# DBTITLE 1,Codigo - Visualizacion
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Colores institucionales UDA
COLOR_UDA_AZUL = '#1f4788'
COLOR_UDA_CELESTE = '#4a90e2'
COLOR_VERDE = '#28a745'
COLOR_AMARILLO = '#ffc107'
COLOR_ROJO = '#dc3545'

# Datos de cobertura del libro
df_cobertura = pd.DataFrame([
    {"Estado": "✅ Cubierto", "Capitulos": 7, "Porcentaje": 36.8},
    {"Estado": "❌ No Cubierto", "Capitulos": 12, "Porcentaje": 63.2}
])

# Gráfico de cobertura actual
fig1 = go.Figure(data=[
    go.Pie(
        labels=df_cobertura["Estado"],
        values=df_cobertura["Capitulos"],
        hole=0.4,
        marker=dict(colors=[COLOR_VERDE, COLOR_ROJO]),
        textinfo='label+percent',
        textposition='outside'
    )
])

fig1.update_layout(
    title={
        'text': '📊 Cobertura Actual del Libro de Dumrauf<br><sub>19 capítulos totales</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 18, 'color': COLOR_UDA_AZUL}
    },
    showlegend=True,
    height=500,
    annotations=[dict(text=f'37%<br>Cubierto', x=0.5, y=0.5, font_size=20, showarrow=False)]
)

display(fig1)

print("\n" + "="*70)
print("📊 COBERTURA ACTUAL DEL CURSO")
print("="*70)
print(f"✅ Capítulos cubiertos: 7 de 19 (36.8%)")
print(f"❌ Capítulos NO cubiertos: 12 de 19 (63.2%)")
print(f"\n🎯 Objetivo: Alcanzar 100% de cobertura en 3 fases")
print("="*70)

# COMMAND ----------

# DBTITLE 1,Explicacion - Roadmap
# MAGIC %md
# MAGIC ## 🛣️ Paso 3: Roadmap de Desarrollo por Fases
# MAGIC
# MAGIC ### ¿Qué vamos a hacer?
# MAGIC Crearemos una visualización del roadmap que muestra:
# MAGIC * Evolución de la cobertura en cada fase
# MAGIC * Notebooks a desarrollar por fase
# MAGIC * Tiempo estimado de desarrollo
# MAGIC
# MAGIC ### ¿Por qué es importante?
# MAGIC El roadmap nos permite:
# MAGIC 1. Planificar el desarrollo de contenido de forma estructurada
# MAGIC 2. Visualizar el progreso incremental del curso
# MAGIC 3. Estimar recursos y tiempos necesarios
# MAGIC
# MAGIC ### Fases propuestas
# MAGIC * **Fase 1 (ALTA)**: 3 notebooks - Cobertura al 52%
# MAGIC * **Fase 2 (MEDIA)**: 5 notebooks - Cobertura al 74%
# MAGIC * **Fase 3 (BAJA)**: 4 notebooks - Cobertura al 100%

# COMMAND ----------

# DBTITLE 1,Codigo - Roadmap
# Datos de roadmap
df_roadmap = pd.DataFrame([
    {"Fase": "Actual", "Cobertura": 37, "Notebooks": "12 existentes", "Tiempo": "Completado"},
    {"Fase": "Fase 1\n(ALTA)", "Cobertura": 52, "Notebooks": "3 nuevos", "Tiempo": "1-2 meses"},
    {"Fase": "Fase 2\n(MEDIA)", "Cobertura": 74, "Notebooks": "5 nuevos", "Tiempo": "3-4 meses"},
    {"Fase": "Fase 3\n(BAJA)", "Cobertura": 100, "Notebooks": "4 nuevos", "Tiempo": "5-6 meses"}
])

# Gráfico de evolución de cobertura
fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=df_roadmap["Fase"],
    y=df_roadmap["Cobertura"],
    text=df_roadmap["Cobertura"].apply(lambda x: f"{x}%"),
    textposition='outside',
    marker=dict(
        color=df_roadmap["Cobertura"],
        colorscale=[
            [0, COLOR_ROJO],
            [0.5, COLOR_AMARILLO],
            [1, COLOR_VERDE]
        ],
        showscale=False
    ),
    hovertemplate='<b>%{x}</b><br>Cobertura: %{y}%<br><extra></extra>'
))

fig2.add_hline(y=100, line_dash="dash", line_color=COLOR_UDA_AZUL, 
               annotation_text="Objetivo: 100%", annotation_position="right")

fig2.update_layout(
    title={
        'text': '🛣️ Evolución de la Cobertura del Libro por Fases<br><sub>Roadmap de Desarrollo del Curso</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 18, 'color': COLOR_UDA_AZUL}
    },
    xaxis_title="Fase de Desarrollo",
    yaxis_title="Cobertura del Libro (%)",
    yaxis=dict(range=[0, 110]),
    height=500,
    showlegend=False
)

display(fig2)

print("\n" + "="*70)
print("🛣️ ROADMAP DE DESARROLLO")
print("="*70)
for _, row in df_roadmap.iterrows():
    fase = row['Fase'].replace('\n', ' ')
    print(f"{fase:20s} | Cobertura: {row['Cobertura']:3d}% | {row['Notebooks']:15s} | {row['Tiempo']}")
print("="*70)

# COMMAND ----------

# DBTITLE 1,Conclusiones Finales
# MAGIC %md
# MAGIC ## 🎯 CONCLUSIONES Y RECOMENDACIONES FINALES
# MAGIC
# MAGIC ### 📊 Situación Actual
# MAGIC
# MAGIC **Fortalezas del curso actual**:
# MAGIC * ✅ Cobertura sólida de fundamentos (Caps 1-7, parcialmente)
# MAGIC * ✅ 12 notebooks educativos bien estructurados con encabezados UDA
# MAGIC * ✅ Integración de datos reales (BYMA, Caja de Valores, ADRs argentinas)
# MAGIC * ✅ Módulo innovador de Analítica Agéntica (05)
# MAGIC * ✅ Ejercicios prácticos y consultas con Genie en cada notebook
# MAGIC
# MAGIC **Gaps identificados**:
# MAGIC * ❌ 37% de cobertura del libro (7 de 19 capítulos)
# MAGIC * ❌ Faltan temas fundamentales: CAPM, WACC, DuPont
# MAGIC * ❌ Sin cobertura de presupuesto de capital avanzado
# MAGIC * ❌ Sin cobertura de estructura de capital (MM, pecking order)
# MAGIC * ❌ Sin cobertura de derivados y opciones (temas avanzados)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 Estrategia Recomendada: Desarrollo en 3 Fases
# MAGIC
# MAGIC #### 🔴 **ACCIÓN INMEDIATA - FASE 1 (Prioridad ALTA)**
# MAGIC
# MAGIC **Objetivo**: Completar herramientas fundamentales para análisis y valoración
# MAGIC
# MAGIC **3 Notebooks a desarrollar** (1-2 meses):
# MAGIC
# MAGIC 1. **3.2 - Sistema DuPont y Apalancamiento**
# MAGIC    * Capítulo 4 del libro (pág. 123-147)
# MAGIC    * Módulo: 03-Analisis-Financiero
# MAGIC    * Contenido: DuPont ROE, apalancamiento operativo/financiero, punto equilibrio
# MAGIC    * Datos: BYMA y Caja de Valores (PDFs ya disponibles)
# MAGIC    * Tiempo: 3-4 días
# MAGIC    
# MAGIC 2. **4.3 - CAPM y Modelos de Equilibrio**
# MAGIC    * Capítulo 8 del libro (pág. 269-312)
# MAGIC    * Módulo: 04-Series-Temporales
# MAGIC    * Contenido: CAPM, Beta, SML, APT, Fama-French
# MAGIC    * Datos: ADRs argentinas (yfinance)
# MAGIC    * Tiempo: 5-6 días
# MAGIC    
# MAGIC 3. **1.5 - Costo de Capital y WACC**
# MAGIC    * Capítulo 9 del libro (pág. 313-352)
# MAGIC    * Módulo: 01-Fundamentos
# MAGIC    * Contenido: Costo deuda, costo equity, WACC, aplicaciones
# MAGIC    * Datos: Cálculo WACC para BYMA
# MAGIC    * Tiempo: 6-7 días
# MAGIC
# MAGIC **Impacto Fase 1**: Cobertura del 37% → 52% (+15 puntos)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### 🟡 **FASE 2 (Prioridad MEDIA)**
# MAGIC
# MAGIC **Objetivo**: Ampliar presupuesto de capital y valoración empresarial
# MAGIC
# MAGIC **5 Notebooks a desarrollar** (3-4 meses):
# MAGIC
# MAGIC 4. **1.6 - Presupuesto de Capital Avanzado** (Cap 10)
# MAGIC 5. **4.4 - Análisis de Riesgo en Proyectos** (Cap 11) - Monte Carlo, escenarios
# MAGIC 6. **2.3 - Valoración de Empresas con DCF** (Cap 12) - DCF, múltiplos, M&A
# MAGIC 7. **6.1 - Estructura de Capital y Teoría MM** (Caps 13-14) - Nuevo Módulo 06
# MAGIC 8. **6.2 - Política de Dividendos** (Cap 15) - Módulo 06
# MAGIC
# MAGIC **Impacto Fase 2**: Cobertura del 52% → 74% (+22 puntos)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC #### ⚪ **FASE 3 (Prioridad BAJA)**
# MAGIC
# MAGIC **Objetivo**: Completar temas avanzados y especializados
# MAGIC
# MAGIC **Crear Módulo 07 - Derivados y Opciones** (5-6 meses):
# MAGIC
# MAGIC 9. **7.1 - Opciones Financieras** (Cap 16) - Black-Scholes, griegas
# MAGIC 10. **7.2 - Opciones Reales** (Cap 17) - Diferir, expandir, abandonar
# MAGIC 11. **7.3 - Derivados y Cobertura** (Cap 18) - Futuros, swaps, VaR
# MAGIC 12. **7.4 - Finanzas Internacionales** (Cap 19) - Tipo cambio, riesgo cambiario
# MAGIC
# MAGIC **Impacto Fase 3**: Cobertura del 74% → 100% (+26 puntos)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ RECOMENDACIÓN FINAL
# MAGIC
# MAGIC **COMENZAR INMEDIATAMENTE CON**:
# MAGIC
# MAGIC 🎯 **Notebook 3.2 - Sistema DuPont y Apalancamiento**
# MAGIC
# MAGIC **Razones**:
# MAGIC 1. 👍 **Complejidad BAJA** - Herramientas conocidas, extensión natural del notebook 3.1
# MAGIC 2. 📊 **Impacto ALTO** - Herramienta fundamental para análisis financiero avanzado
# MAGIC 3. 💾 **Datos disponibles** - BYMA y Caja de Valores (PDFs ya extraídos)
# MAGIC 4. ⏱️ **Rápido** - 3-4 días de desarrollo
# MAGIC 5. 🏛️ **Alineado con UDA** - Contexto argentino, encabezado institucional, Genie integrado
# MAGIC
# MAGIC **Siguiente paso**: Una vez completado 3.2, continuar con **notebook 4.3 (CAPM)** y luego **1.5 (WACC)**.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📝 Resumen Numérico Final
# MAGIC
# MAGIC | Métrica | Valor |
# MAGIC |---------|-------|
# MAGIC | Capítulos del libro | 19 |
# MAGIC | Capítulos cubiertos actualmente | 7 (37%) |
# MAGIC | Capítulos NO cubiertos | 12 (63%) |
# MAGIC | Notebooks actuales | 12 |
# MAGIC | Notebooks propuestos (total) | 12 adicionales |
# MAGIC | **Notebooks propuestos Fase 1** | **3 (ALTA prioridad)** |
# MAGIC | Notebooks propuestos Fase 2 | 5 (MEDIA prioridad) |
# MAGIC | Notebooks propuestos Fase 3 | 4 (BAJA prioridad) |
# MAGIC | Tiempo Fase 1 | 1-2 meses |
# MAGIC | Tiempo Fase 2 | 3-4 meses |
# MAGIC | Tiempo Fase 3 | 5-6 meses |
# MAGIC | **Cobertura tras Fase 1** | **52%** |
# MAGIC | Cobertura tras Fase 2 | 74% |
# MAGIC | Cobertura tras Fase 3 | 100% |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **¿Procedemos con el desarrollo del notebook 3.2 - Sistema DuPont y Apalancamiento?**