from flask import Flask
from flask import request
from flask import render_template
import Tablas_de_divisas as td
import forms


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    
	
    title = " Tu divisa"

    return render_template("index.html", title=title)


@app.route('/Tabla_dolar')
def client():

    x = td.x
    y = td.y
    return render_template("pruebagraf.html", x=x, y=y)


def sumar(val1,val2):
	
	total= val1+val2
	return total


app.run(debug=True, port=5000)
