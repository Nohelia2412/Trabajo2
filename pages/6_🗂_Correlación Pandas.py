import streamlit as st

st.write("""
## TABLA DE DATOS
""")

#Importamos librerias para Ciencia de Datos y Machine Learning
import numpy as np
import pandas as pd

# nos ayuda a realizar graficas de calor
import seaborn as sns

# otra manera de grafic
import matplotlib.pyplot as plt

#archivo CSV separado por comas
data = pd.read_csv('ENCUESTA.csv')
st.dataframe( data )

st.imagen ( 'https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png' )
st.write ( """Correlacion de Pearson y Sustitución de valores NAN""")
pandas  =  pd . read_csv ( 'ENCUESTA.csv' )
st.write ( 'Se visualizan los valores NAN que serán imputados en el dataframe' )
st.dataframe( pandas )
st.write ( 'Se muestra donde se encuentran los valores NAN (float64)' )
pandas.dtypes
st.imagen ( 'https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png' )
st.write ( """Tabla limpia de valores NAN"""  )
st.write ( 'Los valores que reemplazan los NAN son la media' )
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
st.dataframe ( data )
st.imagen ( 'https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png' )
st.markdown ( "<h2 style='text-align: center; color: black;'>Tabla de Correlacion de Pandas</h2>" , unsafe_allow_html = True )
n = data[data1.columns[1:]].to_numpy()
m = data[data1.columns[0]].to_numpy()
df = pd.DataFrame(n.T, columns = m)

m_corr_pandas = df.corr()
m_corr_pandas
    


st.write("""
## TABLA DE DATOS CON IMPUTACIÓN EJECUTADA
""")
n = data[data1.columns[1:]].to_numpy()
m = data[data1.columns[0]].to_numpy()
df = pd.DataFrame(n.T, columns = m)

m_corr_pandas = df.corr()
m_corr_pandas

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

st.dataframe ( data )
st.imagen ( 'https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png' )
st.markdown ( "<h2 style='text-align: center; color: black;'>Tabla de Correlacion de Pandas</h2>" , unsafe_allow_html = True )
n2 = data1[data1.columns[1:]].to_numpy()
m2= data1[data1.columns[0]].to_numpy()
df = pd.DataFrame(n.T, columns = m)

m_corr_pandas = df.corr()
m_corr_pandas
    


st.write("""
## TABLA DE DATOS CON IMPUTACIÓN EJECUTADA
""")
n = data[data1.columns[1:]].to_numpy()
m = data[data1.columns[0]].to_numpy()
df = pd.DataFrame(n.T, columns = m)

m_corr_pandas = df.corr()
m_corr_pandas


st.write(""" ## GRAFICA DE CALOR POR PANDAS """)
st.write(""" !https://scontent.faqp2-1.fna.fbcdn.net/v/t39.30808-6/321675318_717252202968243_2569053303383691197_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeEp9yH_CLdoWx0JxCQD85nTfs03RmKri0R-zTdGYquLROkMmyuHseJ2IaxFcvb8XV9OjFiARttfxMWdFHUJOC7h&_nc_ohc=mflamIikrc8AX_Sm-XR&_nc_ht=scontent.faqp2-1.fna&oh=00_AfD2CJL0JGI7t4xnvU_c3bnrQvRWz3a6Pb65i6lu8jURkQ&oe=63AA0BAC""")


