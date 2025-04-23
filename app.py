#Librerías necesarias
import streamlit as st
import pandas as pd
import joblib

import streamlit as st
from PIL import Image

# Sidebar
st.sidebar.title("📘 Acerca de la App")
st.sidebar.markdown("""
Esta aplicación predice si un tumor es **benigno o maligno** a partir de datos médicos.

Modelo entrenado con Random Forest.

**Rangos esperados para las variables:**
- Clump Thickness: 1 – 10  
- Uniformity of Cell Size: 1 – 10  
- Uniformity of Cell Shape: 1 – 10  
- Marginal Adhesion: 1 – 10  
- Single Epithelial Cell Size: 1 – 10  
- Bare Nuclei: 1 – 10  
- Bland Chromatin: 1 – 10  
- Normal Nucleoli: 1 – 10  
- Mitoses: 1 – 10  

⚠️ *Este sistema no sustituye un diagnóstico médico.*
""")

st.sidebar.markdown("---")
st.sidebar.markdown("👩‍💻 App desarrollada por: **[xionafrica]**")
st.sidebar.markdown("🔗 Conéctate conmigo: xionafricaqc@gmail.com")
st.sidebar.markdown("[GitHub](https://github.com/xionafrica)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/xionafrica/)")

st.sidebar.markdown("🛠️ Proyecto de clasificación de cáncer de mama con aprendizaje automático.")

# Panel Expandible
with st.expander("ℹ️ Más información sobre la aplicación"):
    st.markdown("""
    La predicción se basa en variables obtenidas de imágenes de biopsias.  
    Se han eliminado variables con baja correlación o redundancia para mejorar la precisión del modelo.

    Puedes introducir los valores y la app mostrará si es probable que el tumor sea benigno (2) o maligno (4).

    El modelo fue entrenado con el dataset **Wisconsin Breast Cancer**.

    **Importante:** Los valores deben estar entre 1 y 10, tal como aparecen en el dataset original.
    """)

# Visualización de la matriz de correlación
st.subheader("🧠 Matriz de Correlación del Dataset")
try:
    image = Image.open("pictures/matriz_correlacion.jpg")  
    st.image(image, caption="Matriz de correlación entre variables", use_container_width=True)
except FileNotFoundError:
    st.warning("No se encontró la imagen de la matriz de correlación. Asegúrate de que esté en la carpeta `pictures/`.")


# Cargar modelo y columnas
model = joblib.load("model/model_rf.pkl")
columnas = joblib.load("model/column_model_rf.pkl")

# Título
st.title("Clasificación de Cáncer de Mama")
st.write("Introduce los valores para predecir si el tumor es benigno o maligno.")

# Crear diccionario con campos de entrada
input_data = {}
for col in columnas:
    input_data[col] = st.number_input(col, min_value=0.0, format="%.2f")

# Botón para predecir
if st.button("Predecir"):
    # Convertir entrada en DataFrame con mismo orden de columnas
    input_df = pd.DataFrame([input_data])[columnas]
    
    # Predicción
    pred = model.predict(input_df)[0]

    # Mostrar resultado
    if pred == 0:
        st.success("Resultado: **Benigno**")
    else:
        st.error("Resultado: **Maligno**")
