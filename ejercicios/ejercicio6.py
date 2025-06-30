import numpy as np
import matplotlib.pyplot as plt

def razon_varianzas_bootstrap(a, b, num_bootstrap=1000, ci=95):
    n = len(a)
    razones = []
    for _ in range(num_bootstrap):
        muestra_a = np.random.choice(a, size=n, replace=True)
        muestra_b = np.random.choice(b, size=n, replace=True)
        var_a = np.var(muestra_a, ddof=1)
        var_b = np.var(muestra_b, ddof=1)
        razon = var_a / var_b
        razones.append(razon)

    li = np.percentile(razones, (100 - ci) / 2)
    ls = np.percentile(razones, 100 - (100 - ci) / 2)
    razon_muestral = np.var(a, ddof=1) / np.var(b, ddof=1)
    return razon_muestral, razones, li, ls

def mostrar_resultado():
    import streamlit as st

    proceso_1 = [45.2, 44.8, 45.5, 44.9, 45.1, 45.0, 44.7, 45.3, 44.6, 45.4]
    proceso_2 = [43.8, 44.5, 43.2, 44.1, 43.9, 44.3, 43.6, 44.0, 43.7, 44.2]

    razon, distribucion, li, ls = razon_varianzas_bootstrap(proceso_1, proceso_2)

    st.subheader("📉 Razón de Varianzas con Bootstrap")
    st.write("Proceso 1:", proceso_1)
    st.write("Proceso 2:", proceso_2)
    st.write(f"Razón de varianzas (Pro1 / Pro2): {razon:.3f}")
    st.write(f"Intervalo de Confianza del 95%: ({li:.3f}, {ls:.3f})")

    fig, ax = plt.subplots()
    ax.hist(distribucion, bins=30, color='lightskyblue', edgecolor='black')
    ax.axvline(li, color='red', linestyle='--', label='Límite Inferior')
    ax.axvline(ls, color='green', linestyle='--', label='Límite Superior')
    ax.axvline(1, color='black', linestyle=':', label='Igual varianza')
    ax.axvline(razon, color='blue', linestyle='-', label='Razón muestral')
    ax.set_title("Distribución Bootstrap de la Razón de Varianzas")
    ax.set_xlabel("Razón")
    ax.set_ylabel("Frecuencia")
    ax.legend()
    st.pyplot(fig)
