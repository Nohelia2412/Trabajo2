import streamlit as st
import pandas as pd
import numpy as np

st.write(""" MATRIZ DE CORRELACION""")
pandas = pd.read_csv('ENCUESTA.csv')
st.dataframe(pandas)
st.write("""Cantidad de Filas y Columnas""")
    
st.write("""58 Columnas y 37 Filas""")
pandas.dtypes
st.write("""IMPUTACION DE DATOS NAn""")

pandas['CREO EN TI']=pandas['CREO EN TI'].replace(np.nan,4)
pandas['COLGANDO EN TUS MANOS']=pandas['COLGANDO EN TUS MANOS'].replace(np.nan,4)
pandas['MAMIII']=pandas['MAMIII'].replace(np.nan,3)
pandas['HEY MOR']=pandas['HEY MOR'].replace(np.nan,3)
pandas['DANZA KUDURO']=pandas['DANZA KUDURO'].replace(np.nan,4)
pandas['DESPECHA']=pandas['DESPECHA'].replace(np.nan,3)
pandas['QUE MAS PUES ']=pandas['QUE MAS PUES '].replace(np.nan,3)
pandas['UN VERANO SIN TI']=pandas['UN VERANO SIN TI'].replace(np.nan,3)
pandas['NINACHAY']=pandas['NINACHAY'].replace(np.nan,5)
pandas['POR USTEDES']=pandas['POR USTEDES'].replace(np.nan,4)
pandas['MATADOR']=pandas['MATADOR'].replace(np.nan,3)
pandas['MONTONERO AREQUIPENO']=pandas['MONTONERO AREQUIPENO'].replace(np.nan,4)
pandas['MALA TU']=pandas['MALA TU'].replace(np.nan,3)
pandas['CON LA BRISA ']=pandas['CON LA BRISA '].replace(np.nan,3)
pandas['MY LIFE ']=pandas['MY LIFE '].replace(np.nan,4)
pandas['SIGN OF THE TIMES ']=pandas['SIGN OF THE TIMES '].replace(np.nan,4)
pandas['BLOODY MARY']=pandas['BLOODY MARY'].replace(np.nan,4)
pandas['PROPUESTA INDECENTE']=pandas['PROPUESTA INDECENTE'].replace(np.nan,4)
st.dataframe(pandas)

st.write("""## tabla de correlacion de pandas""")

n = pandas[pandas.columns[1:]].to_numpy()
m = pandas[pandas.columns[0]].to_numpy()
dataframe_pandas = pd.DataFrame(n.T, columns = m)
matrix_correlacion = dataframe_pandas.corr()
matrix_correlacion

def tidy_corr_matrix(corr_pandas):
   
    corr_pandas = corr_pandas.stack().reset_index()
    corr_pandas.columns = ['Datos1','Datos2','relacion']
    corr_pandas = corr_pandas.loc[corr_pandas['Datos1'] != corr_pandas['Datos2'], :]
    corr_pandas['may a men'] = np.abs(corr_pandas['relacion'])
    corr_pandas = corr_pandas.sort_values('may a men', ascending=False)
    
    return(corr_pandas)

tidy_corr_matrix(matrix_correlacion).head(20)


