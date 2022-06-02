# Mi primer Proyecto de Data Analytics 
Este proyecto se encuentra en desarrollo...

## Analisis Exploratorio de Datos
EDA, por sus siglas en inglés, es el proceso de limpieza y descubrimiento de insights a través de la revisión detallada de un conjunto de datos.

### Pasos de preparación
1. Seleccionar las variables a analizar (que sean relevantes para el estudio).(Realizado con pandas_profiling) ✔
2. Verificar la integridad de las variables (si están limpias o qué debemos hacer para limpiarlas o si no se pueden usar). ✔
3. Plantearse preguntas de exploración.(EDA)
4. Plantear hipotesis a partir de nuestras variables.*

### Pasos de EDA
1. Limpiar los datos (80% del tiempo).
2. Responder las preguntas de exploración a partir de los datos (indicadores y gráficas).
3. Responder las hipótesis (Tests estadísticos | estadística descriptiva).*
4. Generar un reporte de resultados para el público en general.

    *Pasos opcionales dependiendo de la experiencia en el area de analisis.


## Datos Usados en el Proyecto
El archivo de Datos de  la calidad del café, dejaré el link para más información:

- [Coffee Quality database from CQI](https://www.kaggle.com/volpatto/coffee-quality-database-from-cqi?select=merged_data_cleaned.csv)

## Visualización de Analisis de Datos en Streamlit

- [App de Analisis en Streamlit](https://share.streamlit.io/romeroelena16/pythonanalytics/main/src/reporte.py)


## Problemas

Durante el desarrollo se encontró algunos problemas de versiones, para resolverlos en `prompt` se ejecutaron lo siguiente

1. ` pip install pandas-profiling==2.8.0 ` , [más información](https://github.com/ydataai/pandas-profiling/issues/528).

2. ` pip install -q --upgrade pandas_profiling`  (Actualiza pandas profiling), [más información](https://community.insaid.co/hc/en-us/community/posts/360046929193-Unable-to-import-pandas-profiling).


