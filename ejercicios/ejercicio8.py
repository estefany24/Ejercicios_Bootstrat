import numpy as np
import matplotlib.pyplot as plt

def diferencia_proporciones_bootstrap(a, b, num_bootstrap=1000, ci=95):
    n = len(a)
    diferencias = []

    for _ in range(num_bootstrap):
        muestra_a = np.random.choice(a, size=n, replace=True)
        muestra_b = np.random.choice(b, size=n, replace=True)
        prop_a = np.mean(muestra_a)
        prop_b = np.mean(muestra_b)
        diferencias.append(prop_a - prop_b)

    diferencias = np.array(diferencias)
    li = np.percentile(diferencias, (100 - ci) / 2)
    ls = np.percentile(diferencias, 100 - (100 - ci) / 2)
    diferencia_muestral = np.mean(a) - np.mean(b)
    return diferencia_muestral, diferencias, li, ls

def mostrar_resultado():
    import streamlit as st

    tratamiento_a = [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
    tratamiento_b = [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0]

    diferencia, distribucion, li, ls = diferencia_proporciones_bootstrap(tratamiento_a, tratamiento_b)

    st.subheader("⚖️ Diferencia de Proporciones con Bootstrap")
    st.write("Tratamiento A (1 = éxito, 0 = fallo):", tratamiento_a)
    st.write("Tratamiento B (1 = éxito, 0 = fallo):", tratamiento_b)
    st.write(f"Diferencia muestral de proporciones (A - B): {diferencia:.3f}")
    st.write(f"Intervalo de Confianza del 95%: ({li:.3f}, {ls:.3f})")

    fig, ax = plt.subplots()
    ax.hist(distribucion, bins=30, color='peachpuff', edgecolor='black')
    ax.axvline(li, color='red', linestyle='--', label='Límite Inferior')
    ax.axvline(ls, color='green', linestyle='--', label='Límite Superior')
    ax.axvline(0, color='black', linestyle=':', label='Sin diferencia')
    ax.axvline(diferencia, color='blue', linestyle='-', label='Diferencia muestral')
    ax.set_title("Distribución Bootstrap de la Diferencia de Proporciones (A - B)")
    ax.set_xlabel("Diferencia de proporciones")
    ax.set_ylabel("Frecuencia")
    ax.legend()
    st.pyplot(fig)
