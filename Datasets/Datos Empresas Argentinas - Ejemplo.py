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
# MAGIC ### Material Complementario - Datasets
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC </div>

# COMMAND ----------

# DBTITLE 1,Introduccion
# MAGIC %md
# MAGIC # Datos de Empresas Argentinas - Guia Practica
# MAGIC
# MAGIC ## Objetivo
# MAGIC Aprender a obtener y analizar datos financieros reales de empresas argentinas.
# MAGIC
# MAGIC ## Empresas Argentinas en Bolsas Internacionales
# MAGIC Muchas empresas argentinas cotizan como ADRs (American Depositary Receipts) en NYSE y NASDAQ:
# MAGIC
# MAGIC * YPF - Energia
# MAGIC * Grupo Financiero Galicia - Banca
# MAGIC * MercadoLibre - Tecnologia/E-commerce
# MAGIC * Banco Macro - Banca
# MAGIC * Telecom Argentina - Telecomunicaciones
# MAGIC * Pampa Energia - Energia
# MAGIC * Cresud - Agropecuario
# MAGIC
# MAGIC Estos datos son de calidad institucional y gratuitos.

# COMMAND ----------

# DBTITLE 1,Fuentes de Datos
# MAGIC %md
# MAGIC ## Fuentes de Datos Disponibles
# MAGIC
# MAGIC ### 1. Yahoo Finance (Recomendado)
# MAGIC **Ventajas:**
# MAGIC * Gratuito, sin necesidad de API key
# MAGIC * Datos historicos de 10+ anos
# MAGIC * Estados financieros completos
# MAGIC * Ratios financieros calculados
# MAGIC * Actualizacion diaria
# MAGIC
# MAGIC **Biblioteca:** yfinance
# MAGIC
# MAGIC ### 2. CNV - Comision Nacional de Valores
# MAGIC **URL:** https://www.cnv.gov.ar/
# MAGIC
# MAGIC **Datos:**
# MAGIC * Estados contables oficiales de empresas argentinas
# MAGIC * Memorias y balances
# MAGIC * Informacion financiera trimestral
# MAGIC
# MAGIC **Limitacion:** No tiene API publica, requiere descarga manual
# MAGIC
# MAGIC ### 3. BCRA - Banco Central
# MAGIC **Datos:**
# MAGIC * Tipos de cambio
# MAGIC * Tasas de interes
# MAGIC * Agregados monetarios
# MAGIC * Indices economicos

# COMMAND ----------

# DBTITLE 1,Instalacion
# MAGIC %md
# MAGIC ## Instalacion de yfinance
# MAGIC
# MAGIC Para usar yfinance en Databricks:

# COMMAND ----------

# DBTITLE 1,Instalar yfinance
# Instalar yfinance (ejecutar una sola vez)
%pip install yfinance

print("yfinance instalado correctamente")

# COMMAND ----------

# DBTITLE 1,Empresas Disponibles
# MAGIC %md
# MAGIC ## Principales Empresas Argentinas (ADRs)
# MAGIC
# MAGIC A continuacion, la lista de empresas argentinas mas importantes:

# COMMAND ----------

# DBTITLE 1,Lista de Empresas
import pandas as pd

# Empresas argentinas con ADRs
empresas_argentinas = [
    {"Ticker": "YPF", "Nombre": "YPF S.A.", "Sector": "Energia", "Bolsa": "NYSE"},
    {"Ticker": "GGAL", "Nombre": "Grupo Financiero Galicia", "Sector": "Financiero", "Bolsa": "NASDAQ"},
    {"Ticker": "MELI", "Nombre": "MercadoLibre", "Sector": "Tecnologia", "Bolsa": "NASDAQ"},
    {"Ticker": "BMA", "Nombre": "Banco Macro", "Sector": "Financiero", "Bolsa": "NYSE"},
    {"Ticker": "TEO", "Nombre": "Telecom Argentina", "Sector": "Telecomunicaciones", "Bolsa": "NYSE"},
    {"Ticker": "SUPV", "Nombre": "Grupo Supervielle", "Sector": "Financiero", "Bolsa": "NYSE"},
    {"Ticker": "PAM", "Nombre": "Pampa Energia", "Sector": "Energia", "Bolsa": "NYSE"},
    {"Ticker": "LOMA", "Nombre": "Loma Negra", "Sector": "Construccion", "Bolsa": "NYSE"},
    {"Ticker": "CRESY", "Nombre": "Cresud", "Sector": "Agropecuario", "Bolsa": "NASDAQ"},
    {"Ticker": "EDN", "Nombre": "Edenor", "Sector": "Energia", "Bolsa": "NYSE"}
]

df_empresas = pd.DataFrame(empresas_argentinas)

print("EMPRESAS ARGENTINAS DISPONIBLES")
print("="*70)
print(df_empresas.to_string(index=False))
print(f"\nTotal: {len(empresas_argentinas)} empresas")

# COMMAND ----------

# DBTITLE 1,Ejemplo 1 - Precios
# MAGIC %md
# MAGIC ## Ejemplo 1: Obtener Precios Historicos
# MAGIC
# MAGIC Vamos a descargar precios de YPF de los ultimos 2 anos.

# COMMAND ----------

# DBTITLE 1,Descargar Precios YPF
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px

# Colores institucionales UDA
UDA_COLORS = {'primary': '#003366', 'accent': '#FF6600', 'success': '#28A745', 'danger': '#DC3545'}

# Descargar datos de YPF
ypf = yf.Ticker("YPF")

# Obtener precios historicos (2 anos)
precios_ypf = ypf.history(period="2y")

print("PRECIOS DE YPF")
print("="*70)
print(f"Periodo: {precios_ypf.index[0].date()} a {precios_ypf.index[-1].date()}")
print(f"Dias de datos: {len(precios_ypf)}")
print(f"\nPrimeras filas:")
print(precios_ypf.head())

print(f"\nUltimas filas:")
print(precios_ypf.tail())

# COMMAND ----------

# DBTITLE 1,Graficar YPF
# Graficar precio de cierre con Plotly (interactivo)
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=precios_ypf.index,
    y=precios_ypf['Close'],
    mode='lines',
    name='Precio de Cierre',
    line=dict(color=UDA_COLORS['primary'], width=2.5),
    hovertemplate='<b>Fecha:</b> %{x|%Y-%m-%d}<br><b>Precio:</b> $%{y:.2f}<extra></extra>'
))

fig.update_layout(
    title=dict(
        text='YPF - Precio de Cierre (Últimos 2 Años)',
        font=dict(size=18, family='Arial', color=UDA_COLORS['primary']),
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title='Fecha',
        gridcolor='#E5E5E5',
        showgrid=True
    ),
    yaxis=dict(
        title='Precio (USD)',
        gridcolor='#E5E5E5',
        showgrid=True
    ),
    plot_bgcolor='white',
    paper_bgcolor='white',
    height=600,
    hovermode='x unified'
)

fig.show(config={'locale': 'es', 'displayModeBar': True, 'displaylogo': False})

print(f"Precio actual: ${precios_ypf['Close'][-1]:.2f}")
print(f"Precio maximo (2 anos): ${precios_ypf['Close'].max():.2f}")
print(f"Precio minimo (2 anos): ${precios_ypf['Close'].min():.2f}")

# COMMAND ----------

# DBTITLE 1,Ejemplo 2 - Estados Financieros
# MAGIC %md
# MAGIC ## Ejemplo 2: Estados Financieros
# MAGIC
# MAGIC Yahoo Finance proporciona balance, estado de resultados y flujo de caja.

# COMMAND ----------

# DBTITLE 1,Balance de YPF
# Obtener balance general
balance = ypf.balance_sheet

print("BALANCE GENERAL DE YPF")
print("="*70)
print("Principales cuentas (en millones):")
print()

# Mostrar algunas cuentas clave
if not balance.empty:
    cuentas_clave = [
        'Total Assets',
        'Total Liabilities Net Minority Interest', 
        'Total Equity Gross Minority Interest',
        'Cash And Cash Equivalents',
        'Total Debt'
    ]
    
    for cuenta in cuentas_clave:
        if cuenta in balance.index:
            valor = balance.loc[cuenta].iloc[0] / 1_000_000  # Convertir a millones
            print(f"{cuenta:40s}: ${valor:,.0f}M")
else:
    print("Balance no disponible o formato diferente")
    print("Consulta con Genie: 'Muestra el balance de YPF'")

# COMMAND ----------

# DBTITLE 1,Ejemplo 3 - Ratios
# MAGIC %md
# MAGIC ## Ejemplo 3: Ratios Financieros
# MAGIC
# MAGIC Yahoo Finance calcula automaticamente ratios clave.

# COMMAND ----------

# DBTITLE 1,Ratios de YPF
# Obtener informacion general y ratios
info = ypf.info

print("RATIOS FINANCIEROS DE YPF")
print("="*70)

ratios = {
    'P/E Ratio (Trailing)': info.get('trailingPE', 'N/A'),
    'P/E Ratio (Forward)': info.get('forwardPE', 'N/A'),
    'Price to Book': info.get('priceToBook', 'N/A'),
    'Debt to Equity': info.get('debtToEquity', 'N/A'),
    'ROE (Return on Equity)': info.get('returnOnEquity', 'N/A'),
    'ROA (Return on Assets)': info.get('returnOnAssets', 'N/A'),
    'Profit Margin': info.get('profitMargins', 'N/A'),
    'Beta': info.get('beta', 'N/A'),
    'Market Cap': info.get('marketCap', 'N/A')
}

for nombre, valor in ratios.items():
    if isinstance(valor, float):
        if 'Margin' in nombre or 'ROE' in nombre or 'ROA' in nombre:
            print(f"{nombre:30s}: {valor*100:>8.2f}%")
        elif 'Market Cap' in nombre:
            print(f"{nombre:30s}: ${valor/1e9:>8.2f}B")
        else:
            print(f"{nombre:30s}: {valor:>8.2f}")
    else:
        print(f"{nombre:30s}: {valor}")

# COMMAND ----------

# DBTITLE 1,Ejemplo 4 - Comparacion
# MAGIC %md
# MAGIC ## Ejemplo 4: Comparacion de Empresas Argentinas
# MAGIC
# MAGIC Comparemos el desempeno de varias empresas.

# COMMAND ----------

# DBTITLE 1,Comparar Empresas
# Seleccionar empresas para comparar
empresas_comparar = ['YPF', 'GGAL', 'MELI', 'BMA']

print("Descargando datos de empresas argentinas...")
print()

precios_comparacion = {}

for ticker in empresas_comparar:
    try:
        empresa = yf.Ticker(ticker)
        hist = empresa.history(period="1y")
        if not hist.empty:
            precios_comparacion[ticker] = hist['Close']
            print(f"✓ {ticker}: {len(hist)} dias de datos")
        else:
            print(f"✗ {ticker}: Sin datos")
    except Exception as e:
        print(f"✗ {ticker}: Error - {str(e)[:50]}")

if precios_comparacion:
    df_comparacion = pd.DataFrame(precios_comparacion)
    print(f"\n✓ Datos descargados para {len(precios_comparacion)} empresas")
else:
    print("\n✗ No se pudieron descargar datos")
    print("Nota: Puede requerir conexion a internet")

# COMMAND ----------

# DBTITLE 1,Graficar Comparacion
if precios_comparacion:
    # Normalizar precios (base 100)
    df_normalizado = (df_comparacion / df_comparacion.iloc[0]) * 100
    
    # Crear gráfico interactivo con Plotly
    fig = go.Figure()
    
    colores = [UDA_COLORS['primary'], UDA_COLORS['accent'], 
               UDA_COLORS['success'], UDA_COLORS['danger']]
    
    for i, columna in enumerate(df_normalizado.columns):
        fig.add_trace(go.Scatter(
            x=df_normalizado.index,
            y=df_normalizado[columna],
            mode='lines+markers',
            name=columna,
            line=dict(color=colores[i % len(colores)], width=2.5),
            marker=dict(size=4),
            hovertemplate=f'<b>{columna}</b><br>Fecha: %{{x|%Y-%m-%d}}<br>Valor: %{{y:.2f}}<extra></extra>'
        ))
    
    fig.update_layout(
        title=dict(
            text='Comparación de Empresas Argentinas (Base 100)',
            font=dict(size=18, family='Arial', color=UDA_COLORS['primary']),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(
            title='Fecha',
            gridcolor='#E5E5E5',
            showgrid=True
        ),
        yaxis=dict(
            title='Precio Normalizado (Base 100)',
            gridcolor='#E5E5E5',
            showgrid=True
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=600,
        hovermode='x unified',
        legend=dict(
            orientation='v',
            yanchor='top',
            y=1,
            xanchor='left',
            x=1.02,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#E5E5E5',
            borderwidth=1
        )
    )
    
    fig.show(config={'locale': 'es', 'displayModeBar': True, 'displaylogo': False})
    
    # Calcular retornos
    print("\nRETORNOS EN EL PERIODO:")
    print("="*70)
    for ticker in df_normalizado.columns:
        retorno = ((df_normalizado[ticker].iloc[-1] / 100) - 1) * 100
        print(f"{ticker:6s}: {retorno:>7.2f}%")
else:
    print("No hay datos para graficar")
    print("\nConsulta alternativa con Genie:")
    print('"Simula precios de YPF, GGAL y MELI para comparar"')

# COMMAND ----------

# DBTITLE 1,Ejercicios
# MAGIC %md
# MAGIC ## Ejercicios Practicos
# MAGIC
# MAGIC ### Ejercicio 1: Analisis Individual
# MAGIC Selecciona una empresa argentina y:
# MAGIC 1. Descarga 5 anos de precios historicos
# MAGIC 2. Calcula retorno anualizado y volatilidad
# MAGIC 3. Identifica maximos y minimos historicos
# MAGIC 4. Grafica precio y volumen
# MAGIC
# MAGIC ### Ejercicio 2: Analisis Sectorial
# MAGIC Compara empresas del sector financiero:
# MAGIC * Grupo Galicia (GGAL)
# MAGIC * Banco Macro (BMA)
# MAGIC * Grupo Supervielle (SUPV)
# MAGIC
# MAGIC Analiza:
# MAGIC 1. Retornos relativos
# MAGIC 2. Correlaciones
# MAGIC 3. Ratios P/E y P/B
# MAGIC 4. ROE de cada banco
# MAGIC
# MAGIC ### Ejercicio 3: Portafolio Argentino
# MAGIC Crea un portafolio con 5 empresas argentinas:
# MAGIC 1. Descarga datos de las 5 empresas
# MAGIC 2. Calcula matriz de correlacion
# MAGIC 3. Determina pesos optimos (maximo Sharpe)
# MAGIC 4. Simula rendimiento del portafolio
# MAGIC
# MAGIC ### Ejercicio 4: Analisis Fundamental
# MAGIC Para YPF:
# MAGIC 1. Obtener ultimos 4 trimestres de estados financieros
# MAGIC 2. Calcular tendencia de ingresos
# MAGIC 3. Analizar margen de utilidad
# MAGIC 4. Comparar deuda/equity con el sector

# COMMAND ----------

# DBTITLE 1,Consultas con Genie
# MAGIC %md
# MAGIC ## Consultas Sugeridas con Genie Code
# MAGIC
# MAGIC ### Analisis Basico
# MAGIC * "Descarga precios de Pampa Energia de los ultimos 3 anos"
# MAGIC * "Calcula la volatilidad historica de MercadoLibre"
# MAGIC * "Grafica el volumen de operaciones de YPF"
# MAGIC * "Compara el P/E de todas las empresas financieras argentinas"
# MAGIC
# MAGIC ### Analisis Avanzado
# MAGIC * "Calcula el beta de cada empresa argentina respecto al S&P 500"
# MAGIC * "Identifica cual empresa tuvo mejor Sharpe Ratio en 2023"
# MAGIC * "Grafica la correlacion entre YPF y el precio del petroleo"
# MAGIC * "Analiza el impacto de eventos macroeconomicos en estas empresas"
# MAGIC
# MAGIC ### Comparaciones
# MAGIC * "Compara la rentabilidad de bancos argentinos vs bancos latinoamericanos"
# MAGIC * "Cual empresa argentina tiene menor deuda/equity?"
# MAGIC * "Ranking de empresas por capitalizacion de mercado"
# MAGIC * "Identifica empresas argentinas infravaloradas segun P/B"
# MAGIC
# MAGIC ### Proyectos
# MAGIC * "Crea un dashboard interactivo con estas empresas"
# MAGIC * "Simula un portafolio de inversion en empresas argentinas"
# MAGIC * "Genera un reporte mensual automatizado"
# MAGIC * "Implementa alertas de precio para estas acciones"

# COMMAND ----------

# DBTITLE 1,Recursos Adicionales
# MAGIC %md
# MAGIC ## Recursos Adicionales
# MAGIC
# MAGIC ### Documentacion
# MAGIC * **yfinance**: https://pypi.org/project/yfinance/
# MAGIC * **Yahoo Finance**: https://finance.yahoo.com/
# MAGIC * **CNV Argentina**: https://www.cnv.gov.ar/
# MAGIC * **BCRA Estadisticas**: https://www.bcra.gob.ar/estadisticas/
# MAGIC
# MAGIC ### Datos Complementarios
# MAGIC * **Tipos de cambio**: BCRA proporciona USD/ARS oficial
# MAGIC * **Indices**: Merval (indice de la bolsa argentina)
# MAGIC * **Bonos soberanos**: Datos disponibles en Bloomberg/Refinitiv
# MAGIC * **Riesgo pais**: J.P. Morgan EMBI Argentina
# MAGIC
# MAGIC ### Consideraciones
# MAGIC 1. **Horarios**: NYSE/NASDAQ operan en horario de EEUU
# MAGIC 2. **Moneda**: Precios en USD (ADRs)
# MAGIC 3. **Dividendos**: Verificar politica de cada empresa
# MAGIC 4. **Splits**: yfinance ajusta automaticamente
# MAGIC 5. **Eventos corporativos**: Fusiones, escisiones, etc.
# MAGIC
# MAGIC ### Proximos Pasos
# MAGIC 1. Explorar datos de mas empresas
# MAGIC 2. Implementar estrategias de trading
# MAGIC 3. Crear dashboards interactivos
# MAGIC 4. Automatizar reportes financieros
# MAGIC 5. Integrar con otros modulos del curso

# COMMAND ----------

# DBTITLE 1,Visualizacion Dashboard
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

# Colores institucionales UDA
UDA_COLORS = {'primary': '#003366', 'success': '#28A745', 'warning': '#FFC107'}

# Datos de ejemplo para el dashboard (adaptables a datos reales)
razon_corriente = 2.5
prueba_acida = 1.8
capital_trabajo = 500_000
activo_total = 1_000_000
pasivo_total = 400_000
patrimonio_neto = 600_000
margen_bruto = 0.35
margen_operativo = 0.22
margen_neto = 0.15
roe = 0.18
roa = 0.12

# Crear subplots 2x2
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Ratios de Liquidez',
        'Estructura de Capital',
        'Márgenes de Rentabilidad',
        'ROA vs ROE'
    ),
    specs=[
        [{'type': 'bar'}, {'type': 'pie'}],
        [{'type': 'bar'}, {'type': 'bar'}]
    ],
    vertical_spacing=0.15,
    horizontal_spacing=0.12
)

# Gráfico 1: Ratios de Liquidez (barras verticales con colores condicionales)
liquidez_nombres = ['Razón Corriente', 'Prueba Ácida']
liquidez_valores = [razon_corriente, prueba_acida]
liquidez_colores = [
    UDA_COLORS['success'] if razon_corriente >= 2.0 else UDA_COLORS['warning'],
    UDA_COLORS['success'] if prueba_acida >= 1.5 else UDA_COLORS['warning']
]

fig.add_trace(
    go.Bar(
        x=liquidez_nombres,
        y=liquidez_valores,
        marker=dict(color=liquidez_colores),
        text=[f'{v:.2f}' for v in liquidez_valores],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Valor: %{y:.2f}<extra></extra>',
        showlegend=False
    ),
    row=1, col=1
)

# Gráfico 2: Estructura de Capital (pie)
capital_labels = ['Pasivo', 'Patrimonio Neto']
capital_valores = [pasivo_total, patrimonio_neto]

fig.add_trace(
    go.Pie(
        labels=capital_labels,
        values=capital_valores,
        marker=dict(colors=[UDA_COLORS['warning'], UDA_COLORS['success']]),
        hovertemplate='<b>%{label}</b><br>$%{value:,.0f}<br>%{percent}<extra></extra>',
        textinfo='label+percent',
        showlegend=False
    ),
    row=1, col=2
)

# Gráfico 3: Márgenes de Rentabilidad (barras verticales)
margenes_nombres = ['Margen Bruto', 'Margen Operativo', 'Margen Neto']
margenes_valores = [margen_bruto * 100, margen_operativo * 100, margen_neto * 100]

fig.add_trace(
    go.Bar(
        x=margenes_nombres,
        y=margenes_valores,
        marker=dict(color=UDA_COLORS['primary']),
        text=[f'{v:.1f}%' for v in margenes_valores],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Margen: %{y:.2f}%<extra></extra>',
        showlegend=False
    ),
    row=2, col=1
)

# Gráfico 4: ROA vs ROE (barras horizontales)
retornos_nombres = ['ROA', 'ROE']
retornos_valores = [roa * 100, roe * 100]
retornos_colores = [UDA_COLORS['primary'], UDA_COLORS['success']]

fig.add_trace(
    go.Bar(
        y=retornos_nombres,
        x=retornos_valores,
        orientation='h',
        marker=dict(color=retornos_colores),
        text=[f'{v:.1f}%' for v in retornos_valores],
        textposition='outside',
        hovertemplate='<b>%{y}</b><br>Retorno: %{x:.2f}%<extra></extra>',
        showlegend=False
    ),
    row=2, col=2
)

# Actualizar ejes y layout
fig.update_xaxes(title_text='Ratio', row=1, col=1, gridcolor='#E5E5E5')
fig.update_yaxes(title_text='Valor', row=1, col=1, gridcolor='#E5E5E5')

fig.update_xaxes(title_text='Margen', row=2, col=1, gridcolor='#E5E5E5')
fig.update_yaxes(title_text='Porcentaje (%)', row=2, col=1, gridcolor='#E5E5E5')

fig.update_xaxes(title_text='Porcentaje (%)', row=2, col=2, gridcolor='#E5E5E5')
fig.update_yaxes(title_text='Indicador', row=2, col=2, gridcolor='#E5E5E5')

# Layout global
fig.update_layout(
    title=dict(
        text='Dashboard Financiero - Análisis Integral',
        font=dict(size=20, family='Arial', color=UDA_COLORS['primary']),
        x=0.5,
        xanchor='center'
    ),
    height=900,
    plot_bgcolor='white',
    paper_bgcolor='white',
    showlegend=False
)

fig.show(config={'locale': 'es', 'displayModeBar': True, 'displaylogo': False})

print("\nDASHBOARD FINANCIERO GENERADO")
print("="*70)
print("✓ 4 visualizaciones interactivas")
print("✓ Colores institucionales UDA")
print("✓ Tooltips en español")
print("✓ Exportable como imagen estática")