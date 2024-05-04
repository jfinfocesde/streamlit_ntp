import streamlit as st
import pandas as pd

st.write("Proyecto Integrador")



# Creamos un DataFrame de ejemplo con información de vehículos
vehiculos_data = {
    'Modelo': ['Ford', 'Toyota', 'Honda', 'Chevrolet', 'Nissan', 'Kia'],
    'Ventas 2020': [100000, 90000, 80000, 70000, 60000, 50000],
    'Ventas 2021': [120000, 95000, 85000, 75000, 65000, 55000]
}
vehiculos_df = pd.DataFrame(vehiculos_data)

# Establecemos la columna 'Modelo' como índice del DataFrame
vehiculos_df.set_index('Modelo', inplace=True)

# Creamos un gráfico de línea con las ventas de los vehículos por año
st.line_chart(vehiculos_df[['Ventas 2020', 'Ventas 2021']])


# Crear el DataFrame con los ingresos de tres tiendas en cuatro trimestres
data = {
    'Tienda': ['Tienda 1', 'Tienda 1', 'Tienda 1', 'Tienda 1', 'Tienda 2', 'Tienda 2', 'Tienda 2', 'Tienda 2', 'Tienda 3', 'Tienda 3', 'Tienda 3', 'Tienda 3'],
    'Trimestre': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
    'Ingresos': [100, 120, 110, 130, 80, 190, 100, 110, 270, 80, 85, 90]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
st.write(df)

# Graficar el DataFrame con un gráfico de área
df_pivot = df.pivot(index='Tienda', columns='Trimestre', values='Ingresos')
st.area_chart(df_pivot)


# Crear el DataFrame con la cantidad de animales por tipo
data = {
    'Tipo': ['Perro', 'Gato', 'Pájaro', 'Conejo', 'Hamster'],
    'Cantidad': [50, 30, 20, 10, 5]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
st.write(df)

# Graficar el DataFrame con un gráfico de barras
st.bar_chart(df.set_index('Tipo'))