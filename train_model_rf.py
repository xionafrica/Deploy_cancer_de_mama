# -*- coding: utf-8 -*-
"""Despliegue modelo clasificación de cancer de mama con RF.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1czmTSlK6z2RYtTZkbSQCE45RWspqFrqs


# **ETAPAS**
"""

#Librerías necesarias
import pandas as pd
from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

"""##**1 cargar datos**

"""

# Cargar dataset
datos = pd.read_csv('data/breast-cancer-wisconsin.data.txt')
datos.head()

"""#**2 Preprocesar datos**"""

#Preparar datos
datos['Bare Nuclei'] = pd.to_numeric(datos['Bare Nuclei'], errors='coerce')
datos.dropna(inplace=True)

#Balancear clases
#Separar clases
class_majority = datos[datos['Class'] == 2]
class_minority = datos[datos['Class'] == 4]

# Aumentar muestras de la clase minoritaria (balanceo)
class_minority_upsampled = resample(class_minority,
                                    replace=True,  # Re-muestreo con reemplazo
                                    n_samples=len(class_majority),  # Igualar tamaño
                                    random_state=42)

# Crear nuevo dataset balanceado
data_balanced = pd.concat([class_majority, class_minority_upsampled])
# print(data_balanced['Class'].value_counts())

#vamos a convertir la Clase 2 en 0 y la clase 4 en 1

data_balanced['Class']=data_balanced['Class'].map({2:0,4:1})

# columnas a eliminar 
columnas_a_eliminar = ['ID', 'Uniformity of Cell Size', 'Bland Chromatin']
# Separar características y variable objetivo
X = data_balanced.drop(columns=columnas_a_eliminar + ['Class'])
y = data_balanced['Class']

"""#**3 Dividir los datos en entrenamiento y prueba**"""

# Dividir en entrenamiento y prueba manteniendo la proporción de clases
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

"""#**4 Entrenar el modelo**"""

#Entranamiento del modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

"""#**5 Evaluar modelo**"""

#Evaluamos el modelo

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

"""#**6 Guardar modelo**"""

# Guardar modelo
joblib.dump(model, 'model_rf.pkl')

# (Opcional) Guardar nombres de columnas
columnas = X.columns.tolist()
joblib.dump(columnas, 'feature_pipeline_rf.pkl')