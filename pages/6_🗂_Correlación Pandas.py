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

st.write("""## HALLANDO VALORES MAXIMOS""")
st.write("""formato de tabla larga (tidy)""")
st.write("""![image.png](https://scontent.faqp2-1.fna.fbcdn.net/v/t39.30808-6/321552936_500751758819345_3826337183629146523_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeEi07FL6iP665uZbMbGVvo9n8ICoCd-TECfwgKgJ35MQKEpPpzqNQi-TlS0TFwbtrtTwxBFW33bBc0FiyjOtXDD&_nc_ohc=6p6_X1LTURcAX9iqC5a&_nc_ht=scontent.faqp2-1.fna&oh=00_AfAW4bTAZFRqRgrrKPWkiGCU8nfaZ_lmxCglMxuTlsfvqA&oe=63A9FE1C) """)

st.write("""# Manera distinta de hallar matriz de correlacion""")
st.write("""![image.png](https://scontent.faqp2-1.fna.fbcdn.net/v/t39.30808-6/321573691_498797728985079_3550727713255455082_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeFc-pKfNzO5r3lzwSBLK_Qwx-RMQYhGNRjH5ExBiEY1GK0GM5ZweRgRfIQsJEUCTgRrUbmVRENuXOQsnBHcpShB&_nc_ohc=Y6B8t0sBlZwAX_s2rnY&tn=VUjINHmzicimbWXE&_nc_ht=scontent.faqp2-1.fna&oh=00_AfAWp0L3FleB-LObEerAdB-lMyu2eWzKxDZOu6FpsHWmYg&oe=63AA0A79) """)
st.write("""## HALLANDO VALORES MAXIMOS""")
st.write("""![image.png](https://scontent.faqp2-1.fna.fbcdn.net/v/t39.30808-6/321508670_848206039798642_1928629146907610132_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeHtNmPSgor5lawaXq1h8y9KFi-4e4ErGwoWL7h7gSsbCt_1B6381KlYZPQaIOWFhetpwrXCoPIclw76pMemKAG9&_nc_ohc=zkC9n-AWTdIAX_X6XZw&_nc_ht=scontent.faqp2-1.fna&oh=00_AfADUwUJIaCS8J3nfgtvzKdUiQYZsUrqalg_OcXw9Pf_Hw&oe=63AADC71) """)


