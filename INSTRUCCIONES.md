# 📚 Instrucciones para Alumnos - Databricks Finance Lab
## Cómo Acceder al Curso desde tu Cuenta Gratuita de Databricks

---

## 🎯 Objetivo

Este documento te guiará paso a paso para:
1. ✅ Crear tu cuenta **gratuita** de Databricks Community Edition
2. ✅ Clonar el repositorio del curso desde GitHub
3. ✅ Trabajar con los notebooks del curso
4. ✅ Entender las limitaciones y mejores prácticas

---

## 📋 Requisitos Previos

* 📧 **Email válido** (puede ser Gmail, Outlook, etc.)
* 🌐 **Navegador web moderno** (Chrome, Firefox, Edge, Safari)
* 💻 **Conexión a internet estable**
* ⏱️ **15-20 minutos** para completar el setup inicial

**💡 IMPORTANTE**: No necesitas instalar nada en tu computadora. Todo funciona en la nube.

---

## 🚀 Paso 1: Crear Cuenta en Databricks Community Edition

### 1.1 Registro

1. **Ve a**: https://community.cloud.databricks.com/

2. **Click en** `Sign Up` (Registrarse)

3. **Completa el formulario**:
   * **Email**: Tu dirección de correo
   * **First Name**: Tu nombre
   * **Last Name**: Tu apellido
   * **Company**: Puedes poner "Universidad del Aconcagua" o "Estudiante"
   * **Password**: Una contraseña segura (mínimo 8 caracteres)

4. **Acepta** los términos y condiciones

5. **Click en** `Sign Up`

6. **Revisa tu email** - Databricks te enviará un correo de verificación

7. **Click en el enlace** del email para activar tu cuenta

8. **Inicia sesión** en: https://community.cloud.databricks.com/

---

### 1.2 Primer Acceso

Al ingresar por primera vez verás:
* 🏠 **Workspace** (tu espacio de trabajo)
* 📊 **Notebooks** (donde ejecutarás código)
* 📁 **Folders** (carpetas para organizar)

---

## 📥 Paso 2: Clonar el Repositorio del Curso

### 2.1 Configurar Git en Databricks

1. **En el menú lateral izquierdo**, haz click en **Workspace**

2. **Click en tu nombre de usuario** (aparece como `/Users/tu-email@dominio.com`)

3. **Click derecho** en cualquier espacio vacío → Selecciona **Create** → **Repo**

4. **Completa el formulario de clonado**:

   * **Git repository URL**:  
     ```
     https://github.com/cristiandarioortegayubro/databricks-finance-lab
     ```

   * **Git provider**: Selecciona `GitHub`

   * **Repository name**: Déjalo como `databricks-finance-lab` (se autocompleta)

5. **Click en** `Create Repo`

6. **Espera 10-20 segundos** mientras Databricks clona el repositorio

---

### 2.2 Verificar el Clonado

Una vez completado, verás:

```
📁 /Users/tu-email@dominio.com/
   └── 📁 databricks-finance-lab/
       ├── 📁 00-Nivelacion-Python/
       ├── 📁 01-Fundamentos/
       ├── 📁 02-Instrumentos/
       ├── 📁 03-Analisis-Financiero/
       ├── 📁 04-Series-Temporales/
       ├── 📁 05-Analitica-Agentica/
       ├── 📁 Balances/
       ├── 📁 Datasets/
       ├── 📁 Libros/
       ├── 📁 Programa del Curso/
       ├── 📄 README.md
       └── 📓 README - Bienvenida al Curso
```

✅ **¡Felicitaciones!** Ya tienes todo el material del curso.

---

## 📖 Paso 3: Abrir y Ejecutar Notebooks

### 3.1 Abrir el Primer Notebook

1. **Navega a**: `databricks-finance-lab/00-Nivelacion-Python/`

2. **Click en**: `0.1 - Introducción a Python`

3. El notebook se abrirá en una nueva pestaña

---

### 3.2 Ejecutar Celdas de Código

#### **Opción A: Ejecutar celda por celda**

1. **Click en una celda** de código (se resalta con borde azul)

2. **Presiona**:
   * `Shift + Enter` (ejecuta y avanza a la siguiente celda)
   * O click en el botón ▶️ **Run Cell** arriba de la celda

3. **Espera** a que aparezca el resultado debajo de la celda

#### **Opción B: Ejecutar todo el notebook**

1. **Click en el menú** `Run` (arriba)

2. **Selecciona** `Run All`

3. **Espera** a que todas las celdas se ejecuten (puede tomar 1-2 minutos)

---

### 3.3 Entender los Resultados

* ✅ **Celda exitosa**: Número verde al lado izquierdo (ej: `[1]`)
* ❌ **Celda con error**: Mensaje de error en rojo
* ⏳ **Celda ejecutándose**: Spinner girando

---

## 💡 Paso 4: Trabajar con el Curso

### 4.1 Orden Recomendado de Estudio

**Si tienes experiencia en Python**:
* Puedes empezar directo en **Módulo 01 - Fundamentos**

**Si NO tienes experiencia en Python**:
* ⭐ **EMPIEZA AQUÍ**: `00-Nivelacion-Python/0.1 - Introducción a Python`
* Dedica 1-2 semanas al Módulo 00 completo
* Luego avanza secuencialmente

**Progresión sugerida**:
```
Semana 1-2:  Módulo 00 (Nivelación Python)
Semana 3-4:  Módulo 01 (Fundamentos)
Semana 5-6:  Módulo 02 (Instrumentos)
Semana 7-8:  Módulo 03 (Análisis Financiero)
Semana 9-10: Módulo 04 (Series Temporales)
Semana 11-12: Módulo 05 (Analítica Agéntica)
```

---

### 4.2 Cómo Aprovechar Genie Code (Asistente IA)

**Genie Code** es tu copiloto de IA dentro de Databricks. Úsalo para:

#### **Preguntas Conceptuales**:
```
"Explica qué es el valor presente neto"
"¿Cómo se calcula la TIR?"
"Diferencia entre tasa nominal y efectiva"
```

#### **Ayuda con Código**:
```
"Crea una función para calcular el VPN de un flujo de caja"
"Muestra cómo usar pandas para leer un CSV"
"Genera un gráfico de línea de precios de acciones"
```

#### **Depuración de Errores**:
```
"Por qué me da este error: [pega el mensaje de error]"
"Cómo soluciono este problema con numpy"
```

#### **Análisis de Datos**:
```
"Analiza este dataset y muestra estadísticas descriptivas"
"Crea un dashboard con métricas financieras"
"Genera un reporte de rentabilidad"
```

**💡 TIP**: Genie Code está en la esquina inferior derecha (ícono de chat 💬)

---

### 4.3 Modificar y Experimentar

**✅ PUEDES**:
* ✏️ Editar cualquier celda de código
* 🧪 Experimentar con diferentes valores
* ➕ Agregar nuevas celdas (botón `+` o `Esc + B`)
* 💾 Los cambios se guardan automáticamente

**❌ NO PUEDES (en Community Edition)**:
* 🚫 Crear clusters personalizados (usa serverless compute)
* 🚫 Trabajar con datasets muy grandes (límite de memoria)
* 🚫 Instalar librerías arbitrarias (solo las pre-instaladas)

---

## ⚠️ Paso 5: Limitaciones de Databricks Community Edition

### 5.1 Restricciones Técnicas

| Característica | Community Edition | Versión Empresarial |
|----------------|-------------------|---------------------|
| **Costo** | 🆓 Gratis | 💰 De pago |
| **Clusters** | ⚡ Solo serverless | ✅ Personalizables |
| **Memoria RAM** | 📊 15 GB | 📊 Hasta 1 TB+ |
| **Concurrencia** | 👤 1 usuario a la vez | 👥 Múltiples usuarios |
| **Timeout** | ⏱️ 2 horas inactividad | ⏱️ Configurable |
| **Databricks Repos** | ✅ Disponible | ✅ Disponible |
| **Genie Code** | ✅ Disponible | ✅ Disponible |
| **Colaboración** | ❌ Limitada | ✅ Completa |

---

### 5.2 Buenas Prácticas para Community Edition

#### **Gestión de Sesión**
* 💾 **Guarda tu trabajo frecuentemente** (aunque es automático)
* ⏰ **Sesiones expiran tras 2 horas de inactividad** - vuelve a iniciar sesión
* 🔄 **Si una celda se "congela"**: Detach & Re-attach del cluster (menú Compute)

#### **Gestión de Datos**
* 📉 **Usa datasets pequeños** (<100 MB) para prácticas
* 🎯 **Filtra datos temprano** en tus queries para reducir memoria
* 🗜️ **Evita cargar datasets completos** si solo necesitas una muestra

#### **Código Eficiente**
* ⚡ **Usa PySpark solo cuando sea necesario** - Pandas es más liviano para datasets pequeños
* 🧹 **Limpia variables grandes** con `del variable` cuando ya no las uses
* 🔍 **Usa `.head()` y `.sample()`** para explorar datos sin cargar todo

---

## 🔄 Paso 6: Actualizar el Repositorio (Pull)

### 6.1 Cuando el Profesor Sube Nuevos Contenidos

1. **Click derecho** en la carpeta `databricks-finance-lab/`

2. **Selecciona** `Git...` → `Pull`

3. **Espera** a que se descarguen los nuevos archivos

4. **Verifica** que aparezcan los nuevos notebooks/carpetas

### 6.2 Conflictos al Hacer Pull

Si modificaste archivos que el profesor también modificó:

**Opción A: Descartar tus cambios locales**
```
Git... → Reset → Hard Reset
```

**Opción B: Guardar tus cambios en otra carpeta**
1. Copia tu notebook modificado a `/Users/tu-email/Mis-Experimentos/`
2. Luego haz Pull

---

## 🆘 Paso 7: Solución de Problemas Comunes

### Problema 1: "Compute is not available"

**Solución**:
1. Espera 30 segundos y vuelve a ejecutar
2. Si persiste, refresca la página (F5)
3. Si aún falla, cierra sesión y vuelve a entrar

---

### Problema 2: "Import Error: No module named X"

**Causa**: La librería no está pre-instalada en Community Edition

**Solución**:
* Usa librerías alternativas que sí están disponibles:
  * ✅ pandas, numpy, matplotlib, seaborn, plotly
  * ✅ scikit-learn, scipy, statsmodels
  * ✅ pyspark, delta
  * ❌ librerías muy especializadas pueden no estar

---

### Problema 3: "Session expired"

**Causa**: 2 horas de inactividad

**Solución**:
1. Vuelve a iniciar sesión
2. Tus notebooks se guardaron automáticamente
3. Vuelve a ejecutar las celdas necesarias

---

### Problema 4: "Out of Memory Error"

**Causa**: Dataset muy grande o muchas variables en memoria

**Solución**:
```python
# Liberar memoria
import gc
del variable_grande  # Elimina la variable
gc.collect()  # Recolector de basura

# Trabajar con muestras
df_sample = df.sample(frac=0.1)  # Solo 10% de los datos
```

---

### Problema 5: No puedo hacer Push a GitHub

**Causa**: Community Edition solo permite **lectura** (Pull) de repos, no escritura (Push)

**Solución**:
* ✅ **Puedes**: Clonar, leer, ejecutar, modificar localmente
* ❌ **No puedes**: Pushear cambios al repo original
* 💡 **Alternativa**: Exporta notebooks individualmente (File → Export → .ipynb)

---

## 📚 Recursos Adicionales

### Documentación Oficial
* 📖 **Databricks Community Docs**: https://docs.databricks.com/getting-started/community-edition.html
* 🐍 **Python Tutorial**: https://docs.python.org/3/tutorial/
* 🐼 **Pandas Cheat Sheet**: https://pandas.pydata.org/docs/
* 📊 **Matplotlib Gallery**: https://matplotlib.org/stable/gallery/

### Videos Recomendados
* 🎥 **Databricks Getting Started**: https://www.youtube.com/c/Databricks
* 🎥 **Python para Finanzas**: Buscar en YouTube "Python for Finance"

### Comunidad
* 💬 **Stack Overflow**: Para preguntas técnicas específicas
* 💬 **Databricks Community Forums**: https://community.databricks.com/

---

## ✅ Checklist de Setup Completo

Marca cuando completes cada paso:

- [ ] 1. Crear cuenta en Databricks Community Edition
- [ ] 2. Verificar email y activar cuenta
- [ ] 3. Iniciar sesión en https://community.cloud.databricks.com/
- [ ] 4. Clonar repositorio del curso desde GitHub
- [ ] 5. Verificar que todas las carpetas estén presentes
- [ ] 6. Abrir notebook `README - Bienvenida al Curso`
- [ ] 7. Ejecutar primera celda de código exitosamente
- [ ] 8. Probar Genie Code (hacer una pregunta)
- [ ] 9. Leer este documento completo
- [ ] 10. Empezar Módulo 00 o Módulo 01 según tu nivel

---

## 🎓 Consejos Finales para el Éxito

### Rutina de Estudio Recomendada

**📅 Sesión Típica (2-3 horas)**:
```
15 min - Revisar notebook anterior
60 min - Nuevo contenido + ejecución de código
30 min - Ejercicios prácticos
15 min - Experimentación libre
30 min - Documentar aprendizajes
```

### Estrategias de Aprendizaje

1. **🔄 Ejecuta TODO**: No te saltes celdas de código
2. **✏️ Modifica valores**: Cambia números y observa resultados
3. **❓ Pregunta a Genie**: No tengas miedo de hacer preguntas "tontas"
4. **📝 Toma notas**: Agrega celdas Markdown con tus reflexiones
5. **🧪 Experimenta**: Crea tus propios ejemplos
6. **🤝 Colabora**: Discute conceptos con compañeros

### Mentalidad de Crecimiento

* 💪 **Los errores son oportunidades** - No te frustres, todos cometemos errores
* 🐌 **Aprende a tu ritmo** - No hay prisa
* 🔍 **Curiosidad primero** - Explora sin miedo a "romper" algo
* 🎯 **Práctica constante** - Mejor 30 min diarios que 4 horas un día

---

## 📧 Contacto

### Instructores

**Prof. Cristian Ortega**
* 📧 Email: cortega@uda.edu.ar

**Prof. Gustavo Machín**
* 📧 Email: gmachin@uda.edu.ar

### Soporte Técnico

Para problemas con Databricks Community Edition:
* 🌐 https://community.databricks.com/
* 📖 https://docs.databricks.com/

---

## 🎉 ¡Bienvenido al Databricks Finance Lab!

Estás a punto de comenzar un viaje emocionante donde combinarás:
* 📊 Finanzas
* 💻 Programación
* 🤖 Inteligencia Artificial
* ☁️ Cloud Computing

**¡Mucha suerte y disfruta el aprendizaje! 🚀**

---

*Versión 1.0 - Junio 2026*
*Universidad del Aconcagua - Facultad de Ciencias Económicas y Jurídicas*