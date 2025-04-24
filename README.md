from pathlib import Path


# 🎗 Clasificación de Cáncer de Mama con Machine Learning

Este proyecto utiliza técnicas de aprendizaje automático para clasificar casos de cáncer de mama como **benignos** o **malignos**, basándose en características obtenidas de imágenes de células mediante aspiración con aguja fina (FNA).

La aplicación ha sido desarrollada con **Streamlit** para ofrecer una interfaz interactiva y visual.

---

## 🚀 Demo en Vivo

👉 [Haz clic aquí para probar la app en Streamlit Cloud](https://clasificacioncancerdemama.streamlit.app/)

---

## 🧠 Dataset

Se utiliza el conjunto de datos **Breast Cancer Wisconsin (Diagnostic) Data Set**, que contiene las siguientes variables:

- Clump Thickness
- Uniformity of Cell Size
- Uniformity of Cell Shape
- Marginal Adhesion
- Single Epithelial Cell Size
- Bare Nuclei
- Bland Chromatin
- Normal Nucleoli
- Mitoses
- Class (0 = Benigno, 1 = Maligno)

🔍 Fuente: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29)

---

## 🧪 Modelo

Se entrenó un modelo de clasificación usando **Random Forest**, obteniendo una alta precisión sobre los datos de test.

El modelo se guarda en `model/model_rf.pkl` y es cargado por la app automáticamente.

---

## 📊 Visualización

Incluye una **matriz de correlación** interactiva para observar la relación entre variables.

![Matriz de correlación](pictures/matriz_correlacion.JPG)

---

## 🛠 Tecnologías

- Python 🐍
- Scikit-learn
- Pandas
- Streamlit
- Matplotlib / Seaborn
- Joblib

---

## 📂 Estructura del Proyecto

Proyecto_clasificacion_cancerdemama/ 
│ ├── app.py # App principal de Streamlit 
├── model/ 
│ └── model_rf.pkl # Modelo entrenado 
├── pictures/ 
│ └── matriz_correlacion.JPG 
├── data.txt # Dataset original 
├── requirements.txt └── README.md


---

## ▶ Cómo ejecutar localmente

```bash
git https://github.com/xionafrica/Deploy_cancer_de_mama.git
cd Deploy_cancer_de_mama
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py


