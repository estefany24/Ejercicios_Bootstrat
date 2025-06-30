import numpy as np
import matplotlib.pyplot as plt

def regresion_bootstrap(x, y, num_bootstrap=1000, ci=95):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    
    betas_0 = []
    betas_1 = []

    for _ in range(num_bootstrap):
        indices = np.random.choice(n, size=n, replace=True)
        x_sample = x[indices]
        y_sample = y[indices]
        
        X = np.vstack([np.ones_like(x_sample), x_sample]).T
        beta = np.linalg.lstsq(X, y_sample, rcond=None)[0]
        betas_0.append(beta[0])
        betas_1.append(beta[1])
    
    def intervalo(valores):
        li = np.percentile(valores, (100 - ci) / 2)
        ls = np.percentile(valores, 100 - (100 - ci) / 2)
        return li, ls

    # Cálculo con datos reales
    X_real = np.vstack([np.ones_like(x), x]).T
    beta_real = np.linalg.lstsq(X_real, y, rcond=None)[0]

    return {
        "b0": (beta_real[0], betas_0, *intervalo(betas_0)),
        "b1": (beta_real[1], betas_1, *intervalo(betas_1)),
    }

def mostrar_resultado():
    import streamlit as st

    x = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    y = [23, 28, 35, 41, 46, 52, 58, 63, 69, 74]

    resultados = regresion_bootstrap(x, y)

    st.subheader("📈 Bootstrap en Regresión Lineal")
    st.write("Publicidad (X):", x)
    st.write("Ventas (Y):", y)

    for nombre, (valor, distribucion, li, ls) in resultados.items():
        etiqueta = r"$\beta_0$ (intercepto)" if nombre == "b0" else r"$\beta_1$ (pendiente)"
        st.write(f"🔹 {etiqueta}")
        st.write(f"  Valor estimado: {valor:.3f}")
        st.write(f"  Intervalo de confianza del 95%: ({li:.3f}, {ls:.3f})")

        fig, ax = plt.subplots()
        ax.hist(distribucion, bins=30, color='lightsteelblue', edgecolor='black')
        ax.axvline(li, color='red', linestyle='--', label='Límite Inferior')
        ax.axvline(ls, color='green', linestyle='--', label='Límite Superior')
        ax.axvline(valor, color='blue', linestyle='-', label='Valor estimado')
        ax.set_title(f"Distribución Bootstrap de {etiqueta}")
        ax.set_xlabel(etiqueta)
        ax.set_ylabel("Frecuencia")
        ax.legend()
        st.pyplot(fig)
