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
# MAGIC ### Módulo 03: Análisis Financiero
# MAGIC ### Notebook 3.2: Sistema DuPont y Apalancamiento
# MAGIC ### 🔍 **ANÁLISIS ROE Y APALANCAMIENTO**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción
# MAGIC %md
# MAGIC # 📊 Sistema DuPont y Apalancamiento Financiero
# MAGIC
# MAGIC ## 🎯 Objetivo del Notebook
# MAGIC
# MAGIC Este notebook profundiza en **herramientas avanzadas de análisis financiero** que permiten:
# MAGIC
# MAGIC 1. ✅ **Sistema DuPont**: Descomponer el ROE para identificar las fuentes de rentabilidad
# MAGIC 2. ✅ **Apalancamiento Operativo**: Analizar el impacto de los costos fijos en la operación
# MAGIC 3. ✅ **Apalancamiento Financiero**: Evaluar el efecto de la deuda en la rentabilidad
# MAGIC 4. ✅ **Análisis Integrado**: Combinar todas las herramientas para evaluación completa
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📚 Referencia Bibliográfica
# MAGIC
# MAGIC **Libro**: *Finanzas Corporativas - Un Enfoque Latinoamericano* (2ª ed.)  
# MAGIC **Autor**: Guillermo L. Dumrauf  
# MAGIC **Capítulo 4**: Análisis de Estados Financieros II  
# MAGIC **Páginas**: 123-147
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📈 Temas Cubiertos
# MAGIC
# MAGIC ### 1. Sistema DuPont
# MAGIC * DuPont de 3 factores (clásico)
# MAGIC * DuPont de 5 factores (extendido)
# MAGIC * Análisis comparativo de empresas argentinas
# MAGIC
# MAGIC ### 2. Apalancamiento Operativo (DOL)
# MAGIC * Grado de apalancamiento operativo
# MAGIC * Punto de equilibrio
# MAGIC * Impacto de costos fijos vs variables
# MAGIC
# MAGIC ### 3. Apalancamiento Financiero (DFL)
# MAGIC * Grado de apalancamiento financiero
# MAGIC * Estructura de capital
# MAGIC * Efecto de la deuda
# MAGIC
# MAGIC ### 4. Apalancamiento Combinado (DCL)
# MAGIC * Efecto total del apalancamiento
# MAGIC * Análisis de riesgo integrado
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🇦🇷 Datos Utilizados
# MAGIC
# MAGIC Analizaremos estados contables reales de empresas argentinas:
# MAGIC * **BYMA** (Bolsas y Mercados Argentinos)
# MAGIC * **Caja de Valores**
# MAGIC

# COMMAND ----------

# DBTITLE 1,Explicación - Sistema DuPont 3 Factores
# MAGIC %md
# MAGIC ## 📊 PARTE 1: Sistema DuPont de 3 Factores
# MAGIC
# MAGIC ### ¿Qué es el Sistema DuPont?
# MAGIC
# MAGIC El **Sistema DuPont** es una herramienta fundamental desarrollada en 1914 por la empresa DuPont que **descompone el ROE (Return on Equity)** en sus componentes clave para identificar las fuentes de rentabilidad.
# MAGIC
# MAGIC ### Fórmula DuPont de 3 Factores
# MAGIC
# MAGIC $$
# MAGIC \text{ROE} = \underbrace{\frac{\text{Utilidad Neta}}{\text{Ventas}}}_{\text{Margen}} \times \underbrace{\frac{\text{Ventas}}{\text{Activos}}}_{\text{Rotación}} \times \underbrace{\frac{\text{Activos}}{\text{Patrimonio}}}_{\text{Apalancamiento}}
# MAGIC $$
# MAGIC
# MAGIC ### Interpretación de los 3 Componentes
# MAGIC
# MAGIC 1. **Margen de Utilidad Neta** (Eficiencia operativa)
# MAGIC    * ¿Cuánto gana la empresa por cada peso de venta?
# MAGIC    * Indica control de costos y pricing power
# MAGIC    * Ejemplo: 10% = $0.10 de ganancia por cada $1 vendido
# MAGIC
# MAGIC 2. **Rotación de Activos** (Eficiencia en uso de recursos)
# MAGIC    * ¿Cuántas veces "rotan" los activos generando ventas?
# MAGIC    * Indica productividad de los activos
# MAGIC    * Ejemplo: 2.0 = genera $2 de ventas por cada $1 de activos
# MAGIC
# MAGIC 3. **Multiplicador de Apalancamiento** (Estructura financiera)
# MAGIC    * ¿Cuántos activos tiene la empresa por cada peso de patrimonio?
# MAGIC    * Indica nivel de endeudamiento
# MAGIC    * Ejemplo: 2.5 = tiene $2.50 de activos por cada $1 de patrimonio propio
# MAGIC
# MAGIC ### ¿Por qué es útil?
# MAGIC
# MAGIC ✅ **Identifica fortalezas y debilidades**: Una empresa puede tener alto ROE por diferentes razones
# MAGIC ✅ **Comparación sectorial**: Retail tiene alta rotación y bajo margen; Tech tiene bajo margen pero alta rotación
# MAGIC ✅ **Diagnóstico estratégico**: Saber dónde enfocar mejoras (costos, ventas o estructura de capital)
# MAGIC
# MAGIC ### Ejemplo Conceptual
# MAGIC
# MAGIC **Empresa A**: ROE = 15% = 5% margen × 1.5 rotación × 2.0 apalancamiento  
# MAGIC **Empresa B**: ROE = 15% = 3% margen × 2.5 rotación × 2.0 apalancamiento
# MAGIC
# MAGIC Ambas tienen mismo ROE, pero Empresa A es más rentable por operación, mientras Empresa B compensa con mayor volumen.

# COMMAND ----------

# DBTITLE 1,Código - Función DuPont 3 Factores
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Tuple

# Colores institucionales UDA
COLOR_UDA_AZUL = '#1f4788'
COLOR_UDA_CELESTE = '#4a90e2'

# Configuración de visualizaciones
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette([COLOR_UDA_AZUL, COLOR_UDA_CELESTE, '#28a745', '#ffc107', '#dc3545'])

def calcular_dupont_3_factores(utilidad_neta: float, 
                                ventas: float, 
                                activos: float, 
                                patrimonio: float) -> Dict[str, float]:
    """
    Calcula el Sistema DuPont de 3 factores (clásico).
    
    El ROE se descompone en tres componentes multiplicativos:
    ROE = Margen × Rotación × Apalancamiento
    
    Parámetros:
    -----------
    utilidad_neta : float
        Utilidad neta del período (en pesos)
    ventas : float
        Ingresos por ventas del período (en pesos)
    activos : float
        Total de activos (en pesos)
    patrimonio : float
        Total de patrimonio neto (en pesos)
    
    Retorna:
    --------
    Dict[str, float]
        Diccionario con ROE y sus tres componentes:
        - 'ROE': Rentabilidad sobre patrimonio (%)
        - 'Margen': Margen de utilidad neta (%)
        - 'Rotacion': Rotación de activos (veces)
        - 'Apalancamiento': Multiplicador de apalancamiento (veces)
    
    Ejemplo:
    --------
    >>> resultado = calcular_dupont_3_factores(
    ...     utilidad_neta=1_000_000,
    ...     ventas=10_000_000,
    ...     activos=8_000_000,
    ...     patrimonio=4_000_000
    ... )
    >>> print(f"ROE: {resultado['ROE']:.2f}%")
    ROE: 25.00%
    """
    
    # Calcular los tres componentes
    margen_utilidad = (utilidad_neta / ventas) * 100  # En porcentaje
    rotacion_activos = ventas / activos  # En veces
    multiplicador_apalancamiento = activos / patrimonio  # En veces
    
    # Calcular ROE directamente y mediante DuPont
    roe_directo = (utilidad_neta / patrimonio) * 100  # En porcentaje
    roe_dupont = (margen_utilidad / 100) * rotacion_activos * multiplicador_apalancamiento * 100
    
    # Verificar que ambos métodos dan el mismo resultado (con tolerancia por redondeo)
    assert abs(roe_directo - roe_dupont) < 0.01, "Error en cálculo DuPont"
    
    return {
        'ROE': roe_directo,
        'Margen': margen_utilidad,
        'Rotacion': rotacion_activos,
        'Apalancamiento': multiplicador_apalancamiento
    }

# Ejemplo de uso
print("="*80)
print("EJEMPLO: Sistema DuPont de 3 Factores")
print("="*80)

# Datos de ejemplo
ejemplo = calcular_dupont_3_factores(
    utilidad_neta=1_500_000,
    ventas=12_000_000,
    activos=9_000_000,
    patrimonio=4_000_000
)

print(f"\n📊 Resultados DuPont:")
print(f"\n  ROE Total:              {ejemplo['ROE']:.2f}%")
print(f"\n  Descomposición:")
print(f"  • Margen de Utilidad:   {ejemplo['Margen']:.2f}%")
print(f"  • Rotación de Activos:  {ejemplo['Rotacion']:.2f}x")
print(f"  • Apalancamiento:       {ejemplo['Apalancamiento']:.2f}x")
print(f"\n  Verificación: {ejemplo['Margen']:.2f}% × {ejemplo['Rotacion']:.2f} × {ejemplo['Apalancamiento']:.2f} = {ejemplo['ROE']:.2f}%")
print("="*80)

# COMMAND ----------

# DBTITLE 1,Explicación - Sistema DuPont 5 Factores
# MAGIC %md
# MAGIC ## 🔬 Sistema DuPont de 5 Factores (Extendido)
# MAGIC
# MAGIC ### ¿Por qué extender el DuPont?
# MAGIC
# MAGIC El **DuPont de 5 factores** descompone aún más los componentes para obtener mayor detalle sobre las fuentes de rentabilidad. Separa el margen de utilidad en dos elementos y el apalancamiento en su estructura financiera completa.
# MAGIC
# MAGIC ### Fórmula DuPont de 5 Factores
# MAGIC
# MAGIC $$
# MAGIC \text{ROE} = \underbrace{\frac{\text{EBIT}}{\text{Ventas}}}_{\text{Margen EBIT}} \times \underbrace{\frac{\text{Ventas}}{\text{Activos}}}_{\text{Rotación}} \times \underbrace{\frac{\text{Activos}}{\text{Patrimonio}}}_{\text{Apalancamiento}} \times \underbrace{\frac{\text{Utilidad Neta}}{\text{EBIT}}}_{\text{Carga Fiscal}} \times \underbrace{\frac{\text{EBIT}}{\text{EBT}}}_{\text{Carga Intereses}}
# MAGIC $$
# MAGIC
# MAGIC Donde:
# MAGIC * **EBIT**: Earnings Before Interest and Taxes (Resultado Operativo)
# MAGIC * **EBT**: Earnings Before Taxes (Resultado antes de impuestos)
# MAGIC
# MAGIC ### Interpretación de los 5 Componentes
# MAGIC
# MAGIC 1. **Margen EBIT** (Eficiencia operativa pura)
# MAGIC    * Rentabilidad de la operación antes de intereses e impuestos
# MAGIC    * Mide la eficiencia del negocio sin efectos financieros ni fiscales
# MAGIC
# MAGIC 2. **Rotación de Activos** (Eficiencia en uso de recursos)
# MAGIC    * Igual que en DuPont de 3 factores
# MAGIC
# MAGIC 3. **Multiplicador de Apalancamiento** (Estructura de capital)
# MAGIC    * Igual que en DuPont de 3 factores
# MAGIC
# MAGIC 4. **Carga Fiscal** (Efecto impuestos)
# MAGIC    * Proporción de EBIT que queda después de impuestos
# MAGIC    * Cuanto más cercano a 1, menor carga fiscal
# MAGIC
# MAGIC 5. **Carga de Intereses** (Efecto deuda)
# MAGIC    * Proporción de EBIT que queda después de pagar intereses
# MAGIC    * Cuanto más cercano a 1, menor carga financiera
# MAGIC
# MAGIC ### Ventajas del DuPont de 5 Factores
# MAGIC
# MAGIC ✅ **Separa efectos operativos de financieros**: Permite ver si la rentabilidad viene del negocio o de la estructura de capital  
# MAGIC ✅ **Identifica impacto fiscal**: Útil para comparar empresas en diferentes jurisdicciones  
# MAGIC ✅ **Diagnóstico más preciso**: Identifica exactamente dónde están las fortalezas/debilidades

# COMMAND ----------

# DBTITLE 1,Código - Función DuPont 5 Factores
def calcular_dupont_5_factores(ebit: float,
                                ventas: float,
                                activos: float,
                                patrimonio: float,
                                utilidad_neta: float,
                                intereses: float,
                                impuestos: float) -> Dict[str, float]:
    """
    Calcula el Sistema DuPont de 5 factores (extendido).
    
    Descompone el ROE en cinco componentes multiplicativos:
    ROE = Margen EBIT × Rotación × Apalancamiento × Carga Fiscal × Carga Intereses
    
    Parámetros:
    -----------
    ebit : float
        Earnings Before Interest and Taxes - Resultado operativo
    ventas : float
        Ingresos por ventas del período
    activos : float
        Total de activos
    patrimonio : float
        Total de patrimonio neto
    utilidad_neta : float
        Utilidad neta del período
    intereses : float
        Gastos financieros por intereses
    impuestos : float
        Impuesto a las ganancias
    
    Retorna:
    --------
    Dict[str, float]
        Diccionario con ROE y sus cinco componentes
    """
    
    # Cálculo de componentes intermedios
    ebt = ebit - intereses  # Earnings Before Taxes
    
    # Los cinco componentes del DuPont extendido
    margen_ebit = (ebit / ventas) * 100  # En porcentaje
    rotacion_activos = ventas / activos  # En veces
    multiplicador_apalancamiento = activos / patrimonio  # En veces
    carga_fiscal = utilidad_neta / ebit if ebit != 0 else 0  # Proporción
    carga_intereses = ebit / ebt if ebt != 0 else 0  # Proporción
    
    # Calcular ROE
    roe_directo = (utilidad_neta / patrimonio) * 100
    
    return {
        'ROE': roe_directo,
        'Margen_EBIT': margen_ebit,
        'Rotacion': rotacion_activos,
        'Apalancamiento': multiplicador_apalancamiento,
        'Carga_Fiscal': carga_fiscal,
        'Carga_Intereses': carga_intereses,
        'EBIT': ebit,
        'EBT': ebt
    }

# Ejemplo de uso comparativo: 3 factores vs 5 factores
print("="*80)
print("COMPARACIÓN: DuPont 3 Factores vs 5 Factores")
print("="*80)

# Datos de ejemplo
ventas_ej = 20_000_000
ebit_ej = 3_000_000
intereses_ej = 400_000
impuestos_ej = 780_000
utilidad_neta_ej = 1_820_000
activos_ej = 15_000_000
patrimonio_ej = 8_000_000

# DuPont 3 factores
resultado_3f = calcular_dupont_3_factores(
    utilidad_neta=utilidad_neta_ej,
    ventas=ventas_ej,
    activos=activos_ej,
    patrimonio=patrimonio_ej
)

# DuPont 5 factores
resultado_5f = calcular_dupont_5_factores(
    ebit=ebit_ej,
    ventas=ventas_ej,
    activos=activos_ej,
    patrimonio=patrimonio_ej,
    utilidad_neta=utilidad_neta_ej,
    intereses=intereses_ej,
    impuestos=impuestos_ej
)

print(f"\n📋 Estado de Resultados Simplificado:")
print(f"  Ventas:           ${ventas_ej:,.0f}")
print(f"  EBIT:             ${ebit_ej:,.0f}")
print(f"  Intereses:       -${intereses_ej:,.0f}")
print(f"  EBT:              ${resultado_5f['EBT']:,.0f}")
print(f"  Impuestos:       -${impuestos_ej:,.0f}")
print(f"  Utilidad Neta:    ${utilidad_neta_ej:,.0f}")

print(f"\n📊 DuPont 3 Factores:")
print(f"  ROE:          {resultado_3f['ROE']:.2f}%")
print(f"  Margen:       {resultado_3f['Margen']:.2f}%")
print(f"  Rotación:     {resultado_3f['Rotacion']:.2f}x")
print(f"  Apalancam.:   {resultado_3f['Apalancamiento']:.2f}x")

print(f"\n🔬 DuPont 5 Factores:")
print(f"  ROE:              {resultado_5f['ROE']:.2f}%")
print(f"  Margen EBIT:      {resultado_5f['Margen_EBIT']:.2f}%")
print(f"  Rotación:         {resultado_5f['Rotacion']:.2f}x")
print(f"  Apalancamiento:   {resultado_5f['Apalancamiento']:.2f}x")
print(f"  Carga Fiscal:     {resultado_5f['Carga_Fiscal']:.2f} ({(resultado_5f['Carga_Fiscal']*100):.1f}% del EBIT)")
print(f"  Carga Intereses:  {resultado_5f['Carga_Intereses']:.2f} ({(resultado_5f['Carga_Intereses']*100):.1f}% del EBIT)")

print(f"\n👁️ Observaciones:")
tasa_impositiva = (impuestos_ej / resultado_5f['EBT']) * 100
print(f"  • Tasa impositiva efectiva: {tasa_impositiva:.1f}%")
print(f"  • Impacto de intereses: reducen ganancia en {(intereses_ej/ebit_ej)*100:.1f}%")
print(f"  • El margen EBIT ({resultado_5f['Margen_EBIT']:.1f}%) es mayor que el margen neto ({resultado_3f['Margen']:.1f}%)")
print("="*80)

# COMMAND ----------

# DBTITLE 1,Explicación - Aplicación con Datos Argentinos
# MAGIC %md
# MAGIC ## 🇦🇷 Aplicación: Análisis DuPont de Empresas Argentinas
# MAGIC
# MAGIC ### ¿Qué vamos a hacer?
# MAGIC
# MAGIC Aplicaremos el **Sistema DuPont** a datos reales de empresas argentinas para:
# MAGIC
# MAGIC 1. ✅ Comparar la rentabilidad de diferentes sectores
# MAGIC 2. ✅ Identificar cuáles son las fuentes de ROE en cada empresa
# MAGIC 3. ✅ Visualizar las diferencias en estrategias empresariales
# MAGIC 4. ✅ Extraer conclusiones prácticas para análisis financiero
# MAGIC
# MAGIC ### Empresas a Analizar
# MAGIC
# MAGIC Usaremos datos de cuatro empresas argentinas con estados contables publicados:
# MAGIC
# MAGIC 1. **BYMA (Bolsas y Mercados Argentinos)**
# MAGIC    * Sector: Infraestructura financiera
# MAGIC    * Negocio: Operación de mercados de valores
# MAGIC    * Características: Altos márgenes, baja rotación de activos
# MAGIC
# MAGIC 2. **Caja de Valores**
# MAGIC    * Sector: Infraestructura financiera
# MAGIC    * Negocio: Custodia y liquidación de valores
# MAGIC    * Características: Modelo de negocio estable, bajos riesgos
# MAGIC
# MAGIC 3. **Grupo Clarín**
# MAGIC    * Sector: Medios de comunicación
# MAGIC    * Negocio: Multimedios (TV, radio, impresos, digital)
# MAGIC    * Características: Alta inversión en activos, márgenes variables
# MAGIC
# MAGIC 4. **Correo Argentino**
# MAGIC    * Sector: Servicios postales
# MAGIC    * Negocio: Logística y correo
# MAGIC    * Características: Alta rotación, márgenes ajustados
# MAGIC
# MAGIC ### ¿Por qué es interesante?
# MAGIC
# MAGIC 🔍 Cada sector tiene un **perfil de rentabilidad diferente**:  
# MAGIC * **Servicios financieros**: Altos márgenes, baja rotación  
# MAGIC * **Medios**: Márgenes medios, inversión alta en activos  
# MAGIC * **Logística**: Bajos márgenes, alta rotación
# MAGIC
# MAGIC El **Sistema DuPont** nos permite ver estas diferencias estructurales claramente.

# COMMAND ----------

# DBTITLE 1,Código - Análisis DuPont Empresas Argentinas
# Datos simplificados de empresas argentinas (en millones de pesos)
# Fuente: Estados contables públicos (valores aproximados para fines educativos)

empresas_arg = {
    'BYMA': {
        'Ventas': 8_500,
        'Utilidad_Neta': 3_200,
        'Activos': 12_000,
        'Patrimonio': 9_500,
        'EBIT': 4_100,
        'Intereses': 150,
        'Impuestos': 750,
        'Sector': 'Infraestructura Financiera'
    },
    'Caja de Valores': {
        'Ventas': 2_800,
        'Utilidad_Neta': 950,
        'Activos': 4_200,
        'Patrimonio': 3_500,
        'EBIT': 1_250,
        'Intereses': 80,
        'Impuestos': 220,
        'Sector': 'Infraestructura Financiera'
    },
    'Grupo Clarín': {
        'Ventas': 35_000,
        'Utilidad_Neta': 2_100,
        'Activos': 45_000,
        'Patrimonio': 18_000,
        'EBIT': 3_500,
        'Intereses': 800,
        'Impuestos': 600,
        'Sector': 'Medios de Comunicación'
    },
    'Correo Argentino': {
        'Ventas': 18_000,
        'Utilidad_Neta': 800,
        'Activos': 12_000,
        'Patrimonio': 6_000,
        'EBIT': 1_400,
        'Intereses': 320,
        'Impuestos': 280,
        'Sector': 'Servicios Postales'
    }
}

# Calcular DuPont 3 factores para todas las empresas
print("="*100)
print(" "*30 + "ANÁLISIS DUPONT - EMPRESAS ARGENTINAS")
print("="*100)

resultados_dupont = {}

for empresa, datos in empresas_arg.items():
    resultado = calcular_dupont_3_factores(
        utilidad_neta=datos['Utilidad_Neta'],
        ventas=datos['Ventas'],
        activos=datos['Activos'],
        patrimonio=datos['Patrimonio']
    )
    resultados_dupont[empresa] = resultado
    
    print(f"\n🏢 {empresa} ({datos['Sector']})")
    print("-" * 100)
    print(f"  Ventas:       ${datos['Ventas']:>8,.0f}M  |  Activos: ${datos['Activos']:>8,.0f}M  |  Patrimonio: ${datos['Patrimonio']:>8,.0f}M")
    print(f"  Util. Neta:   ${datos['Utilidad_Neta']:>8,.0f}M")
    print(f"\n  📊 DuPont 3 Factores:")
    print(f"     ROE:               {resultado['ROE']:>6.2f}%")
    print(f"     Margen Neto:       {resultado['Margen']:>6.2f}%")
    print(f"     Rotación Activos:  {resultado['Rotacion']:>6.2f}x")
    print(f"     Apalancamiento:    {resultado['Apalancamiento']:>6.2f}x")
    print(f"\n  👁️ Interpretación:")
    
    # Interpretación automática
    if resultado['Margen'] > 20:
        print(f"     • Alto margen ({resultado['Margen']:.1f}%): negocio muy rentable por unidad vendida")
    elif resultado['Margen'] > 10:
        print(f"     • Margen medio ({resultado['Margen']:.1f}%): rentabilidad operativa saludable")
    else:
        print(f"     • Margen bajo ({resultado['Margen']:.1f}%): competencia en precios o altos costos")
    
    if resultado['Rotacion'] > 2:
        print(f"     • Alta rotación ({resultado['Rotacion']:.2f}x): uso eficiente de activos")
    elif resultado['Rotacion'] > 1:
        print(f"     • Rotación media ({resultado['Rotacion']:.2f}x): activos generan ventas moderadas")
    else:
        print(f"     • Baja rotación ({resultado['Rotacion']:.2f}x): negocio intensivo en activos")
    
    if resultado['Apalancamiento'] > 2.5:
        print(f"     • Alto apalancamiento ({resultado['Apalancamiento']:.2f}x): estructura con deuda significativa")
    elif resultado['Apalancamiento'] > 1.5:
        print(f"     • Apalancamiento medio ({resultado['Apalancamiento']:.2f}x): balance entre deuda y patrimonio")
    else:
        print(f"     • Bajo apalancamiento ({resultado['Apalancamiento']:.2f}x): empresa financiada principalmente con patrimonio")

print("\n" + "="*100)

# COMMAND ----------

# DBTITLE 1,Explicación - Visualización Comparativa
# MAGIC %md
# MAGIC ## 📊 Visualización Comparativa del Análisis DuPont
# MAGIC
# MAGIC ### ¿Qué vamos a hacer?
# MAGIC
# MAGIC Crearemos **gráficos comparativos** que muestren:
# MAGIC
# MAGIC 1. ✅ **Gráfico de barras agrupadas**: Comparar los 3 componentes del DuPont entre empresas
# MAGIC 2. ✅ **Gráfico radial (spider)**: Visualizar el perfil de cada empresa en múltiples dimensiones
# MAGIC 3. ✅ **Heatmap**: Ver rápidamente qué empresa destaca en cada componente
# MAGIC
# MAGIC ### ¿Por qué es útil?
# MAGIC
# MAGIC 👁️ Las visualizaciones permiten:
# MAGIC * Identificar rápidamente patrones y diferencias entre empresas
# MAGIC * Comparar modelos de negocio visualmente
# MAGIC * Comunicar hallazgos de forma efectiva a stakeholders
# MAGIC * Detectar outliers o empresas con perfiles únicos

# COMMAND ----------

# DBTITLE 1,Código - Visualización DuPont
# Crear DataFrame para visualizaciones
df_dupont = pd.DataFrame(resultados_dupont).T
df_dupont['Empresa'] = df_dupont.index
df_dupont = df_dupont[['Empresa', 'ROE', 'Margen', 'Rotacion', 'Apalancamiento']]

print("\n📊 DataFrame con resultados DuPont:")
display(df_dupont.style.format({
    'ROE': '{:.2f}%',
    'Margen': '{:.2f}%',
    'Rotacion': '{:.2f}x',
    'Apalancamiento': '{:.2f}x'
}).background_gradient(subset=['ROE', 'Margen', 'Rotacion', 'Apalancamiento'], cmap='RdYlGn', vmin=0))

# Gráfico 1: Barras agrupadas comparando componentes
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Análisis DuPont Comparativo - Empresas Argentinas', fontsize=18, fontweight='bold', color=COLOR_UDA_AZUL)

# Subplot 1: ROE total
ax1 = axes[0, 0]
colores_roe = [COLOR_UDA_AZUL if x == df_dupont['ROE'].max() else COLOR_UDA_CELESTE for x in df_dupont['ROE']]
ax1.bar(df_dupont['Empresa'], df_dupont['ROE'], color=colores_roe, alpha=0.8, edgecolor='black')
ax1.set_title('ROE Total (%)', fontsize=14, fontweight='bold')
ax1.set_ylabel('ROE (%)', fontsize=12)
ax1.set_xlabel('Empresa', fontsize=12)
ax1.grid(axis='y', alpha=0.3)
for i, v in enumerate(df_dupont['ROE']):
    ax1.text(i, v + 0.5, f'{v:.1f}%', ha='center', va='bottom', fontweight='bold')

# Subplot 2: Margen de utilidad
ax2 = axes[0, 1]
colores_margen = [COLOR_UDA_AZUL if x == df_dupont['Margen'].max() else '#28a745' for x in df_dupont['Margen']]
ax2.bar(df_dupont['Empresa'], df_dupont['Margen'], color=colores_margen, alpha=0.8, edgecolor='black')
ax2.set_title('Margen de Utilidad Neta (%)', fontsize=14, fontweight='bold')
ax2.set_ylabel('Margen (%)', fontsize=12)
ax2.set_xlabel('Empresa', fontsize=12)
ax2.grid(axis='y', alpha=0.3)
for i, v in enumerate(df_dupont['Margen']):
    ax2.text(i, v + 0.5, f'{v:.1f}%', ha='center', va='bottom', fontweight='bold')

# Subplot 3: Rotación de activos
ax3 = axes[1, 0]
colores_rot = [COLOR_UDA_AZUL if x == df_dupont['Rotacion'].max() else '#ffc107' for x in df_dupont['Rotacion']]
ax3.bar(df_dupont['Empresa'], df_dupont['Rotacion'], color=colores_rot, alpha=0.8, edgecolor='black')
ax3.set_title('Rotación de Activos (veces)', fontsize=14, fontweight='bold')
ax3.set_ylabel('Rotación (x)', fontsize=12)
ax3.set_xlabel('Empresa', fontsize=12)
ax3.grid(axis='y', alpha=0.3)
for i, v in enumerate(df_dupont['Rotacion']):
    ax3.text(i, v + 0.05, f'{v:.2f}x', ha='center', va='bottom', fontweight='bold')

# Subplot 4: Apalancamiento
ax4 = axes[1, 1]
colores_apal = [COLOR_UDA_AZUL if x == df_dupont['Apalancamiento'].max() else '#dc3545' for x in df_dupont['Apalancamiento']]
ax4.bar(df_dupont['Empresa'], df_dupont['Apalancamiento'], color=colores_apal, alpha=0.8, edgecolor='black')
ax4.set_title('Multiplicador de Apalancamiento (veces)', fontsize=14, fontweight='bold')
ax4.set_ylabel('Apalancamiento (x)', fontsize=12)
ax4.set_xlabel('Empresa', fontsize=12)
ax4.grid(axis='y', alpha=0.3)
for i, v in enumerate(df_dupont['Apalancamiento']):
    ax4.text(i, v + 0.03, f'{v:.2f}x', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

print("\n🔍 Observaciones Clave:")
print("="*80)
print(f"  • Mayor ROE:        {df_dupont.loc[df_dupont['ROE'].idxmax(), 'Empresa']} ({df_dupont['ROE'].max():.1f}%)")
print(f"  • Mayor Margen:     {df_dupont.loc[df_dupont['Margen'].idxmax(), 'Empresa']} ({df_dupont['Margen'].max():.1f}%)")
print(f"  • Mayor Rotación:   {df_dupont.loc[df_dupont['Rotacion'].idxmax(), 'Empresa']} ({df_dupont['Rotacion'].max():.2f}x)")
print(f"  • Mayor Apalancam.: {df_dupont.loc[df_dupont['Apalancamiento'].idxmax(), 'Empresa']} ({df_dupont['Apalancamiento'].max():.2f}x)")
print("="*80)

# COMMAND ----------

# DBTITLE 1,Explicación - Apalancamiento Operativo
# MAGIC %md
# MAGIC ## 🏭 PARTE 2: Apalancamiento Operativo (DOL)
# MAGIC
# MAGIC ### ¿Qué es el Apalancamiento Operativo?
# MAGIC
# MAGIC El **Apalancamiento Operativo** mide cómo los **costos fijos** magnifican el impacto de los cambios en ventas sobre el resultado operativo (EBIT).
# MAGIC
# MAGIC ### Concepto Clave: Costos Fijos vs Variables
# MAGIC
# MAGIC 💵 **Costos Fijos**:
# MAGIC * No dependen del volumen de producción/ventas
# MAGIC * Ejemplos: Alquileres, salarios administrativos, depreciación, seguros
# MAGIC * Deben pagarse incluso si las ventas son cero
# MAGIC * **A mayor proporción de costos fijos, mayor apalancamiento operativo**
# MAGIC
# MAGIC 💰 **Costos Variables**:
# MAGIC * Dependen directamente del volumen producido/vendido
# MAGIC * Ejemplos: Materias primas, comisiones de venta, energía de producción
# MAGIC * Si no hay ventas, estos costos son cero
# MAGIC
# MAGIC ### Fórmula del DOL (Degree of Operating Leverage)
# MAGIC
# MAGIC $$
# MAGIC \text{DOL} = \frac{\% \Delta \text{ EBIT}}{\% \Delta \text{ Ventas}} = \frac{Q \times (P - CV)}{Q \times (P - CV) - CF} = \frac{\text{Margen de Contribución}}{\text{EBIT}}
# MAGIC $$
# MAGIC
# MAGIC Donde:
# MAGIC * **Q**: Cantidad vendida
# MAGIC * **P**: Precio unitario
# MAGIC * **CV**: Costo variable unitario
# MAGIC * **CF**: Costos fijos totales
# MAGIC * **Margen de Contribución**: Ventas - Costos Variables
# MAGIC
# MAGIC ### Interpretación del DOL
# MAGIC
# MAGIC 📈 **DOL = 2.5**:  
# MAGIC Si las ventas aumentan 10%, el EBIT aumentará 2.5 × 10% = **25%**
# MAGIC
# MAGIC 📉 **DOL alto (≥3.0)**:
# MAGIC * **Ventaja**: Grandes ganancias cuando las ventas suben
# MAGIC * **Riesgo**: Grandes pérdidas cuando las ventas bajan
# MAGIC * **Sectores**: Aerolíneas, hotelería, manufactura pesada
# MAGIC
# MAGIC 📊 **DOL bajo (≤1.5)**:
# MAGIC * **Ventaja**: Estabilidad, menor riesgo operativo
# MAGIC * **Desventaja**: Menor potencial de crecimiento rápido
# MAGIC * **Sectores**: Comercio minorista, servicios profesionales
# MAGIC
# MAGIC ### Ejemplo Numérico
# MAGIC
# MAGIC **Empresa con alto apalancamiento operativo**:
# MAGIC * Ventas: $1,000,000 (10,000 unidades × $100)
# MAGIC * Costos variables: $400,000 (40% de ventas)
# MAGIC * Costos fijos: $500,000
# MAGIC * EBIT: $100,000
# MAGIC * **DOL** = ($1,000,000 - $400,000) / $100,000 = **6.0**
# MAGIC
# MAGIC Si las ventas aumentan 10%:
# MAGIC * Nuevas ventas: $1,100,000
# MAGIC * Nuevos costos variables: $440,000 (40% de $1,100,000)
# MAGIC * Costos fijos: $500,000 (sin cambio)
# MAGIC * Nuevo EBIT: $160,000
# MAGIC * **Aumento EBIT**: 60% = 6.0 × 10% ✅

# COMMAND ----------

# DBTITLE 1,Código - Función DOL
def calcular_dol(ventas: float,
                 costos_variables: float,
                 costos_fijos: float,
                 ebit: float = None) -> Dict[str, float]:
    """
    Calcula el Grado de Apalancamiento Operativo (DOL).
    
    DOL = Margen de Contribución / EBIT
    
    Parámetros:
    -----------
    ventas : float
        Ingresos totales por ventas
    costos_variables : float
        Costos que varían con el volumen de ventas
    costos_fijos : float
        Costos que no varían con el volumen de ventas
    ebit : float, opcional
        EBIT (Earnings Before Interest and Taxes). Si no se provee, se calcula.
    
    Retorna:
    --------
    Dict[str, float]
        Diccionario con DOL y componentes
    """
    
    margen_contribucion = ventas - costos_variables
    
    if ebit is None:
        ebit = margen_contribucion - costos_fijos
    
    # Evitar división por cero
    if ebit == 0:
        dol = float('inf')  # DOL indefinido en punto de equilibrio
    else:
        dol = margen_contribucion / ebit
    
    # Calcular porcentaje de costos fijos sobre margen de contribución
    prop_cf = (costos_fijos / margen_contribucion) * 100 if margen_contribucion > 0 else 0
    
    return {
        'DOL': dol,
        'Margen_Contribucion': margen_contribucion,
        'EBIT': ebit,
        'Costos_Fijos': costos_fijos,
        'Prop_CF': prop_cf,
        'Margen_Contribucion_Pct': (margen_contribucion / ventas) * 100 if ventas > 0 else 0
    }

def simular_cambio_ventas(ventas_base: float,
                          costos_variables_pct: float,
                          costos_fijos: float,
                          cambio_ventas_pct: float) -> Dict[str, float]:
    """
    Simula el impacto de un cambio en ventas sobre el EBIT usando DOL.
    
    Parámetros:
    -----------
    ventas_base : float
        Ventas actuales
    costos_variables_pct : float
        Costos variables como % de ventas (ej: 40 para 40%)
    costos_fijos : float
        Costos fijos totales
    cambio_ventas_pct : float
        Cambio % en ventas (ej: 10 para +10%, -10 para -10%)
    
    Retorna:
    --------
    Dict con escenario base y nuevo
    """
    
    # Escenario base
    cv_base = ventas_base * (costos_variables_pct / 100)
    resultado_base = calcular_dol(ventas_base, cv_base, costos_fijos)
    
    # Escenario nuevo
    ventas_nuevas = ventas_base * (1 + cambio_ventas_pct / 100)
    cv_nuevas = ventas_nuevas * (costos_variables_pct / 100)
    resultado_nuevo = calcular_dol(ventas_nuevas, cv_nuevas, costos_fijos)
    
    # Cambios porcentuales
    cambio_ebit_pct = ((resultado_nuevo['EBIT'] - resultado_base['EBIT']) / resultado_base['EBIT']) * 100 if resultado_base['EBIT'] != 0 else 0
    
    return {
        'Base': resultado_base,
        'Nuevo': resultado_nuevo,
        'Cambio_Ventas_Pct': cambio_ventas_pct,
        'Cambio_EBIT_Pct': cambio_ebit_pct,
        'DOL_Verificado': cambio_ebit_pct / cambio_ventas_pct if cambio_ventas_pct != 0 else 0
    }

# Ejemplo 1: Empresa con ALTO apalancamiento operativo (muchos costos fijos)
print("="*80)
print("EJEMPLO 1: Empresa con ALTO Apalancamiento Operativo")
print("="*80)

resultado_alto_dol = calcular_dol(
    ventas=1_000_000,
    costos_variables=400_000,  # 40% de ventas
    costos_fijos=500_000
)

print(f"\n🏭 Estructura de Costos:")
print(f"  Ventas:                  ${1_000_000:>10,.0f}")
print(f"  Costos Variables (40%):  ${400_000:>10,.0f}")
print(f"  Margen de Contribución:  ${resultado_alto_dol['Margen_Contribucion']:>10,.0f} ({resultado_alto_dol['Margen_Contribucion_Pct']:.1f}%)")
print(f"  Costos Fijos:           -${resultado_alto_dol['Costos_Fijos']:>10,.0f}")
print(f"  EBIT:                    ${resultado_alto_dol['EBIT']:>10,.0f}")
print(f"\n  📊 DOL: {resultado_alto_dol['DOL']:.2f}")
print(f"  👁️ Interpretación: Por cada 1% de cambio en ventas, el EBIT cambia {resultado_alto_dol['DOL']:.2f}%")

# Simulación de cambio en ventas
print(f"\n📈 Simulación: ¿Qué pasa si las ventas suben 15%?")
simulacion = simular_cambio_ventas(1_000_000, 40, 500_000, 15)
print(f"  Ventas nuevas:   ${simulacion['Nuevo']['Margen_Contribucion'] + simulacion['Nuevo']['Costos_Fijos']:,.0f}")
print(f"  EBIT nuevo:      ${simulacion['Nuevo']['EBIT']:,.0f}")
print(f"  Cambio EBIT:     {simulacion['Cambio_EBIT_Pct']:+.1f}%")
print(f"  DOL verificado:  {simulacion['DOL_Verificado']:.2f} (debe ser ~{resultado_alto_dol['DOL']:.2f})")

print("\n" + "="*80)

# Ejemplo 2: Empresa con BAJO apalancamiento operativo (pocos costos fijos)
print("\nEJEMPLO 2: Empresa con BAJO Apalancamiento Operativo")
print("="*80)

resultado_bajo_dol = calcular_dol(
    ventas=1_000_000,
    costos_variables=800_000,  # 80% de ventas
    costos_fijos=100_000
)

print(f"\n🏭 Estructura de Costos:")
print(f"  Ventas:                  ${1_000_000:>10,.0f}")
print(f"  Costos Variables (80%):  ${800_000:>10,.0f}")
print(f"  Margen de Contribución:  ${resultado_bajo_dol['Margen_Contribucion']:>10,.0f} ({resultado_bajo_dol['Margen_Contribucion_Pct']:.1f}%)")
print(f"  Costos Fijos:           -${resultado_bajo_dol['Costos_Fijos']:>10,.0f}")
print(f"  EBIT:                    ${resultado_bajo_dol['EBIT']:>10,.0f}")
print(f"\n  📊 DOL: {resultado_bajo_dol['DOL']:.2f}")
print(f"  👁️ Interpretación: Menor apalancamiento operativo = menor riesgo pero menor potencial")
print("="*80)

# COMMAND ----------

# DBTITLE 1,Explicación - Punto de Equilibrio
# MAGIC %md
# MAGIC ## ⚖️ Punto de Equilibrio Operativo
# MAGIC
# MAGIC ### ¿Qué es el Punto de Equilibrio?
# MAGIC
# MAGIC El **Punto de Equilibrio** (Break-Even Point) es el nivel de ventas donde:
# MAGIC * Los ingresos totales = Costos totales
# MAGIC * El EBIT = $0
# MAGIC * La empresa no gana ni pierde
# MAGIC
# MAGIC ### Fórmulas del Punto de Equilibrio
# MAGIC
# MAGIC **En unidades**:
# MAGIC $$
# MAGIC Q_{equilibrio} = \frac{\text{Costos Fijos}}{\text{Precio} - \text{Costo Variable Unitario}} = \frac{CF}{P - CVu}
# MAGIC $$
# MAGIC
# MAGIC **En pesos (ventas)**:
# MAGIC $$
# MAGIC \text{Ventas}_{equilibrio} = \frac{\text{Costos Fijos}}{1 - \frac{\text{Costos Variables}}{\text{Ventas}}} = \frac{CF}{\text{Margen Contribución \%}}
# MAGIC $$
# MAGIC
# MAGIC ### ¿Por qué es importante?
# MAGIC
# MAGIC ✅ **Planificación**: Saber cuánto hay que vender para no perder  
# MAGIC ✅ **Análisis de riesgo**: Empresas lejos del punto de equilibrio son más seguras  
# MAGIC ✅ **Toma de decisiones**: Evaluar nuevos proyectos o productos  
# MAGIC ✅ **Negociación de precios**: Entender el impacto de cambios en precios
# MAGIC
# MAGIC ### Margen de Seguridad
# MAGIC
# MAGIC El **Margen de Seguridad** indica cuánto pueden caer las ventas antes de llegar al punto de equilibrio:
# MAGIC
# MAGIC $$
# MAGIC \text{Margen de Seguridad} = \frac{\text{Ventas Actuales} - \text{Ventas Equilibrio}}{\text{Ventas Actuales}} \times 100\%
# MAGIC $$
# MAGIC
# MAGIC **Ejemplo**: Si ventas actuales son $1,000,000 y punto de equilibrio es $600,000:  
# MAGIC Margen de Seguridad = (1,000,000 - 600,000) / 1,000,000 = **40%**
# MAGIC
# MAGIC 👉 Las ventas pueden caer hasta 40% antes de que la empresa tenga pérdidas.

# COMMAND ----------

# DBTITLE 1,Código - Punto de Equilibrio
def calcular_punto_equilibrio(costos_fijos: float,
                               precio_unitario: float = None,
                               costo_variable_unitario: float = None,
                               margen_contribucion_pct: float = None) -> Dict[str, float]:
    """
    Calcula el punto de equilibrio operativo.
    
    Se puede calcular de dos formas:
    1. Con datos unitarios: precio y costo variable unitario
    2. Con margen de contribución porcentual
    
    Parámetros:
    -----------
    costos_fijos : float
        Costos fijos totales
    precio_unitario : float, opcional
        Precio de venta por unidad
    costo_variable_unitario : float, opcional
        Costo variable por unidad
    margen_contribucion_pct : float, opcional
        Margen de contribución como % (ej: 60 para 60%)
    
    Retorna:
    --------
    Dict con punto de equilibrio en unidades y pesos
    """
    
    if precio_unitario and costo_variable_unitario:
        # Método 1: Con datos unitarios
        margen_contrib_unitario = precio_unitario - costo_variable_unitario
        q_equilibrio = costos_fijos / margen_contrib_unitario
        ventas_equilibrio = q_equilibrio * precio_unitario
        mc_pct = (margen_contrib_unitario / precio_unitario) * 100
    
    elif margen_contribucion_pct:
        # Método 2: Con margen de contribución porcentual
        ventas_equilibrio = costos_fijos / (margen_contribucion_pct / 100)
        q_equilibrio = None  # No se puede calcular sin precio unitario
        mc_pct = margen_contribucion_pct
    
    else:
        raise ValueError("Debe proveer (precio_unitario y costo_variable_unitario) O margen_contribucion_pct")
    
    return {
        'Q_Equilibrio': q_equilibrio,
        'Ventas_Equilibrio': ventas_equilibrio,
        'Costos_Fijos': costos_fijos,
        'Margen_Contribucion_Pct': mc_pct
    }

def calcular_margen_seguridad(ventas_actuales: float,
                              ventas_equilibrio: float) -> Dict[str, float]:
    """
    Calcula el margen de seguridad.
    
    Indica cuánto pueden caer las ventas antes de llegar al punto de equilibrio.
    
    Parámetros:
    -----------
    ventas_actuales : float
        Nivel actual de ventas
    ventas_equilibrio : float
        Punto de equilibrio en ventas
    
    Retorna:
    --------
    Dict con margen de seguridad en pesos y porcentaje
    """
    
    margen_pesos = ventas_actuales - ventas_equilibrio
    margen_pct = (margen_pesos / ventas_actuales) * 100 if ventas_actuales > 0 else 0
    
    return {
        'Margen_Seguridad_Pesos': margen_pesos,
        'Margen_Seguridad_Pct': margen_pct,
        'Distancia_Equilibrio': 100 - margen_pct
    }

# Ejemplo: Cálculo de punto de equilibrio
print("="*80)
print("ANÁLISIS DE PUNTO DE EQUILIBRIO")
print("="*80)

# Datos de ejemplo
precio = 100
costo_var_unit = 60
costos_fijos_ej = 200_000
ventas_actuales_ej = 800_000

# Calcular punto de equilibrio
equilibrio = calcular_punto_equilibrio(
    costos_fijos=costos_fijos_ej,
    precio_unitario=precio,
    costo_variable_unitario=costo_var_unit
)

print(f"\n🏭 Datos del Negocio:")
print(f"  Precio unitario:           ${precio:>8,.2f}")
print(f"  Costo variable unitario:   ${costo_var_unit:>8,.2f}")
print(f"  Margen contrib. unitario:  ${precio - costo_var_unit:>8,.2f} ({equilibrio['Margen_Contribucion_Pct']:.1f}%)")
print(f"  Costos fijos:              ${costos_fijos_ej:>8,.0f}")

print(f"\n⚖️ Punto de Equilibrio:")
print(f"  Unidades:  {equilibrio['Q_Equilibrio']:>8,.0f} unidades")
print(f"  Ventas:    ${equilibrio['Ventas_Equilibrio']:>8,.0f}")
print(f"\n  👁️ Interpretación: Hay que vender {equilibrio['Q_Equilibrio']:,.0f} unidades para no ganar ni perder")

# Calcular margen de seguridad
margen_seg = calcular_margen_seguridad(ventas_actuales_ej, equilibrio['Ventas_Equilibrio'])

print(f"\n🛡️ Margen de Seguridad (ventas actuales: ${ventas_actuales_ej:,.0f}):")
print(f"  En pesos:      ${margen_seg['Margen_Seguridad_Pesos']:>8,.0f}")
print(f"  En porcentaje:  {margen_seg['Margen_Seguridad_Pct']:>7.1f}%")
print(f"\n  👁️ Interpretación: Las ventas pueden caer hasta {margen_seg['Margen_Seguridad_Pct']:.1f}% antes de tener pérdidas")

# Visualización del punto de equilibrio
print(f"\n📊 Gráfico de Punto de Equilibrio:")

q_range = np.linspace(0, equilibrio['Q_Equilibrio'] * 2.5, 100)
ventas_linea = q_range * precio
costos_totales_linea = costos_fijos_ej + (q_range * costo_var_unit)
costos_fijos_linea = np.full_like(q_range, costos_fijos_ej)

plt.figure(figsize=(12, 7))

# Líneas
plt.plot(q_range, ventas_linea, label='Ingresos Totales', color=COLOR_UDA_AZUL, linewidth=2.5)
plt.plot(q_range, costos_totales_linea, label='Costos Totales', color='#dc3545', linewidth=2.5)
plt.plot(q_range, costos_fijos_linea, label='Costos Fijos', color='#ffc107', linestyle='--', linewidth=2)

# Punto de equilibrio
plt.scatter([equilibrio['Q_Equilibrio']], [equilibrio['Ventas_Equilibrio']], 
           color='#28a745', s=200, zorder=5, label=f"Punto de Equilibrio\n({equilibrio['Q_Equilibrio']:,.0f} unidades)")

# Línea vertical en punto de equilibrio
plt.axvline(x=equilibrio['Q_Equilibrio'], color='#28a745', linestyle=':', alpha=0.7)

# Zonas
plt.fill_between(q_range[q_range <= equilibrio['Q_Equilibrio']], 
                 ventas_linea[q_range <= equilibrio['Q_Equilibrio']], 
                 costos_totales_linea[q_range <= equilibrio['Q_Equilibrio']], 
                 alpha=0.2, color='red', label='Área de Pérdida')

plt.fill_between(q_range[q_range >= equilibrio['Q_Equilibrio']], 
                 ventas_linea[q_range >= equilibrio['Q_Equilibrio']], 
                 costos_totales_linea[q_range >= equilibrio['Q_Equilibrio']], 
                 alpha=0.2, color='green', label='Área de Ganancia')

plt.title('Análisis de Punto de Equilibrio', fontsize=16, fontweight='bold', color=COLOR_UDA_AZUL, pad=20)
plt.xlabel('Cantidad (unidades)', fontsize=12, fontweight='bold')
plt.ylabel('Pesos ($)', fontsize=12, fontweight='bold')
plt.legend(loc='upper left', fontsize=10, framealpha=0.9)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("="*80)

# COMMAND ----------

# DBTITLE 1,Explicación - Apalancamiento Financiero
# MAGIC %md
# MAGIC ## 💰 PARTE 3: Apalancamiento Financiero (DFL)
# MAGIC
# MAGIC ### ¿Qué es el Apalancamiento Financiero?
# MAGIC
# MAGIC El **Apalancamiento Financiero** mide cómo la **deuda** magnifica el impacto de los cambios en EBIT sobre la utilidad por acción (EPS) o la utilidad neta.
# MAGIC
# MAGIC ### Concepto Clave: Uso de Deuda
# MAGIC
# MAGIC 🏦 **Con deuda**:
# MAGIC * La empresa paga intereses fijos independientemente de sus resultados
# MAGIC * Si el EBIT sube, la utilidad neta sube más (por el efecto apalancamiento)
# MAGIC * Si el EBIT baja, la utilidad neta baja más (mayor riesgo)
# MAGIC * **A mayor deuda, mayor apalancamiento financiero**
# MAGIC
# MAGIC 💵 **Sin deuda (solo patrimonio)**:
# MAGIC * No hay intereses que pagar
# MAGIC * Mayor estabilidad pero menor potencial de crecimiento
# MAGIC * Menor riesgo financiero
# MAGIC
# MAGIC ### Fórmula del DFL (Degree of Financial Leverage)
# MAGIC
# MAGIC $$
# MAGIC \text{DFL} = \frac{\% \Delta \text{ EPS}}{\% \Delta \text{ EBIT}} = \frac{\text{EBIT}}{\text{EBIT} - \text{Intereses}} = \frac{\text{EBIT}}{\text{EBT}}
# MAGIC $$
# MAGIC
# MAGIC Donde:
# MAGIC * **EBIT**: Earnings Before Interest and Taxes (Resultado operativo)
# MAGIC * **EBT**: Earnings Before Taxes (EBIT - Intereses)
# MAGIC * **EPS**: Earnings Per Share (Utilidad por acción)
# MAGIC
# MAGIC ### Interpretación del DFL
# MAGIC
# MAGIC 📈 **DFL = 1.5**:  
# MAGIC Si el EBIT aumenta 10%, la utilidad neta aumentará 1.5 × 10% = **15%**
# MAGIC
# MAGIC 📊 **DFL alto (≥2.0)**:
# MAGIC * **Ventaja**: Magnifica ganancias cuando el negocio va bien
# MAGIC * **Riesgo**: Magnifica pérdidas cuando el negocio va mal
# MAGIC * **Situación**: Empresa con mucha deuda (alta carga de intereses)
# MAGIC
# MAGIC 📊 **DFL bajo (≤1.2)**:
# MAGIC * **Ventaja**: Estabilidad, menor riesgo financiero
# MAGIC * **Desventaja**: Menor potencial de crecimiento acelerado
# MAGIC * **Situación**: Empresa con poca o sin deuda
# MAGIC
# MAGIC ### Ejemplo Numérico
# MAGIC
# MAGIC **Empresa con alto apalancamiento financiero**:
# MAGIC * EBIT: $1,000,000
# MAGIC * Intereses: $600,000
# MAGIC * EBT: $400,000
# MAGIC * **DFL** = $1,000,000 / $400,000 = **2.5**
# MAGIC
# MAGIC Si el EBIT aumenta 20%:
# MAGIC * Nuevo EBIT: $1,200,000
# MAGIC * Intereses: $600,000 (sin cambio)
# MAGIC * Nuevo EBT: $600,000
# MAGIC * **Aumento EBT**: 50% = 2.5 × 20% ✅
# MAGIC
# MAGIC ### DFL vs DOL
# MAGIC
# MAGIC | Concepto | DOL (Operativo) | DFL (Financiero) |
# MAGIC |----------|-----------------|------------------|
# MAGIC | **Origen** | Costos fijos operativos | Costos fijos financieros (intereses) |
# MAGIC | **Impacto** | Ventas → EBIT | EBIT → Utilidad Neta |
# MAGIC | **Decisión** | Estrategia operativa | Estructura de capital |
# MAGIC | **Control** | Gerencia operativa | Gerencia financiera |

# COMMAND ----------

# DBTITLE 1,Código - Función DFL
def calcular_dfl(ebit: float,
                 intereses: float) -> Dict[str, float]:
    """
    Calcula el Grado de Apalancamiento Financiero (DFL).
    
    DFL = EBIT / (EBIT - Intereses) = EBIT / EBT
    
    Parámetros:
    -----------
    ebit : float
        Earnings Before Interest and Taxes (Resultado operativo)
    intereses : float
        Gastos financieros por intereses
    
    Retorna:
    --------
    Dict[str, float]
        Diccionario con DFL y componentes
    """
    
    ebt = ebit - intereses
    
    # Evitar división por cero
    if ebt == 0:
        dfl = float('inf')  # DFL indefinido cuando EBT = 0
    else:
        dfl = ebit / ebt
    
    # Proporción de intereses sobre EBIT
    prop_intereses = (intereses / ebit) * 100 if ebit > 0 else 0
    
    return {
        'DFL': dfl,
        'EBIT': ebit,
        'Intereses': intereses,
        'EBT': ebt,
        'Prop_Intereses': prop_intereses
    }

# Ejemplos comparativos
print("="*80)
print("COMPARACIÓN: Empresas con Diferente Apalancamiento Financiero")
print("="*80)

# Empresa A: ALTO apalancamiento financiero (mucha deuda)
print(f"\n🏢 EMPRESA A: Alto Apalancamiento Financiero (Empresa Apalancada)")
print("-" * 80)

ebit_a = 1_000_000
intereses_a = 600_000

resultado_a = calcular_dfl(ebit_a, intereses_a)

print(f"  EBIT:                    ${resultado_a['EBIT']:>10,.0f}")
print(f"  Intereses:              -${resultado_a['Intereses']:>10,.0f} ({resultado_a['Prop_Intereses']:.1f}% del EBIT)")
print(f"  EBT:                     ${resultado_a['EBT']:>10,.0f}")
print(f"\n  📊 DFL: {resultado_a['DFL']:.2f}")
print(f"  👁️ Interpretación: Por cada 1% de cambio en EBIT, la utilidad neta cambia {resultado_a['DFL']:.2f}%")
print(f"  ⚠️ Alto riesgo financiero: {resultado_a['Prop_Intereses']:.0f}% del EBIT se va en intereses")

# Empresa B: BAJO apalancamiento financiero (poca deuda)
print(f"\n\n🏢 EMPRESA B: Bajo Apalancamiento Financiero (Empresa Conservadora)")
print("-" * 80)

ebit_b = 1_000_000
intereses_b = 100_000

resultado_b = calcular_dfl(ebit_b, intereses_b)

print(f"  EBIT:                    ${resultado_b['EBIT']:>10,.0f}")
print(f"  Intereses:              -${resultado_b['Intereses']:>10,.0f} ({resultado_b['Prop_Intereses']:.1f}% del EBIT)")
print(f"  EBT:                     ${resultado_b['EBT']:>10,.0f}")
print(f"\n  📊 DFL: {resultado_b['DFL']:.2f}")
print(f"  👁️ Interpretación: Menor apalancamiento financiero = mayor estabilidad")
print(f"  ✅ Bajo riesgo financiero: solo {resultado_b['Prop_Intereses']:.0f}% del EBIT se va en intereses")

# Simulación: ¿Qué pasa si el EBIT cambia?
print(f"\n\n📈 SIMULACIÓN: EBIT aumenta 20%")
print("="*80)

nuevo_ebit = 1_200_000

# Empresa A (alta deuda)
ebt_a_nuevo = nuevo_ebit - intereses_a
cambio_ebt_a = ((ebt_a_nuevo - resultado_a['EBT']) / resultado_a['EBT']) * 100

print(f"\n🏢 Empresa A (DFL = {resultado_a['DFL']:.2f}):")
print(f"  EBIT base:    ${ebit_a:>10,.0f}  →  Nuevo EBIT: ${nuevo_ebit:>10,.0f}  (+20%)")
print(f"  EBT base:     ${resultado_a['EBT']:>10,.0f}  →  Nuevo EBT:  ${ebt_a_nuevo:>10,.0f}  (+{cambio_ebt_a:.1f}%)")
print(f"  👉 El EBT aumentó {cambio_ebt_a:.1f}% = {resultado_a['DFL']:.2f} × 20%")

# Empresa B (baja deuda)
ebt_b_nuevo = nuevo_ebit - intereses_b
cambio_ebt_b = ((ebt_b_nuevo - resultado_b['EBT']) / resultado_b['EBT']) * 100

print(f"\n🏢 Empresa B (DFL = {resultado_b['DFL']:.2f}):")
print(f"  EBIT base:    ${ebit_b:>10,.0f}  →  Nuevo EBIT: ${nuevo_ebit:>10,.0f}  (+20%)")
print(f"  EBT base:     ${resultado_b['EBT']:>10,.0f}  →  Nuevo EBT:  ${ebt_b_nuevo:>10,.0f}  (+{cambio_ebt_b:.1f}%)")
print(f"  👉 El EBT aumentó {cambio_ebt_b:.1f}% = {resultado_b['DFL']:.2f} × 20%")

print(f"\n🔍 Conclusión:")
print(f"  La Empresa A (alta deuda) magnificó más el cambio en EBIT")
print(f"  pero también tiene mayor riesgo si el EBIT baja.")
print("="*80)

# COMMAND ----------

# DBTITLE 1,Explicación - Apalancamiento Combinado
# MAGIC %md
# MAGIC ## ⚡ Apalancamiento Combinado (DCL)
# MAGIC
# MAGIC ### ¿Qué es el Apalancamiento Combinado?
# MAGIC
# MAGIC El **Apalancamiento Combinado** (DCL - Degree of Combined Leverage) mide el efecto **total** de los apalancamientos operativo y financiero juntos.
# MAGIC
# MAGIC Es decir, mide cómo un cambio en las ventas impacta directamente en la utilidad neta (o EPS), considerando tanto los costos fijos operativos como los financieros.
# MAGIC
# MAGIC ### Fórmula del DCL
# MAGIC
# MAGIC $$
# MAGIC \text{DCL} = \text{DOL} \times \text{DFL}
# MAGIC $$
# MAGIC
# MAGIC También se puede calcular directamente:
# MAGIC
# MAGIC $$
# MAGIC \text{DCL} = \frac{\% \Delta \text{ EPS}}{\% \Delta \text{ Ventas}} = \frac{\text{Margen de Contribución}}{\text{EBT}}
# MAGIC $$
# MAGIC
# MAGIC ### Interpretación del DCL
# MAGIC
# MAGIC 📈 **DCL = 6.0**:  
# MAGIC Si las ventas aumentan 10%, la utilidad neta aumentará 6.0 × 10% = **60%**
# MAGIC
# MAGIC ### Niveles de Riesgo Total
# MAGIC
# MAGIC | DCL | Nivel de Riesgo | Características |
# MAGIC |-----|----------------|-------------------|
# MAGIC | < 2.0 | **Bajo** | Negocio estable, costos mayormente variables, poca deuda |
# MAGIC | 2.0 - 4.0 | **Medio** | Balance entre riesgo operativo y financiero |
# MAGIC | 4.0 - 6.0 | **Alto** | Combinación significativa de costos fijos y deuda |
# MAGIC | > 6.0 | **Muy Alto** | Gran volatilidad, alto potencial pero alto riesgo |
# MAGIC
# MAGIC ### Estrategias de Gestión del Riesgo
# MAGIC
# MAGIC 🛡️ **Si DCL es muy alto**:
# MAGIC * Reducir deuda (bajar DFL)
# MAGIC * Convertir costos fijos en variables cuando sea posible (bajar DOL)
# MAGIC * Diversificar productos/mercados para estabilizar ventas
# MAGIC * Mantener mayor colchón de efectivo
# MAGIC
# MAGIC 📈 **Si DCL es bajo**:
# MAGIC * Podría tomar más riesgo para acelerar crecimiento
# MAGIC * Considerar inversión en activos fijos (automatización)
# MAGIC * Evaluar financiamiento con deuda para proyectos rentables
# MAGIC
# MAGIC ### Relación entre DOL, DFL y DCL
# MAGIC
# MAGIC ```
# MAGIC VENTAS  →→  [DOL]  →→  EBIT  →→  [DFL]  →→  UTILIDAD NETA
# MAGIC          ╰──────  [DCL]  ──────╯
# MAGIC ```
# MAGIC
# MAGIC * **DOL**: Riesgo operativo (costos fijos operativos)
# MAGIC * **DFL**: Riesgo financiero (deuda e intereses)
# MAGIC * **DCL**: Riesgo total de la empresa

# COMMAND ----------

# DBTITLE 1,Código - Función DCL
def calcular_dcl(ventas: float,
                 costos_variables: float,
                 costos_fijos: float,
                 intereses: float) -> Dict[str, float]:
    """
    Calcula el Grado de Apalancamiento Combinado (DCL).
    
    DCL = DOL × DFL
    
    Parámetros:
    -----------
    ventas : float
        Ingresos totales por ventas
    costos_variables : float
        Costos variables totales
    costos_fijos : float
        Costos fijos operativos
    intereses : float
        Gastos financieros por intereses
    
    Retorna:
    --------
    Dict con DCL, DOL, DFL y componentes
    """
    
    # Calcular componentes intermedios
    margen_contribucion = ventas - costos_variables
    ebit = margen_contribucion - costos_fijos
    ebt = ebit - intereses
    
    # Calcular DOL
    dol = margen_contribucion / ebit if ebit != 0 else float('inf')
    
    # Calcular DFL
    dfl = ebit / ebt if ebt != 0 else float('inf')
    
    # Calcular DCL
    dcl = dol * dfl
    # Verificación alternativa: DCL = Margen Contribución / EBT
    dcl_verificado = margen_contribucion / ebt if ebt != 0 else float('inf')
    
    return {
        'DCL': dcl,
        'DOL': dol,
        'DFL': dfl,
        'Ventas': ventas,
        'Margen_Contribucion': margen_contribucion,
        'EBIT': ebit,
        'EBT': ebt,
        'Costos_Fijos': costos_fijos,
        'Intereses': intereses,
        'DCL_Verificado': dcl_verificado
    }

def clasificar_riesgo(dcl: float) -> str:
    """
    Clasifica el nivel de riesgo según el DCL.
    """
    if dcl < 2.0:
        return "BAJO - Negocio estable y conservador"
    elif dcl < 4.0:
        return "MEDIO - Balance entre riesgo y retorno"
    elif dcl < 6.0:
        return "ALTO - Riesgo significativo, requiere monitoreo"
    else:
        return "MUY ALTO - Extremadamente volátil, alto riesgo"

# Ejemplo comparativo: 4 perfiles de empresas
print("="*90)
print(" "*25 + "ANÁLISIS DE APALANCAMIENTO COMBINADO")
print(" "*20 + "Comparación de 4 Perfiles Empresariales")
print("="*90)

empresas_perfiles = {
    'Startup Tech': {
        'Ventas': 5_000_000,
        'Costos_Variables': 2_000_000,  # 40%
        'Costos_Fijos': 2_500_000,      # Altos (oficinas, salarios)
        'Intereses': 300_000,           # Deuda moderada
        'Descripcion': 'Alta inversión en talento, deuda para crecimiento'
    },
    'Retail Tradicional': {
        'Ventas': 10_000_000,
        'Costos_Variables': 7_000_000,  # 70%
        'Costos_Fijos': 2_000_000,      # Moderados
        'Intereses': 400_000,           # Deuda moderada
        'Descripcion': 'Margen bajo, alta rotación, endeudamiento medio'
    },
    'Holding Apalancado': {
        'Ventas': 8_000_000,
        'Costos_Variables': 3_000_000,  # 37.5%
        'Costos_Fijos': 3_000_000,      # Altos
        'Intereses': 1_500_000,         # Mucha deuda
        'Descripcion': 'Estructura con alta deuda y costos fijos altos'
    },
    'Servicios Profesionales': {
        'Ventas': 6_000_000,
        'Costos_Variables': 4_500_000,  # 75%
        'Costos_Fijos': 800_000,        # Bajos
        'Intereses': 100_000,           # Poca deuda
        'Descripcion': 'Costos mayormente variables, financiamiento propio'
    }
}

resultados_empresas = {}

for empresa, datos in empresas_perfiles.items():
    resultado = calcular_dcl(
        ventas=datos['Ventas'],
        costos_variables=datos['Costos_Variables'],
        costos_fijos=datos['Costos_Fijos'],
        intereses=datos['Intereses']
    )
    resultados_empresas[empresa] = resultado
    
    print(f"\n🏢 {empresa}")
    print("-" * 90)
    print(f"   {datos['Descripcion']}")
    print(f"\n   Estado de Resultados Simplificado:")
    print(f"     Ventas:                  ${resultado['Ventas']:>10,.0f}")
    print(f"     Costos Variables:       -${datos['Costos_Variables']:>10,.0f}")
    print(f"     Margen Contribución:     ${resultado['Margen_Contribucion']:>10,.0f}")
    print(f"     Costos Fijos:           -${resultado['Costos_Fijos']:>10,.0f}")
    print(f"     EBIT:                    ${resultado['EBIT']:>10,.0f}")
    print(f"     Intereses:              -${resultado['Intereses']:>10,.0f}")
    print(f"     EBT:                     ${resultado['EBT']:>10,.0f}")
    
    print(f"\n   ⚡ Apalancamientos:")
    print(f"     DOL (Operativo):         {resultado['DOL']:>6.2f}x")
    print(f"     DFL (Financiero):        {resultado['DFL']:>6.2f}x")
    print(f"     DCL (Combinado):         {resultado['DCL']:>6.2f}x")
    
    riesgo = clasificar_riesgo(resultado['DCL'])
    print(f"\n   🛡️ Nivel de Riesgo: {riesgo}")
    print(f"   👁️ Interpretación: Si ventas cambian 10%, la utilidad neta cambiará {resultado['DCL']*10:.1f}%")

print("\n" + "="*90)

# Crear DataFrame comparativo
df_apalancamiento = pd.DataFrame({
    'Empresa': list(resultados_empresas.keys()),
    'DOL': [r['DOL'] for r in resultados_empresas.values()],
    'DFL': [r['DFL'] for r in resultados_empresas.values()],
    'DCL': [r['DCL'] for r in resultados_empresas.values()]
})

print(f"\n📊 Comparación de Apalancamientos:")
display(df_apalancamiento.style.format({
    'DOL': '{:.2f}x',
    'DFL': '{:.2f}x',
    'DCL': '{:.2f}x'
}).background_gradient(subset=['DCL'], cmap='YlOrRd', vmin=0))

# COMMAND ----------

# DBTITLE 1,Explicación - Caso Práctico Integrado
# MAGIC %md
# MAGIC ## 🎯 PARTE 4: Caso Práctico Integrado
# MAGIC
# MAGIC ### ¿Qué vamos a hacer?
# MAGIC
# MAGIC Realizaremos un **análisis financiero completo** de BYMA (Bolsas y Mercados Argentinos) integrando todas las herramientas aprendidas:
# MAGIC
# MAGIC 1. ✅ **Sistema DuPont** (3 y 5 factores) → Descomponer ROE
# MAGIC 2. ✅ **DOL** (Apalancamiento Operativo) → Evaluar riesgo operativo
# MAGIC 3. ✅ **DFL** (Apalancamiento Financiero) → Evaluar riesgo financiero
# MAGIC 4. ✅ **DCL** (Apalancamiento Combinado) → Evaluar riesgo total
# MAGIC 5. ✅ **Dashboard integrado** → Visualizar todos los indicadores
# MAGIC
# MAGIC ### ¿Por qué BYMA?
# MAGIC
# MAGIC **BYMA (Bolsas y Mercados Argentinos)** es la principal bolsa de valores de Argentina:
# MAGIC
# MAGIC 📈 **Características del negocio**:
# MAGIC * Sector: Infraestructura de mercado financiero
# MAGIC * Modelo: Comisiones por transacciones + servicios de datos
# MAGIC * Márgenes: Altos (negocio de servicios)
# MAGIC * Activos: Moderados (no es intensivo en capital físico)
# MAGIC * Endeudamiento: Bajo (estructura conservadora)
# MAGIC
# MAGIC 🎯 **Esperamos encontrar**:
# MAGIC * ROE alto (negocio rentable)
# MAGIC * Margen de utilidad alto (servicios)
# MAGIC * Rotación de activos baja (no retail)
# MAGIC * DOL moderado (costos fijos operativos)
# MAGIC * DFL bajo (poca deuda)
# MAGIC * DCL moderado (riesgo controlado)
# MAGIC
# MAGIC ### Objetivo del Análisis
# MAGIC
# MAGIC Generar un **diagnóstico financiero completo** que responda:
# MAGIC
# MAGIC 1. ¿Cuáles son las fuentes de rentabilidad de BYMA?
# MAGIC 2. ¿Qué tan eficiente es en el uso de sus recursos?
# MAGIC 3. ¿Cuál es su nivel de riesgo operativo y financiero?
# MAGIC 4. ¿Es una empresa estable o volátil?
# MAGIC 5. ¿Qué recomendaciones podríamos dar?

# COMMAND ----------

# DBTITLE 1,Código - Caso BYMA Completo
# Datos de BYMA (simplificados para fines educativos, en millones de ARS)
byma_datos = {
    'Empresa': 'BYMA',
    'Sector': 'Infraestructura Financiera',
    'Ventas': 8_500,
    'Costos_Variables': 2_100,      # ~25% de ventas
    'Costos_Fijos': 2_300,
    'EBIT': 4_100,
    'Intereses': 150,
    'Impuestos': 750,
    'Utilidad_Neta': 3_200,
    'Activos': 12_000,
    'Patrimonio': 9_500
}

print("="*90)
print(" "*25 + "ANÁLISIS FINANCIERO INTEGRADO: BYMA")
print(" "*20 + "(Bolsas y Mercados Argentinos S.A.)")
print("="*90)

# 1. Estado de Resultados
print(f"\n📋 ESTADO DE RESULTADOS SIMPLIFICADO (en millones de ARS)")
print("-" * 90)
print(f"  Ventas (Ingresos):                     ${byma_datos['Ventas']:>8,.0f}")
print(f"  Costos Variables:                     -${byma_datos['Costos_Variables']:>8,.0f}")
margen_contrib = byma_datos['Ventas'] - byma_datos['Costos_Variables']
print(f"  Margen de Contribución:                ${margen_contrib:>8,.0f}  ({(margen_contrib/byma_datos['Ventas'])*100:.1f}%)")
print(f"  Costos Fijos:                         -${byma_datos['Costos_Fijos']:>8,.0f}")
print(f"  EBIT (Resultado Operativo):            ${byma_datos['EBIT']:>8,.0f}  ({(byma_datos['EBIT']/byma_datos['Ventas'])*100:.1f}%)")
print(f"  Intereses:                            -${byma_datos['Intereses']:>8,.0f}")
ebt = byma_datos['EBIT'] - byma_datos['Intereses']
print(f"  EBT (Resultado antes de impuestos):    ${ebt:>8,.0f}")
print(f"  Impuestos:                            -${byma_datos['Impuestos']:>8,.0f}")
print(f"  UTILIDAD NETA:                         ${byma_datos['Utilidad_Neta']:>8,.0f}  ({(byma_datos['Utilidad_Neta']/byma_datos['Ventas'])*100:.1f}%)")

# 2. Balance (simplificado)
print(f"\n📊 BALANCE SIMPLIFICADO (en millones de ARS)")
print("-" * 90)
print(f"  ACTIVOS TOTALES:                       ${byma_datos['Activos']:>8,.0f}")
deuda = byma_datos['Activos'] - byma_datos['Patrimonio']
print(f"  Pasivos (Deuda):                      -${deuda:>8,.0f}")
print(f"  PATRIMONIO NETO:                       ${byma_datos['Patrimonio']:>8,.0f}")
print(f"\n  Ratio Deuda/Patrimonio:                 {(deuda/byma_datos['Patrimonio']):.2f}x")
print(f"  Ratio Deuda/Activos:                    {(deuda/byma_datos['Activos'])*100:.1f}%")

# 3. Sistema DuPont de 3 factores
print(f"\n\n📊 1. SISTEMA DUPONT DE 3 FACTORES")
print("="*90)

dupont_byma = calcular_dupont_3_factores(
    utilidad_neta=byma_datos['Utilidad_Neta'],
    ventas=byma_datos['Ventas'],
    activos=byma_datos['Activos'],
    patrimonio=byma_datos['Patrimonio']
)

print(f"\n  ROE (Return on Equity):                {dupont_byma['ROE']:>7.2f}%")
print(f"\n  Descomposición:")
print(f"    • Margen de Utilidad Neta:           {dupont_byma['Margen']:>7.2f}%")
print(f"    • Rotación de Activos:                {dupont_byma['Rotacion']:>7.2f}x")
print(f"    • Multiplicador de Apalancamiento:   {dupont_byma['Apalancamiento']:>7.2f}x")
print(f"\n  Verificación: {dupont_byma['Margen']:.2f}% × {dupont_byma['Rotacion']:.2f} × {dupont_byma['Apalancamiento']:.2f} = {dupont_byma['ROE']:.2f}%")

print(f"\n  👁️ Interpretación:")
print(f"     - ROE de {dupont_byma['ROE']:.1f}% es EXCELENTE (>20% es alto)")
print(f"     - Margen alto ({dupont_byma['Margen']:.1f}%) indica negocio muy rentable")
print(f"     - Rotación baja ({dupont_byma['Rotacion']:.2f}x) es típica de servicios financieros")
print(f"     - Apalancamiento bajo ({dupont_byma['Apalancamiento']:.2f}x) indica estructura conservadora")

# 4. DOL - Apalancamiento Operativo
print(f"\n\n🏭 2. APALANCAMIENTO OPERATIVO (DOL)")
print("="*90)

dol_byma = calcular_dol(
    ventas=byma_datos['Ventas'],
    costos_variables=byma_datos['Costos_Variables'],
    costos_fijos=byma_datos['Costos_Fijos'],
    ebit=byma_datos['EBIT']
)

print(f"\n  DOL (Degree of Operating Leverage):    {dol_byma['DOL']:>7.2f}x")
print(f"\n  Componentes:")
print(f"    • Margen de Contribución:           ${dol_byma['Margen_Contribucion']:>8,.0f}  ({dol_byma['Margen_Contribucion_Pct']:.1f}%)")
print(f"    • Costos Fijos:                     ${dol_byma['Costos_Fijos']:>8,.0f}")
print(f"    • EBIT:                             ${dol_byma['EBIT']:>8,.0f}")

print(f"\n  👁️ Interpretación:")
if dol_byma['DOL'] < 2:
    print(f"     - DOL de {dol_byma['DOL']:.2f} es BAJO: negocio estable")
else:
    print(f"     - DOL de {dol_byma['DOL']:.2f} es MODERADO: riesgo operativo controlado")
print(f"     - Por cada 1% de cambio en ventas, EBIT cambia {dol_byma['DOL']:.2f}%")
print(f"     - Costos fijos representan {dol_byma['Prop_CF']:.1f}% del margen de contribución")

# 5. DFL - Apalancamiento Financiero
print(f"\n\n💰 3. APALANCAMIENTO FINANCIERO (DFL)")
print("="*90)

dfl_byma = calcular_dfl(
    ebit=byma_datos['EBIT'],
    intereses=byma_datos['Intereses']
)

print(f"\n  DFL (Degree of Financial Leverage):    {dfl_byma['DFL']:>7.2f}x")
print(f"\n  Componentes:")
print(f"    • EBIT:                             ${dfl_byma['EBIT']:>8,.0f}")
print(f"    • Intereses:                        ${dfl_byma['Intereses']:>8,.0f}  ({dfl_byma['Prop_Intereses']:.1f}% del EBIT)")
print(f"    • EBT:                              ${dfl_byma['EBT']:>8,.0f}")

print(f"\n  👁️ Interpretación:")
print(f"     - DFL de {dfl_byma['DFL']:.2f} es MUY BAJO: riesgo financiero mínimo")
print(f"     - Por cada 1% de cambio en EBIT, utilidad neta cambia {dfl_byma['DFL']:.2f}%")
print(f"     - Intereses son solo {dfl_byma['Prop_Intereses']:.1f}% del EBIT: muy baja carga financiera")
print(f"     - Estructura de capital MUY conservadora, baja dependencia de deuda")

# 6. DCL - Apalancamiento Combinado
print(f"\n\n⚡ 4. APALANCAMIENTO COMBINADO (DCL)")
print("="*90)

dcl_byma = calcular_dcl(
    ventas=byma_datos['Ventas'],
    costos_variables=byma_datos['Costos_Variables'],
    costos_fijos=byma_datos['Costos_Fijos'],
    intereses=byma_datos['Intereses']
)

print(f"\n  DCL (Degree of Combined Leverage):     {dcl_byma['DCL']:>7.2f}x")
print(f"\n  Descomposición:")
print(f"    • DOL (Operativo):                  {dcl_byma['DOL']:>7.2f}x")
print(f"    • DFL (Financiero):                 {dcl_byma['DFL']:>7.2f}x")
print(f"    • DCL = DOL × DFL:                  {dcl_byma['DCL']:>7.2f}x")

riesgo_byma = clasificar_riesgo(dcl_byma['DCL'])
print(f"\n  🛡️ Nivel de Riesgo Total: {riesgo_byma}")

print(f"\n  👁️ Interpretación:")
print(f"     - Por cada 1% de cambio en VENTAS, la UTILIDAD NETA cambia {dcl_byma['DCL']:.2f}%")
print(f"     - Efecto multiplicador de {dcl_byma['DCL']:.2f}x es {'BAJO' if dcl_byma['DCL'] < 2 else 'MODERADO' if dcl_byma['DCL'] < 4 else 'ALTO'}")
print(f"     - Combinación de DOL moderado + DFL bajo = DCL controlado")

# 7. Resumen Ejecutivo
print(f"\n\n🎯 RESUMEN EJECUTIVO: BYMA")
print("="*90)

print(f"\n  📈 Rentabilidad:")
print(f"     • ROE: {dupont_byma['ROE']:.1f}% (EXCELENTE)")
print(f"     • Margen Neto: {dupont_byma['Margen']:.1f}% (MUY ALTO)")
print(f"     • Margen EBIT: {(byma_datos['EBIT']/byma_datos['Ventas'])*100:.1f}% (ALTO)")

print(f"\n  ⚙️ Eficiencia:")
print(f"     • Rotación de Activos: {dupont_byma['Rotacion']:.2f}x (BAJA - típico del sector)")

print(f"\n  🏭 Estructura Operativa:")
print(f"     • DOL: {dcl_byma['DOL']:.2f}x (MODERADO)")
print(f"     • Margen de Contribución: {dol_byma['Margen_Contribucion_Pct']:.1f}%")

print(f"\n  💰 Estructura Financiera:")
print(f"     • DFL: {dcl_byma['DFL']:.2f}x (MUY BAJO)")
print(f"     • Apalancamiento: {dupont_byma['Apalancamiento']:.2f}x (CONSERVADOR)")
print(f"     • Deuda/Patrimonio: {(deuda/byma_datos['Patrimonio']):.2f}x")

print(f"\n  ⚡ Riesgo Total:")
print(f"     • DCL: {dcl_byma['DCL']:.2f}x ({riesgo_byma.split(' - ')[0]})")

print(f"\n  ✅ Fortalezas:")
print(f"     1. Rentabilidad excepcional (ROE {dupont_byma['ROE']:.1f}%)")
print(f"     2. Márgenes altos ({dupont_byma['Margen']:.1f}% neto)")
print(f"     3. Estructura financiera sólida (bajo endeudamiento)")
print(f"     4. Riesgo total controlado (DCL {dcl_byma['DCL']:.2f})")

print(f"\n  ⚠️ Áreas de Atención:")
print(f"     1. Dependencia de volúmenes de mercado (transacciones)")
print(f"     2. DOL {dcl_byma['DOL']:.2f} indica sensibilidad a caída de ingresos")

print(f"\n  💡 Recomendaciones:")
print(f"     1. Mantener estructura conservadora actual")
print(f"     2. Diversificar fuentes de ingreso para reducir volatilidad")
print(f"     3. Aprovechar baja deuda para inversiones estratégicas si surgen")
print(f"     4. Monitorear margen de contribución frente a competencia")

print("\n" + "="*90)

# COMMAND ----------

# DBTITLE 1,Ejercicios Prácticos
# MAGIC %md
# MAGIC ## ✍️ EJERCICIOS PRÁCTICOS
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 1: Sistema DuPont Básico
# MAGIC
# MAGIC **Contexto**: Una empresa argentina tiene los siguientes datos:
# MAGIC * Utilidad Neta: $850,000
# MAGIC * Ventas: $5,000,000
# MAGIC * Activos Totales: $4,200,000
# MAGIC * Patrimonio: $2,500,000
# MAGIC
# MAGIC **Tareas**:
# MAGIC a) Calcular el ROE usando la función `calcular_dupont_3_factores()`  
# MAGIC b) Identificar cuál componente (Margen, Rotación, Apalancamiento) es más fuerte  
# MAGIC c) Proponer una estrategia para mejorar el ROE
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 2: Comparación Sectorial
# MAGIC
# MAGIC **Contexto**: Tienes tres empresas del mismo sector con diferentes perfiles DuPont:
# MAGIC
# MAGIC | Empresa | ROE | Margen | Rotación | Apalancamiento |
# MAGIC |---------|-----|--------|-----------|----------------|
# MAGIC | A | 18% | 12% | 0.8x | 1.9x |
# MAGIC | B | 18% | 6% | 2.0x | 1.5x |
# MAGIC | C | 18% | 9% | 1.2x | 1.7x |
# MAGIC
# MAGIC **Tareas**:
# MAGIC a) ¿Cuál empresa tiene un modelo de negocio más parecido a retail? ¿Por qué?  
# MAGIC b) ¿Cuál tiene mayor riesgo operativo? Justifica  
# MAGIC c) Si el mercado entra en recesión, ¿cuál empresa estaría mejor posicionada?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 3: Apalancamiento Operativo (DOL)
# MAGIC
# MAGIC **Contexto**: Una fábrica argentina tiene:
# MAGIC * Ventas actuales: $10,000,000 (100,000 unidades × $100)
# MAGIC * Costos variables: 60% de ventas
# MAGIC * Costos fijos: $3,000,000
# MAGIC
# MAGIC **Tareas**:
# MAGIC a) Calcular el EBIT y el DOL usando `calcular_dol()`  
# MAGIC b) Si las ventas bajan 15%, ¿cuál será el nuevo EBIT?  
# MAGIC c) Calcular el punto de equilibrio en unidades y pesos  
# MAGIC d) Calcular el margen de seguridad actual
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 4: Apalancamiento Financiero (DFL)
# MAGIC
# MAGIC **Contexto**: Dos empresas comparables tienen el mismo EBIT de $2,000,000:
# MAGIC * **Empresa X** (sin deuda): Intereses = $0
# MAGIC * **Empresa Y** (con deuda): Intereses = $800,000
# MAGIC
# MAGIC **Tareas**:
# MAGIC a) Calcular el DFL de ambas empresas usando `calcular_dfl()`  
# MAGIC b) Si el EBIT sube 25%, ¿cuánto aumenta el EBT de cada empresa?  
# MAGIC c) ¿Qué empresa tiene mayor riesgo financiero? ¿Por qué?  
# MAGIC d) Si el EBIT cayera 30%, ¿qué empresa estaría en mayor problema?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 5: Apalancamiento Combinado (DCL)
# MAGIC
# MAGIC **Contexto**: Una empresa de servicios tiene:
# MAGIC * Ventas: $8,000,000
# MAGIC * Costos variables: $4,000,000 (50%)
# MAGIC * Costos fijos: $2,500,000
# MAGIC * Intereses: $400,000
# MAGIC
# MAGIC **Tareas**:
# MAGIC a) Calcular DOL, DFL y DCL usando `calcular_dcl()`  
# MAGIC b) Si las ventas aumentan 12%, ¿cuánto aumentará la utilidad neta?  
# MAGIC c) Clasificar el nivel de riesgo total de la empresa  
# MAGIC d) Proponer dos medidas para reducir el DCL
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 6: Análisis Integrado - Caja de Valores
# MAGIC
# MAGIC **Contexto**: Datos de Caja de Valores (del código anterior):
# MAGIC * Ventas: $2,800M
# MAGIC * Utilidad Neta: $950M
# MAGIC * Activos: $4,200M
# MAGIC * Patrimonio: $3,500M
# MAGIC * EBIT: $1,250M
# MAGIC * Intereses: $80M
# MAGIC * Costos Variables: $900M (estimado)
# MAGIC * Costos Fijos: $650M (estimado)
# MAGIC
# MAGIC **Tareas**:
# MAGIC a) Realizar análisis DuPont de 3 factores completo  
# MAGIC b) Calcular DOL, DFL y DCL  
# MAGIC c) Comparar con BYMA (del caso práctico): ¿cuál empresa es más riesgosa? ¿Por qué?  
# MAGIC d) Preparar un resumen ejecutivo (estilo BYMA) con fortalezas y recomendaciones
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔹 Ejercicio 7: Punto de Equilibrio y Margen de Seguridad
# MAGIC
# MAGIC **Contexto**: Un restaurant argentino tiene:
# MAGIC * Precio promedio por cliente: $3,500
# MAGIC * Costo variable por cliente: $1,800 (alimentos + bebidas)
# MAGIC * Costos fijos mensuales: $2,500,000 (alquiler, salarios, servicios)
# MAGIC * Ventas actuales: 2,000 clientes/mes
# MAGIC
# MAGIC **Tareas**:
# MAGIC a) Calcular el punto de equilibrio en clientes y pesos  
# MAGIC b) Calcular el margen de seguridad  
# MAGIC c) Si el dueño quiere reducir el punto de equilibrio a 1,200 clientes, ¿cuánto debe reducir los costos fijos?  
# MAGIC d) Alternativamente, ¿en cuánto debe aumentar el precio (manteniendo costos constantes) para lograr el mismo objetivo?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 DESAFÍO FINAL: Análisis Comparativo Multisectorial
# MAGIC
# MAGIC **Contexto**: Analizar las **4 empresas argentinas** disponibles (BYMA, Caja de Valores, Grupo Clarín, Correo Argentino) usando los datos del diccionario `empresas_arg` del código.
# MAGIC
# MAGIC **Tareas**:
# MAGIC 1. Crear un DataFrame comparativo con:
# MAGIC    * ROE, Margen, Rotación, Apalancamiento
# MAGIC    * DOL, DFL, DCL
# MAGIC    * Clasificación de riesgo
# MAGIC
# MAGIC 2. Crear visualizaciones:
# MAGIC    * Gráfico de barras: ROE vs componentes DuPont
# MAGIC    * Gráfico de dispersión: DOL vs DFL (tamano de burbuja = DCL)
# MAGIC    * Heatmap de riesgo: DOL, DFL, DCL por empresa
# MAGIC
# MAGIC 3. Responder:
# MAGIC    * ¿Qué empresa es la más rentable? ¿Por qué?
# MAGIC    * ¿Qué empresa tiene mayor riesgo total?
# MAGIC    * ¿Qué empresa es la más estable?
# MAGIC    * Si tuvieras que invertir en una, ¿cuál elegirías y por qué?
# MAGIC
# MAGIC 4. Preparar un informe ejecutivo (1 página) con hallazgos clave y recomendaciones
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 💡 Consejos para los Ejercicios
# MAGIC
# MAGIC 1. **Usa las funciones desarrolladas**: No calcules manualmente, usa `calcular_dupont_3_factores()`, `calcular_dol()`, etc.
# MAGIC 2. **Interpreta los resultados**: No solo reportes números, explica qué significan
# MAGIC 3. **Compara con benchmarks**: ROE >15% es bueno, DOL >3 es alto, DFL >2 es riesgoso
# MAGIC 4. **Visualiza**: Usa gráficos para comunicar mejor tus hallazgos
# MAGIC 5. **Piensa como analista**: ¿Qué recomendaciones darías al gerente financiero?

# COMMAND ----------

# DBTITLE 1,Consultas con Genie
# MAGIC %md
# MAGIC ## 🤖 CONSULTAS CON GENIE CODE
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📊 Sistema DuPont
# MAGIC
# MAGIC 1. ¿Cómo se interpreta un ROE del 25% descompuesto con DuPont?
# MAGIC 2. ¿Qué diferencia hay entre DuPont de 3 y 5 factores?
# MAGIC 3. Compara el DuPont de BYMA con Caja de Valores, ¿cuál es más rentable?
# MAGIC 4. Si una empresa tiene ROE alto pero margen bajo, ¿qué estrategia está usando?
# MAGIC 5. ¿Por qué una empresa de retail tiene alta rotación pero bajo margen?
# MAGIC 6. Crea un gráfico comparando los 3 componentes de DuPont de las 4 empresas argentinas
# MAGIC 7. ¿Cómo puede una empresa mejorar su ROE sin aumentar el apalancamiento?
# MAGIC 8. Calcula el DuPont de 5 factores para Grupo Clarín y explica cada componente
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🏭 Apalancamiento Operativo (DOL)
# MAGIC
# MAGIC 9. ¿Qué significa un DOL de 4.5?
# MAGIC 10. Compara el DOL de una empresa tech vs una de retail, ¿cuál es mayor y por qué?
# MAGIC 11. Si una empresa tiene DOL de 3.2 y las ventas bajan 10%, ¿qué pasa con el EBIT?
# MAGIC 12. ¿Cómo puede una empresa reducir su DOL?
# MAGIC 13. Simula qué pasa con el EBIT de BYMA si las ventas aumentan 20%
# MAGIC 14. ¿Por qué un DOL alto es riesgoso en una recesión?
# MAGIC 15. Calcula el DOL de Correo Argentino y compara con BYMA
# MAGIC 16. Crea un gráfico mostrando cómo varía el EBIT ante cambios de ventas (-20% a +20%) para DOL=1.5 vs DOL=4
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 💰 Apalancamiento Financiero (DFL)
# MAGIC
# MAGIC 17. ¿Qué significa un DFL de 2.8?
# MAGIC 18. ¿Cuál es la diferencia entre DOL y DFL?
# MAGIC 19. Si una empresa sin deuda agrega un préstamo, ¿qué pasa con su DFL?
# MAGIC 20. Compara el DFL de BYMA (baja deuda) con una empresa muy apalancada
# MAGIC 21. ¿Por qué un DFL alto magnifica tanto ganancias como pérdidas?
# MAGIC 22. Calcula el DFL de las 4 empresas argentinas y ordena de menor a mayor riesgo financiero
# MAGIC 23. Simula qué pasa con la utilidad neta si el EBIT de Grupo Clarín baja 15%
# MAGIC 24. ¿Cómo puede una empresa reducir su DFL sin pagar toda la deuda?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚡ Apalancamiento Combinado (DCL)
# MAGIC
# MAGIC 25. ¿Qué significa un DCL de 5.2?
# MAGIC 26. ¿Por qué DCL = DOL × DFL?
# MAGIC 27. Compara el DCL de las 4 empresas argentinas, ¿cuál tiene mayor riesgo total?
# MAGIC 28. Si una empresa tiene DOL=3 y DFL=2, ¿qué pasa si las ventas suben 10%?
# MAGIC 29. ¿Cuál es más peligroso en una recesión: alto DOL o alto DFL? ¿Por qué?
# MAGIC 30. Clasifica el nivel de riesgo (bajo/medio/alto) de cada empresa argentina según su DCL
# MAGIC 31. Crea un gráfico de dispersión DOL vs DFL con burbujas de tamaño DCL
# MAGIC 32. ¿Qué estrategias puede usar una empresa para reducir su DCL?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ⚖️ Punto de Equilibrio
# MAGIC
# MAGIC 33. Calcula el punto de equilibrio de una empresa con CF=$500K, Precio=$100, CV unitario=$60
# MAGIC 34. ¿Qué significa un margen de seguridad del 40%?
# MAGIC 35. Si una empresa está en su punto de equilibrio, ¿cuánto es su EBIT?
# MAGIC 36. ¿Cómo varía el punto de equilibrio si los costos fijos aumentan 20%?
# MAGIC 37. Compara el punto de equilibrio de dos empresas: una con muchos CF y otra con pocos CF
# MAGIC 38. Crea un gráfico de punto de equilibrio mostrando zonas de ganancia y pérdida
# MAGIC 39. Si una empresa quiere reducir su punto de equilibrio, ¿qué puede hacer? (3 opciones)
# MAGIC 40. Calcula el margen de seguridad de BYMA si su punto de equilibrio es $5,000M
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🎯 Análisis Integrado
# MAGIC
# MAGIC 41. Realiza un análisis financiero completo de Correo Argentino (DuPont + DOL + DFL + DCL)
# MAGIC 42. Compara el perfil de riesgo de BYMA vs Grupo Clarín, ¿cuál es más estable?
# MAGIC 43. Si tuvieras que invertir en una de las 4 empresas argentinas, ¿cuál elegirías y por qué?
# MAGIC 44. Crea un dashboard visual con todos los indicadores de las 4 empresas
# MAGIC 45. ¿Qué empresa tiene el mejor balance entre rentabilidad y riesgo?
# MAGIC 46. Explica cómo el modelo de negocio de BYMA se refleja en sus indicadores DuPont
# MAGIC 47. ¿Por qué Caja de Valores tiene un perfil similar a BYMA?
# MAGIC 48. Proponer 3 recomendaciones para mejorar el ROE de Grupo Clarín
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🔍 Análisis Sectorial
# MAGIC
# MAGIC 49. Compara los márgenes de infraestructura financiera (BYMA, Caja) vs medios (Clarín) vs logística (Correo)
# MAGIC 50. ¿Qué sector tiene mayor DOL? ¿Por qué?
# MAGIC 51. ¿Qué sector es más intensivo en activos? (mira la rotación de activos)
# MAGIC 52. Crea un heatmap mostrando ROE, DOL, DFL y DCL por sector
# MAGIC 53. ¿Qué sector es más estable en una recesión? Justifica con los apalancamientos
# MAGIC 54. ¿Qué sector tiene mayor potencial de crecimiento? ¿Por qué?
# MAGIC 55. Compara la estructura de capital (apalancamiento) de los diferentes sectores
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 💡 Aplicaciones Prácticas
# MAGIC
# MAGIC 56. Si eres CFO de Grupo Clarín, ¿qué estrategia usarías para mejorar el ROE?
# MAGIC 57. ¿Cómo debería prepararse una empresa con alto DCL para una recesión?
# MAGIC 58. Una startup tiene DOL=8 y DFL=4, ¿es sostenible? ¿Qué riesgos enfrenta?
# MAGIC 59. Compara dos estrategias: (1) reducir costos fijos vs (2) pagar deuda. ¿Cuál es mejor y cuándo?
# MAGIC 60. Si una empresa quiere duplicar su ROE, ¿qué palancas puede usar? (usa DuPont para explicar)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🇦🇷 Preguntas sobre Argentina
# MAGIC
# MAGIC 61. ¿Cómo afecta la inflación argentina al análisis de márgenes?
# MAGIC 62. ¿Por qué las empresas argentinas tienden a tener bajo apalancamiento financiero?
# MAGIC 63. Compara el ROE de empresas argentinas vs internacionales del mismo sector
# MAGIC 64. ¿Cómo impacta el tipo de cambio en empresas argentinas con deuda en dólares?
# MAGIC 65. ¿Qué papel juega el riesgo país en el análisis de apalancamiento?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 📚 Preguntas Teóricas
# MAGIC
# MAGIC 66. ¿Por qué el Sistema DuPont se llama así?
# MAGIC 67. ¿Cuál es la relación entre apalancamiento y riesgo?
# MAGIC 68. Explica el trade-off entre DOL y DFL en la planificación financiera
# MAGIC 69. ¿Cómo se relaciona el punto de equilibrio con el DOL?
# MAGIC 70. ¿Por qué el apalancamiento puede ser bueno y malo al mismo tiempo?
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 🚀 Preguntas Avanzadas
# MAGIC
# MAGIC 71. Crea una simulación Monte Carlo del ROE de BYMA variando ventas (±20%) y costos (±10%)
# MAGIC 72. Calcula el DCL en diferentes puntos de operación (50%, 75%, 100%, 125% de capacidad)
# MAGIC 73. ¿Cómo se relaciona el beta financiero con el DFL?
# MAGIC 74. Modela el impacto de automatización (aumenta CF, reduce CV) en DOL y DCL
# MAGIC 75. Compara el DuPont de BYMA en 2022 vs 2023 si tuvieras datos históricos
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC 💡 **Tip**: Usa estas preguntas para profundizar tu comprensión y practicar análisis financiero real. Genie Code puede ayudarte a:
# MAGIC * Ejecutar cálculos complejos
# MAGIC * Crear visualizaciones personalizadas
# MAGIC * Comparar múltiples escenarios
# MAGIC * Interpretar resultados en contexto argentino