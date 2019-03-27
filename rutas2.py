from flask import Flask
from flask import request
from flask import render_template
import Tablas_de_divisas as td
import forms
from flask import request
from flask import jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    #x=1881|hTayEgZ3xeee6SRdw3e~ZCvd9hmiA4iS
    #r=requests.get('http://api.wahrungsrechner.org/v1/quotes/THB/EUR/json?qty=1&key={1881|hTayEgZ3xeee6SRdw3e~ZCvd9hmiA4iS}')
    UsdtoCop=td.UsdtoCop
    eurotoCol=td.EuroDivisacolombiana
    usdtoEu=td.UsdToEU
    return render_template("index.html",eurotoCol=eurotoCol,UsdtoCop=UsdtoCop,usdtoEu=usdtoEu)


@app.route('/pruebagraf.html')
def client():

    
    return render_template("pruebagraf.html")


@app.route('/inversion.html', methods=['GET', 'POST'])
def inversion():

    title = " Tu divisa"

    return render_template("inversion.html", title=title)
app.run(debug=True, port=5000)
