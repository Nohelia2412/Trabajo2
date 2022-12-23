import streamlit as st
import pandas as pd

st.write(""" MATRIZ DE CORRELACION""")
data = pd.read_csv('ENCUESTA.csv')
st.dataframe(data)
st.write("""Cantidad de Filas y Columnas""")
    
st.write("""58 Columnas y 37 Filas""")
data.dtypes
st.write("""IMPUTACION DE DATOS NAn""")
data['CREO EN TI']=data['CREO EN TI'].replace(np.nan,4)
data['COLGANDO EN TUS MANOS']=data['COLGANDO EN TUS MANOS'].replace(np.nan,4)
data['MAMIII']=data['MAMIII'].replace(np.nan,3)
data['HEY MOR']=data['HEY MOR'].replace(np.nan,3)
data['DANZA KUDURO']=data['DANZA KUDURO'].replace(np.nan,4)
data['DESPECHA']=data['DESPECHA'].replace(np.nan,3)
data['QUE MAS PUES ']=data['QUE MAS PUES '].replace(np.nan,3)
data['UN VERANO SIN TI']=data['UN VERANO SIN TI'].replace(np.nan,3)
data['NINACHAY']=data['NINACHAY'].replace(np.nan,5)
data['POR USTEDES']=data['POR USTEDES'].replace(np.nan,4)
data['MATADOR']=data['MATADOR'].replace(np.nan,3)
data['MONTONERO AREQUIPENO']=data['MONTONERO AREQUIPENO'].replace(np.nan,4)
data['MALA TU']=data['MALA TU'].replace(np.nan,3)
data['CON LA BRISA ']=data['CON LA BRISA '].replace(np.nan,3)
data['MY LIFE ']=data['MY LIFE '].replace(np.nan,4)
data['SIGN OF THE TIMES ']=data['SIGN OF THE TIMES '].replace(np.nan,4)
data['BLOODY MARY']=data['BLOODY MARY'].replace(np.nan,4)
data['PROPUESTA INDECENTE']=data['PROPUESTA INDECENTE'].replace(np.nan,4)
st.dataframe(data)

st.write("""## tabla de correlacion de pandas""")

n = data[data.columns[1:]].to_numpy()
m = data[data.columns[0]].to_numpy()
dataframe_pandas = pd.DataFrame(n.T, columns = m)
matrix_correlacion = dataframe_pandas.corr()
matrix_correlacion




