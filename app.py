from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/ejercicio3')
def ejercicio3():
    return render_template('ejercicio3.html')

@app.route('/ejercicio4')
def ejercicio4():
    return render_template('ejercicio4.html')

@app.route('/ejercicio5')
def ejercicio5():
    return render_template('ejercicio5.html')

if __name__ == '__main__':
    # Para desarrollo local
    app.run(debug=True)
else:
    # Para servidor de producción
    app.debug = False