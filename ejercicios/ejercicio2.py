import numpy as np
import matplotlib.pyplot as plt

def diferencia_medias_bootstrap(a, b, num_bootstrap=1000, ci=95):
    n = len(a)
    dif_medias = []
    for _ in range(num_bootstrap):
        muestra_a = np.random.choice(a, size=n, replace=True)
        muestra_b = np.random.choice(b, size=n, replace=True)
        dif = np.mean(muestra_a) - np.mean(muestra_b)
        dif_medias.append(dif)

    dif_medias = np.array(dif_medias)
    li = np.percentile(dif_medias, (100 - ci) / 2)
    ls = np.percentile(dif_medias, 100 - (100 - ci) / 2)
    return np.mean(a), np.mean(b), dif_medias, li, ls

def mostrar_resultado():
    import streamlit as st

    sistema_a = [120, 115, 125, 118, 122, 119, 123, 117, 121, 124]
    sistema_b = [135, 132, 138, 134, 136, 133, 139, 131, 137, 140]

    media_a, media_b, distribucion, li, ls = diferencia_medias_bootstrap(sistema_a, sistema_b)

    st.subheader("⚖️ Comparación de Medias con Bootstrap")
    st.write("Sistema A:", sistema_a)
    st.write("Sistema B:", sistema_b)
    st.write(f"Media de A: {media_a:.2f} ms")
    st.write(f"Media de B: {media_b:.2f} ms")
    st.write(f"Diferencia de medias (A - B): {media_a - media_b:.2f} ms")
    st.write(f"Intervalo de Confianza del {95}%: ({li:.2f}, {ls:.2f})")

    fig, ax = plt.subplots()
    ax.hist(distribucion, bins=30, color='lightgreen', edgecolor='black')
    ax.axvline(li, color='red', linestyle='--', label='Límite Inferior')
    ax.axvline(ls, color='blue', linestyle='--', label='Límite Superior')
    ax.axvline(0, color='black', linestyle=':', label='Línea de no diferencia')
    ax.set_title("Distribución Bootstrap de la Diferencia de Medias (A - B)")
    ax.set_xlabel("Diferencia de medias")
    ax.set_ylabel("Frecuencia")
    ax.legend()
    st.pyplot(fig)
