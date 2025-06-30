import numpy as np
import matplotlib.pyplot as plt

def estimar_media_bootstrap(data, num_bootstrap=1000, ci=95):
    n = len(data)
    medias = [np.mean(np.random.choice(data, size=n, replace=True)) for _ in range(num_bootstrap)]
    lower = np.percentile(medias, (100 - ci) / 2)
    upper = np.percentile(medias, 100 - (100 - ci) / 2)
    return np.mean(data), medias, lower, upper

def mostrar_resultado():
    import streamlit as st

    data = [502, 498, 505, 501, 499, 503, 497, 504, 500, 502, 498, 506, 499, 501, 504]
    media, distribucion, li, ls = estimar_media_bootstrap(data)

    st.subheader("🎯 Estimación de la Media")
    st.write("Datos:", data)
    st.write(f"Media Muestral: {media:.2f}")
    st.write(f"Intervalo de Confianza al 95%: ({li:.2f}, {ls:.2f})")

    fig, ax = plt.subplots()
    ax.hist(distribucion, bins=30, color='skyblue', edgecolor='black')
    ax.axvline(li, color='red', linestyle='--', label='Límite Inferior')
    ax.axvline(ls, color='green', linestyle='--', label='Límite Superior')
    ax.set_title("Distribución Bootstrap de la Media")
    ax.set_xlabel("Media")
    ax.set_ylabel("Frecuencia")
    ax.legend()
    st.pyplot(fig)
