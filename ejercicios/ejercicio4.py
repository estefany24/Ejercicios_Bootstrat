import numpy as np
import matplotlib.pyplot as plt

def correlacion_bootstrap(x, y, num_bootstrap=1000, ci=95):
    n = len(x)
    correlaciones = []
    for _ in range(num_bootstrap):
        indices = np.random.choice(range(n), size=n, replace=True)
        muestra_x = [x[i] for i in indices]
        muestra_y = [y[i] for i in indices]
        corr = np.corrcoef(muestra_x, muestra_y)[0, 1]
        correlaciones.append(corr)

    li = np.percentile(correlaciones, (100 - ci) / 2)
    ls = np.percentile(correlaciones, 100 - (100 - ci) / 2)
    return np.corrcoef(x, y)[0, 1], correlaciones, li, ls

def mostrar_resultado():
    import streamlit as st

    horas = [2, 4, 3, 5, 1, 6, 3, 4, 2, 5, 7, 3, 4, 6, 2]
    notas = [65, 78, 72, 85, 58, 88, 70, 79, 63, 82, 92, 68, 75, 86, 61]

    correlacion, distribucion, li, ls = correlacion_bootstrap(horas, notas)

    st.subheader("📈 Correlación entre Horas de Estudio y Notas")
    st.write("Horas de estudio:", horas)
    st.write("Calificaciones:", notas)
    st.write(f"Correlación muestral: {correlacion:.3f}")
    st.write(f"Intervalo de Confianza del 95%: ({li:.3f}, {ls:.3f})")

    fig, ax = plt.subplots()
    ax.hist(distribucion, bins=30, color='lightblue', edgecolor='black')
    ax.axvline(li, color='red', linestyle='--', label='Límite Inferior')
    ax.axvline(ls, color='green', linestyle='--', label='Límite Superior')
    ax.axvline(0, color='black', linestyle=':', label='Sin correlación')
    ax.set_title("Distribución Bootstrap del Coeficiente de Correlación")
    ax.set_xlabel("Correlación")
    ax.set_ylabel("Frecuencia")
    ax.legend()
    st.pyplot(fig)
