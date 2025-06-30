import numpy as np
import matplotlib.pyplot as plt

def proporcion_bootstrap(data, num_bootstrap=1000, ci=90):
    n = len(data)
    proporciones = [
        np.mean(np.random.choice(data, size=n, replace=True))
        for _ in range(num_bootstrap)
    ]
    li = np.percentile(proporciones, (100 - ci) / 2)
    ls = np.percentile(proporciones, 100 - (100 - ci) / 2)
    return np.mean(data), proporciones, li, ls

def mostrar_resultado():
    import streamlit as st

    datos = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1,
             1, 1, 0, 1, 1, 1, 1, 0, 1, 1]

    proporcion, distribucion, li, ls = proporcion_bootstrap(datos)

    st.subheader("📊 Estimación de Proporción de Éxito con Bootstrap")
    st.write("Datos (1 = éxito, 0 = fallo):", datos)
    st.write(f"Proporción muestral de éxito: {proporcion:.2f}")
    st.write(f"Intervalo de Confianza del 90%: ({li:.2f}, {ls:.2f})")

    fig, ax = plt.subplots()
    ax.hist(distribucion, bins=30, color='lightcoral', edgecolor='black')
    ax.axvline(li, color='red', linestyle='--', label='Límite Inferior')
    ax.axvline(ls, color='green', linestyle='--', label='Límite Superior')
    ax.set_title("Distribución Bootstrap de la Proporción")
    ax.set_xlabel("Proporción de éxito")
    ax.set_ylabel("Frecuencia")
    ax.legend()
    st.pyplot(fig)
