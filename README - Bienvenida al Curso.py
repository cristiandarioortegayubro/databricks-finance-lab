# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Bienvenida
# MAGIC %md
# MAGIC # 🏛️ Databricks Finance Lab: Analítica Financiera Agéntica
# MAGIC
# MAGIC ## 🎯 Descripción del Curso
# MAGIC
# MAGIC Bienvenido al **Databricks Finance Lab**, un curso innovador que combina:
# MAGIC * 📊 **Matemática Financiera** - Fundamentos teóricos sólidos
# MAGIC * 💻 **Analítica de Datos** - Python, SQL y visualización
# MAGIC * 🤖 **IA Generativa** - Agentes inteligentes (Genie Code) como asistentes
# MAGIC * ☁️ **Cloud Computing** - Databricks Free Edition
# MAGIC
# MAGIC Este curso te enseña a resolver problemas financieros reales usando herramientas modernas de ciencia de datos, potenciadas por inteligencia artificial conversacional.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📚 Estructura del Curso
# MAGIC
# MAGIC ### Módulo 1: Fundamentos 🏛️
# MAGIC **Carpeta**: `01-Fundamentos/`
# MAGIC
# MAGIC Conceptos base de matemática financiera:
# MAGIC * 1.1 - Valor del Dinero en el Tiempo
# MAGIC * 1.2 - Tasas de Interés y Conversiones
# MAGIC * 1.3 - Anualidades y Amortización
# MAGIC
# MAGIC **Habilidades**: Cálculos de VP/VF, interés simple/compuesto, análisis temporal
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Módulo 2: Instrumentos Financieros 💰
# MAGIC **Carpeta**: `02-Instrumentos/`
# MAGIC
# MAGIC Análisis de productos financieros:
# MAGIC * Bonos y renta fija
# MAGIC * Acciones y valoración
# MAGIC * Derivados básicos (futuros, opciones)
# MAGIC * Índices y ETFs
# MAGIC
# MAGIC **Habilidades**: Valoración, análisis de flujos, sensibilidad a tasas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Módulo 3: Gestión de Portafolios 📈
# MAGIC **Carpeta**: `03-Portafolios/`
# MAGIC
# MAGIC Optimización y riesgo:
# MAGIC * Teoría moderna de portafolios
# MAGIC * Diversificación y correlación
# MAGIC * Modelo de Markowitz
# MAGIC * VaR (Value at Risk)
# MAGIC * Métricas de desempeño (Sharpe, Sortino)
# MAGIC
# MAGIC **Habilidades**: Optimización, análisis de riesgo, backtesting
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Módulo 4: Series Temporales Financieras 📉
# MAGIC **Carpeta**: `04-Series-Temporales/`
# MAGIC
# MAGIC Análisis predictivo:
# MAGIC * Componentes de series de tiempo
# MAGIC * Estacionalidad y tendencias
# MAGIC * Modelos ARIMA/SARIMA
# MAGIC * Volatilidad y modelos GARCH
# MAGIC * Forecasting con ML
# MAGIC
# MAGIC **Habilidades**: Predicción, análisis de volatilidad, detección de patrones
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Módulo 5: Analítica Agéntica 🤖
# MAGIC **Carpeta**: `05-Analitica-Agentica/`
# MAGIC
# MAGIC **✨ El diferenciador del curso:**
# MAGIC Aprender a trabajar con agentes de IA (Genie Code) como copiloto:
# MAGIC * Consultas en lenguaje natural sobre datos financieros
# MAGIC * Generación automática de análisis
# MAGIC * Genie Spaces para exploración de datasets
# MAGIC * Dashboards inteligentes
# MAGIC * Automatización de reportes
# MAGIC
# MAGIC **Habilidades**: Prompting efectivo, integración IA-Analytics, workflows agénticos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 💾 Carpetas Adicionales
# MAGIC
# MAGIC ### 📁 `Datasets/`
# MAGIC Datasets de práctica:
# MAGIC * Datos sintéticos de mercados
# MAGIC * Series históricas de precios
# MAGIC * Datos de portafolios
# MAGIC * APIs públicas (Yahoo Finance, Alpha Vantage)
# MAGIC
# MAGIC ### 📊 `Dashboards/`
# MAGIC Dashboards interactivos:
# MAGIC * Monitores de mercado
# MAGIC * Análisis de portafolios
# MAGIC * Métricas de riesgo en tiempo real
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🚀 Cómo Empezar
# MAGIC
# MAGIC 1. **Explora el Módulo 1** - Comienza con `01-Fundamentos/1.1 - Valor del Dinero en el Tiempo`
# MAGIC 2. **Ejecuta las celdas** - Usa serverless compute (sin necesidad de cluster)
# MAGIC 3. **Interactúa con Genie** - Haz preguntas en lenguaje natural
# MAGIC 4. **Practica con ejercicios** - Cada notebook tiene ejercicios al final
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 👥 Compartir el Curso
# MAGIC
# MAGIC ### Para compartir con el profesor Gustavo Machin:
# MAGIC
# MAGIC 1. **Desde la carpeta principal** (`Databricks Finance Lab`):
# MAGIC    * Click derecho → **Share**
# MAGIC    * Buscar usuario: `gustavomachin@uda.edu.ar`
# MAGIC    * Seleccionar permisos:
# MAGIC      * **Can Edit** - Si quiere modificar contenido
# MAGIC      * **Can Run** - Si solo ejecutará notebooks
# MAGIC      * **Can Read** - Si solo revisará
# MAGIC
# MAGIC 2. **Compartir vía URL**:
# MAGIC    * Click en **Share** → **Get link**
# MAGIC    * Copiar y enviar por email/mensaje
# MAGIC
# MAGIC 3. **Exportar como colección**:
# MAGIC    * Menú → **Export** → **DBC Archive**
# MAGIC    * Compartir archivo .dbc
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🛠️ Herramientas Utilizadas
# MAGIC
# MAGIC * **Python** - NumPy, Pandas, Matplotlib, Seaborn
# MAGIC * **SQL** - Análisis con Spark SQL
# MAGIC * **PySpark** - Para datasets grandes
# MAGIC * **Genie Code** - Asistente IA conversacional
# MAGIC * **Databricks Notebooks** - Entorno colaborativo
# MAGIC * **Databricks Dashboards** - Visualización interactiva
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎯 Objetivos de Aprendizaje
# MAGIC
# MAGIC Al finalizar el curso, los estudiantes podrán:
# MAGIC
# MAGIC * ✅ Aplicar conceptos de matemática financiera con código
# MAGIC * ✅ Analizar instrumentos y portafolios financieros
# MAGIC * ✅ Construir modelos predictivos de series temporales
# MAGIC * ✅ Calcular y gestionar riesgo financiero
# MAGIC * ✅ Crear dashboards interactivos
# MAGIC * ✅ Utilizar agentes de IA para acelerar análisis
# MAGIC * ✅ Integrar múltiples fuentes de datos financieros
# MAGIC * ✅ Documentar y compartir análisis reproducibles
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📝 Requisitos Previos
# MAGIC
# MAGIC ### Conocimientos:
# MAGIC * Matemáticas básicas (álgebra, cálculo)
# MAGIC * Conceptos financieros introductorios (recomendado)
# MAGIC * Programación básica (Python o SQL) - ¡Genie ayuda si no tienes experiencia!
# MAGIC
# MAGIC ### Herramientas:
# MAGIC * Cuenta Databricks Community Edition (gratis)
# MAGIC * Navegador web moderno
# MAGIC * Conexión a internet
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🤝 Contribuciones y Mejoras
# MAGIC
# MAGIC Este curso es un proyecto vivo. Sugerencias de mejora:
# MAGIC * Nuevos casos de estudio
# MAGIC * Datasets adicionales
# MAGIC * Ejercicios más complejos
# MAGIC * Integraciones con APIs
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 💬 Soporte
# MAGIC
# MAGIC ¿Preguntas? Usa Genie Code:
# MAGIC * "Explica el concepto de valor presente"
# MAGIC * "Crea un ejemplo de valoración de bonos"
# MAGIC * "Muéstrame cómo calcular la volatilidad de un portafolio"
# MAGIC * "Genera un dashboard con métricas financieras"
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎓 Autores
# MAGIC
# MAGIC **Prof. Cristian Dario Ortega Yubro**
# MAGIC * Universidad del Aconcagua - Facultad de Ciencias Económicas y Jurídicas
# MAGIC * cortega@uda.edu.ar
# MAGIC
# MAGIC
# MAGIC **Prof. Gustavo Raúl Machín Urbay**
# MAGIC * Universidad del Aconcagua - Facultad de Ciencias Económicas y Jurídicas
# MAGIC * gustavomachin@uda.edu.ar
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📅 Versión
# MAGIC
# MAGIC **Versión 1.0** - Junio 2026
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 🚀 **¡Comienza tu viaje en Analítica Financiera Agéntica!**

# COMMAND ----------

# DBTITLE 1,Estructura Completa y Actualizada
# MAGIC %md
# MAGIC ## 📊 Módulos Educativos Completados
# MAGIC
# MAGIC ### ✅ Módulo 01 - Fundamentos (4 notebooks)
# MAGIC **Carpeta**: `01-Fundamentos/`
# MAGIC
# MAGIC Basado en Capítulos 1, 2, 5 del libro de Dumrauf:
# MAGIC
# MAGIC * **1.1 - Valor del Dinero en el Tiempo** 
# MAGIC   - Valor presente y futuro con fórmulas
# MAGIC   - Ejemplos con Python
# MAGIC   - Visualizaciones y ejercicios
# MAGIC   - Referencias al libro (pág. 123-146)
# MAGIC   
# MAGIC * **1.2 - Tasas de Interés y Conversiones**
# MAGIC   - Tasa nominal vs efectiva
# MAGIC   - Tasa equivalente
# MAGIC   - Tasa real vs inflación
# MAGIC   - Referencias al libro (pág. 126-132)
# MAGIC   
# MAGIC * **1.3 - Anualidades y Amortización**
# MAGIC   - Anualidades temporarias y perpetuas
# MAGIC   - Sistemas de amortización
# MAGIC   - Referencias al libro (pág. 133-143)
# MAGIC   
# MAGIC * **1.4 - VPN y TIR en Proyectos de Inversión**
# MAGIC   - Evaluación de proyectos
# MAGIC   - Criterios de decisión
# MAGIC   - Casos prácticos argentinos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Módulo 02 - Instrumentos Financieros (2 notebooks)
# MAGIC **Carpeta**: `02-Instrumentos/`
# MAGIC
# MAGIC Basado en Capítulo 6 del libro:
# MAGIC
# MAGIC * **2.1 - Valoración de Bonos**
# MAGIC   - Conceptos fundamentales
# MAGIC   - Cálculo de precio del bono
# MAGIC   - Yield to Maturity (YTM)
# MAGIC   - Relación precio-rendimiento
# MAGIC   - Análisis de sensibilidad
# MAGIC   - Ejercicios prácticos
# MAGIC   - Referencias al libro (pág. 148-166)
# MAGIC   
# MAGIC * **2.2 - Valoración de Acciones**
# MAGIC   - Modelos de descuento de dividendos
# MAGIC   - Modelo de Gordon (crecimiento constante)
# MAGIC   - Crecimiento variable
# MAGIC   - Price-Earning ratio (P/E)
# MAGIC   - ✅ **Ejercicio integrador**: Valoración de BYMA con datos reales
# MAGIC   - Referencias al libro (pág. 166-179)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Módulo 03 - Análisis Financiero (1 notebook)
# MAGIC **Carpeta**: `03-Analisis-Financiero/`
# MAGIC
# MAGIC Basado en Capítulos 3 y 4 del libro:
# MAGIC
# MAGIC * **3.1 - Análisis con Ratios Financieros**
# MAGIC   - Análisis vertical y horizontal
# MAGIC   - Índices de liquidez, endeudamiento, actividad, rentabilidad
# MAGIC   - Índices de valor de mercado
# MAGIC   - ✅ **Ejemplos con datos reales**: BYMA y Caja de Valores
# MAGIC   - Referencias al libro (pág. 53-82)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Módulo 04 - Series Temporales (2 notebooks)
# MAGIC **Carpeta**: `04-Series-Temporales/`
# MAGIC
# MAGIC Basado en Capítulo 7 del libro:
# MAGIC
# MAGIC * **4.1 - Riesgo y Rentabilidad**
# MAGIC   - Rendimientos históricos
# MAGIC   - Prima por riesgo de mercado
# MAGIC   - Estadística aplicada (media, varianza, covarianza, correlación)
# MAGIC   - Referencias al libro (pág. 185-204)
# MAGIC   
# MAGIC * **4.2 - Construcción y Optimización de Portafolios**
# MAGIC   - Rendimiento esperado del portafolio
# MAGIC   - Riesgo del portafolio
# MAGIC   - Portafolios eficientes
# MAGIC   - Frontera eficiente de Markowitz
# MAGIC   - Diversificación
# MAGIC   - Referencias al libro (pág. 205-220)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Módulo 05 - Analítica Agéntica (3 notebooks)
# MAGIC **Carpeta**: `05-Analitica-Agentica/`
# MAGIC
# MAGIC Integración de IA con finanzas:
# MAGIC
# MAGIC * **5.1 - Introducción a Genie Code para Finanzas**
# MAGIC   - Prompts efectivos para finanzas
# MAGIC   - Análisis conversacional de estados financieros
# MAGIC   - Consultas sobre el libro
# MAGIC   
# MAGIC * **5.2 - Casos de Uso con IA**
# MAGIC   - Valoración interactiva de instrumentos
# MAGIC   - Optimización de portafolios asistida por IA
# MAGIC   - Generación automática de reportes
# MAGIC   
# MAGIC * **5.3 - Automatización y Workflows Agénticos**
# MAGIC   - Pipelines de datos financieros
# MAGIC   - Dashboards dinámicos
# MAGIC   - Alertas y monitoreo
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📂 Datasets y Casos Prácticos
# MAGIC
# MAGIC ### 📊 Carpeta Datasets
# MAGIC **Carpeta**: `Datasets/`
# MAGIC
# MAGIC * ✅ **Datos Empresas Argentinas - Ejemplo.ipynb** (19 celdas)
# MAGIC   - Uso de `yfinance` para obtener datos de ADRs argentinas
# MAGIC   - **10 empresas incluidas**: YPF, GGAL, MELI, BMA, TEO, SUPV, PAM, LOMA, CRESY, EDN
# MAGIC   - Ejemplos: precios históricos, estados financieros, ratios, comparaciones
# MAGIC   - 4 ejercicios prácticos
# MAGIC   - 20+ consultas con Genie sugeridas
# MAGIC   - ✅ **Integrable con todos los módulos del curso**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📊 Carpeta Balances
# MAGIC **Carpeta**: `Balances/`
# MAGIC
# MAGIC ✅ **PDFs de Estados Contables Oficiales (CNV)**:
# MAGIC * `Bolsas y Mercados Argentinos SA.pdf` (1.20 MB)
# MAGIC * `Caja de Valores SA.pdf` (2.80 MB)
# MAGIC
# MAGIC ✅ **Analisis de Estados Contables Argentinos.ipynb** (24 celdas):
# MAGIC * ✅ **Extracción automática de datos** con `pdfplumber`
# MAGIC * ✅ **Validación de escala** y corrección automática
# MAGIC * ✅ **Sistema de fallback** a datos estimados si falla extracción
# MAGIC
# MAGIC **Análisis de 2 entidades de infraestructura del mercado de capitales**:
# MAGIC
# MAGIC 1. **BYMA** (Bolsas y Mercados Argentinos)
# MAGIC    - Rol: Plataforma de negociación de valores
# MAGIC    - Datos extraídos: Activo $2.76 billones, Patrimonio $737M, Resultado $14.9M
# MAGIC    - ROE: 2.02%, Debt/Equity: 2.74
# MAGIC    
# MAGIC 2. **Caja de Valores S.A.**
# MAGIC    - Rol: Depositaria central y sistema de compensación
# MAGIC    - Datos extraídos: Activo $1.27 billones, Patrimonio $323M, Resultado $2M
# MAGIC    - ROE: 0.63%, Debt/Equity: 2.92
# MAGIC
# MAGIC **Contenido del notebook**:
# MAGIC * Funciones de extracción con regex y validación
# MAGIC * Análisis comparativo de modelos de negocio
# MAGIC * Ratios específicos de infraestructura financiera
# MAGIC * Visualizaciones interactivas con Plotly (colores institucionales UDA)
# MAGIC
# MAGIC **💎 Ejercicio Integrador - Valoración de BYMA**:
# MAGIC * **3 métodos de valoración**: Perpetuidad (Gordon), Múltiplos P/E, Valor Libro
# MAGIC * **Simulador interactivo** con escenarios:
# MAGIC   - Caso base (datos reales)
# MAGIC   - Escenario optimista (mejora de rentabilidad)
# MAGIC   - Escenario pesimista (deterioro)
# MAGIC   - Escenario personalizado
# MAGIC * **Análisis de sensibilidad automático**:
# MAGIC   - Sensibilidad a tasa de descuento (k)
# MAGIC   - Sensibilidad a múltiplo P/E
# MAGIC   - Sensibilidad a mejora de utilidades
# MAGIC * **Preguntas de reflexión** y análisis crítico
# MAGIC * **Integración con los 5 módulos** del curso
# MAGIC
# MAGIC **Ejercicios prácticos**:
# MAGIC * 6 ejercicios enfocados en BYMA y Caja de Valores
# MAGIC * 1 ejercicio integrador de valoración completo
# MAGIC * 50+ consultas con Genie organizadas por categoría
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📚 Carpeta de Libros
# MAGIC **Carpeta**: `Libros/`
# MAGIC
# MAGIC * ✅ **Finanzas corporativas.pdf** - Libro principal del curso
# MAGIC   - Autor: Guillermo L. Dumrauf
# MAGIC   - Edición: 2ª
# MAGIC   - Páginas: 752
# MAGIC   
# MAGIC * ✅ **Analisis-Libro-Finanzas-Corporativas.ipynb**
# MAGIC   - Extracción de metadata y contenido
# MAGIC   - Tabla de contenidos completa
# MAGIC   - Mapeo con módulos del curso
# MAGIC   - Funciones de búsqueda de conceptos
# MAGIC   - Templates para referencias
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎯 Resumen del Estado del Curso
# MAGIC
# MAGIC ### ✅ Notebooks Completados: 16 en total
# MAGIC
# MAGIC **Módulos educativos**: 12 notebooks
# MAGIC * Módulo 01: 4 notebooks
# MAGIC * Módulo 02: 2 notebooks
# MAGIC * Módulo 03: 1 notebook
# MAGIC * Módulo 04: 2 notebooks
# MAGIC * Módulo 05: 3 notebooks
# MAGIC
# MAGIC **Datasets y casos prácticos**: 4 notebooks/archivos
# MAGIC * 1 notebook de empresas argentinas (yfinance)
# MAGIC * 1 notebook de análisis de balances (pdfplumber)
# MAGIC * 1 notebook de análisis del libro
# MAGIC * 2 PDFs de estados contables oficiales (+ 2 adicionales archivados)
# MAGIC
# MAGIC ### ✅ Integración de Datos Reales
# MAGIC
# MAGIC **Datos de empresas argentinas**:
# MAGIC * ✅ 10 ADRs argentinas disponibles via yfinance
# MAGIC * ✅ Precios históricos, estados financieros, ratios
# MAGIC * ✅ Integrables con Módulos 02, 03 y 04
# MAGIC
# MAGIC **Datos de balances oficiales**:
# MAGIC * ✅ BYMA: Extracción automática completa
# MAGIC * ✅ Caja de Valores: Extracción con corrección de escala
# MAGIC * ✅ Ejercicio integrador de valoración (Módulo 02)
# MAGIC * ✅ Ejemplos de ratios (Módulo 03)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🚀 Próximos Pasos Sugeridos
# MAGIC
# MAGIC ### Expansión del Contenido
# MAGIC * ➕ **Genie Spaces**: Crear espacios interactivos para exploración de datasets
# MAGIC * ➕ **Lakeview Dashboards**: Desarrollar dashboards dinámicos con métricas financieras
# MAGIC * ➕ **Más casos de estudio**: Agregar análisis de otros sectores (banca, energía, tech)
# MAGIC * ➕ **APIs en tiempo real**: Integrar fuentes de datos en vivo (Yahoo Finance, Alpha Vantage)
# MAGIC
# MAGIC ### Mejoras Pedagógicas
# MAGIC * ➕ **Videos tutoriales**: Grabar explicaciones de conceptos clave
# MAGIC * ➕ **Evaluaciones**: Agregar quizzes y exámenes prácticos
# MAGIC * ➕ **Proyectos finales**: Casos integradores que usen múltiples módulos
# MAGIC * ➕ **Foro de discusión**: Espacio para preguntas y colaboración
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📈 Métricas del Curso
# MAGIC
# MAGIC * 📚 **16 notebooks** totales (12 educativos + 4 datasets/casos)
# MAGIC * 📑 **1 libro de referencia** (752 páginas)
# MAGIC * 📊 **4 PDFs de balances** oficiales argentinos
# MAGIC * 👨‍🏫 **2 instructores** (Cristian Ortega, Gustavo Machin)
# MAGIC * 🏛️ **1 universidad** (Universidad del Aconcagua - UDA)
# MAGIC * 🇦🇷 **100% contenido argentino** adaptado al contexto local
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **CURSO 100% COMPLETO Y LISTO PARA USO EDUCATIVO**

# COMMAND ----------

# DBTITLE 1,Integracion de Datos Reales
# MAGIC %md
# MAGIC ## 🔗 Integración de Datos Reales en los Módulos
# MAGIC
# MAGIC ### 📊 Datos Disponibles
# MAGIC
# MAGIC **Empresas argentinas** (vía yfinance - ADRs):
# MAGIC * 10 empresas: YPF, GGAL, MELI, BMA, TEO, SUPV, PAM, LOMA, CRESY, EDN
# MAGIC * Datos: Precios históricos, estados financieros, ratios
# MAGIC * Ubicación: `/Datasets/Datos Empresas Argentinas - Ejemplo.ipynb`
# MAGIC
# MAGIC **Estados contables oficiales** (vía pdfplumber - CNV):
# MAGIC * **BYMA** (Bolsas y Mercados Argentinos)
# MAGIC   - Activo: $2.76 billones | Patrimonio: $737M | Resultado: $14.9M
# MAGIC   - ROE: 2.02% | Debt/Equity: 2.74
# MAGIC   
# MAGIC * **Caja de Valores S.A.**
# MAGIC   - Activo: $1.27 billones | Patrimonio: $323M | Resultado: $2M
# MAGIC   - ROE: 0.63% | Debt/Equity: 2.92
# MAGIC   
# MAGIC * Ubicación: `/Balances/Analisis de Estados Contables Argentinos.ipynb`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Integraciones Completadas
# MAGIC
# MAGIC **Módulo 02 - Valoración de Acciones**
# MAGIC * ✅ **Ejercicio integrador completo**: Valoración de BYMA
# MAGIC * 3 métodos: Perpetuidad (Gordon), Múltiplos P/E, Valor Libro
# MAGIC * Simulador interactivo con escenarios (optimista, pesimista, personalizado)
# MAGIC * Análisis de sensibilidad a k, g, P/E
# MAGIC * Preguntas de reflexión y casos de uso
# MAGIC * **Cómo usarlo**: Notebook 2.2 incluye el ejercicio completo al final
# MAGIC
# MAGIC **Módulo 05 - Analítica Agéntica**
# MAGIC * ✅ Consultas con Genie usando balances como ejemplos
# MAGIC * ✅ 50+ consultas sugeridas en el notebook de balances
# MAGIC * ✅ Casos de uso de extracción automática de PDFs
# MAGIC * **Cómo usarlo**: Notebooks 5.1-5.3 referencian los datasets
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔄 Integraciones Recomendadas
# MAGIC
# MAGIC **Módulo 03 - Análisis Financiero** (⚡ PRIORIDAD ALTA):
# MAGIC * 📝 Agregar sección "Ejemplo Real: BYMA vs Caja de Valores"
# MAGIC * Calcular ratios de liquidez, solvencia, rentabilidad, actividad
# MAGIC * Comparar modelos de negocio (negociación vs custodia)
# MAGIC * Interpretar diferencias en ROE, Debt/Equity, márgenes
# MAGIC * **Acción**: Agregar celda en notebook 3.1 con importación de datos
# MAGIC
# MAGIC **Módulo 04 - Riesgo y Rentabilidad** (🔷 PRIORIDAD MEDIA):
# MAGIC * 📝 Comparar ROE y perfil de riesgo de BYMA vs Caja de Valores
# MAGIC * Analizar estabilidad de resultados (volatilidad teórica)
# MAGIC * Discutir trade-off rentabilidad-riesgo en infraestructura financiera
# MAGIC * **Acción**: Agregar ejemplo comparativo en notebook 4.1
# MAGIC
# MAGIC **Módulo 04 - Portafolios** (🔹 OPCIONAL):
# MAGIC * 📝 Crear portafolio teórico: 60% BYMA + 40% Caja de Valores
# MAGIC * Calcular retorno esperado y riesgo del portafolio
# MAGIC * Analizar beneficios de diversificación
# MAGIC * **Acción**: Ejercicio opcional en notebook 4.2
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🛠️ Cómo Integrar Datos en Tus Propios Análisis
# MAGIC
# MAGIC **Opción 1: Importar desde notebook de balances**
# MAGIC ```python
# MAGIC # En cualquier notebook del curso
# MAGIC %run "/Databricks Finance Lab/Balances/Analisis de Estados Contables Argentinos"
# MAGIC
# MAGIC # Ahora tienes acceso a:
# MAGIC print(f"BYMA - ROE: {roe:.2f}%")
# MAGIC print(f"BYMA - Activo: ${byma_datos['Activo_Total']:,.0f}")
# MAGIC print(f"Caja de Valores - ROE: {roe_caja:.2f}%")
# MAGIC ```
# MAGIC
# MAGIC **Opción 2: Usar empresas argentinas vía yfinance**
# MAGIC ```python
# MAGIC # En cualquier notebook del curso
# MAGIC %run "/Databricks Finance Lab/Datasets/Datos Empresas Argentinas - Ejemplo"
# MAGIC
# MAGIC # Ahora tienes acceso a datos de 10 empresas
# MAGIC print(ypf.info['sector'])
# MAGIC print(ggal.history(period="1y"))
# MAGIC ```
# MAGIC
# MAGIC **Opción 3: Extraer directamente de PDFs**
# MAGIC ```python
# MAGIC import pdfplumber
# MAGIC
# MAGIC pdf_path = "/Workspace/Users/cortega@uda.edu.ar/Databricks Finance Lab/Balances/Bolsas y Mercados Argentinos SA.pdf"
# MAGIC
# MAGIC with pdfplumber.open(pdf_path) as pdf:
# MAGIC     texto = pdf.pages[10].extract_text()  # Página del balance
# MAGIC     # Aplicar regex para extraer valores
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 Ventajas de Usar Datos Reales
# MAGIC
# MAGIC ✅ **Contexto argentino**: Empresas conocidas, formatos CNV
# MAGIC ✅ **Aprendizaje práctico**: Código funcional con datos reales
# MAGIC ✅ **Extracción automática**: Habilidad transferible (pdfplumber, regex)
# MAGIC ✅ **Comparaciones significativas**: Modelos de negocio complementarios
# MAGIC ✅ **Casos de estudio completos**: Ejercicio de valoración integrador
# MAGIC ✅ **Replicable**: Proceso adaptable a otros balances
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Tabla Resumen Final
# MAGIC %md
# MAGIC ## 📊 Tabla Resumen: Estado del Curso
# MAGIC
# MAGIC | Módulo | Notebooks | Estado | Datos Reales | Comentarios |
# MAGIC |--------|-----------|--------|--------------|-------------|
# MAGIC | **01-Fundamentos** | 1.1 - 1.4 | ✅ 100% | ⚪ Ejemplos teóricos | VPN, TIR, tasas, anualidades |
# MAGIC | **02-Instrumentos** | 2.1 - 2.2 | ✅ 100% | ✅ **BYMA valoración** | Bonos + Acciones + Ejercicio integrador |
# MAGIC | **03-Análisis Financiero** | 3.1 | ✅ 100% | 🔄 Por integrar | Ratios - Recomendado: agregar BYMA/CdV |
# MAGIC | **04-Series Temporales** | 4.1 - 4.2 | ✅ 100% | 🔄 Opcional | Riesgo y portafolios |
# MAGIC | **05-Analítica Agéntica** | 5.1 - 5.3 | ✅ 100% | ✅ Referencias | Genie Code + casos de uso |
# MAGIC | **Datasets** | Empresas ARG | ✅ 100% | ✅ **10 ADRs** | yfinance + ejemplos |
# MAGIC | **Balances** | Análisis | ✅ 100% | ✅ **BYMA + CdV** | Extracción PDF + valoración |
# MAGIC | **Libros** | Análisis Dumrauf | ✅ 100% | 📚 Referencia | Mapeo completo |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎆 Resumen Ejecutivo
# MAGIC
# MAGIC ### 📚 Contenido Completo
# MAGIC * **16 notebooks totales** (12 educativos + 4 datasets/casos)
# MAGIC * **Todos los módulos al 100%** según libro de Dumrauf
# MAGIC * **Datos reales argentinos** integrados en notebooks clave
# MAGIC * **Libro de referencia** analizado y mapeado
# MAGIC * **Imágenes institucionales** (logo UDA)
# MAGIC
# MAGIC ### ✅ Integraciones de Datos Reales
# MAGIC * ✅ **Módulo 02**: Ejercicio completo de valoración de BYMA (3 métodos + simulador)
# MAGIC * ✅ **Datasets**: 10 empresas argentinas vía yfinance con ejemplos
# MAGIC * ✅ **Balances**: 2 estados contables oficiales con extracción automática
# MAGIC * 🔄 **Módulo 03**: Pendiente (fácil de agregar - solo importar datos)
# MAGIC * 🔄 **Módulo 04**: Opcional (ejercicios teóricos funcionan bien)
# MAGIC
# MAGIC ### 🎯 Casos de Uso Destacados
# MAGIC 1. **Valoración completa de BYMA** - Módulo 02
# MAGIC    - 3 métodos (Perpetuidad, Múltiplos, Valor Libro)
# MAGIC    - Simulador interactivo con escenarios
# MAGIC    - Análisis de sensibilidad automático
# MAGIC    
# MAGIC 2. **Extracción automática de PDFs** - Balances
# MAGIC    - pdfplumber + regex + validación
# MAGIC    - Sistema de corrección de escala
# MAGIC    - Fallback a datos estimados
# MAGIC    
# MAGIC 3. **Datos de mercado en tiempo real** - Datasets
# MAGIC    - yfinance para ADRs argentinas
# MAGIC    - Precios, estados financieros, ratios
# MAGIC    - Integración con todos los módulos
# MAGIC
# MAGIC ### 🚀 Próxima Acción Recomendada
# MAGIC
# MAGIC **Para completar integración de datos reales**:
# MAGIC 1. Abrir: `03-Analisis-Financiero/3.1 - Análisis con Ratios`
# MAGIC 2. Agregar celda después de teoría de ratios
# MAGIC 3. Título: "📊 Ejemplo Real: BYMA vs Caja de Valores"
# MAGIC 4. Código:
# MAGIC ```python
# MAGIC %run "/Databricks Finance Lab/Balances/Analisis de Estados Contables Argentinos"
# MAGIC
# MAGIC print("\n🏛️ BYMA - Bolsas y Mercados Argentinos")
# MAGIC print(f"  ROE: {roe:.2f}%")
# MAGIC print(f"  ROA: {roe * byma_datos['Patrimonio_Neto'] / byma_datos['Activo_Total']:.2f}%")
# MAGIC print(f"  Debt/Equity: {debt_equity:.2f}")
# MAGIC
# MAGIC print("\n🏛️ Caja de Valores S.A.")
# MAGIC print(f"  ROE: {roe_caja:.2f}%")
# MAGIC print(f"  ROA: {roe_caja * caja_datos['Patrimonio_Neto'] / caja_datos['Activo_Total']:.2f}%")
# MAGIC print(f"  Debt/Equity: {debt_equity_caja:.2f}")
# MAGIC
# MAGIC print("\n📊 Comparación:")
# MAGIC print(f"  BYMA tiene ROE {roe/roe_caja:.1f}x mayor (negocio transaccional)")
# MAGIC print(f"  Caja de Valores más estable (modelo de custodia)")
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎓 Información del Curso
# MAGIC
# MAGIC **Universidad**: Universidad del Aconcagua (UDA)
# MAGIC **Facultad**: Ciencias Económicas y Jurídicas
# MAGIC **Curso**: Analítica Financiera Agéntica
# MAGIC **Plataforma**: Databricks Community Edition (Free)
# MAGIC
# MAGIC **Instructores**:
# MAGIC * Prof. Cristian Dario Ortega Yubro (cortega@uda.edu.ar)
# MAGIC * Prof. Gustavo Machin Urbay (gustavomachin@uda.edu.ar)
# MAGIC
# MAGIC **Libro de Texto**:
# MAGIC * Finanzas Corporativas - Un Enfoque Latinoamericano (2ª ed.)
# MAGIC * Autor: Guillermo L. Dumrauf
# MAGIC * 752 páginas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ✅ **CURSO 100% COMPLETO - LISTO PARA USO EDUCATIVO**
# MAGIC
# MAGIC 🚀 **¡Comienza tu aprendizaje en Analítica Financiera con datos reales argentinos!**