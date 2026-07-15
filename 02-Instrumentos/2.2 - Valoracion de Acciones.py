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
# MAGIC ### Módulo 02: Valoración de Instrumentos Financieros
# MAGIC ### Notebook 2.2: Valoración de Acciones
# MAGIC ### 💹 **MODELO DE GORDON Y MÚTIPLOS**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introduccion
# MAGIC %md
# MAGIC # 2.2 - Valoracion de Acciones
# MAGIC
# MAGIC ## Objetivo
# MAGIC Comprender modelos de valoracion de acciones.
# MAGIC
# MAGIC ## Conceptos Clave
# MAGIC * Modelo de Descuento de Dividendos (DDM)
# MAGIC * Modelo de Gordon (crecimiento constante)
# MAGIC * Modelo de crecimiento multiple
# MAGIC * P/E Ratio
# MAGIC * Valoracion por multiplos

# COMMAND ----------

# DBTITLE 1,Referencias
# MAGIC %md
# MAGIC ## Referencias del Libro
# MAGIC
# MAGIC **Libro**: Finanzas Corporativas - Un Enfoque Latinoamericano (2a ed.)
# MAGIC **Autor**: Guillermo L. Dumrauf
# MAGIC **Capitulo**: 6 - Valuacion de instrumentos financieros
# MAGIC **Seccion**: 6.4 - Valuacion de acciones (pag. 166-180)
# MAGIC **Ubicacion**: `/Workspace/Shared/Databricks Finance Lab/Libros/Finanzas corporativas.pdf`

# COMMAND ----------

# DBTITLE 1,Librerias
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Colores institucionales UDA
UDA_COLORS = {'primary': '#003366', 'accent': '#FF6600', 'success': '#28A745', 'danger': '#DC3545'}

print("Librerias cargadas")

# COMMAND ----------

# DBTITLE 1,Formulas
# MAGIC %md
# MAGIC ## Modelos de Valoracion
# MAGIC
# MAGIC ### Modelo de Gordon (crecimiento constante)
# MAGIC
# MAGIC P0 = D1 / (r - g)
# MAGIC
# MAGIC Donde:
# MAGIC * P0 = Precio actual
# MAGIC * D1 = Dividendo proximo periodo
# MAGIC * r = Tasa de retorno requerida
# MAGIC * g = Tasa de crecimiento constante
# MAGIC
# MAGIC ### Modelo de crecimiento multiple
# MAGIC
# MAGIC P0 = VP(Dividendos fase rapida) + VP(Precio terminal)
# MAGIC
# MAGIC Precio terminal = Dn+1 / (r - g)

# COMMAND ----------

# DBTITLE 1,Funciones
def gordon_model(d1, r, g):
    """Modelo de Gordon para valoracion"""
    if r <= g:
        raise ValueError("Tasa requerida debe ser mayor que crecimiento")
    return d1 / (r - g)

def valoracion_pe(utilidad_por_accion, pe_ratio):
    """Valoracion por P/E ratio"""
    return utilidad_por_accion * pe_ratio

print("Funciones definidas")

# COMMAND ----------

# DBTITLE 1,Ejemplo 1
# MAGIC %md
# MAGIC ## Ejemplo 1: Modelo de Gordon
# MAGIC
# MAGIC Empresa ABC:
# MAGIC * Dividendo actual: $2.00
# MAGIC * Crecimiento esperado: 5% anual
# MAGIC * Tasa requerida: 12%
# MAGIC
# MAGIC Calcular precio de la accion

# COMMAND ----------

# DBTITLE 1,Solucion 1
d0 = 2.00
g = 0.05
r = 0.12

d1 = d0 * (1 + g)
precio = gordon_model(d1, r, g)

print(f"Dividendo D0: ${d0:.2f}")
print(f"Dividendo D1: ${d1:.2f}")
print(f"Precio calculado: ${precio:.2f}")
print(f"\nDividend Yield: {(d1/precio)*100:.2f}%")
print(f"Capital Gain Yield: {g*100:.2f}%")
print(f"Retorno total: {((d1/precio) + g)*100:.2f}%")

# COMMAND ----------

# DBTITLE 1,Ejemplo 2
# MAGIC %md
# MAGIC ## Ejemplo 2: Valoracion por P/E
# MAGIC
# MAGIC Empresa XYZ:
# MAGIC * Utilidad por accion: $5.00
# MAGIC * P/E promedio del sector: 15x
# MAGIC
# MAGIC Estimar precio de la accion

# COMMAND ----------

# DBTITLE 1,Solucion 2
eps = 5.00
pe_sector = 15

precio_estimado = valoracion_pe(eps, pe_sector)

print(f"EPS: ${eps:.2f}")
print(f"P/E del sector: {pe_sector}x")
print(f"Precio estimado: ${precio_estimado:.2f}")
print(f"\nSi el precio actual es diferente:")
print(f"  > ${precio_estimado:.2f} = Sobrevalorada")
print(f"  < ${precio_estimado:.2f} = Subvalorada")

# COMMAND ----------

# DBTITLE 1,Resumen
# MAGIC %md
# MAGIC ## Resumen
# MAGIC
# MAGIC ### Puntos Clave
# MAGIC 1. DDM valua acciones por dividendos futuros
# MAGIC 2. Modelo de Gordon: dividendos con crecimiento constante
# MAGIC 3. P/E ratio compara precio vs utilidades
# MAGIC 4. Valoracion relativa usa multiplos del sector
# MAGIC
# MAGIC ### Consultas con Genie
# MAGIC * "Valua una accion con dividendo $3, crecimiento 4%, tasa requerida 10%"
# MAGIC * "Compara valoracion de estas 3 acciones por P/E"
# MAGIC * "Explica cuando usar DDM vs valoracion por multiplos"

# COMMAND ----------

