import streamlit as st
import pandas as pd

st.write("Simulador Cesde")

df = pd.read_csv('datasets\cesde.csv')

edad_min = st.number_input("Ingrese la edad minima")
edad_max = st.number_input("Ingrese la edad máxima")

filtro_edad = df[(df['EDAD']>=edad_min)&(df['EDAD']<=edad_max)]

st.table(filtro_edad)

print(df.info())