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
# MAGIC ### Notebook 0.6: Visualización de Datos
# MAGIC ### 📊 **MATPLOTLIB, SEABORN Y PLOTLY**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción
# MAGIC %md
# MAGIC # 📊 Introducción: Visualización de Datos en Finanzas
# MAGIC
# MAGIC ## 🎯 ¿Por qué visualizar datos?
# MAGIC
# MAGIC **"Una imagen vale más que mil números"**
# MAGIC
# MAGIC En finanzas, la visualización de datos es fundamental para:
# MAGIC
# MAGIC ✅ **Identificar tendencias**: Ver si un precio está subiendo o bajando
# MAGIC ✅ **Detectar anomalías**: Precios atípicos, volatilidad extrema
# MAGIC ✅ **Comparar activos**: Rendimientos de múltiples acciones
# MAGIC ✅ **Comunicar resultados**: Reportes ejecutivos, presentaciones
# MAGIC ✅ **Tomar decisiones**: Visualizar para decidir mejor
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🛠️ Las 3 Librerías de Visualización en Python
# MAGIC
# MAGIC ### 1️⃣ **Matplotlib** - La Base
# MAGIC
# MAGIC 🔹 **Características**:
# MAGIC * Librería más antigua y establecida
# MAGIC * Control total sobre cada elemento
# MAGIC * Gráficos estáticos de alta calidad
# MAGIC * Base de otras librerías (Seaborn usa Matplotlib)
# MAGIC
# MAGIC 👉 **Cuándo usarla**: Reportes estáticos, publicaciones, control preciso
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 2️⃣ **Seaborn** - La Elegante
# MAGIC
# MAGIC 🔹 **Características**:
# MAGIC * Construida sobre Matplotlib
# MAGIC * Gráficos estadísticos hermosos "out of the box"
# MAGIC * Temas profesionales predefinidos
# MAGIC * Sintaxis más simple que Matplotlib
# MAGIC
# MAGIC 👉 **Cuándo usarla**: Análisis exploratorio, gráficos estadísticos, correlaciones
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 3️⃣ **Plotly** - La Interactiva 🚀
# MAGIC
# MAGIC 🔹 **Características**:
# MAGIC * **Gráficos interactivos** (zoom, hover, pan)
# MAGIC * Dashboards profesionales
# MAGIC * Gráficos financieros especializados (candlestick, OHLC)
# MAGIC * Se ve en navegadores web
# MAGIC
# MAGIC 👉 **Cuándo usarla**: Dashboards interactivos, exploración de datos, presentaciones modernas
# MAGIC
# MAGIC 💎 **Recomendación para finanzas modernas**: **Plotly** es cada vez más popular
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📋 Estructura de Este Notebook
# MAGIC
# MAGIC **Parte 1: Matplotlib** (Gráficos Básicos)
# MAGIC * Gráficos de líneas, dispersión, barras
# MAGIC * Personalización
# MAGIC * Subplots
# MAGIC * Gráficos financieros
# MAGIC
# MAGIC **Parte 2: Seaborn** (Gráficos Estadísticos)
# MAGIC * Distribuciones
# MAGIC * Relaciones
# MAGIC * Heatmaps
# MAGIC * Correlaciones
# MAGIC
# MAGIC **Parte 3: Plotly** (Interactividad) 🚀
# MAGIC * Gráficos interactivos
# MAGIC * Candlestick charts
# MAGIC * Dashboards
# MAGIC * Casos financieros
# MAGIC
# MAGIC **Parte 4: Comparación y Casos Integrados**
# MAGIC * Cuándo usar cada librería
# MAGIC * Dashboard completo
# MAGIC * Paleta de colores UDA
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ⏱️ **Tiempo estimado**: 60-75 minutos
# MAGIC
# MAGIC ¡Empecemos a crear gráficos profesionales!

# COMMAND ----------

# DBTITLE 1,Explicación - Instalar Plotly
# MAGIC %md
# MAGIC ## 📦 Instalación de Plotly
# MAGIC
# MAGIC Matplotlib y Seaborn ya vienen instalados en Databricks, pero **Plotly necesita ser instalado**.
# MAGIC
# MAGIC 👉 Usamos el comando `%pip install` en una celda para instalar paquetes.
# MAGIC
# MAGIC **Nota**: Solo necesitas instalar una vez por sesión de cluster.

# COMMAND ----------

# DBTITLE 1,Código - Instalar Plotly
# MAGIC %pip install plotly --quiet

# COMMAND ----------

# DBTITLE 1,Explicación - Importar Librerías
# MAGIC %md
# MAGIC ## 📥 Importar las Librerías
# MAGIC
# MAGIC Antes de empezar a graficar, importamos las 3 librerías principales y otras auxiliares.
# MAGIC
# MAGIC ### Convenciones de importación
# MAGIC
# MAGIC ```python
# MAGIC import matplotlib.pyplot as plt  # "plt" es la convención universal
# MAGIC import seaborn as sns            # "sns" (por Samuel Norman Seaborn)
# MAGIC import plotly.express as px      # "px" para Express API (simple)
# MAGIC import plotly.graph_objects as go # "go" para Graph Objects (avanzado)
# MAGIC ```
# MAGIC
# MAGIC También importamos:
# MAGIC * `numpy` para generar datos
# MAGIC * `pandas` para manejar DataFrames

# COMMAND ----------

# DBTITLE 1,Código - Importar Librerías
# Importar librerías de visualización
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Librerías auxiliares
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo
sns.set_theme()  # Activar tema de Seaborn
plt.style.use('seaborn-v0_8-darkgrid')  # Estilo para matplotlib

print("✅ Librerías importadas correctamente")
print(f"   Matplotlib versión: {plt.matplotlib.__version__}")
print(f"   Seaborn versión: {sns.__version__}")
import plotly
print(f"   Plotly versión: {plotly.__version__}")

# COMMAND ----------

# DBTITLE 1,Sección - MATPLOTLIB Parte 1
# MAGIC %md
# MAGIC # 📊 MATPLOTLIB - Parte 1: Gráficos Básicos
# MAGIC
# MAGIC ## ¿Qué es Matplotlib?
# MAGIC
# MAGIC Matplotlib es la librería de visualización **más antigua y fundamental** de Python. Fue creada para replicar las capacidades de graficación de MATLAB.
# MAGIC
# MAGIC ### Estructura Básica
# MAGIC
# MAGIC ```python
# MAGIC import matplotlib.pyplot as plt
# MAGIC
# MAGIC # 1. Crear datos
# MAGIC x = [1, 2, 3, 4]
# MAGIC y = [10, 20, 25, 30]
# MAGIC
# MAGIC # 2. Crear gráfico
# MAGIC plt.plot(x, y)
# MAGIC
# MAGIC # 3. Mostrar
# MAGIC plt.show()
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Tipos de Gráficos Básicos
# MAGIC
# MAGIC ### 1. **plt.plot()** - Líneas
# MAGIC Perfecto para **series de tiempo**: precios a lo largo del tiempo
# MAGIC
# MAGIC ### 2. **plt.scatter()** - Dispersión
# MAGIC Perfecto para **relaciones**: riesgo vs rendimiento
# MAGIC
# MAGIC ### 3. **plt.bar()** - Barras
# MAGIC Perfecto para **comparaciones**: rendimientos de diferentes acciones
# MAGIC
# MAGIC ### 4. **plt.hist()** - Histograma
# MAGIC Perfecto para **distribuciones**: frecuencia de rendimientos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Vamos a ver ejemplos financieros de cada uno.

# COMMAND ----------

# DBTITLE 1,Código - Matplotlib Gráficos Básicos
# Crear datos de ejemplo: precios de una acción durante 30 días
fechas = pd.date_range(start='2024-01-01', periods=30, freq='D')
precios = [5000 + i*50 + np.random.randint(-100, 150) for i in range(30)]

# Crear figura con 4 subgráficos
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Matplotlib: Gráficos Básicos en Finanzas', fontsize=16, fontweight='bold')

# 1. GRÁFICO DE LÍNEAS - Evolución de precios
axes[0, 0].plot(fechas, precios, color='blue', linewidth=2)
axes[0, 0].set_title('1. Líneas: Evolución de Precio', fontweight='bold')
axes[0, 0].set_xlabel('Fecha')
axes[0, 0].set_ylabel('Precio ($)')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. GRÁFICO DE DISPERSIÓN - Riesgo vs Rendimiento
rendimientos = np.random.normal(0.10, 0.05, 20) * 100
volatilidad = np.random.normal(0.15, 0.03, 20) * 100
axes[0, 1].scatter(volatilidad, rendimientos, s=100, alpha=0.6, color='green')
axes[0, 1].set_title('2. Dispersión: Riesgo vs Rendimiento', fontweight='bold')
axes[0, 1].set_xlabel('Volatilidad (%)')
axes[0, 1].set_ylabel('Rendimiento (%)')
axes[0, 1].grid(True, alpha=0.3)

# 3. GRÁFICO DE BARRAS - Rendimientos de acciones
acciones = ['YPF', 'GGAL', 'MELI', 'COME', 'TRAN']
rendimientos_acciones = [15.5, 8.2, -3.5, 22.1, 5.8]
colores = ['green' if r > 0 else 'red' for r in rendimientos_acciones]
axes[1, 0].bar(acciones, rendimientos_acciones, color=colores, alpha=0.7)
axes[1, 0].set_title('3. Barras: Rendimientos por Acción', fontweight='bold')
axes[1, 0].set_xlabel('Acción')
axes[1, 0].set_ylabel('Rendimiento (%)')
axes[1, 0].axhline(y=0, color='black', linestyle='-', linewidth=0.5)
axes[1, 0].grid(True, alpha=0.3, axis='y')

# 4. HISTOGRAMA - Distribución de rendimientos diarios
rendimientos_diarios = np.random.normal(0.5, 2.0, 1000)
axes[1, 1].hist(rendimientos_diarios, bins=30, color='purple', alpha=0.7, edgecolor='black')
axes[1, 1].set_title('4. Histograma: Distribución de Rendimientos', fontweight='bold')
axes[1, 1].set_xlabel('Rendimiento Diario (%)')
axes[1, 1].set_ylabel('Frecuencia')
axes[1, 1].axvline(x=0, color='red', linestyle='--', linewidth=2, label='Rendimiento 0%')
axes[1, 1].legend()

plt.tight_layout()
plt.show()

print("✅ Gráficos básicos de Matplotlib creados")

# COMMAND ----------

# DBTITLE 1,Sección - MATPLOTLIB Parte 2
# MAGIC %md
# MAGIC # 🎨 MATPLOTLIB - Parte 2: Personalización
# MAGIC
# MAGIC ## Hacer Gráficos Profesionales
# MAGIC
# MAGIC Un gráfico básico no es suficiente para una presentación o reporte. Necesitamos **personalizarlo**.
# MAGIC
# MAGIC ### Elementos que podemos personalizar:
# MAGIC
# MAGIC 1. **Títulos**: `plt.title()`, `plt.suptitle()`
# MAGIC 2. **Etiquetas de ejes**: `plt.xlabel()`, `plt.ylabel()`
# MAGIC 3. **Leyendas**: `plt.legend()`
# MAGIC 4. **Colores**: `color='blue'`, `color='#FF5733'`
# MAGIC 5. **Estilos de línea**: `linestyle='-'`, `'--'`, `'-.'`, `':'`
# MAGIC 6. **Grosor de línea**: `linewidth=2`
# MAGIC 7. **Tamaño de figura**: `plt.figure(figsize=(12, 6))`
# MAGIC 8. **Grilla**: `plt.grid(True)`
# MAGIC 9. **Límites de ejes**: `plt.xlim()`, `plt.ylim()`
# MAGIC 10. **Anotaciones**: `plt.annotate()`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Ejemplo: Gráfico Profesional de Rendimientos

# COMMAND ----------

# DBTITLE 1,Código - Matplotlib Personalización
# Crear datos de múltiples acciones
fechas = pd.date_range(start='2024-01-01', periods=60, freq='D')

# Simular precios base
np.random.seed(42)
ypf_base = 5000
ggal_base = 175
meli_base = 1450

# Generar series de precios
ypf_precios = [ypf_base]
ggal_precios = [ggal_base]
meli_precios = [meli_base]

for i in range(1, 60):
    ypf_precios.append(ypf_precios[-1] * (1 + np.random.normal(0.002, 0.02)))
    ggal_precios.append(ggal_precios[-1] * (1 + np.random.normal(0.001, 0.015)))
    meli_precios.append(meli_precios[-1] * (1 + np.random.normal(0.0005, 0.01)))

# Normalizar a 100 para comparar
ypf_norm = [(p / ypf_precios[0]) * 100 for p in ypf_precios]
ggal_norm = [(p / ggal_precios[0]) * 100 for p in ggal_precios]
meli_norm = [(p / meli_precios[0]) * 100 for p in meli_precios]

# Crear gráfico profesional
plt.figure(figsize=(14, 8))

# Graficar las 3 acciones
plt.plot(fechas, ypf_norm, color='#1f77b4', linewidth=2.5, label='YPF', linestyle='-')
plt.plot(fechas, ggal_norm, color='#ff7f0e', linewidth=2.5, label='Banco Galicia', linestyle='--')
plt.plot(fechas, meli_norm, color='#2ca02c', linewidth=2.5, label='Mercado Libre', linestyle='-.')

# Línea de referencia en 100
plt.axhline(y=100, color='black', linestyle=':', linewidth=1, alpha=0.5, label='Valor Inicial')

# Títulos y etiquetas
plt.title('Comparación de Rendimiento Normalizado\nAcciones Argentinas - 2 Meses', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Fecha', fontsize=12, fontweight='bold')
plt.ylabel('Rendimiento Normalizado (Base 100)', fontsize=12, fontweight='bold')

# Leyenda
plt.legend(loc='upper left', fontsize=11, frameon=True, shadow=True)

# Grilla
plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

# Formato del eje X
plt.xticks(rotation=45)
plt.tight_layout()

# Agregar anotación
max_ypf_idx = np.argmax(ypf_norm)
plt.annotate(f'Máx: {ypf_norm[max_ypf_idx]:.1f}',
             xy=(fechas[max_ypf_idx], ypf_norm[max_ypf_idx]),
             xytext=(10, 10), textcoords='offset points',
             bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.show()

print("✅ Gráfico profesional personalizado creado")
print(f"\n📊 Rendimientos finales:")
print(f"   YPF: {ypf_norm[-1] - 100:+.2f}%")
print(f"   GGAL: {ggal_norm[-1] - 100:+.2f}%")
print(f"   MELI: {meli_norm[-1] - 100:+.2f}%")

# COMMAND ----------

# DBTITLE 1,Sección - SEABORN Parte 1
# MAGIC %md
# MAGIC # 🎨 SEABORN - Parte 1: Gráficos Elegantes
# MAGIC
# MAGIC ## ¿Qué es Seaborn?
# MAGIC
# MAGIC Seaborn es una librería de visualización **construida sobre Matplotlib** que facilita la creación de gráficos **estadísticos hermosos**.
# MAGIC
# MAGIC ### Ventajas sobre Matplotlib
# MAGIC
# MAGIC ✅ **Gráficos hermosos por defecto**: Sin necesidad de mucha personalización
# MAGIC ✅ **Temas profesionales**: `sns.set_theme()`
# MAGIC ✅ **Integración con Pandas**: Trabaja directamente con DataFrames
# MAGIC ✅ **Gráficos estadísticos avanzados**: Boxplots, violin plots, heatmaps
# MAGIC ✅ **Sintaxis más simple**: Menos líneas de código
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Gráficos Principales de Seaborn
# MAGIC
# MAGIC 1. **sns.histplot()** - Histogramas y distribuciones
# MAGIC 2. **sns.boxplot()** - Cajas y bigotes
# MAGIC 3. **sns.violinplot()** - Violines (distribución + densidad)
# MAGIC 4. **sns.scatterplot()** - Dispersión
# MAGIC 5. **sns.lineplot()** - Líneas
# MAGIC 6. **sns.heatmap()** - Mapas de calor (correlaciones)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Empecemos con distribuciones y cajas.

# COMMAND ----------

# DBTITLE 1,Código - Seaborn Distribuciones
# Generar datos de rendimientos de múltiples acciones
np.random.seed(123)

rendimientos_data = pd.DataFrame({
    'YPF': np.random.normal(0.12, 0.08, 250),
    'GGAL': np.random.normal(0.09, 0.06, 250),
    'MELI': np.random.normal(0.04, 0.05, 250),
    'COME': np.random.normal(0.15, 0.12, 250)
})

# Convertir a formato largo para Seaborn
rendimientos_long = rendimientos_data.melt(var_name='Acción', value_name='Rendimiento')
rendimientos_long['Rendimiento'] = rendimientos_long['Rendimiento'] * 100  # Convertir a %

# Crear figura con 3 subgráficos
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Seaborn: Gráficos Estadísticos de Rendimientos', fontsize=16, fontweight='bold')

# 1. HISTOGRAMA con KDE
sns.histplot(data=rendimientos_long, x='Rendimiento', hue='Acción', 
             kde=True, alpha=0.6, ax=axes[0])
axes[0].set_title('1. Histograma con KDE', fontweight='bold')
axes[0].set_xlabel('Rendimiento (%)')
axes[0].set_ylabel('Frecuencia')
axes[0].axvline(x=0, color='red', linestyle='--', linewidth=1)

# 2. BOXPLOT (Cajas y bigotes)
sns.boxplot(data=rendimientos_long, x='Acción', y='Rendimiento', 
            palette='Set2', ax=axes[1])
axes[1].set_title('2. Boxplot: Distribución y Outliers', fontweight='bold')
axes[1].set_xlabel('Acción')
axes[1].set_ylabel('Rendimiento (%)')
axes[1].axhline(y=0, color='red', linestyle='--', linewidth=1)

# 3. VIOLINPLOT (Densidad + Boxplot)
sns.violinplot(data=rendimientos_long, x='Acción', y='Rendimiento', 
               palette='muted', ax=axes[2])
axes[2].set_title('3. Violin Plot: Densidad Completa', fontweight='bold')
axes[2].set_xlabel('Acción')
axes[2].set_ylabel('Rendimiento (%)')
axes[2].axhline(y=0, color='red', linestyle='--', linewidth=1)

plt.tight_layout()
plt.show()

print("✅ Gráficos estadísticos de Seaborn creados")
print(f"\n📊 Estadísticas:")
for col in rendimientos_data.columns:
    media = rendimientos_data[col].mean() * 100
    std = rendimientos_data[col].std() * 100
    print(f"   {col}: Media {media:+.2f}%, Desv. Est. {std:.2f}%")

# COMMAND ----------

# DBTITLE 1,Sección - SEABORN Heatmap
# MAGIC %md
# MAGIC # 🔥 SEABORN - Parte 2: Heatmap (Matriz de Correlaciones)
# MAGIC
# MAGIC ## ¿Qué es un Heatmap?
# MAGIC
# MAGIC Un **heatmap** (mapa de calor) es una representación visual de una **matriz de números** usando colores.
# MAGIC
# MAGIC ### Uso en Finanzas: Correlaciones
# MAGIC
# MAGIC La **matriz de correlación** muestra cómo se relacionan los rendimientos de diferentes activos:
# MAGIC
# MAGIC * **Correlación = +1**: Se mueven juntos perfectamente (misma dirección)
# MAGIC * **Correlación = 0**: No hay relación
# MAGIC * **Correlación = -1**: Se mueven en direcciones opuestas
# MAGIC
# MAGIC 💡 **Importancia**: Para **diversificar** un portafolio, buscamos activos con **baja correlación**.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Sintaxis
# MAGIC
# MAGIC ```python
# MAGIC # Calcular matriz de correlación
# MAGIC corr_matrix = df.corr()
# MAGIC
# MAGIC # Crear heatmap
# MAGIC sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Código - Seaborn Heatmap
# Crear DataFrame con precios de 6 acciones argentinas
np.random.seed(456)
dias = 252  # Un año de trading

precios_df = pd.DataFrame({
    'YPF': np.cumsum(np.random.normal(0.001, 0.02, dias)) + 100,
    'GGAL': np.cumsum(np.random.normal(0.0008, 0.015, dias)) + 100,
    'MELI': np.cumsum(np.random.normal(0.0005, 0.012, dias)) + 100,
    'COME': np.cumsum(np.random.normal(0.001, 0.025, dias)) + 100,
    'TRAN': np.cumsum(np.random.normal(0.0002, 0.018, dias)) + 100,
    'LOMA': np.cumsum(np.random.normal(0.0009, 0.022, dias)) + 100
})

# Calcular rendimientos diarios
rendimientos_diarios = precios_df.pct_change().dropna()

# Calcular matriz de correlación
matriz_correlacion = rendimientos_diarios.corr()

# Crear figura con 2 heatmaps
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Seaborn: Matriz de Correlaciones entre Acciones', fontsize=16, fontweight='bold')

# 1. Heatmap con anotaciones
sns.heatmap(matriz_correlacion, annot=True, fmt='.2f', 
            cmap='coolwarm', center=0, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8},
            ax=axes[0])
axes[0].set_title('1. Matriz de Correlaciones (Completa)', fontweight='bold', pad=10)

# 2. Heatmap triangular (sin duplicados)
mask = np.triu(np.ones_like(matriz_correlacion, dtype=bool))
sns.heatmap(matriz_correlacion, mask=mask, annot=True, fmt='.2f',
            cmap='RdYlGn', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8},
            ax=axes[1])
axes[1].set_title('2. Matriz Triangular (Sin Duplicados)', fontweight='bold', pad=10)

plt.tight_layout()
plt.show()

print("✅ Heatmap de correlaciones creado")
print(f"\n🔗 Pares más correlacionados:")
corr_pairs = matriz_correlacion.unstack().sort_values(ascending=False)
corr_pairs = corr_pairs[corr_pairs < 1.0]  # Quitar diagonal
for i in range(3):
    pair = corr_pairs.index[i]
    corr_value = corr_pairs.iloc[i]
    print(f"   {pair[0]} - {pair[1]}: {corr_value:.3f}")

print(f"\n🔗 Pares menos correlacionados (mejor para diversificar):")
for i in range(-3, 0):
    pair = corr_pairs.index[i]
    corr_value = corr_pairs.iloc[i]
    print(f"   {pair[0]} - {pair[1]}: {corr_value:.3f}")

# COMMAND ----------

# DBTITLE 1,Sección - PLOTLY Parte 1
# MAGIC %md
# MAGIC # 🚀 PLOTLY - Parte 1: Gráficos Interactivos
# MAGIC
# MAGIC ## ¿Qué es Plotly?
# MAGIC
# MAGIC Plotly es una librería para crear **gráficos interactivos** de calidad profesional. Es el **estándar moderno** para dashboards financieros.
# MAGIC
# MAGIC ### 🌟 ¿Por qué Plotly es TAN popular en finanzas?
# MAGIC
# MAGIC ✅ **Interactividad nativa**:
# MAGIC * **Zoom**: Ampliar zonas específicas
# MAGIC * **Hover**: Ver valores exactos al pasar el mouse
# MAGIC * **Pan**: Desplazar el gráfico
# MAGIC * **Selección**: Marcar áreas de interés
# MAGIC * **Exportar**: Guardar como imagen PNG
# MAGIC
# MAGIC ✅ **Gráficos financieros especializados**:
# MAGIC * Candlestick (velas japonesas)
# MAGIC * OHLC (Open-High-Low-Close)
# MAGIC * Waterfall charts
# MAGIC
# MAGIC ✅ **Dashboards profesionales**:
# MAGIC * Múltiples subgráficos
# MAGIC * Actualización en tiempo real
# MAGIC * Integración con aplicaciones web
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Dos APIs de Plotly
# MAGIC
# MAGIC ### 1. **Plotly Express** (`px`) - Simple y Rápida
# MAGIC ```python
# MAGIC import plotly.express as px
# MAGIC fig = px.line(df, x='fecha', y='precio')
# MAGIC fig.show()
# MAGIC ```
# MAGIC ✅ **Usa esto** para gráficos rápidos
# MAGIC
# MAGIC ### 2. **Graph Objects** (`go`) - Control Total
# MAGIC ```python
# MAGIC import plotly.graph_objects as go
# MAGIC fig = go.Figure(data=go.Scatter(x=x, y=y))
# MAGIC fig.show()
# MAGIC ```
# MAGIC ✅ **Usa esto** para personalización avanzada
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Empecemos con Plotly Express.

# COMMAND ----------

# DBTITLE 1,Código - Plotly Gráficos Interactivos
# Crear datos de ejemplo: precios históricos de YPF
np.random.seed(789)
fechas = pd.date_range(start='2023-01-01', end='2024-06-01', freq='D')
precio_base = 5000

precios_ypf = [precio_base]
for i in range(1, len(fechas)):
    cambio = np.random.normal(0.001, 0.02)
    nuevo_precio = precios_ypf[-1] * (1 + cambio)
    precios_ypf.append(nuevo_precio)

df_ypf = pd.DataFrame({
    'Fecha': fechas,
    'Precio': precios_ypf,
    'Volumen': np.random.randint(800000, 2000000, len(fechas))
})

# Calcular medias móviles
df_ypf['MA_20'] = df_ypf['Precio'].rolling(window=20).mean()
df_ypf['MA_50'] = df_ypf['Precio'].rolling(window=50).mean()

print("✅ Datos preparados")
print(f"   Período: {fechas[0].date()} a {fechas[-1].date()}")
print(f"   Días: {len(fechas)}")
print(f"   Precio inicial: ${precios_ypf[0]:,.2f}")
print(f"   Precio final: ${precios_ypf[-1]:,.2f}")
print(f"   Rendimiento total: {((precios_ypf[-1] / precios_ypf[0]) - 1) * 100:+.2f}%")

# 1. GRÁFICO DE LÍNEAS INTERACTIVO
fig1 = px.line(df_ypf, x='Fecha', y='Precio',
               title='Plotly: Precio Histórico de YPF (INTERACTIVO)',
               labels={'Precio': 'Precio ($)', 'Fecha': 'Fecha'})

# Personalizar
fig1.update_traces(line_color='#1f77b4', line_width=2)
fig1.update_layout(
    hovermode='x unified',
    height=500,
    font=dict(size=12),
    title_font_size=16
)

fig1.show()

print("\n👆 Prueba estas interacciones:")
print("   • Pasa el mouse sobre el gráfico (hover)")
print("   • Haz zoom con la herramienta o seleccionando un área")
print("   • Doble clic para resetear el zoom")
print("   • Usa los botones de la barra superior")

# COMMAND ----------

# DBTITLE 1,Sección - PLOTLY Candlestick
# MAGIC %md
# MAGIC # 🕯️ PLOTLY - Parte 2: Candlestick (Velas Japonesas)
# MAGIC
# MAGIC ## ¿Qué es un Gráfico de Velas?
# MAGIC
# MAGIC El **gráfico de velas japonesas** (candlestick) es el **estándar** en finanzas para visualizar precios.
# MAGIC
# MAGIC ### Estructura de una Vela
# MAGIC
# MAGIC Cada vela representa **un período** (día, hora, minuto) y muestra **4 precios**:
# MAGIC
# MAGIC ```
# MAGIC    |
# MAGIC    |  <- High (Máximo)
# MAGIC  |───|
# MAGIC  |   | <- Open/Close (Apertura/Cierre)
# MAGIC  |   |    Si Close > Open: Vela VERDE (alcista)
# MAGIC  |   |    Si Close < Open: Vela ROJA (bajista)
# MAGIC  |───|
# MAGIC    |  <- Low (Mínimo)
# MAGIC    |
# MAGIC ```
# MAGIC
# MAGIC ### Datos OHLC
# MAGIC
# MAGIC **OHLC** = Open, High, Low, Close
# MAGIC
# MAGIC Necesitamos estas 4 columnas:
# MAGIC * **Open**: Precio de apertura
# MAGIC * **High**: Precio máximo
# MAGIC * **Low**: Precio mínimo
# MAGIC * **Close**: Precio de cierre
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Ventajas del Candlestick
# MAGIC
# MAGIC ✅ Muestra más información que una línea simple
# MAGIC ✅ Identifica patrones de trading
# MAGIC ✅ Estándar en plataformas financieras
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 👉 Vamos a crear un gráfico de velas con Plotly.

# COMMAND ----------

# DBTITLE 1,Código - Plotly Candlestick
# Crear datos OHLC (Open-High-Low-Close) para 60 días
np.random.seed(100)
fechas_ohlc = pd.date_range(start='2024-03-01', periods=60, freq='D')

ohlc_data = []
precio_actual = 5250

for fecha in fechas_ohlc:
    # Precio de apertura
    open_price = precio_actual
    
    # Simular variación intradiaria
    variacion = np.random.normal(0, 150)
    close_price = open_price + variacion
    
    # High y Low
    high_price = max(open_price, close_price) + abs(np.random.normal(0, 50))
    low_price = min(open_price, close_price) - abs(np.random.normal(0, 50))
    
    # Volumen
    volumen = np.random.randint(1000000, 3000000)
    
    ohlc_data.append({
        'Fecha': fecha,
        'Open': open_price,
        'High': high_price,
        'Low': low_price,
        'Close': close_price,
        'Volumen': volumen
    })
    
    # Actualizar precio para el siguiente día
    precio_actual = close_price

df_ohlc = pd.DataFrame(ohlc_data)

print("✅ Datos OHLC generados")
print(f"   Período: {df_ohlc['Fecha'].min().date()} a {df_ohlc['Fecha'].max().date()}")
print(f"   Precio inicial: ${df_ohlc['Open'].iloc[0]:,.2f}")
print(f"   Precio final: ${df_ohlc['Close'].iloc[-1]:,.2f}")
print(f"   Rendimiento: {((df_ohlc['Close'].iloc[-1] / df_ohlc['Open'].iloc[0]) - 1) * 100:+.2f}%")

# Crear gráfico de velas japonesas
fig_candle = go.Figure(data=[go.Candlestick(
    x=df_ohlc['Fecha'],
    open=df_ohlc['Open'],
    high=df_ohlc['High'],
    low=df_ohlc['Low'],
    close=df_ohlc['Close'],
    name='YPF'
)])

# Personalizar
fig_candle.update_layout(
    title='Plotly: Gráfico de Velas Japonesas - YPF',
    yaxis_title='Precio ($)',
    xaxis_title='Fecha',
    height=600,
    xaxis_rangeslider_visible=False,  # Ocultar rango slider
    hovermode='x unified',
    font=dict(size=12)
)

fig_candle.show()

print("\n👆 Interpretación de las velas:")
print("   🟢 VERDE: El precio de cierre fue mayor que la apertura (alcista)")
print("   🔴 ROJA: El precio de cierre fue menor que la apertura (bajista)")
print("   📊 Las 'mechas' muestran el rango High-Low del día")
print("\n👆 Interacciones:")
print("   • Hover para ver OHLC exactos")
print("   • Zoom para analizar períodos específicos")
print("   • Identifica patrones visuales")

# COMMAND ----------

# DBTITLE 1,Sección - PLOTLY Dashboard
# MAGIC %md
# MAGIC # 📊 PLOTLY - Parte 3: Dashboard de Análisis
# MAGIC
# MAGIC ## Crear Dashboards con Subplots
# MAGIC
# MAGIC Un **dashboard** combina múltiples gráficos en una sola visualización.
# MAGIC
# MAGIC ### `make_subplots()`
# MAGIC
# MAGIC Plotly permite crear **layouts complejos** con múltiples subgráficos:
# MAGIC
# MAGIC ```python
# MAGIC from plotly.subplots import make_subplots
# MAGIC import plotly.graph_objects as go
# MAGIC
# MAGIC fig = make_subplots(
# MAGIC     rows=2, cols=2,
# MAGIC     specs=[[{'type': 'scatter'}, {'type': 'bar'}],
# MAGIC            [{'colspan': 2}, None]]
# MAGIC )
# MAGIC
# MAGIC fig.add_trace(go.Scatter(...), row=1, col=1)
# MAGIC fig.add_trace(go.Bar(...), row=1, col=2)
# MAGIC fig.add_trace(go.Candlestick(...), row=2, col=1)
# MAGIC
# MAGIC fig.show()
# MAGIC ```
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Uso en Finanzas
# MAGIC
# MAGIC Dashboards típicos incluyen:
# MAGIC
# MAGIC 1. **Precios históricos** (Candlestick)
# MAGIC 2. **Volumen de operaciones** (Barras)
# MAGIC 3. **Indicadores técnicos** (Líneas: MA, RSI, MACD)
# MAGIC 4. **Distribución de rendimientos** (Histograma)
# MAGIC
# MAGIC 👉 Vamos a crear un dashboard completo.

# COMMAND ----------

# DBTITLE 1,Código - Plotly Dashboard
# Usar los datos OHLC anteriores y agregar indicadores
df_dash = df_ohlc.copy()

# Calcular medias móviles
df_dash['MA_10'] = df_dash['Close'].rolling(window=10).mean()
df_dash['MA_20'] = df_dash['Close'].rolling(window=20).mean()

# Calcular rendimientos diarios
df_dash['Rendimiento'] = df_dash['Close'].pct_change() * 100

print("✅ Indicadores calculados")

# Crear dashboard con subplots
fig_dash = make_subplots(
    rows=3, cols=2,
    subplot_titles=('Precio y Medias Móviles', 'Volumen de Operaciones',
                    'Candlestick con Zoom', 'Distribución de Rendimientos',
                    'Evolución del Precio (Normalizado)', 'Rendimientos Diarios'),
    specs=[[{'type': 'scatter'}, {'type': 'bar'}],
           [{'type': 'candlestick'}, {'type': 'histogram'}],
           [{'type': 'scatter'}, {'type': 'scatter'}]],
    row_heights=[0.3, 0.4, 0.3],
    vertical_spacing=0.08,
    horizontal_spacing=0.1
)

# 1. Precio y Medias Móviles
fig_dash.add_trace(go.Scatter(x=df_dash['Fecha'], y=df_dash['Close'], 
                              name='Precio', line=dict(color='blue', width=2)),
                   row=1, col=1)
fig_dash.add_trace(go.Scatter(x=df_dash['Fecha'], y=df_dash['MA_10'], 
                              name='MA 10', line=dict(color='orange', width=1.5)),
                   row=1, col=1)
fig_dash.add_trace(go.Scatter(x=df_dash['Fecha'], y=df_dash['MA_20'], 
                              name='MA 20', line=dict(color='red', width=1.5)),
                   row=1, col=1)

# 2. Volumen
fig_dash.add_trace(go.Bar(x=df_dash['Fecha'], y=df_dash['Volumen'], 
                          name='Volumen', marker_color='lightblue'),
                   row=1, col=2)

# 3. Candlestick
fig_dash.add_trace(go.Candlestick(
    x=df_dash['Fecha'],
    open=df_dash['Open'],
    high=df_dash['High'],
    low=df_dash['Low'],
    close=df_dash['Close'],
    name='OHLC'),
    row=2, col=1)

# 4. Histograma de rendimientos
fig_dash.add_trace(go.Histogram(x=df_dash['Rendimiento'].dropna(), 
                                name='Rendimientos', 
                                marker_color='purple', 
                                nbinsx=20),
                   row=2, col=2)

# 5. Precio normalizado
precio_norm = (df_dash['Close'] / df_dash['Close'].iloc[0]) * 100
fig_dash.add_trace(go.Scatter(x=df_dash['Fecha'], y=precio_norm, 
                              name='Normalizado (Base 100)', 
                              line=dict(color='green', width=2),
                              fill='tozeroy'),
                   row=3, col=1)

# 6. Rendimientos diarios
colores = ['green' if r > 0 else 'red' for r in df_dash['Rendimiento'].fillna(0)]
fig_dash.add_trace(go.Bar(x=df_dash['Fecha'], y=df_dash['Rendimiento'], 
                          name='Rend. Diario', marker_color=colores),
                   row=3, col=2)

# Actualizar layout
fig_dash.update_layout(
    title_text='Dashboard Completo: Análisis de YPF',
    title_font_size=18,
    height=1200,
    showlegend=False,
    hovermode='x unified'
)

# Quitar rangeslider del candlestick
fig_dash.update_xaxes(rangeslider_visible=False, row=2, col=1)

fig_dash.show()

print("\n✅ Dashboard interactivo creado")
print("\n📊 Resumen del Análisis:")
print(f"   Rendimiento total: {((df_dash['Close'].iloc[-1] / df_dash['Close'].iloc[0]) - 1) * 100:+.2f}%")
print(f"   Volatilidad (std rendimientos): {df_dash['Rendimiento'].std():.2f}%")
print(f"   Mejor día: {df_dash['Rendimiento'].max():+.2f}%")
print(f"   Peor día: {df_dash['Rendimiento'].min():+.2f}%")
print(f"   Volumen promedio: {df_dash['Volumen'].mean():,.0f}")

# COMMAND ----------

# DBTITLE 1,Sección - Comparación
# MAGIC %md
# MAGIC # ⚖️ COMPARACIÓN: Matplotlib vs Seaborn vs Plotly
# MAGIC
# MAGIC ## ¿Cuándo usar cada librería?
# MAGIC
# MAGIC ### 🟦 **Matplotlib** - Control Total
# MAGIC
# MAGIC **✅ Usa Matplotlib cuando**:
# MAGIC * Necesitas control preciso sobre cada elemento
# MAGIC * Reportes estáticos para publicación
# MAGIC * Gráficos para papers académicos
# MAGIC * Exportar imágenes de alta resolución
# MAGIC
# MAGIC **❌ NO uses Matplotlib para**:
# MAGIC * Dashboards interactivos
# MAGIC * Exploración rápida de datos
# MAGIC * Presentaciones modernas
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🟩 **Seaborn** - Elegancia Rápida
# MAGIC
# MAGIC **✅ Usa Seaborn cuando**:
# MAGIC * Análisis exploratorio de datos (EDA)
# MAGIC * Gráficos estadísticos (distribuciones, correlaciones)
# MAGIC * Quieres gráficos hermosos con poco código
# MAGIC * Trabajas con DataFrames de Pandas
# MAGIC
# MAGIC **❌ NO uses Seaborn para**:
# MAGIC * Gráficos interactivos
# MAGIC * Dashboards en producción
# MAGIC * Personalización extrema
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🟨 **Plotly** - Interactividad Moderna 🚀
# MAGIC
# MAGIC **✅ Usa Plotly cuando**:
# MAGIC * **Dashboards interactivos** (LA RAZÓN #1)
# MAGIC * Presentaciones modernas
# MAGIC * Exploración de datos en equipo
# MAGIC * Gráficos financieros especializados (candlestick)
# MAGIC * Necesitas zoom, hover, pan
# MAGIC * Aplicaciones web
# MAGIC
# MAGIC **❌ NO uses Plotly para**:
# MAGIC * Reportes estáticos impresos (puede ser pesado)
# MAGIC * Cuando no necesitas interactividad
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🏆 Recomendación para Finanzas
# MAGIC
# MAGIC **Para análisis y dashboards modernos**: **Plotly** 🚀
# MAGIC
# MAGIC **Para reportes estáticos**: **Matplotlib** o **Seaborn**
# MAGIC
# MAGIC **Para exploración rápida**: **Seaborn**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Comparación Visual
# MAGIC
# MAGIC Vamos a crear el **mismo gráfico** con las 3 librerías.

# COMMAND ----------

# DBTITLE 1,Código - Comparación Visual
# Datos comunes
fechas_comp = pd.date_range(start='2024-01-01', periods=90, freq='D')
precios_comp = 5000 + np.cumsum(np.random.normal(10, 80, 90))

df_comp = pd.DataFrame({'Fecha': fechas_comp, 'Precio': precios_comp})

print("═" * 70)
print("COMPARACIÓN: Mismo gráfico en 3 librerías")
print("═" * 70)

# 1. MATPLOTLIB
print("\n1️⃣ MATPLOTLIB:")
plt.figure(figsize=(12, 4))
plt.plot(df_comp['Fecha'], df_comp['Precio'], color='blue', linewidth=2)
plt.title('Precio de YPF - Matplotlib', fontsize=14, fontweight='bold')
plt.xlabel('Fecha')
plt.ylabel('Precio ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
print("   ✅ Gráfico estático creado")
print("   • Pros: Control total, alta resolución")
print("   • Contras: No es interactivo")

# 2. SEABORN
print("\n2️⃣ SEABORN:")
plt.figure(figsize=(12, 4))
sns.lineplot(data=df_comp, x='Fecha', y='Precio', linewidth=2.5)
plt.title('Precio de YPF - Seaborn', fontsize=14, fontweight='bold')
plt.xlabel('Fecha')
plt.ylabel('Precio ($)')
plt.tight_layout()
plt.show()
print("   ✅ Gráfico elegante creado")
print("   • Pros: Hermoso por defecto, sintaxis simple")
print("   • Contras: No es interactivo")

# 3. PLOTLY
print("\n3️⃣ PLOTLY:")
fig_comp = px.line(df_comp, x='Fecha', y='Precio',
                   title='Precio de YPF - Plotly (INTERACTIVO)')
fig_comp.update_traces(line_color='blue', line_width=3)
fig_comp.update_layout(height=400, hovermode='x unified')
fig_comp.show()
print("   ✅ Gráfico interactivo creado")
print("   • Pros: INTERACTIVO, zoom, hover, moderno")
print("   • Contras: Puede ser más pesado")

print("\n" + "═" * 70)
print("🏆 VEREDICTO PARA FINANZAS:")
print("═" * 70)
print("\n🥇 GANADOR: Plotly")
print("   La interactividad es CLAVE para análisis financiero moderno")
print("\n🥈 Segundo lugar: Seaborn")
print("   Perfecto para EDA rápido y reportes internos")
print("\n🥉 Tercer lugar: Matplotlib")
print("   Aún útil para reportes estáticos especializados")

# COMMAND ----------

# DBTITLE 1,Ejercicios Prácticos
# MAGIC %md
# MAGIC ## ✍️ EJERCICIOS PRÁCTICOS
# MAGIC
# MAGIC ### 🔹 Ejercicio 1: Matplotlib - Líneas Múltiples
# MAGIC Crea un gráfico con los precios de 3 acciones (YPF, GGAL, MELI) en el mismo gráfico.
# MAGIC **Datos**: Genera 30 días de precios aleatorios para cada una.
# MAGIC
# MAGIC ### 🔹 Ejercicio 2: Matplotlib - Barras Comparativas
# MAGIC Crea un gráfico de barras comparando los rendimientos anuales de 5 acciones.
# MAGIC **Usa colores**: Verde para positivos, rojo para negativos.
# MAGIC
# MAGIC ### 🔹 Ejercicio 3: Matplotlib - Subplots
# MAGIC Crea una figura con 2x2 subplots mostrando: precio, volumen, histograma de rendimientos, y boxplot.
# MAGIC
# MAGIC ### 🔹 Ejercicio 4: Seaborn - Histograma con KDE
# MAGIC Crea un histograma de 1000 rendimientos diarios simulados con curva KDE superpuesta.
# MAGIC
# MAGIC ### 🔹 Ejercicio 5: Seaborn - Heatmap de Correlaciones
# MAGIC Genera datos de 5 acciones (100 días) y crea un heatmap de sus correlaciones.
# MAGIC **Personaliza**: Usa cmap='RdYlGn' y annot=True.
# MAGIC
# MAGIC ### 🔹 Ejercicio 6: Seaborn - Boxplot Comparativo
# MAGIC Crea un boxplot comparando la distribución de rendimientos de 4 sectores diferentes.
# MAGIC
# MAGIC ### 🔹 Ejercicio 7: Plotly - Línea Interactiva con Hover
# MAGIC Crea un gráfico de línea interactivo de precios con hover personalizado mostrando fecha y precio.
# MAGIC
# MAGIC ### 🔹 Ejercicio 8: Plotly - Scatter con Color y Tamaño
# MAGIC Crea un scatter plot de Riesgo vs Rendimiento donde:
# MAGIC * Color = Sector
# MAGIC * Tamaño = Capitalización de mercado
# MAGIC
# MAGIC ### 🔹 Ejercicio 9: Plotly - Candlestick de 30 Días
# MAGIC Genera datos OHLC para 30 días y crea un gráfico de velas japonesas.
# MAGIC
# MAGIC ### 🔹 Ejercicio 10: Plotly - Dashboard Simple
# MAGIC Crea un dashboard con 2 subplots:
# MAGIC 1. Candlestick de precios
# MAGIC 2. Barras de volumen
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 DESAFÍO FINAL: Dashboard Completo con las 3 Librerías
# MAGIC
# MAGIC **Objetivo**: Crear un reporte visual completo de un portafolio de 4 acciones argentinas.
# MAGIC
# MAGIC **Requisitos**:
# MAGIC
# MAGIC 1. **Matplotlib**: Gráfico de líneas múltiples (precios normalizados)
# MAGIC 2. **Seaborn**: Heatmap de correlaciones
# MAGIC 3. **Plotly**: Dashboard interactivo con:
# MAGIC    * Candlestick de cada acción
# MAGIC    * Volumen
# MAGIC    * Distribución de rendimientos
# MAGIC    * Resumen de métricas
# MAGIC
# MAGIC **Bonus**: Aplicar la paleta de colores UDA en todos los gráficos.

# COMMAND ----------

# DBTITLE 1,Consultas con Genie
# MAGIC %md
# MAGIC ## 🤖 CONSULTAS CON GENIE CODE
# MAGIC
# MAGIC ### 📊 Matplotlib
# MAGIC 1. ¿Cuál es la diferencia entre `plt.plot()` y `plt.scatter()`?
# MAGIC 2. ¿Cómo cambio el tamaño de una figura en Matplotlib?
# MAGIC 3. ¿Qué hace `plt.tight_layout()`?
# MAGIC 4. ¿Cómo creo subplots en Matplotlib?
# MAGIC 5. ¿Cómo guardo un gráfico como imagen PNG?
# MAGIC 6. ¿Cómo cambio los colores de las líneas?
# MAGIC 7. ¿Qué estilos de línea existen? (`linestyle`)
# MAGIC 8. ¿Cómo agrego una leyenda?
# MAGIC 9. ¿Cómo roto las etiquetas del eje X?
# MAGIC 10. ¿Qué es `plt.figure()` vs `plt.subplot()`?
# MAGIC 11. ¿Cómo agrego anotaciones con flechas?
# MAGIC 12. ¿Cómo crear un gráfico de área?
# MAGIC 13. Muéstrame 10 paletas de colores de Matplotlib
# MAGIC 14. ¿Cómo crear un histograma con bins personalizados?
# MAGIC 15. ¿Qué hace `plt.axhline()` y `plt.axvline()`?
# MAGIC
# MAGIC ### 🎨 Seaborn
# MAGIC 16. ¿Qué ventajas tiene Seaborn sobre Matplotlib?
# MAGIC 17. ¿Cómo cambio el tema de Seaborn?
# MAGIC 18. ¿Qué hace `sns.set_theme()`?
# MAGIC 19. ¿Cuál es la diferencia entre `histplot()` y `distplot()`?
# MAGIC 20. ¿Cómo creo un heatmap triangular?
# MAGIC 21. ¿Qué es un violinplot y cuándo usarlo?
# MAGIC 22. ¿Cómo usar `hue` para colorear por categoría?
# MAGIC 23. ¿Qué hace `sns.pairplot()`?
# MAGIC 24. ¿Cómo crear un countplot?
# MAGIC 25. ¿Qué paletas de colores tiene Seaborn?
# MAGIC 26. ¿Cómo personalizar un heatmap (annot, fmt, cmap)?
# MAGIC 27. ¿Qué es `sns.regplot()` y cómo funciona?
# MAGIC 28. ¿Cómo hacer un boxplot horizontal?
# MAGIC 29. Muéstrame 5 tipos de gráficos estadísticos de Seaborn
# MAGIC 30. ¿Cómo integrar Seaborn con Matplotlib para personalización?
# MAGIC
# MAGIC ### 🚀 Plotly
# MAGIC 31. ¿Qué diferencia hay entre Plotly Express y Graph Objects?
# MAGIC 32. ¿Cuándo usar `px` vs `go`?
# MAGIC 33. ¿Cómo hacer que un gráfico sea interactivo?
# MAGIC 34. ¿Qué es `fig.show()` en Plotly?
# MAGIC 35. ¿Cómo personalizar el hover?
# MAGIC 36. ¿Cómo crear un candlestick chart?
# MAGIC 37. ¿Qué datos necesito para un gráfico OHLC?
# MAGIC 38. ¿Cómo crear subplots en Plotly?
# MAGIC 39. ¿Qué hace `make_subplots()`?
# MAGIC 40. ¿Cómo quitar el rangeslider de un candlestick?
# MAGIC 41. ¿Cómo exportar un gráfico de Plotly como imagen?
# MAGIC 42. ¿Qué es `hovermode='x unified'`?
# MAGIC 43. ¿Cómo cambiar el tema/template de Plotly?
# MAGIC 44. ¿Cómo agregar botones de interacción?
# MAGIC 45. ¿Cómo crear un gráfico de waterfall?
# MAGIC 46. ¿Qué es `fig.update_layout()`?
# MAGIC 47. ¿Cómo crear animaciones en Plotly?
# MAGIC 48. ¿Cómo hacer un scatter con línea de tendencia?
# MAGIC 49. Muéstrame 10 tipos de gráficos de Plotly
# MAGIC 50. ¿Cómo integrar Plotly con Dash?
# MAGIC
# MAGIC ### 💼 Aplicaciones Financieras
# MAGIC 51. Crea un gráfico de rendimientos acumulados
# MAGIC 52. Crea un gráfico de frontera eficiente (riesgo-rendimiento)
# MAGIC 53. Visualiza la evolución de un portafolio
# MAGIC 54. Crea un gráfico de torta de asignación de activos
# MAGIC 55. Visualiza la volatilidad histórica
# MAGIC 56. Crea un gráfico de bandas de Bollinger
# MAGIC 57. Visualiza el VaR (Valor en Riesgo)
# MAGIC 58. Crea un gráfico de correlaciones rodantes
# MAGIC 59. Visualiza backtest de estrategias de trading
# MAGIC 60. Crea un dashboard de métricas de riesgo
# MAGIC
# MAGIC ### ⚖️ Comparación
# MAGIC 61. ¿Cuándo usar Matplotlib vs Seaborn vs Plotly?
# MAGIC 62. ¿Cuál es más rápida para renderizar?
# MAGIC 63. ¿Cuál consume más memoria?
# MAGIC 64. ¿Puedo combinar las 3 en un mismo proyecto?
# MAGIC 65. ¿Cuál es mejor para reportes PDF?
# MAGIC 66. ¿Cuál es mejor para dashboards web?
# MAGIC 67. Comparación de curva de aprendizaje
# MAGIC 68. ¿Cuál tiene más documentación?
# MAGIC
# MAGIC ### 🎨 Personalización
# MAGIC 69. ¿Cómo crear una paleta de colores personalizada?
# MAGIC 70. ¿Cómo aplicar colores corporativos (UDA)?
# MAGIC 71. ¿Cómo agregar logos a los gráficos?
# MAGIC 72. ¿Cómo crear templates reutilizables?
# MAGIC 73. ¿Cómo hacer gráficos con fondo oscuro?
# MAGIC 74. ¿Cómo cambiar las fuentes de texto?
# MAGIC 75. Best practices de visualización de datos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🎉 ¡Felicitaciones!
# MAGIC
# MAGIC Has completado el **Notebook 0.6 - Visualización de Datos**.
# MAGIC
# MAGIC ### ¿Qué aprendiste?
# MAGIC
# MAGIC ✅ **Matplotlib**: Gráficos básicos, personalización, subplots
# MAGIC ✅ **Seaborn**: Gráficos estadísticos elegantes, heatmaps, distribuciones
# MAGIC ✅ **Plotly**: Gráficos interactivos, candlestick, dashboards 🚀
# MAGIC ✅ **Comparación**: Cuándo usar cada librería
# MAGIC ✅ **Aplicaciones**: Dashboards financieros completos
# MAGIC
# MAGIC ### 👉 Próximo Paso
# MAGIC
# MAGIC **Notebook 0.7 - Python Aplicado a Finanzas**: Integrar todo lo aprendido en casos reales.
# MAGIC
# MAGIC ¡Sigue avanzando! 🚀

# COMMAND ----------

# DBTITLE 1,TODO Final
# MAGIC %md
# MAGIC # ✅ TODO PARA COMPLETAR (Final del notebook)
# MAGIC
# MAGIC **PLOTLY PARTE 3 - CANDLESTICK COMPLETO** 
# MAGIC - Markdown explicativo (velas japonesas, OHLC)
# MAGIC - Código: Datos simulados YPF 30 días, gráfico candlestick + volumen
# MAGIC
# MAGIC **PLOTLY PARTE 4 - DASHBOARD INTERACTIVO**
# MAGIC - Markdown explicativo (subplots)
# MAGIC - Código: Dashboard 2x2 con línea precios, barras volumen, scatter rendimientos, heatmap correlación
# MAGIC
# MAGIC **PARTE FINAL - COMPARACIÓN DE LIBRERÍAS**
# MAGIC - Tabla comparativa Matplotlib vs Seaborn vs Plotly
# MAGIC - Código: Mismo gráfico en las tres
# MAGIC
# MAGIC **PALETA DE COLORES UDA**
# MAGIC - Definir colores institucionales
# MAGIC - Código: Usar azul, rojo, verde UDA en gráficos
# MAGIC
# MAGIC **CASOS INTEGRADOS**
# MAGIC - 3 casos: Análisis técnico YPF (precio + MA + Bollinger), Comparación múltiples acciones Merval, Dashboard ejecutivo cartera
# MAGIC
# MAGIC **EJERCICIOS PRÁCTICOS**
# MAGIC - 5 ejercicios: Líneas dólar blue, heatmap rendimientos por sector, boxplot volatilidad por acción, dashboard bonos argentinos, gráfico interactivo cartera
# MAGIC
# MAGIC **CONSULTAS GENIE**
# MAGIC - 3 ejemplos de consultas sobre visualizaciones
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC *Datos argentinos, comentarios en español, usar display() en gráficos, NO ejecutar las celdas, solo crearlas*