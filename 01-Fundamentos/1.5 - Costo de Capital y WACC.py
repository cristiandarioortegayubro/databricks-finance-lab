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
# MAGIC ### Módulo 01: Fundamentos de Finanzas
# MAGIC ### Notebook 1.5: Costo de Capital y WACC
# MAGIC ### 💰 **CAPM, COSTO DE DEUDA Y WACC**
# MAGIC
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Introducción
# MAGIC %md
# MAGIC # 💰 Costo de Capital y WACC
# MAGIC
# MAGIC ## 🎯 Objetivo del Notebook
# MAGIC
# MAGIC Este notebook desarrolla uno de los conceptos más importantes en finanzas corporativas: el **costo de capital** y el **WACC (Weighted Average Cost of Capital)**.
# MAGIC
# MAGIC ¿Por qué es fundamental?
# MAGIC
# MAGIC 1. ✅ **Evaluación de proyectos**: El WACC es la tasa de descuento para calcular VAN
# MAGIC 2. ✅ **Valoración de empresas**: Se usa en modelos DCF (Discounted Cash Flow)
# MAGIC 3. ✅ **Decisiones de estructura de capital**: ¿Cuánta deuda vs patrimonio?
# MAGIC 4. ✅ **Creación de valor**: Un proyecto crea valor si su retorno > WACC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📚 Referencia Bibliográfica
# MAGIC
# MAGIC **Libro**: *Finanzas Corporativas - Un Enfoque Latinoamericano* (2ª ed.)  
# MAGIC **Autor**: Guillermo L. Dumrauf  
# MAGIC **Capítulo 9**: Costo de Capital  
# MAGIC **Páginas**: 313-352
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 📈 Temas Cubiertos
# MAGIC
# MAGIC ### 1. Costo de Capital Propio (ke)
# MAGIC * Método CAPM (Capital Asset Pricing Model)
# MAGIC * Modelo de Gordon (crecimiento de dividendos)
# MAGIC * Método de bonos + prima de riesgo
# MAGIC
# MAGIC ### 2. Costo de Deuda (kd)
# MAGIC * Costo de deuda antes de impuestos
# MAGIC * Costo de deuda después de impuestos
# MAGIC * Cálculo con bonos corporativos
# MAGIC
# MAGIC ### 3. WACC (Weighted Average Cost of Capital)
# MAGIC * Fórmula del WACC
# MAGIC * Ponderación por valores de mercado
# MAGIC * Aplicaciones y ejemplos
# MAGIC
# MAGIC ### 4. Estructura de Capital Óptima
# MAGIC * Trade-off entre deuda y patrimonio
# MAGIC * Efecto del apalancamiento en el WACC
# MAGIC * Decisión financiera estratégica
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## 🇦🇷 Datos Utilizados
# MAGIC
# MAGIC Aplicaremos los conceptos con datos reales de:
# MAGIC * **Empresas argentinas**: BYMA, YPF, Mercado Libre (MELI)
# MAGIC * **ADRs argentinas**: cotizaciones en NYSE
# MAGIC * **Bonos soberanos argentinos**: para estimar tasa libre de riesgo local
# MAGIC * **Índice Merval**: para calcular beta del mercado

# COMMAND ----------

# DBTITLE 1,Explicación - Costo de Capital Propio (CAPM)
# MAGIC %md
# MAGIC ## 📊 PARTE 1: Costo de Capital Propio (ke)
# MAGIC
# MAGIC ### ¿Qué es el Costo de Capital Propio?
# MAGIC
# MAGIC El **costo de capital propio (ke)** es la **tasa de retorno mínima** que los accionistas esperan recibir por invertir en la empresa.
# MAGIC
# MAGIC 👉 Es un **costo de oportunidad**: lo que los accionistas podrían ganar invirtiendo en activos de riesgo similar.
# MAGIC
# MAGIC ### Método 1: CAPM (Capital Asset Pricing Model)
# MAGIC
# MAGIC El **CAPM** es el método más utilizado para estimar el costo de capital propio:
# MAGIC
# MAGIC $$
# MAGIC k_e = r_f + \beta \times (r_m - r_f)
# MAGIC $$
# MAGIC
# MAGIC Donde:
# MAGIC * **$r_f$**: Tasa libre de riesgo (bonos gubernamentales)
# MAGIC * **$\beta$**: Beta de la acción (riesgo sistemático)
# MAGIC * **$r_m$**: Retorno esperado del mercado
# MAGIC * **$(r_m - r_f)$**: Prima de riesgo de mercado (market risk premium)
# MAGIC
# MAGIC ### Componentes del CAPM
# MAGIC
# MAGIC 1. **Tasa libre de riesgo ($r_f$)**
# MAGIC    * En Argentina: bonos del Tesoro de EEUU (T-bonds) o bonos soberanos argentinos
# MAGIC    * Problema argentino: riesgo país alto, bonos locales no son "libres de riesgo"
# MAGIC    * Alternativa: T-bonds USA + ajuste por riesgo país
# MAGIC
# MAGIC 2. **Beta ($\beta$)**
# MAGIC    * Mide la sensibilidad de la acción a los movimientos del mercado
# MAGIC    * $\beta = 1$: Se mueve igual que el mercado
# MAGIC    * $\beta > 1$: Más volátil que el mercado (más riesgosa)
# MAGIC    * $\beta < 1$: Menos volátil que el mercado (más estable)
# MAGIC    * Cálculo: Regresión lineal de retornos de la acción vs retornos del mercado
# MAGIC
# MAGIC 3. **Prima de riesgo de mercado ($r_m - r_f$)**
# MAGIC    * Retorno adicional que exigen los inversionistas por invertir en acciones vs bonos
# MAGIC    * Históricamente: ~6-8% en mercados desarrollados
# MAGIC    * Argentina: puede ser mayor por volatilidad e incertidumbre
# MAGIC
# MAGIC ### Ejemplo Conceptual
# MAGIC
# MAGIC Empresa argentina con:
# MAGIC * Tasa libre de riesgo: 4% (T-bonds USA)
# MAGIC * Beta: 1.2 (20% más volátil que el mercado)
# MAGIC * Prima de riesgo: 7%
# MAGIC
# MAGIC $$
# MAGIC k_e = 4\% + 1.2 \times 7\% = 4\% + 8.4\% = 12.4\%
# MAGIC $$
# MAGIC
# MAGIC 👉 Los accionistas esperan un retorno mínimo del **12.4% anual**

# COMMAND ----------

# DBTITLE 1,Código - Función CAPM
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from typing import Dict, List, Tuple
from datetime import datetime, timedelta

# Colores institucionales UDA
COLOR_UDA_AZUL = '#1f4788'
COLOR_UDA_CELESTE = '#4a90e2'

# Configuración de visualizaciones
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette([COLOR_UDA_AZUL, COLOR_UDA_CELESTE, '#28a745', '#ffc107', '#dc3545'])

def calcular_ke_capm(tasa_libre_riesgo: float,
                     beta: float,
                     prima_riesgo_mercado: float,
                     riesgo_pais: float = 0) -> Dict[str, float]:
    """
    Calcula el costo de capital propio usando CAPM.
    
    Fórmula: ke = rf + β * (rm - rf) + riesgo_país
    
    Parámetros:
    -----------
    tasa_libre_riesgo : float
        Tasa libre de riesgo (ej: T-bonds USA), en porcentaje
    beta : float
        Beta de la acción (riesgo sistemático)
    prima_riesgo_mercado : float
        Prima de riesgo de mercado (rm - rf), en porcentaje
    riesgo_pais : float, opcional
        Prima adicional por riesgo país (para mercados emergentes), en porcentaje
    
    Retorna:
    --------
    Dict[str, float]
        Diccionario con ke y componentes
    
    Ejemplo:
    --------
    >>> resultado = calcular_ke_capm(
    ...     tasa_libre_riesgo=4.0,
    ...     beta=1.2,
    ...     prima_riesgo_mercado=7.0,
    ...     riesgo_pais=3.0
    ... )
    >>> print(f"Costo de capital propio: {resultado['ke']:.2f}%")
    Costo de capital propio: 15.40%
    """
    
    # Cálculo CAPM básico
    ke_base = tasa_libre_riesgo + (beta * prima_riesgo_mercado)
    
    # Ajuste por riesgo país (para mercados emergentes)
    ke_ajustado = ke_base + riesgo_pais
    
    # Componente de riesgo sistemático
    componente_sistematico = beta * prima_riesgo_mercado
    
    return {
        'ke': ke_ajustado,
        'ke_base': ke_base,
        'tasa_libre_riesgo': tasa_libre_riesgo,
        'beta': beta,
        'prima_riesgo_mercado': prima_riesgo_mercado,
        'componente_sistematico': componente_sistematico,
        'riesgo_pais': riesgo_pais
    }

# Ejemplo 1: Empresa argentina típica
print("="*80)
print("EJEMPLO 1: Cálculo de ke con CAPM - Empresa Argentina")
print("="*80)

resultado_arg = calcular_ke_capm(
    tasa_libre_riesgo=4.5,      # T-bonds USA a 10 años
    beta=1.3,                    # Beta típico de empresa argentina
    prima_riesgo_mercado=7.0,    # Prima de mercado histórica
    riesgo_pais=8.0             # Riesgo país Argentina (EMBI+)
)

print(f"\n🇦🇷 Empresa Argentina:")
print(f"\n  Componentes:")
print(f"    • Tasa libre de riesgo (rf):      {resultado_arg['tasa_libre_riesgo']:.2f}%")
print(f"    • Beta (β):                        {resultado_arg['beta']:.2f}")
print(f"    • Prima de riesgo mercado:        {resultado_arg['prima_riesgo_mercado']:.2f}%")
print(f"    • Componente sistemático (β*MRP): {resultado_arg['componente_sistematico']:.2f}%")
print(f"    • Riesgo país:                   +{resultado_arg['riesgo_pais']:.2f}%")

print(f"\n  Resultados:")
print(f"    • ke (sin riesgo país):           {resultado_arg['ke_base']:.2f}%")
print(f"    • ke AJUSTADO (con riesgo país):  {resultado_arg['ke']:.2f}%")

print(f"\n  👁️ Interpretación:")
print(f"     Los accionistas exigen un retorno mínimo de {resultado_arg['ke']:.2f}% anual")
print(f"     Esto incluye {resultado_arg['riesgo_pais']:.1f}% adicional por el riesgo país de Argentina")

print("\n" + "="*80)

# Ejemplo 2: Comparación de empresas con diferente riesgo (beta)
print("\nEJEMPLO 2: Impacto del Beta en el ke")
print("="*80)

betas = [0.8, 1.0, 1.2, 1.5, 1.8]
resultados_beta = []

for beta in betas:
    resultado = calcular_ke_capm(
        tasa_libre_riesgo=4.5,
        beta=beta,
        prima_riesgo_mercado=7.0,
        riesgo_pais=8.0
    )
    resultados_beta.append(resultado)

df_beta = pd.DataFrame(resultados_beta)
df_beta = df_beta[['beta', 'ke_base', 'ke']]
df_beta.columns = ['Beta', 'ke (sin riesgo país) %', 'ke (con riesgo país) %']

print(f"\n📈 Cómo varía el ke según el beta:")
print(df_beta.to_string(index=False))

print(f"\n👁️ Observaciones:")
print(f"  • Beta 0.8 (defensiva): ke = {resultados_beta[0]['ke']:.1f}% - Empresa estable, menor riesgo")
print(f"  • Beta 1.0 (neutra):    ke = {resultados_beta[1]['ke']:.1f}% - Igual volatilidad que el mercado")
print(f"  • Beta 1.8 (agresiva):  ke = {resultados_beta[4]['ke']:.1f}% - Empresa muy volátil, mayor riesgo")
print(f"  • Cada 0.1 de aumento en beta añade ~0.7% al ke")

print("="*80)

# COMMAND ----------

# DBTITLE 1,Explicación - Método Gordon
# MAGIC %md
# MAGIC ### Método 2: Modelo de Gordon (Crecimiento de Dividendos)
# MAGIC
# MAGIC El **Modelo de Gordon** estima el costo de capital propio a partir del precio de la acción, los dividendos esperados y su tasa de crecimiento.
# MAGIC
# MAGIC $$
# MAGIC k_e = \frac{D_1}{P_0} + g
# MAGIC $$
# MAGIC
# MAGIC Donde:
# MAGIC * **$D_1$**: Dividendo esperado en el próximo período
# MAGIC * **$P_0$**: Precio actual de la acción
# MAGIC * **$g$**: Tasa de crecimiento constante esperada de los dividendos
# MAGIC
# MAGIC ### Interpretación de los Componentes
# MAGIC
# MAGIC 1. **$\frac{D_1}{P_0}$**: Dividend yield (rendimiento por dividendo)
# MAGIC    * Es el retorno "directo" que reciben los accionistas
# MAGIC    * Ejemplo: Si P₀ = $100 y D₁ = $5, entonces yield = 5%
# MAGIC
# MAGIC 2. **$g$**: Tasa de crecimiento
# MAGIC    * Es el retorno "indirecto" por apreciación de capital
# MAGIC    * Se puede estimar de varias formas:
# MAGIC      - Crecimiento histórico de dividendos
# MAGIC      - ROE × (1 - payout ratio) = tasa de retención × ROE
# MAGIC      - Estimaciones de analistas
# MAGIC
# MAGIC ### Ventajas y Limitaciones
# MAGIC
# MAGIC ✅ **Ventajas**:
# MAGIC * Simple de calcular
# MAGIC * Basado en observables (precio y dividendos)
# MAGIC * Útil para empresas con dividendos estables
# MAGIC
# MAGIC ⚠️ **Limitaciones**:
# MAGIC * Solo aplica a empresas que pagan dividendos
# MAGIC * Asume crecimiento constante perpetuo (irreal)
# MAGIC * Muy sensible a la estimación de $g$
# MAGIC * No funciona bien para empresas de alto crecimiento
# MAGIC
# MAGIC ### Ejemplo Conceptual
# MAGIC
# MAGIC Empresa con:
# MAGIC * Precio actual: $50
# MAGIC * Dividendo esperado: $3.00
# MAGIC * Crecimiento esperado: 5% anual
# MAGIC
# MAGIC $$
# MAGIC k_e = \frac{3.00}{50} + 0.05 = 0.06 + 0.05 = 0.11 = 11\%
# MAGIC $$
# MAGIC
# MAGIC 👉 El costo de capital propio es **11% anual**
# MAGIC
# MAGIC ### ¿Cuándo usar Gordon vs CAPM?
# MAGIC
# MAGIC | Criterio | Gordon | CAPM |
# MAGIC |----------|--------|------|
# MAGIC | **Empresa paga dividendos** | Sí ✅ | No importa |
# MAGIC | **Dividendos estables** | Sí ✅ | No importa |
# MAGIC | **Beta disponible** | No importa | Sí ✅ |
# MAGIC | **Mercado emergente** | Difícil | Más robusto |
# MAGIC | **Empresa de alto crecimiento** | No recomendado | Mejor opción |

# COMMAND ----------

# DBTITLE 1,Código - Función Gordon
def calcular_ke_gordon(dividendo_actual: float,
                       precio_accion: float,
                       tasa_crecimiento: float) -> Dict[str, float]:
    """
    Calcula el costo de capital propio usando el Modelo de Gordon.
    
    Fórmula: ke = (D1 / P0) + g
    
    Parámetros:
    -----------
    dividendo_actual : float
        Dividendo por acción actual o esperado próximo período (D1)
    precio_accion : float
        Precio actual de la acción (P0)
    tasa_crecimiento : float
        Tasa de crecimiento constante esperada de dividendos (g), en porcentaje
    
    Retorna:
    --------
    Dict[str, float]
        Diccionario con ke y componentes
    
    Ejemplo:
    --------
    >>> resultado = calcular_ke_gordon(
    ...     dividendo_actual=3.50,
    ...     precio_accion=60.0,
    ...     tasa_crecimiento=4.0
    ... )
    >>> print(f"Costo de capital propio: {resultado['ke']:.2f}%")
    Costo de capital propio: 9.83%
    """
    
    # Dividend yield
    dividend_yield = (dividendo_actual / precio_accion) * 100
    
    # Costo de capital propio
    ke = dividend_yield + tasa_crecimiento
    
    return {
        'ke': ke,
        'dividend_yield': dividend_yield,
        'tasa_crecimiento': tasa_crecimiento,
        'dividendo': dividendo_actual,
        'precio': precio_accion
    }

# Ejemplo: Empresa argentina que paga dividendos
print("="*80)
print("EJEMPLO: Cálculo de ke con Modelo de Gordon")
print("="*80)

resultado_gordon = calcular_ke_gordon(
    dividendo_actual=4.50,      # Dividendo esperado: $4.50 por acción
    precio_accion=55.0,         # Precio actual: $55
    tasa_crecimiento=6.0        # Crecimiento esperado: 6% anual
)

print(f"\n📈 Datos de la Empresa:")
print(f"  Precio actual (P₀):                ${resultado_gordon['precio']:.2f}")
print(f"  Dividendo esperado (D₁):           ${resultado_gordon['dividendo']:.2f}")
print(f"  Tasa de crecimiento (g):           {resultado_gordon['tasa_crecimiento']:.2f}%")

print(f"\n📊 Cálculo:")
print(f"  Dividend Yield (D₁/P₀):             {resultado_gordon['dividend_yield']:.2f}%")
print(f"  Tasa de crecimiento (g):          +{resultado_gordon['tasa_crecimiento']:.2f}%")
print(f"  " + "-" * 50)
print(f"  Costo de capital propio (ke):      {resultado_gordon['ke']:.2f}%")

print(f"\n👁️ Interpretación:")
print(f"  Los accionistas esperan un retorno de {resultado_gordon['ke']:.2f}% anual:")
print(f"  • {resultado_gordon['dividend_yield']:.2f}% por dividendos")
print(f"  • {resultado_gordon['tasa_crecimiento']:.2f}% por apreciación de capital")

print("\n" + "="*80)

# Comparación: CAPM vs Gordon
print("\nCOMPARACION: CAPM vs Modelo de Gordon")
print("="*80)

print(f"\n🔄 Para la misma empresa:")
print(f"  • ke (CAPM):   {resultado_arg['ke']:.2f}%")
print(f"  • ke (Gordon): {resultado_gordon['ke']:.2f}%")

if abs(resultado_arg['ke'] - resultado_gordon['ke']) < 3:
    print(f"\n  ✅ Los dos métodos dan resultados similares (diferencia < 3%)")
else:
    print(f"\n  ⚠️ Los métodos dan resultados diferentes (diferencia ≥ 3%)")
    print(f"     Esto puede deberse a:")
    print(f"     - Supuestos diferentes sobre riesgo y crecimiento")
    print(f"     - Estimaciones imprecisas de beta o g")
    print(f"     - Condiciones de mercado particulares")
    print(f"\n     💡 Recomendación: Usar un promedio ponderado o varios métodos")

print("="*80)

# COMMAND ----------

# DBTITLE 1,Explicación - Costo de Deuda
# MAGIC %md
# MAGIC ## 📄 PARTE 2: Costo de Deuda (kd)
# MAGIC
# MAGIC ### ¿Qué es el Costo de Deuda?
# MAGIC
# MAGIC El **costo de deuda (kd)** es la **tasa de interés efectiva** que la empresa paga por su deuda.
# MAGIC
# MAGIC 👉 A diferencia del costo de capital propio, el costo de deuda es **observable** y **contractual**.
# MAGIC
# MAGIC ### Fórmulas del Costo de Deuda
# MAGIC
# MAGIC #### 1. Costo de Deuda ANTES de Impuestos
# MAGIC
# MAGIC $$
# MAGIC k_d = \text{Tasa de interés de la deuda}
# MAGIC $$
# MAGIC
# MAGIC * Es la tasa pactada en préstamos o bonos
# MAGIC * Se puede calcular como YTM (Yield to Maturity) de bonos corporativos
# MAGIC
# MAGIC #### 2. Costo de Deuda DESPUÉS de Impuestos
# MAGIC
# MAGIC $$
# MAGIC k_d(1 - T) = k_d \times (1 - \text{Tasa impositiva})
# MAGIC $$
# MAGIC
# MAGIC Donde:
# MAGIC * **$k_d$**: Costo de deuda antes de impuestos
# MAGIC * **$T$**: Tasa impositiva efectiva (ej: 35% en Argentina)
# MAGIC
# MAGIC ### ¿Por qué Ajustar por Impuestos?
# MAGIC
# MAGIC 💵 **Los intereses son deducibles de impuestos** (escudo fiscal o tax shield):
# MAGIC
# MAGIC * Si una empresa paga $100 de intereses y tiene tasa impositiva del 35%:
# MAGIC   - Ahorra $35 en impuestos
# MAGIC   - Costo neto = $100 - $35 = $65
# MAGIC   - Costo después de impuestos = $65 / $100 = 65% del costo original
# MAGIC
# MAGIC * Fórmula: Costo neto = $100 × (1 - 0.35) = $65
# MAGIC
# MAGIC 👉 **IMPORTANTE**: Para calcular el WACC, se usa el costo de deuda **después de impuestos** porque refleja el costo real para la empresa.
# MAGIC
# MAGIC ### Métodos de Cálculo
# MAGIC
# MAGIC #### Método 1: Tasa de Préstamos Bancarios
# MAGIC * Usar la tasa promedio ponderada de préstamos actuales
# MAGIC * Útil si la empresa tiene mayormente deuda bancaria
# MAGIC
# MAGIC #### Método 2: YTM de Bonos Corporativos
# MAGIC * Calcular el rendimiento al vencimiento (YTM) de los bonos de la empresa
# MAGIC * Más preciso si la empresa tiene bonos cotizando
# MAGIC
# MAGIC #### Método 3: Modelo de Calificación Crediticia
# MAGIC * Usar la calificación crediticia (rating) para estimar tasa
# MAGIC * Ejemplo: AAA → rf + 0.5%, BBB → rf + 2%, B → rf + 5%
# MAGIC
# MAGIC ### Ejemplo Conceptual
# MAGIC
# MAGIC Empresa con:
# MAGIC * Deuda a tasa del 10% anual
# MAGIC * Tasa impositiva: 35%
# MAGIC
# MAGIC **Costo antes de impuestos**: 10%
# MAGIC
# MAGIC **Costo después de impuestos**: 
# MAGIC $$
# MAGIC k_d(1-T) = 10\% \times (1 - 0.35) = 10\% \times 0.65 = 6.5\%
# MAGIC $$
# MAGIC
# MAGIC 👉 El costo efectivo de la deuda es **6.5%** (la empresa ahorra 3.5% en impuestos)

# COMMAND ----------

# DBTITLE 1,Código - Función Costo de Deuda
def calcular_kd(tasa_deuda: float,
                tasa_impositiva: float) -> Dict[str, float]:
    """
    Calcula el costo de deuda antes y después de impuestos.
    
    Parámetros:
    -----------
    tasa_deuda : float
        Tasa de interés de la deuda (antes de impuestos), en porcentaje
    tasa_impositiva : float
        Tasa impositiva efectiva, en porcentaje
    
    Retorna:
    --------
    Dict[str, float]
        Diccionario con kd antes y después de impuestos, y escudo fiscal
    
    Ejemplo:
    --------
    >>> resultado = calcular_kd(tasa_deuda=12.0, tasa_impositiva=35.0)
    >>> print(f"Costo de deuda (después impuestos): {resultado['kd_neto']:.2f}%")
    Costo de deuda (después impuestos): 7.80%
    """
    
    # Costo de deuda después de impuestos
    kd_neto = tasa_deuda * (1 - tasa_impositiva / 100)
    
    # Escudo fiscal (tax shield)
    escudo_fiscal = tasa_deuda * (tasa_impositiva / 100)
    
    return {
        'kd_bruto': tasa_deuda,
        'kd_neto': kd_neto,
        'tasa_impositiva': tasa_impositiva,
        'escudo_fiscal': escudo_fiscal,
        'ahorro_impuestos_pct': (escudo_fiscal / tasa_deuda) * 100
    }

# Ejemplo 1: Empresa argentina con deuda bancaria
print("="*80)
print("EJEMPLO 1: Costo de Deuda - Empresa Argentina")
print("="*80)

resultado_kd = calcular_kd(
    tasa_deuda=12.0,         # Tasa de interés: 12% anual
    tasa_impositiva=35.0     # Impuesto a las ganancias: 35%
)

print(f"\n🏦 Estructura de la Deuda:")
print(f"  Tasa de interés pactada:          {resultado_kd['kd_bruto']:.2f}%")
print(f"  Tasa impositiva:                  {resultado_kd['tasa_impositiva']:.2f}%")

print(f"\n💰 Escudo Fiscal (Tax Shield):")
print(f"  Ahorro por deducción de intereses: {resultado_kd['escudo_fiscal']:.2f}%")
print(f"  Ahorro como % del costo:          {resultado_kd['ahorro_impuestos_pct']:.1f}%")

print(f"\n📊 Costo de Deuda:")
print(f"  kd (ANTES de impuestos):          {resultado_kd['kd_bruto']:.2f}%")
print(f"  kd (DESPUÉS de impuestos):        {resultado_kd['kd_neto']:.2f}%")

print(f"\n👁️ Interpretación:")
print(f"  Por cada $100 de intereses pagados:")
print(f"  • La empresa paga ${resultado_kd['kd_bruto']:.2f} nominalmente")
print(f"  • Ahorra ${resultado_kd['escudo_fiscal']:.2f} en impuestos")
print(f"  • Costo neto real: ${resultado_kd['kd_neto']:.2f}")

print("\n" + "="*80)

# Ejemplo 2: Comparación de diferentes tasas impositivas
print("\nEJEMPLO 2: Impacto de la Tasa Impositiva en el Costo de Deuda")
print("="*80)

tasas_imp = [0, 15, 25, 35, 45]
resultados_imp = []

for tasa in tasas_imp:
    resultado = calcular_kd(tasa_deuda=10.0, tasa_impositiva=tasa)
    resultados_imp.append(resultado)

df_imp = pd.DataFrame(resultados_imp)
df_imp = df_imp[['tasa_impositiva', 'kd_bruto', 'kd_neto', 'escudo_fiscal']]
df_imp.columns = ['Tasa Impositiva (%)', 'kd Bruto (%)', 'kd Neto (%)', 'Escudo Fiscal (%)']

print(f"\n📈 Deuda al 10% con diferentes tasas impositivas:")
print(df_imp.to_string(index=False))

print(f"\n👁️ Observaciones:")
print(f"  • Sin impuestos (0%): No hay escudo fiscal, kd neto = kd bruto")
print(f"  • Con impuestos (35%): El escudo fiscal reduce el costo en 35%")
print(f"  • A mayor tasa impositiva, mayor el beneficio de la deuda")
print(f"  • Esto incentiva el uso de deuda (apalancamiento financiero)")

print("="*80)