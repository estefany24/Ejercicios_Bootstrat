import numpy as np
import matplotlib.pyplot as plt

def mediana_percentiles_bootstrap(data, num_bootstrap=1000, ci=95):
    n = len(data)
    medianas = []
    p25s = []
    p75s = []
    
    for _ in range(num_bootstrap):
        muestra = np.random.choice(data, size=n, replace=True)
        medianas.append(np.median(muestra))
        p25s.append(np.percentile(muestra, 25))
        p75s.append(np.percentile(muestra, 75))
    
    def intervalo(valores):
        li = np.percentile(valores, (100 - ci) / 2)
        ls = np.percentile(valores, 100 - (100 - ci) / 2)
        return li, ls

    return {
        "mediana": (np.median(data), medianas, *intervalo(medianas)),
        "p25": (np.percentile(data, 25), p25s, *intervalo(p25s)),
        "p75": (np.percentile(data, 75), p75s, *intervalo(p75s)),
    }

def mostrar_resultado():
    import streamlit as st

    datos = [2.5, 3.2, 2.8, 3.5, 2.9, 3.1, 2.7, 3.4, 3.0, 3.3,
             2.6, 3.6, 2.9, 3.2, 2.8, 3.1, 2.7, 3.3, 3.0, 2.9]

    resultados = mediana_percentiles_bootstrap(datos)

    st.subheader("📊 Mediana y Percentiles con Bootstrap")
    st.write("Datos de ingresos mensuales (en miles):", datos)

    for nombre, (valor, distribucion, li, ls) in resultados.items():
        st.write(f"🔹 {nombre.upper()}")
        st.write(f"  Valor muestral: {valor:.2f}")
        st.write(f"  Intervalo de Confianza del 95%: ({li:.2f}, {ls:.2f})")
        
        fig, ax = plt.subplots()
        ax.hist(distribucion, bins=30, color='plum', edgecolor='black')
        ax.axvline(li, color='red', linestyle='--', label='Límite Inferior')
        ax.axvline(ls, color='green', linestyle='--', label='Límite Superior')
        ax.axvline(valor, color='blue', linestyle='-', label='Valor Muestral')
        ax.set_title(f"Distribución Bootstrap: {nombre.upper()}")
        ax.set_xlabel(nombre)
        ax.set_ylabel("Frecuencia")
        ax.legend()
        st.pyplot(fig)
