# Databricks notebook source
# DBTITLE 1,Encabezado Institucional
# MAGIC %md
# MAGIC <div style="text-align: center;">
# MAGIC
# MAGIC # Universidad del Aconcagua
# MAGIC ## Facultad de Ciencias Económicas
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
# MAGIC ### Programa del Curso
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC </div>

# COMMAND ----------

# DBTITLE 1,Datos Generales del Curso
# MAGIC %md
# MAGIC # DATOS GENERALES DEL CURSO
# MAGIC
# MAGIC ## Información Básica
# MAGIC
# MAGIC | Campo | Detalle |
# MAGIC |-------|--------|
# MAGIC | **Nombre del Curso** | Databricks Finance Lab - Analítica Financiera Agéntica |
# MAGIC | **Institución** | Universidad del Aconcagua |
# MAGIC | **Facultad** | Facultad de Ciencias Económicas |
# MAGIC | **Nivel** | Grado / Pregrado |
# MAGIC | **Modalidad** | Teórico-Práctico con Laboratorio de IA |
# MAGIC | **Plataforma** | Databricks Community Edition |
# MAGIC | **Duración** | 15 semanas (60 horas totales) |
# MAGIC | **Créditos** | 4 créditos académicos |
# MAGIC | **Año Académico** | 2026 |
# MAGIC
# MAGIC ## Prerrequisitos
# MAGIC * Matemática Financiera básica
# MAGIC * Conocimientos básicos de estadística
# MAGIC * Familiaridad con hojas de cálculo
# MAGIC * No se requiere experiencia previa en programación
# MAGIC
# MAGIC ## Recursos Tecnológicos
# MAGIC * **Plataforma**: Databricks Community Edition (gratuita)
# MAGIC * **Lenguajes**: Python y SQL
# MAGIC * **IA Integrada**: Genie Code para asistencia en análisis
# MAGIC * **Acceso**: 100% online, disponible 24/7

# COMMAND ----------

# DBTITLE 1,Objetivos Generales
# MAGIC %md
# MAGIC # OBJETIVOS GENERALES
# MAGIC
# MAGIC El curso **Databricks Finance Lab - Analítica Financiera Agéntica** tiene como objetivos generales:
# MAGIC
# MAGIC ## 1. Dominio de Conceptos Financieros Fundamentales
# MAGIC Desarrollar una comprensión sólida de los principios fundamentales de matemática financiera, valoración de instrumentos y análisis de portafolios, integrándolos con herramientas modernas de analítica de datos.
# MAGIC
# MAGIC ## 2. Competencia en Analítica de Datos Financieros
# MAGIC Capacitar a los estudiantes en el uso de plataformas modernas de analítica (Databricks) para procesar, analizar y visualizar grandes volúmenes de datos financieros de manera eficiente y escalable.
# MAGIC
# MAGIC ## 3. Aplicación de Inteligencia Artificial en Finanzas
# MAGIC Introducir a los estudiantes en el uso de agentes de IA (Genie Code) como herramienta de asistencia para resolver problemas financieros complejos, automatizar análisis y generar insights accionables.
# MAGIC
# MAGIC ## 4. Contextualización Latinoamericana
# MAGIC Analizar casos prácticos y datos reales del mercado financiero argentino y latinoamericano, conectando la teoría con la realidad económica regional.
# MAGIC
# MAGIC ## 5. Preparación Profesional Integral
# MAGIC Formar profesionales con competencias técnicas y analíticas que les permitan destacarse en áreas de finanzas corporativas, banca, inversiones, fintechs y consultoría financiera en la era de la transformación digital.

# COMMAND ----------

# DBTITLE 1,Objetivos Específicos
# MAGIC %md
# MAGIC # OBJETIVOS ESPECÍFICOS
# MAGIC
# MAGIC Al finalizar el curso, los estudiantes serán capaces de:
# MAGIC
# MAGIC ## Competencias Técnicas - Matemática Financiera
# MAGIC
# MAGIC 1. **Calcular y aplicar** el valor del dinero en el tiempo utilizando fórmulas de valor presente y valor futuro en contextos de inversión y financiamiento.
# MAGIC
# MAGIC 2. **Convertir y comparar** diferentes tipos de tasas de interés (nominal, efectiva, equivalente, real) y aplicarlas en decisiones financieras.
# MAGIC
# MAGIC 3. **Analizar y resolver** problemas de anualidades, amortización de préstamos y sistemas de pago (francés y alemán).
# MAGIC
# MAGIC 4. **Valorar instrumentos financieros** como bonos y acciones utilizando modelos de descuento de flujos de caja.
# MAGIC
# MAGIC 5. **Calcular e interpretar** ratios financieros clave para evaluar la salud financiera de empresas.
# MAGIC
# MAGIC 6. **Medir y gestionar** el riesgo y retorno de activos individuales y portafolios de inversión.
# MAGIC
# MAGIC ## Competencias en Analítica de Datos
# MAGIC
# MAGIC 7. **Utilizar Python** para implementar funciones financieras, procesar datos y automatizar cálculos complejos.
# MAGIC
# MAGIC 8. **Escribir consultas SQL** para extraer, transformar y analizar datos financieros almacenados en bases de datos.
# MAGIC
# MAGIC 9. **Crear visualizaciones** efectivas (gráficos, tablas, dashboards) para comunicar resultados financieros.
# MAGIC
# MAGIC 10. **Trabajar con datos reales** de empresas argentinas y latinoamericanas utilizando APIs financieras (Yahoo Finance, datos de CNV).
# MAGIC
# MAGIC ## Competencias en IA Generativa
# MAGIC
# MAGIC 11. **Interactuar con Genie Code** mediante consultas en lenguaje natural para resolver problemas financieros.
# MAGIC
# MAGIC 12. **Validar y depurar** código generado por IA, asegurando precisión y consistencia.
# MAGIC
# MAGIC 13. **Optimizar flujos de trabajo** combinando programación manual con asistencia de IA para maximizar productividad.
# MAGIC
# MAGIC ## Competencias Profesionales
# MAGIC
# MAGIC 14. **Analizar casos reales** del mercado argentino y latinoamericano aplicando los conceptos teóricos del curso.
# MAGIC
# MAGIC 15. **Tomar decisiones financieras informadas** basadas en análisis cuantitativos rigurosos.

# COMMAND ----------

# DBTITLE 1,Módulo 01 - Fundamentos
# MAGIC %md
# MAGIC # CONTENIDO DE LOS MÓDULOS
# MAGIC
# MAGIC ## Módulo 01: Fundamentos de Matemática Financiera
# MAGIC **Duración**: 3 semanas (12 horas)
# MAGIC
# MAGIC ### Notebook 1.1 - Valor del Dinero en el Tiempo
# MAGIC * Concepto fundamental del valor temporal del dinero
# MAGIC * Valor Presente (VP) y Valor Futuro (VF)
# MAGIC * Fórmulas de capitalización simple y compuesta
# MAGIC * Aplicaciones prácticas en inversiones y ahorro
# MAGIC * **Referencia libro**: Capítulo 5, Sección 5.1-5.2 (pág. 123-125)
# MAGIC
# MAGIC ### Notebook 1.2 - Tasas de Interés y Conversiones
# MAGIC * Tasa Nominal Anual (TNA) vs Tasa Efectiva Anual (TEA)
# MAGIC * Tasas proporcionales y tasas equivalentes
# MAGIC * Conversión entre diferentes períodos de capitalización
# MAGIC * Tasa real vs tasa nominal (ajuste por inflación)
# MAGIC * Tasa de descuento comercial
# MAGIC * **Referencia libro**: Capítulo 5, Sección 5.3 (pág. 126-131)
# MAGIC
# MAGIC ### Notebook 1.3 - Anualidades y Amortización
# MAGIC * Anualidades ordinarias y anticipadas
# MAGIC * Valor actual y valor futuro de anualidades
# MAGIC * Perpetuidades simples y crecientes
# MAGIC * Sistema Francés de amortización (cuota constante)
# MAGIC * Sistema Alemán de amortización (amortización constante)
# MAGIC * Tablas de amortización y cálculo de cuotas
# MAGIC * **Referencia libro**: Capítulo 5, Sección 5.4 (pág. 132-143)
# MAGIC
# MAGIC ### Notebook 1.4 - Estados Financieros y Análisis
# MAGIC * Balance General: estructura y componentes
# MAGIC * Estado de Resultados: ingresos, costos y márgenes
# MAGIC * Estado de Flujo de Efectivo: operativo, inversión, financiamiento
# MAGIC * Conexión entre estados financieros
# MAGIC * **Referencia libro**: Capítulos 2-4 (pág. 33-120)

# COMMAND ----------

# DBTITLE 1,Módulos 02 y 03
# MAGIC %md
# MAGIC ## Módulo 02: Valoración de Instrumentos Financieros
# MAGIC **Duración**: 2 semanas (8 horas)
# MAGIC
# MAGIC ### Notebook 2.1 - Valoración de Bonos
# MAGIC * Características de los bonos: cupones, vencimiento, valor nominal
# MAGIC * Precio de un bono: descuento de flujos de caja
# MAGIC * Relación inversa entre precio y tasa de interés
# MAGIC * Duración y convexidad
# MAGIC * Bonos cupón cero vs bonos con cupones
# MAGIC * Valoración de bonos argentinos (contexto local)
# MAGIC * **Referencia libro**: Capítulo 6, Sección 6.1-6.3 (pág. 147-165)
# MAGIC
# MAGIC ### Notebook 2.2 - Valoración de Acciones
# MAGIC * Modelo de descuento de dividendos (DDM)
# MAGIC * Modelo de Gordon (crecimiento constante)
# MAGIC * Modelos de múltiples etapas de crecimiento
# MAGIC * Ratio Precio/Utilidad (P/E) y múltiplos comparables
# MAGIC * Valoración relativa vs valoración absoluta
# MAGIC * Análisis de empresas argentinas (ADRs)
# MAGIC * **Referencia libro**: Capítulo 6, Sección 6.4-6.6 (pág. 166-185)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Módulo 03: Análisis Financiero y Ratios
# MAGIC **Duración**: 2 semanas (8 horas)
# MAGIC
# MAGIC ### Notebook 3.1 - Ratios Financieros
# MAGIC * **Ratios de Liquidez**: Liquidez corriente, Prueba ácida, Capital de trabajo
# MAGIC * **Ratios de Solvencia**: Endeudamiento, Cobertura de intereses, Apalancamiento
# MAGIC * **Ratios de Rentabilidad**: ROA, ROE, Margen neto, Margen operativo
# MAGIC * **Ratios de Eficiencia**: Rotación de activos, Rotación de inventarios, Período de cobro
# MAGIC * **Ratios de Mercado**: P/E, P/B, Dividend Yield, EPS
# MAGIC * Análisis comparativo (benchmarking)
# MAGIC * Interpretación y aplicación práctica
# MAGIC * **Referencia libro**: Capítulos 3-4 (pág. 67-120)

# COMMAND ----------

# DBTITLE 1,Módulos 04 y 05
# MAGIC %md
# MAGIC ## Módulo 04: Series Temporales y Gestión de Portafolios
# MAGIC **Duración**: 3 semanas (12 horas)
# MAGIC
# MAGIC ### Notebook 4.1 - Riesgo y Rentabilidad
# MAGIC * Retorno esperado y retorno histórico
# MAGIC * Medidas de riesgo: varianza, desviación estándar, VaR
# MAGIC * Distribución de retornos y análisis de normalidad
# MAGIC * Relación riesgo-retorno
# MAGIC * Coeficiente de Sharpe, Sortino y Treynor
# MAGIC * Beta y riesgo sistemático vs no sistemático
# MAGIC * **Referencia libro**: Capítulo 7, Sección 7.1-7.3 (pág. 189-215)
# MAGIC
# MAGIC ### Notebook 4.2 - Construcción de Portafolios
# MAGIC * Teoría moderna de portafolios (Markowitz)
# MAGIC * Diversificación y reducción de riesgo
# MAGIC * Frontera eficiente y portafolio óptimo
# MAGIC * Modelo CAPM (Capital Asset Pricing Model)
# MAGIC * Asignación de activos y rebalanceo
# MAGIC * Optimización con restricciones
# MAGIC * **Referencia libro**: Capítulo 7, Sección 7.4-7.6 (pág. 216-245)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Módulo 05: Analítica Agéntica con IA
# MAGIC **Duración**: 5 semanas (20 horas)
# MAGIC
# MAGIC ### Notebook 5.1 - Introducción a Genie Code para Finanzas
# MAGIC * Qué es Genie Code y cómo funciona
# MAGIC * Ventajas de IA en análisis financiero
# MAGIC * Cómo formular consultas efectivas
# MAGIC * Mejores prácticas con agentes de IA
# MAGIC * Casos de uso en finanzas
# MAGIC
# MAGIC ### Notebook 5.2 - Análisis de Datos Financieros con IA
# MAGIC * Automatización de cálculos financieros
# MAGIC * Generación de visualizaciones con IA
# MAGIC * Debugging y validación de código
# MAGIC * Análisis exploratorio asistido por IA
# MAGIC * Optimización de flujos de trabajo
# MAGIC
# MAGIC ### Notebook 5.3 - Caso Integrador: Portfolio Inteligente
# MAGIC * Proyecto final integrador
# MAGIC * Construcción de un portafolio usando IA
# MAGIC * Análisis completo de riesgo-retorno
# MAGIC * Optimización y backtesting
# MAGIC * Presentación de resultados y recomendaciones

# COMMAND ----------

# DBTITLE 1,Material Complementario
# MAGIC %md
# MAGIC ---
# MAGIC
# MAGIC ## Material Complementario
# MAGIC
# MAGIC ### Notebooks de Datos Argentinos
# MAGIC
# MAGIC #### Datos Empresas Argentinas - Ejemplo
# MAGIC * Obtención de datos de ADRs argentinas vía Yahoo Finance
# MAGIC * Empresas incluidas: YPF, GGAL, MELI, BMA, TEO, SUPV, PAM, LOMA, CRESY, EDN
# MAGIC * Análisis de precios históricos, estados financieros y ratios
# MAGIC * Comparación de desempeño entre empresas
# MAGIC * Integración con todos los módulos del curso
# MAGIC
# MAGIC #### Análisis de Estados Contables Argentinos
# MAGIC * Análisis de balances reales de entidades argentinas
# MAGIC * Entidades: BYMA, Caja de Valores, Grupo Clarín, Correo Argentino
# MAGIC * Estados contables oficiales en formato CNV (4 PDFs incluidos)
# MAGIC * Análisis multisectorial: infraestructura financiera, medios, servicios
# MAGIC * Uso de AI_PARSE_DOCUMENT() para extracción de datos de PDFs
# MAGIC * Ejercicios prácticos integrados
# MAGIC
# MAGIC ### Recursos Adicionales
# MAGIC * **Libro de texto** en PDF: Finanzas Corporativas - Dumrauf (2ª ed.)
# MAGIC * **Estados contables reales**: 4 PDFs de entidades argentinas
# MAGIC * **Imágenes institucionales**: Logo UDA para branding del curso
# MAGIC * **Dashboards**: Plantillas de visualización financiera

# COMMAND ----------

# DBTITLE 1,Bibliografía
# MAGIC %md
# MAGIC # BIBLIOGRAFÍA
# MAGIC
# MAGIC ## Bibliografía Obligatoria
# MAGIC
# MAGIC ### Libro de Texto Principal
# MAGIC
# MAGIC **Dumrauf, Guillermo L. (2013)**  
# MAGIC *Finanzas Corporativas: Un Enfoque Latinoamericano* (2ª edición)  
# MAGIC Editorial Alfaomega  
# MAGIC ISBN: 978-987-1609-86-5  
# MAGIC **Ubicación**: `/Workspace/Users/cortega@uda.edu.ar/Databricks Finance Lab/Libros/Finanzas corporativas.pdf`
# MAGIC
# MAGIC **Cobertura del curso**:
# MAGIC * Capítulo 1: Introducción a las finanzas corporativas (pág. 1-32)
# MAGIC * Capítulos 2-4: Estados financieros y análisis (pág. 33-120)
# MAGIC * Capítulo 5: El valor tiempo del dinero (pág. 123-146)
# MAGIC * Capítulo 6: Valoración de títulos valores (pág. 147-185)
# MAGIC * Capítulo 7: Riesgo y rendimiento (pág. 189-245)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Bibliografía Complementaria
# MAGIC
# MAGIC ### Libros de Referencia
# MAGIC
# MAGIC 1. **Ross, S., Westerfield, R., & Jaffe, J. (2018)**  
# MAGIC    *Finanzas Corporativas* (11ª edición)  
# MAGIC    McGraw-Hill  
# MAGIC    ISBN: 978-607-15-1588-8
# MAGIC
# MAGIC 2. **Brealey, R., Myers, S., & Allen, F. (2020)**  
# MAGIC    *Principios de Finanzas Corporativas* (13ª edición)  
# MAGIC    McGraw-Hill  
# MAGIC    ISBN: 978-607-15-1617-5
# MAGIC
# MAGIC 3. **Bodie, Z., Kane, A., & Marcus, A. (2018)**  
# MAGIC    *Inversiones* (10ª edición)  
# MAGIC    McGraw-Hill  
# MAGIC    ISBN: 978-607-15-1445-4
# MAGIC
# MAGIC ### Recursos en Línea
# MAGIC
# MAGIC 4. **Databricks Documentation**  
# MAGIC    https://docs.databricks.com/  
# MAGIC    Documentación oficial de la plataforma Databricks
# MAGIC
# MAGIC 5. **Python for Finance**  
# MAGIC    https://www.python.org/  
# MAGIC    Documentación de Python y librerías financieras (pandas, numpy, matplotlib)
# MAGIC
# MAGIC 6. **Yahoo Finance API**  
# MAGIC    https://finance.yahoo.com/  
# MAGIC    Fuente de datos financieros en tiempo real
# MAGIC
# MAGIC ### Artículos Académicos
# MAGIC
# MAGIC 7. **Markowitz, H. (1952)**  
# MAGIC    "Portfolio Selection"  
# MAGIC    *The Journal of Finance*, Vol. 7, No. 1, pp. 77-91
# MAGIC
# MAGIC 8. **Sharpe, W. F. (1964)**  
# MAGIC    "Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk"  
# MAGIC    *The Journal of Finance*, Vol. 19, No. 3, pp. 425-442
# MAGIC
# MAGIC ### Bases de Datos y Fuentes de Información
# MAGIC
# MAGIC 9. **Comisión Nacional de Valores (CNV)**  
# MAGIC    https://www.cnv.gov.ar/  
# MAGIC    Estados contables y memorias de empresas argentinas
# MAGIC
# MAGIC 10. **Banco Central de la República Argentina (BCRA)**  
# MAGIC     https://www.bcra.gob.ar/  
# MAGIC     Tasas de interés, tipos de cambio e indicadores macroeconómicos
# MAGIC
# MAGIC 11. **Bolsas y Mercados Argentinos (BYMA)**  
# MAGIC     https://www.byma.com.ar/  
# MAGIC     Cotizaciones y datos de mercado de capitales argentino

# COMMAND ----------

# DBTITLE 1,Equipo Docente
# MAGIC %md
# MAGIC # EQUIPO DOCENTE
# MAGIC
# MAGIC ## Profesores del Curso
# MAGIC
# MAGIC ### Prof. Cristian Dario Ortega Yubro
# MAGIC **Profesor e Instructor Principal**
# MAGIC
# MAGIC #### Información de Contacto
# MAGIC * **Email**: cortega@uda.edu.ar
# MAGIC * **LinkedIn**: [linkedin.com/in/cristiandarioortegayubro](https://www.linkedin.com/in/cristiandarioortegayubro/)
# MAGIC * **Institución**: Universidad del Aconcagua
# MAGIC
# MAGIC #### Perfil Profesional
# MAGIC Profesor de Finanzas y Analítica de Datos en la Facultad de Ciencias Económicas de la Universidad del Aconcagua. Especializado en la integración de tecnologías modernas de datos e inteligencia artificial en la enseñanza de finanzas corporativas.
# MAGIC
# MAGIC #### Áreas de Especialización
# MAGIC * Finanzas Corporativas
# MAGIC * Analítica de Datos Financieros
# MAGIC * Inteligencia Artificial aplicada a Finanzas
# MAGIC * Valoración de Empresas
# MAGIC * Gestión de Portafolios
# MAGIC
# MAGIC #### Responsabilidades en el Curso
# MAGIC * Diseño curricular y planificación del programa
# MAGIC * Desarrollo de materiales didácticos y notebooks
# MAGIC * Instrucción teórica y práctica
# MAGIC * Evaluación de estudiantes
# MAGIC * Tutorías y acompañamiento académico
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Prof. Gustavo Machin Urbay
# MAGIC **Profesor e Instructor**
# MAGIC
# MAGIC #### Información de Contacto
# MAGIC * **Email**: gustavomachin@uda.edu.ar
# MAGIC * **LinkedIn**: [linkedin.com/in/gustavomachinurbay](https://www.linkedin.com/in/gustavomachinurbay/)
# MAGIC * **Institución**: Universidad del Aconcagua
# MAGIC
# MAGIC #### Perfil Profesional
# MAGIC Profesor de Finanzas y Tecnología en la Facultad de Ciencias Económicas de la Universidad del Aconcagua. Experto en la aplicación de plataformas de Big Data y herramientas de analítica avanzada en el ámbito financiero.
# MAGIC
# MAGIC #### Áreas de Especialización
# MAGIC * Finanzas Cuantitativas
# MAGIC * Big Data y Analytics
# MAGIC * Programación en Python y SQL
# MAGIC * Plataformas Cloud (Databricks, AWS, Azure)
# MAGIC * Machine Learning para Finanzas
# MAGIC
# MAGIC #### Responsabilidades en el Curso
# MAGIC * Soporte técnico en Databricks
# MAGIC * Instrucción en programación y análisis de datos
# MAGIC * Desarrollo de ejercicios prácticos
# MAGIC * Asesoramiento en proyectos integradores
# MAGIC * Supervisión de laboratorios de IA
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Metodología de Enseñanza
# MAGIC
# MAGIC El curso combina:
# MAGIC * **Clases teóricas**: Exposición de conceptos fundamentales
# MAGIC * **Laboratorios prácticos**: Implementación en Databricks
# MAGIC * **Casos de estudio**: Análisis de empresas argentinas reales
# MAGIC * **Proyecto integrador**: Construcción de portafolio inteligente
# MAGIC * **Asistencia con IA**: Uso de Genie Code como herramienta pedagógica
# MAGIC
# MAGIC ## Evaluación
# MAGIC * **Ejercicios prácticos**: 30%
# MAGIC * **Parciales**: 40%
# MAGIC * **Proyecto final integrador**: 30%

# COMMAND ----------

# DBTITLE 1,Metodología de Enseñanza
# MAGIC %md
# MAGIC # METODOLOGÍA DE ENSEÑANZA
# MAGIC
# MAGIC ## Enfoque Pedagógico
# MAGIC
# MAGIC El curso utiliza un **modelo de aprendizaje híbrido** que combina:
# MAGIC
# MAGIC ### 1. Aprendizaje Basado en Problemas (ABP)
# MAGIC * Los estudiantes resuelven problemas financieros reales desde el inicio
# MAGIC * Casos de estudio de empresas argentinas (YPF, GGAL, MELI, BMA, etc.)
# MAGIC * Análisis de estados contables oficiales de entidades nacionales
# MAGIC * Toma de decisiones basada en datos
# MAGIC
# MAGIC ### 2. Learning by Doing (Aprender Haciendo)
# MAGIC * **100% de notebooks ejecutables**: Cada concepto se implementa en código
# MAGIC * **Ejercicios prácticos integrados**: Mínimo 3 ejercicios por notebook
# MAGIC * **Proyecto final integrador**: Portfolio inteligente con datos reales
# MAGIC * **Experimentación guiada**: Los estudiantes modifican parámetros y observan resultados
# MAGIC
# MAGIC ### 3. Analítica Agéntica con IA
# MAGIC * **Asistencia de Genie Code**: Resolución de problemas con lenguaje natural
# MAGIC * **Consultas sugeridas**: 10+ consultas por notebook para practicar con IA
# MAGIC * **Validación crítica**: Los estudiantes aprenden a verificar código generado por IA
# MAGIC * **Optimización de flujo**: Combinar programación manual con asistencia de IA
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Estructura de las Clases
# MAGIC
# MAGIC ### Clases Teórico-Prácticas (90 minutos)
# MAGIC
# MAGIC | Tiempo | Actividad | Descripción |
# MAGIC |--------|-----------|-------------|
# MAGIC | **0-15 min** | Introducción Teórica | Exposición de conceptos fundamentales del libro |
# MAGIC | **15-40 min** | Demostración en Vivo | Implementación paso a paso en Databricks |
# MAGIC | **40-70 min** | Laboratorio Guiado | Estudiantes ejecutan notebooks con supervisión |
# MAGIC | **70-85 min** | Ejercicios Prácticos | Resolución individual/grupal de problemas |
# MAGIC | **85-90 min** | Consultas y Q&A | Dudas, consultas con Genie, cierre |
# MAGIC
# MAGIC ### Trabajo Fuera de Clase
# MAGIC
# MAGIC * **Lectura del libro**: Capítulos asignados antes de cada módulo
# MAGIC * **Completar ejercicios**: Notebooks con ejercicios no resueltos en clase
# MAGIC * **Proyecto integrador**: Desarrollo gradual a lo largo del curso
# MAGIC * **Consultas asíncronas**: Uso de Genie Code para dudas fuera de horario
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Recursos de Aprendizaje
# MAGIC
# MAGIC ### Materiales del Curso
# MAGIC
# MAGIC | Recurso | Cantidad | Ubicación |
# MAGIC |---------|----------|----------|
# MAGIC | **Notebooks Educativos** | 12 notebooks | Módulos 01-05 |
# MAGIC | **Notebooks de Datasets** | 2 notebooks | `/Datasets/` y `/Balances/` |
# MAGIC | **Estados Contables (PDF)** | 4 archivos | `/Balances/` |
# MAGIC | **Libro de Texto (PDF)** | 1 archivo | `/Libros/` |
# MAGIC | **Dashboards** | Plantillas | `/Dashboards/` |
# MAGIC | **Total de Celdas Ejecutables** | 250+ celdas | Todo el curso |
# MAGIC
# MAGIC ### Empresas Argentinas Analizadas
# MAGIC
# MAGIC **ADRs (American Depositary Receipts)**: 10 empresas
# MAGIC * YPF, Grupo Financiero Galicia, MercadoLibre, Banco Macro
# MAGIC * Telecom Argentina, Supervielle, Pampa Energía, Loma Negra
# MAGIC * Cresud, Edenor
# MAGIC
# MAGIC **Entidades Nacionales**: 4 empresas
# MAGIC * BYMA (Bolsas y Mercados Argentinos)
# MAGIC * Caja de Valores S.A.
# MAGIC * Grupo Clarín S.A.
# MAGIC * Correo Argentino S.A.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Modalidades de Trabajo
# MAGIC
# MAGIC ### Individual
# MAGIC * Lectura y estudio del libro
# MAGIC * Ejecución de notebooks
# MAGIC * Ejercicios prácticos básicos
# MAGIC * Consultas con Genie Code
# MAGIC
# MAGIC ### Colaborativo
# MAGIC * Análisis de casos complejos en grupos de 2-3
# MAGIC * Comparación de resultados entre estudiantes
# MAGIC * Discusión de interpretaciones financieras
# MAGIC * Revisión de código entre pares
# MAGIC
# MAGIC ### Asistido por IA
# MAGIC * Generación de código con Genie Code
# MAGIC * Debugging automático
# MAGIC * Optimización de análisis
# MAGIC * Exploración de alternativas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Progresión del Aprendizaje
# MAGIC
# MAGIC ### Nivel Inicial (Semanas 1-3)
# MAGIC * Conceptos básicos de programación en Python
# MAGIC * Fórmulas financieras fundamentales
# MAGIC * Introducción a Databricks y Genie Code
# MAGIC * Ejercicios estructurados con soluciones
# MAGIC
# MAGIC ### Nivel Intermedio (Semanas 4-9)
# MAGIC * Análisis de datos financieros reales
# MAGIC * Implementación de modelos de valoración
# MAGIC * Cálculo de ratios e indicadores
# MAGIC * Ejercicios semi-estructurados
# MAGIC
# MAGIC ### Nivel Avanzado (Semanas 10-15)
# MAGIC * Construcción y optimización de portafolios
# MAGIC * Integración de múltiples fuentes de datos
# MAGIC * Análisis multisectorial
# MAGIC * Proyecto integrador autónomo

# COMMAND ----------

# DBTITLE 1,Sistema de Evaluación
# MAGIC %md
# MAGIC # SISTEMA DE EVALUACIÓN
# MAGIC
# MAGIC ## Componentes de Evaluación
# MAGIC
# MAGIC La calificación final se compone de:
# MAGIC
# MAGIC | Componente | Ponderación | Cantidad | Descripción |
# MAGIC |------------|--------------|----------|-------------|
# MAGIC | **Ejercicios Prácticos** | 30% | Continuo | Notebooks completados semanalmente |
# MAGIC | **Exámenes Parciales** | 40% | 2 parciales | Evaluaciones teórico-prácticas |
# MAGIC | **Proyecto Integrador** | 30% | 1 proyecto | Portfolio inteligente con datos reales |
# MAGIC | **TOTAL** | **100%** | - | Nota final del curso |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 1. Ejercicios Prácticos (30%)
# MAGIC
# MAGIC ### Características
# MAGIC * **Frecuencia**: Semanal (1 notebook por semana)
# MAGIC * **Modalidad**: Individual, entrega vía Databricks
# MAGIC * **Plazo**: 7 días desde la asignación
# MAGIC * **Formato**: Notebook con células ejecutadas y resultados visibles
# MAGIC
# MAGIC ### Criterios de Evaluación
# MAGIC
# MAGIC | Criterio | Puntaje | Descripción |
# MAGIC |----------|---------|-------------|
# MAGIC | **Correctitud** | 40% | Cálculos y resultados correctos |
# MAGIC | **Código** | 30% | Calidad, legibilidad, documentación |
# MAGIC | **Interpretación** | 20% | Análisis y conclusiones financieras |
# MAGIC | **Completitud** | 10% | Todos los ejercicios resueltos |
# MAGIC
# MAGIC ### Política de Entregas
# MAGIC * **A tiempo (100%)**: Entrega dentro del plazo
# MAGIC * **Tardía 1-3 días (80%)**: Penalización del 20%
# MAGIC * **Tardía 4-7 días (60%)**: Penalización del 40%
# MAGIC * **Más de 7 días**: No se acepta
# MAGIC
# MAGIC ### Notebooks Evaluables por Módulo
# MAGIC
# MAGIC | Módulo | Notebooks | Ejercicios Totales |
# MAGIC |---------|-----------|--------------------|
# MAGIC | **Módulo 01** | 1.1, 1.2, 1.3, 1.4 | 12 ejercicios |
# MAGIC | **Módulo 02** | 2.1, 2.2 | 6 ejercicios |
# MAGIC | **Módulo 03** | 3.1 | 4 ejercicios |
# MAGIC | **Módulo 04** | 4.1, 4.2 | 8 ejercicios |
# MAGIC | **Módulo 05** | 5.1, 5.2 | 6 ejercicios |
# MAGIC | **TOTAL** | 12 notebooks | 36 ejercicios |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 2. Exámenes Parciales (40%)
# MAGIC
# MAGIC ### Parcial 1 - Fundamentos y Valoración (20%)
# MAGIC **Semana 7 | Duración: 2 horas**
# MAGIC
# MAGIC **Contenido**:
# MAGIC * Módulo 01: Valor del dinero, tasas, anualidades
# MAGIC * Módulo 02: Valoración de bonos y acciones
# MAGIC * Capítulos 5-6 del libro de Dumrauf
# MAGIC
# MAGIC **Formato**:
# MAGIC * **Parte Teórica (30%)**: Preguntas conceptuales y de selección múltiple
# MAGIC * **Parte Práctica (70%)**: Problemas en Databricks con código ejecutable
# MAGIC
# MAGIC **Temas Evaluados**:
# MAGIC * Cálculo de VP, VF, tasas equivalentes
# MAGIC * Amortización de préstamos (sistemas Francés y Alemán)
# MAGIC * Valoración de bonos (precio, duración, convexidad)
# MAGIC * Valoración de acciones (DDM, Modelo de Gordon)
# MAGIC * Análisis de datos de empresas argentinas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Parcial 2 - Análisis y Portafolios (20%)
# MAGIC **Semana 12 | Duración: 2 horas**
# MAGIC
# MAGIC **Contenido**:
# MAGIC * Módulo 03: Ratios financieros y análisis
# MAGIC * Módulo 04: Riesgo, retorno y portafolios
# MAGIC * Capítulos 2-4 y 7 del libro de Dumrauf
# MAGIC
# MAGIC **Formato**:
# MAGIC * **Parte Teórica (30%)**: Preguntas conceptuales y de selección múltiple
# MAGIC * **Parte Práctica (70%)**: Problemas en Databricks con código ejecutable
# MAGIC
# MAGIC **Temas Evaluados**:
# MAGIC * Cálculo e interpretación de ratios financieros
# MAGIC * Análisis de estados contables
# MAGIC * Medición de riesgo y retorno
# MAGIC * Construcción de portafolios eficientes
# MAGIC * Optimización con restricciones
# MAGIC * Uso de Genie Code para análisis
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Política de Recuperatorios
# MAGIC
# MAGIC * **Recuperatorio por parcial**: Se puede recuperar 1 parcial con nota < 4
# MAGIC * **Fecha**: 2 semanas después del parcial original
# MAGIC * **Contenido**: Mismo temario del parcial original
# MAGIC * **Nota máxima recuperatorio**: 7 (siete)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 3. Proyecto Integrador Final (30%)
# MAGIC
# MAGIC ### Características Generales
# MAGIC
# MAGIC **Título**: Portfolio Inteligente con Datos Argentinos
# MAGIC
# MAGIC **Modalidad**: Individual o Grupal (máximo 2 personas)
# MAGIC
# MAGIC **Plazo**: Semanas 13-15 (3 semanas)
# MAGIC
# MAGIC **Entregables**:
# MAGIC 1. Notebook ejecutable con análisis completo
# MAGIC 2. Presentación (10-15 minutos)
# MAGIC 3. Informe ejecutivo (2-3 páginas)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Objetivo del Proyecto
# MAGIC
# MAGIC Construir un **portafolio de inversión diversificado** utilizando:
# MAGIC * Mínimo 5 empresas argentinas (ADRs o locales)
# MAGIC * Datos reales de Yahoo Finance y/o CNV
# MAGIC * Optimización con restricciones
# MAGIC * Asistencia de Genie Code
# MAGIC * Backtesting de estrategia
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Componentes del Proyecto
# MAGIC
# MAGIC | Componente | Peso | Descripción |
# MAGIC |------------|------|-------------|
# MAGIC | **1. Selección de Activos** | 15% | Justificación de empresas elegidas, sectores, diversificación |
# MAGIC | **2. Análisis Histórico** | 20% | Retornos, volatilidad, correlaciones, ratios financieros |
# MAGIC | **3. Optimización** | 25% | Frontera eficiente, portafolio óptimo, restricciones |
# MAGIC | **4. Backtesting** | 20% | Evaluación fuera de muestra, métricas de desempeño |
# MAGIC | **5. Presentación** | 10% | Claridad, visualizaciones, comunicación de resultados |
# MAGIC | **6. Código y Documentación** | 10% | Calidad del código, comentarios, reproduciblidad |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Criterios de Evaluación Detallados
# MAGIC
# MAGIC #### Excelente (9-10)
# MAGIC * Análisis profundo y justificado
# MAGIC * Uso avanzado de técnicas de optimización
# MAGIC * Backtesting riguroso con múltiples métricas
# MAGIC * Visualizaciones profesionales
# MAGIC * Código limpio y bien documentado
# MAGIC * Uso efectivo de Genie Code
# MAGIC
# MAGIC #### Bueno (7-8)
# MAGIC * Análisis correcto y completo
# MAGIC * Optimización adecuada con restricciones básicas
# MAGIC * Backtesting con métricas estándar
# MAGIC * Visualizaciones claras
# MAGIC * Código funcional
# MAGIC
# MAGIC #### Aprobado (4-6)
# MAGIC * Análisis básico pero correcto
# MAGIC * Optimización simple sin restricciones
# MAGIC * Backtesting limitado
# MAGIC * Visualizaciones básicas
# MAGIC * Código funciona pero poco documentado
# MAGIC
# MAGIC #### Insuficiente (< 4)
# MAGIC * Análisis incompleto o incorrecto
# MAGIC * No hay optimización o tiene errores
# MAGIC * No hay backtesting
# MAGIC * Visualizaciones ausentes o confusas
# MAGIC * Código no funciona
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Régimen de Promoción y Regularidad
# MAGIC
# MAGIC ### Promoción Directa (sin examen final)
# MAGIC **Requisitos**:
# MAGIC * Asistencia ≥ 80%
# MAGIC * Ejercicios prácticos ≥ 7
# MAGIC * Ambos parciales ≥ 7
# MAGIC * Proyecto integrador ≥ 7
# MAGIC * **Promedio final ≥ 7**
# MAGIC
# MAGIC ### Regularidad (con examen final)
# MAGIC **Requisitos**:
# MAGIC * Asistencia ≥ 70%
# MAGIC * Ejercicios prácticos ≥ 4
# MAGIC * Ambos parciales ≥ 4
# MAGIC * Proyecto integrador ≥ 4
# MAGIC * **Promedio final ≥ 4**
# MAGIC
# MAGIC ### Examen Final (para alumnos regulares)
# MAGIC * **Formato**: Teórico-práctico en Databricks
# MAGIC * **Contenido**: Todo el programa
# MAGIC * **Duración**: 3 horas
# MAGIC * **Nota mínima**: 4 (cuatro)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Escala de Calificaciones
# MAGIC
# MAGIC | Rango | Calificación | Concepto |
# MAGIC |-------|---------------|----------|
# MAGIC | 9-10 | Sobresaliente | Dominio excepcional |
# MAGIC | 7-8 | Distinguido | Muy buen desempeño |
# MAGIC | 6 | Bueno | Desempeño satisfactorio |
# MAGIC | 4-5 | Aprobado | Desempeño mínimo aceptable |
# MAGIC | 0-3 | Insuficiente | No alcanza los objetivos |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Integridad Académica
# MAGIC
# MAGIC ### Uso de IA (Genie Code)
# MAGIC **Permitido y Fomentado**:
# MAGIC * Consultas para debugging
# MAGIC * Generación de código base
# MAGIC * Exploración de alternativas
# MAGIC * Optimización de análisis
# MAGIC
# MAGIC **Obligatorio**:
# MAGIC * **Validar y comprender** todo código generado por IA
# MAGIC * **Documentar** cuándo se usó IA
# MAGIC * **Citar fuentes** externas utilizadas
# MAGIC
# MAGIC ### Plagio
# MAGIC * **Cero tolerancia** al plagio
# MAGIC * Código copiado sin atribución: Nota 0
# MAGIC * Presentaciones idénticas entre grupos: Investigación académica
# MAGIC * Uso responsable de GitHub, Stack Overflow, etc. (con citas)

# COMMAND ----------

# DBTITLE 1,Estructura del Curso y Resumen
# MAGIC %md
# MAGIC # ESTRUCTURA DEL CURSO EN DATABRICKS
# MAGIC
# MAGIC ## Organización de Carpetas
# MAGIC
# MAGIC ```
# MAGIC Databricks Finance Lab/
# MAGIC │
# MAGIC ├── 01-Fundamentos/
# MAGIC │   ├── 1.1 - Valor del Dinero en el Tiempo
# MAGIC │   ├── 1.2 - Tasas de Interés y Conversiones
# MAGIC │   ├── 1.3 - Anualidades y Amortización
# MAGIC │   └── 1.4 - Estados Financieros y Análisis
# MAGIC │
# MAGIC ├── 02-Instrumentos/
# MAGIC │   ├── 2.1 - Valoracion de Bonos
# MAGIC │   └── 2.2 - Valoracion de Acciones
# MAGIC │
# MAGIC ├── 03-Analisis-Financiero/
# MAGIC │   └── 3.1 - Ratios Financieros
# MAGIC │
# MAGIC ├── 04-Series-Temporales/
# MAGIC │   ├── 4.1 - Riesgo y Rentabilidad
# MAGIC │   └── 4.2 - Construcción de Portafolios
# MAGIC │
# MAGIC ├── 05-Analitica-Agentica/
# MAGIC │   ├── 5.1 - Introducción a Genie Code para Finanzas
# MAGIC │   ├── 5.2 - Análisis de Datos Financieros con IA
# MAGIC │   └── 5.3 - Caso Integrador Portfolio Inteligente
# MAGIC │
# MAGIC ├── Datasets/
# MAGIC │   └── Datos Empresas Argentinas - Ejemplo
# MAGIC │
# MAGIC ├── Balances/
# MAGIC │   ├── Analisis de Estados Contables Argentinos (notebook)
# MAGIC │   ├── Bolsas y Mercados Argentinos SA.pdf
# MAGIC │   ├── Caja de Valores SA.pdf
# MAGIC │   ├── Grupo Clarin SA.pdf
# MAGIC │   └── Correo Argentino SA.pdf
# MAGIC │
# MAGIC ├── Libros/
# MAGIC │   └── Finanzas corporativas.pdf (Dumrauf, 2ª ed.)
# MAGIC │
# MAGIC ├── Imagenes/
# MAGIC │   └── uda.jpg (logo institucional)
# MAGIC │
# MAGIC ├── Programa del Curso/
# MAGIC │   └── Programa Completo (este notebook)
# MAGIC │
# MAGIC └── Dashboards/
# MAGIC     └── (plantillas de visualización)
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Resumen Ejecutivo
# MAGIC
# MAGIC ### Datos del Curso
# MAGIC * **Total de notebooks**: 14 notebooks educativos + 2 notebooks de datasets
# MAGIC * **Duración**: 15 semanas (60 horas)
# MAGIC * **Módulos**: 5 módulos temáticos
# MAGIC * **Empresas analizadas**: 10 ADRs argentinas + 4 entidades nacionales
# MAGIC * **Estados contables**: 4 PDFs de empresas argentinas reales
# MAGIC
# MAGIC ### Innovación Pedagógica
# MAGIC * ✅ Integración de IA generativa (Genie Code) en el proceso de aprendizaje
# MAGIC * ✅ Uso de datos reales del mercado argentino y latinoamericano
# MAGIC * ✅ Plataforma profesional de Big Data (Databricks)
# MAGIC * ✅ Enfoque práctico con ejercicios ejecutables
# MAGIC * ✅ Contextualización regional con casos locales
# MAGIC
# MAGIC ### Competencias Desarrolladas
# MAGIC 1. **Finanzas**: Valoración, análisis de riesgo, gestión de portafolios
# MAGIC 2. **Programación**: Python y SQL aplicado a finanzas
# MAGIC 3. **Analítica**: Procesamiento y visualización de datos financieros
# MAGIC 4. **IA**: Uso efectivo de agentes de IA para resolver problemas
# MAGIC 5. **Pensamiento crítico**: Interpretación y toma de decisiones basada en datos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Contacto e Información
# MAGIC
# MAGIC **Universidad del Aconcagua**  
# MAGIC Facultad de Ciencias Económicas  
# MAGIC Mendoza, Argentina
# MAGIC
# MAGIC **Profesores**:  
# MAGIC * Cristian Dario Ortega Yubro - cortega@uda.edu.ar  
# MAGIC * Gustavo Machin Urbay - gustavomachin@uda.edu.ar
# MAGIC
# MAGIC **Ubicación del curso**:  
# MAGIC `/Workspace/Users/cortega@uda.edu.ar/Databricks Finance Lab/`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎓 Databricks Finance Lab - Analítica Financiera Agéntica
# MAGIC ### 🏛️ Universidad del Aconcagua | Año 2026

# COMMAND ----------

