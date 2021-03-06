#from turtle import color
from optparse import Values
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


st.title('Reporte de la Calidad del Café')

@st.cache
def load_data(nrows):
    df = pd.read_csv('./data/merged_data_cleaned.csv',nrows=nrows)
    return df

df_load_state = st.text('Cargando data ...')
df = load_data(8486)

if st.checkbox('Mostrar datos crudos'):
    st.subheader('Datos crudos')
    st.write(df)

###-----

# Función para descargar csv
@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')

csv = convert_df(df)
st.download_button('Descargar datos crudos del café',csv,'merged_data_cleaned.csv','text/csv',key='download-csv')


## ----------------###
# data procesada
df_main = pd.read_csv('./data/df_main_cleaning.csv')

####### Primera pregunta

conteo_variedad_x_especie = (df_main[['Variety']] # Seleccion de columna y elimino NaNs
                            .groupby(['Variety']).size() # Agrupo y cuento las obs. por intervalo de
                            .reset_index() # Convierte a df 
                            .rename({0: 'conteo'}, axis=1) # Cambia el nombre de "0" a "conteo"
                            .sort_values(by=['conteo'],ascending=False)) # Ordena los Datos de mayor a menor


conteo_variedad_x_especie = conteo_variedad_x_especie[(conteo_variedad_x_especie['Variety']!='Other') 
                                                        & (conteo_variedad_x_especie['Variety']!='Other_2') ]
conteo_variedad_x_especie = conteo_variedad_x_especie.head(8)
conteo_variedad_x_especie = conteo_variedad_x_especie.reset_index()

# Gráfica 
st.subheader('1. Se obtiene las variedades más sembradas')
conteo_variedad_x_especie_fig = px.bar(conteo_variedad_x_especie, x='conteo', y='Variety')
st.plotly_chart(conteo_variedad_x_especie_fig, use_container_width = True)
# Tabla 
st.write('Se obtiene las variedades más sembradas')
st.write(conteo_variedad_x_especie[['Variety','conteo']])


####### Segunda pregunta

altitud_promedio_variedad = (df_main.groupby('Variety')['altitude_mean_meters'].mean()
                            .sort_values(ascending=False)
                            .reset_index() # Convierte a df 
                            .rename({0: 'conteo'}, axis=1)) # Cambia el nombre de "0" a "conteo")
altitud_promedio_variedad_8_mas = altitud_promedio_variedad[altitud_promedio_variedad.Variety.isin(
                                                        conteo_variedad_x_especie['Variety'].tolist())]
altitud_promedio_variedad_8_mas = altitud_promedio_variedad_8_mas.reset_index(drop=True)

# Gráfica 
st.subheader('2. Altitud promedio de las 8 Variedades más sembradas en el mundo')
altitud_promedio_variedad_8_mas_fig = px.bar(altitud_promedio_variedad_8_mas,x='altitude_mean_meters', y='Variety',
                                            color=altitud_promedio_variedad_8_mas['Variety'].tolist())                                             
st.plotly_chart(altitud_promedio_variedad_8_mas_fig, use_container_width = True)
# Tabla
st.write(altitud_promedio_variedad_8_mas)



####### Tercera pregunta

st.subheader('3. La altitud impacta con la calidad del café')

Variables_Calidad_Cafe_fig = px.scatter(df_main[df_main.Variety.isin(conteo_variedad_x_especie['Variety'].tolist())],
                                        x='altitude_mean_meters',
                                        y='Total_Cup_Points',
                                        color = 'Variety')
                                 
                                    
st.plotly_chart(Variables_Calidad_Cafe_fig, use_container_width = True)


####### Cuarta pregunta



st.subheader('4. Que variables impacta con la calidad del café')

# Variables principales que afectan la puntuación total
Variables_Calidad_Cafe = ['Aroma','Flavor', 'Aftertaste', 'Acidity', 'Body', 'Balance', 'Uniformity',
                          'Clean_Cup', 'Sweetness','Cupper_Points']

# Realizar Unpivot al data frame inicial
dis_calidad = pd.melt(df_main, id_vars=['Total_Cup_Points'],value_vars=Variables_Calidad_Cafe)

fig = px.scatter(dis_calidad, x='value', y='Total_Cup_Points', color = 'variable', opacity = .4)
st.plotly_chart(fig, use_container_width = True)

st.write(dis_calidad)


st.subheader('5. Que variables impacta con la calidad del café de la variedades más sembradas')
# Variables principales que afectan la puntuación total
Variables_Calidad_Cafe = ['Aroma','Flavor', 'Aftertaste', 'Acidity', 'Body', 'Balance', 'Uniformity',
                          'Clean_Cup', 'Sweetness','Cupper_Points']

# Realizar Unpivot al data frame inicial de las variedades más sembradas
dis_calidad = pd.melt(df_main[df_main.Variety.isin(conteo_variedad_x_especie['Variety'].tolist())],
                     id_vars=['Total_Cup_Points'],
                     value_vars=Variables_Calidad_Cafe)


fig = px.scatter(dis_calidad, x='value', y='Total_Cup_Points', color = 'variable', opacity = .4)
st.plotly_chart(fig, use_container_width = True)

st.write(dis_calidad)