import streamlit as st
from ejercicios import (
    ejercicio1, ejercicio2, ejercicio3, ejercicio4, ejercicio5,
    ejercicio6, ejercicio7, ejercicio8, ejercicio9, ejercicio10
)

st.set_page_config(page_title="Ejercicios con Bootstrap", layout="centered")

st.title("📊 Aplicación de Ejercicios Bootstrap")

menu = [
    "Ejercicio 1: Estimación de la Media",
    "Ejercicio 2: Comparación de Medias",
    "Ejercicio 3: Estimación de Proporciones",
    "Ejercicio 4: Correlación",
    "Ejercicio 5: Mediana y Percentiles",
    "Ejercicio 6: Razón de Varianzas",
    "Ejercicio 7: Regresión",
    "Ejercicio 8: Diferencia de Proporciones",
    "Ejercicio 9: Bootstrap Paramétrico",
    "Ejercicio 10: Datos Dependientes"
]

eleccion = st.sidebar.selectbox("Selecciona un ejercicio", menu)

if "Ejercicio 1" in eleccion:
    ejercicio1.mostrar_resultado()
elif "Ejercicio 2" in eleccion:
    ejercicio2.mostrar_resultado()
elif "Ejercicio 3" in eleccion:
    ejercicio3.mostrar_resultado()
elif "Ejercicio 4" in eleccion:
    ejercicio4.mostrar_resultado()
elif "Ejercicio 5" in eleccion:
    ejercicio5.mostrar_resultado()
elif "Ejercicio 6" in eleccion:
    ejercicio6.mostrar_resultado()
elif "Ejercicio 7" in eleccion:
    ejercicio7.mostrar_resultado()
elif "Ejercicio 8" in eleccion:
    ejercicio8.mostrar_resultado()
elif "Ejercicio 9" in eleccion:
    ejercicio9.mostrar_resultado()
elif "Ejercicio 10" in eleccion:
    ejercicio10.mostrar_resultado()
