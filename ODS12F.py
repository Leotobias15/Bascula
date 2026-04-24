# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 12: Producción y consumo responsable ''')
# Insertamos texto con formato
st.markdown("""
Esta aplicación utiliza **Machine Learning** ara predecir la cantidad de residuos enviados a relleno sanitario
a partir del porcentaje de reciclaje, alineado con el **ODS 12: Producción y Consumo Responsables**.
""")
# Insertamos una imagen
st.image("ods12.png", caption="Impacto del porcentaje de reciclaje en la reducción de residuos enviados a la basura.")


# Definimos cómo ingresará los datos el usuario
# Usaremos un deslizador
st.sidebar.header("% de reciclaje")
# Definimos los parámetros de nuestro deslizador:
  # Límite inferior: 24°C. Es el límite inferior donde los arrecifes tropicales suelen estar cómodos
  # Límite superior: 35°C. La mayoría de los corales mueren o se blanquean totalmente mucho antes de llegar a esa temperatura
  # Valor inicial: 28°C. En muchos arrecifes, a partir de los 28.5°C o 29°C comienza el estrés térmico severo
temp_input = st.sidebar.slider("Temperatura del Agua (°C)", 0.0, 100.0, 50.0)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('ods12.csv', encoding='latin-1')
# Seleccionamos las variables
X = df[['% de reciclaje']]
y = df['kg de reciduos enviados a la basura']

# Creamos y entrenamos el modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

# Hacemos la predicción con el modelo y la temperatura seleccionada por el usuario
b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*temp_input

# Presentamos loa resultados
st.subheader('Nivel de residuos generados')
st.write(f'Los residuos enviados a la basura son: {prediccion:.2f}%')

if prediccion < 20:
        st.success("Estado: Bajo nivel de residuos (consumo responsable)")
elif prediccion < 50:
        st.warning("Estado: Nivel moderado de residuos")
else:
        st.error("Estado: Alto nivel de residuos (consumo no responsable)")
