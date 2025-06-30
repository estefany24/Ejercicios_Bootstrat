import numpy as np
import matplotlib.pyplot as plt

def bootstrap_parametrico_exponencial(data, num_bootstrap=1000, ci=95):
    # Estimación de lambda con MLE
    lambda_muestral = 1 / np.mean(data)
    n = len(data)

    lambdas = []
    medias = []

    for _ in range(num_bootstrap):
        # Generar datos con distribución exponencial
        muestra = np.random.exponential(scale=1/lambda_muestral, size=n)
        lambda_est = 1 / np.mean(muestra)
        media_est = np.mean(muestra)
        lambdas.append(lambda_est)
        medias.append(media_est)

    def intervalo(valores):
        li = np.percentile(valores, (100 - ci) / 2)
        ls = np.percentile(valores, 100 - (100 - ci) / 2)
        return li, ls

    return {
        "lambda": (lambda_muestral, lambdas, *intervalo(lambdas)),
        "media": (np.mean(data), medias, *intervalo(medias)),
    }

def mostrar_resultado():
    import streamlit as st

    datos = [145, 167, 132, 178, 156, 143, 189, 134, 165, 152,
             171, 148, 163, 139, 175]

    resultados = bootstrap_parametrico_exponencial(datos)

    st.subheader("📉 Bootstrap Paramétrico (Exponencial)")
    st.write("Datos (tiempo hasta el fallo en días):", datos)

    for nombre, (valor, distribucion, li, ls) in resultados.items():
        etiqueta = "λ (tasa de fallo)" if nombre == "lambda" else "Vida media"
        st.write(f"🔹 {etiqueta}")
        st.write(f"  Estimación muestral: {valor:.3f}")
        st.write(f"  Intervalo de confianza del 95%: ({li:.3f}, {ls:.3f})")

        fig, ax = plt.subplots()
        ax.hist(distribucion, bins=30, color='khaki', edgecolor='black')
        ax.axvline(li, color='red', linestyle='--', label='Límite Inferior')
        ax.axvline(ls, color='green', linestyle='--', label='Límite Superior')
        ax.axvline(valor, color='blue', linestyle='-', label='Valor estimado')
        ax.set_title(f"Distribución Bootstrap de {etiqueta}")
        ax.set_xlabel(etiqueta)
        ax.set_ylabel("Frecuencia")
        ax.legend()
        st.pyplot(fig)
