import numpy as np
import matplotlib.pyplot as plt

def bootstrap_bloques(data, block_size=3, num_bootstrap=1000, ci=95):
    n = len(data)
    num_blocks = n - block_size + 1
    bloques = [data[i:i+block_size] for i in range(num_blocks)]
    
    volatilidades = []

    for _ in range(num_bootstrap):
        muestras = [bloques[np.random.randint(0, num_blocks)] for _ in range(n // block_size)]
        muestra_completa = np.concatenate(muestras)[:n]
        volatilidad = np.std(muestra_completa, ddof=1)
        volatilidades.append(volatilidad)

    li = np.percentile(volatilidades, (100 - ci) / 2)
    ls = np.percentile(volatilidades, 100 - (100 - ci) / 2)
    return np.std(data, ddof=1), volatilidades, li, ls

def mostrar_resultado():
    import streamlit as st

    datos = [0.5, 1.2, -0.3, 0.8, 1.1, -0.6, 0.4, 0.9, -0.2, 1.3,
             0.7, -0.4, 0.6, 1.0, -0.1, 0.8, 1.2, -0.5, 0.3, 0.9]

    volatilidad, distribucion, li, ls = bootstrap_bloques(datos, block_size=3)

    st.subheader("📉 Bootstrap con Datos Dependientes (por bloques)")
    st.write("Retornos diarios (%):", datos)
    st.write(f"Volatilidad muestral (std): {volatilidad:.4f}")
    st.write(f"Intervalo de Confianza del 95%: ({li:.4f}, {ls:.4f})")

    fig, ax = plt.subplots()
    ax.hist(distribucion, bins=30, color='lightpink', edgecolor='black')
    ax.axvline(li, color='red', linestyle='--', label='Límite Inferior')
    ax.axvline(ls, color='green', linestyle='--', label='Límite Superior')
    ax.axvline(volatilidad, color='blue', linestyle='-', label='Valor muestral')
    ax.set_title("Distribución Bootstrap de la Volatilidad")
    ax.set_xlabel("Volatilidad (desviación estándar)")
    ax.set_ylabel("Frecuencia")
    ax.legend()
    st.pyplot(fig)
