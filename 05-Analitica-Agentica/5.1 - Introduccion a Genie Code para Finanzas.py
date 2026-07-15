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
# MAGIC ### Módulo 05: Analítica Agéntica con IA
# MAGIC ### Notebook 5.1: Introducción a Genie Code para Finanzas
# MAGIC ### 🤖 **IA APLICADA A FINANZAS**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introduccion
# MAGIC %md
# MAGIC # 5.1 - Introduccion a Genie Code para Finanzas
# MAGIC
# MAGIC ## Objetivo
# MAGIC Aprender a usar Genie Code como asistente de IA para analisis financiero.
# MAGIC
# MAGIC ## Que es Genie Code
# MAGIC Genie Code es un asistente de IA integrado en Databricks que:
# MAGIC * Genera codigo Python y SQL automaticamente
# MAGIC * Analiza datos financieros
# MAGIC * Crea visualizaciones
# MAGIC * Responde preguntas en lenguaje natural
# MAGIC * Ayuda a resolver problemas complejos
# MAGIC
# MAGIC ## Por que usar IA en Finanzas
# MAGIC * Acelera el analisis de datos
# MAGIC * Reduce errores de calculo
# MAGIC * Automatiza tareas repetitivas
# MAGIC * Descubre patrones ocultos
# MAGIC * Genera insights mas rapido

# COMMAND ----------

# DBTITLE 1,Como usar Genie Code
# MAGIC %md
# MAGIC ## Como Usar Genie Code
# MAGIC
# MAGIC ### 1. Acceso a Genie
# MAGIC Genie Code esta disponible en:
# MAGIC * Chat lateral en notebooks
# MAGIC * Espacios Genie (Genie Spaces)
# MAGIC * Integrado en el editor de codigo
# MAGIC
# MAGIC ### 2. Tipos de Consultas
# MAGIC
# MAGIC **Analisis Exploratorio**:
# MAGIC * "Muestra estadisticas descriptivas de este dataset"
# MAGIC * "Grafica la distribucion de retornos"
# MAGIC * "Identifica outliers en los datos"
# MAGIC
# MAGIC **Calculos Financieros**:
# MAGIC * "Calcula el VPN de este flujo de caja"
# MAGIC * "Valua este bono con estos parametros"
# MAGIC * "Optimiza este portafolio"
# MAGIC
# MAGIC **Visualizaciones**:
# MAGIC * "Crea un grafico de lineas de precios historicos"
# MAGIC * "Grafica la frontera eficiente"
# MAGIC * "Muestra una matriz de correlacion"
# MAGIC
# MAGIC **Codigo Automatico**:
# MAGIC * "Escribe una funcion para calcular el Sharpe Ratio"
# MAGIC * "Genera codigo para descargar datos de Yahoo Finance"
# MAGIC * "Crea un script para backtesting"

# COMMAND ----------

# DBTITLE 1,Ventajas en Finanzas
# MAGIC %md
# MAGIC ## Ventajas de IA en Analisis Financiero
# MAGIC
# MAGIC ### 1. Velocidad
# MAGIC * Analiza miles de acciones en segundos
# MAGIC * Procesa reportes financieros automaticamente
# MAGIC * Genera reportes en tiempo real
# MAGIC
# MAGIC ### 2. Precision
# MAGIC * Reduce errores humanos en calculos
# MAGIC * Valida formulas automaticamente
# MAGIC * Detecta inconsistencias en datos
# MAGIC
# MAGIC ### 3. Escala
# MAGIC * Analiza multiples portafolios simultaneamente
# MAGIC * Procesa grandes volumenes de datos historicos
# MAGIC * Monitorea mercados 24/7
# MAGIC
# MAGIC ### 4. Insights
# MAGIC * Descubre correlaciones no obvias
# MAGIC * Identifica patrones de comportamiento
# MAGIC * Predice tendencias con machine learning

# COMMAND ----------

# DBTITLE 1,Ejemplo Practico
# MAGIC %md
# MAGIC ## Ejemplo Practico: Analisis de Retornos
# MAGIC
# MAGIC Vamos a usar Genie Code para analizar retornos de un portafolio.

# COMMAND ----------

# DBTITLE 1,Datos de Ejemplo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simular retornos de 3 activos
np.random.seed(42)
n_dias = 252  # 1 ano de trading

retornos = pd.DataFrame({
    'Accion_A': np.random.normal(0.0008, 0.02, n_dias),
    'Accion_B': np.random.normal(0.0006, 0.015, n_dias),
    'Bono_C': np.random.normal(0.0003, 0.005, n_dias)
})

retornos.index = pd.date_range('2024-01-01', periods=n_dias, freq='D')

print("Datos de retornos diarios creados")
print(f"Periodo: {retornos.index[0].date()} a {retornos.index[-1].date()}")
print(f"\nPrimeras filas:")
print(retornos.head())

# COMMAND ----------

# DBTITLE 1,Consultas con Genie
# MAGIC %md
# MAGIC ## Consultas Sugeridas para Genie Code
# MAGIC
# MAGIC Prueba estas consultas con Genie:
# MAGIC
# MAGIC ### Analisis Basico
# MAGIC * "Calcula las estadisticas descriptivas de estos retornos"
# MAGIC * "Cual activo tiene mayor retorno promedio?"
# MAGIC * "Grafica la evolucion acumulada de cada activo"
# MAGIC * "Muestra la matriz de correlacion entre activos"
# MAGIC
# MAGIC ### Analisis Avanzado
# MAGIC * "Calcula el Sharpe Ratio de cada activo (asume rf=3% anual)"
# MAGIC * "Identifica los dias con mayores caidas"
# MAGIC * "Crea un portafolio equiponderado y calcula su retorno"
# MAGIC * "Grafica la distribucion de retornos con histogramas"
# MAGIC
# MAGIC ### Optimizacion
# MAGIC * "Optimiza los pesos para maximo Sharpe Ratio"
# MAGIC * "Cual es el portafolio de minima varianza?"
# MAGIC * "Simula 1000 portafolios aleatorios y grafica la frontera eficiente"

# COMMAND ----------

# DBTITLE 1,Mejores Practicas
# MAGIC %md
# MAGIC ## Mejores Practicas con Genie Code
# MAGIC
# MAGIC ### 1. Se Especifico
# MAGIC * Malo: "Analiza estos datos"
# MAGIC * Bueno: "Calcula el retorno anualizado y la volatilidad de cada activo"
# MAGIC
# MAGIC ### 2. Da Contexto
# MAGIC * Malo: "Calcula el ratio"
# MAGIC * Bueno: "Calcula el Sharpe Ratio usando tasa libre de riesgo de 3% anual"
# MAGIC
# MAGIC ### 3. Pide Visualizaciones
# MAGIC * Malo: "Muestra los resultados"
# MAGIC * Bueno: "Crea un grafico de barras comparando los Sharpe Ratios"
# MAGIC
# MAGIC ### 4. Itera
# MAGIC * Empieza simple, luego refina
# MAGIC * Pide explicaciones si no entiendes
# MAGIC * Ajusta parametros basado en resultados
# MAGIC
# MAGIC ### 5. Valida Resultados
# MAGIC * Verifica que los numeros tengan sentido
# MAGIC * Compara con calculos manuales en casos simples
# MAGIC * Revisa el codigo generado

# COMMAND ----------

# DBTITLE 1,Ejercicios
# MAGIC %md
# MAGIC ## Ejercicios Practicos
# MAGIC
# MAGIC ### Ejercicio 1: Analisis Descriptivo
# MAGIC Usa Genie para:
# MAGIC 1. Calcular retorno promedio anual de cada activo
# MAGIC 2. Calcular volatilidad anualizada
# MAGIC 3. Identificar el activo mas riesgoso
# MAGIC 4. Graficar retornos acumulados
# MAGIC
# MAGIC ### Ejercicio 2: Correlaciones
# MAGIC Usa Genie para:
# MAGIC 1. Calcular la matriz de correlacion
# MAGIC 2. Identificar el par de activos mas correlacionado
# MAGIC 3. Graficar un heatmap de correlaciones
# MAGIC 4. Explicar que significa esa correlacion para diversificacion
# MAGIC
# MAGIC ### Ejercicio 3: Optimizacion Simple
# MAGIC Usa Genie para:
# MAGIC 1. Crear 3 portafolios con diferentes ponderaciones
# MAGIC 2. Calcular retorno y riesgo de cada uno
# MAGIC 3. Identificar cual tiene mejor Sharpe Ratio
# MAGIC 4. Graficar los 3 portafolios en el espacio riesgo-retorno

# COMMAND ----------

# DBTITLE 1,Resumen
# MAGIC %md
# MAGIC ## Resumen
# MAGIC
# MAGIC ### Puntos Clave
# MAGIC 1. Genie Code es un asistente de IA para analisis financiero
# MAGIC 2. Acelera el trabajo y reduce errores
# MAGIC 3. Funciona con lenguaje natural
# MAGIC 4. Genera codigo, visualizaciones y analisis
# MAGIC 5. Mejores resultados con consultas especificas
# MAGIC
# MAGIC ### Proximos Pasos
# MAGIC * **Notebook 5.2**: Casos practicos de analisis con IA
# MAGIC * **Notebook 5.3**: Proyecto integrador - Portfolio inteligente
# MAGIC
# MAGIC ### Recursos Adicionales
# MAGIC * Documentacion de Databricks Genie
# MAGIC * Tutoriales de AI en finanzas
# MAGIC * Foro de la comunidad Databricks

# COMMAND ----------

