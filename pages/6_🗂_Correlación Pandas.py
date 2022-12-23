import streamlit as st
import pandas as pd


pandas = pd.read_csv('ENCUESTA.csv')
st.dataframe(pandas)




