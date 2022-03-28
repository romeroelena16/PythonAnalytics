#from turtle import color
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title('Reporte de la Calidad del Café')

@st.cache
def load_data(nrows):
    df = pd.read_csv('./data/merged_data_cleaned.csv',nrows=nrows)
    return df

df_load_state = st.text('Cargando data ...')
df = load_data(8486)

df_main = pd.read_csv('./data/merged_data_cleaned.csv')

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


# Primera pregunta


conteo_variedad_x_especie = (df_main[['Variety']] # Seleccion de columna y elimino NaNs
                            .groupby(['Variety']).size() # Agrupo y cuento las obs. por intervalo de
                            .reset_index() # Convierte a df 
                            .rename({0: 'conteo'}, axis=1) # Cambia el nombre de "0" a "conteo"
                            .sort_values(by=['conteo'],ascending=False)) # Ordena los Datos de mayor a menor


conteo_variedad_x_especie = conteo_variedad_x_especie[(conteo_variedad_x_especie['Variety']!='Other') 
                                                        & (conteo_variedad_x_especie['Variety']!='Other_2') ]
conteo_variedad_x_especie = conteo_variedad_x_especie.head(8)

#conteo_variedad_x_especie_fig = px.bar(conteo_variedad_x_especie, x='conteo'
# , y='Variety',color=['a','b','c','d','e','f','g','h'])
conteo_variedad_x_especie_fig = px.bar(conteo_variedad_x_especie, x='conteo', y='Variety')
st.plotly_chart(conteo_variedad_x_especie_fig, use_container_width = True)
st.write('Se obtiene las variedades más sembradas')   

