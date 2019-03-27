
from pandas import pandas as pd
from matplotlib import pyplot as plt
from flask import Response
import numpy as np
import json
import os
import requests
  
r=requests.get('http://api.wahrungsrechner.org/v1/full/EUR/json?key=1881|hTayEgZ3xeee6SRdw3e~ZCvd9hmiA4iS')
Usd=requests.get('http://api.wahrungsrechner.org/v1/full/USD/json?key=1881|hTayEgZ3xeee6SRdw3e~ZCvd9hmiA4iS')
url = 'http://api.wahrungsrechner.org/v1/full/EUR/json?key={1881|hTayEgZ3xeee6SRdw3e~ZCvd9hmiA4iS}'


#d=pd.read_json(r)
respuesta = r.json()
t2=Usd.json()
#print(t2)
rate = respuesta['result']['conversion'][30]['rate']
UsdtoCop= t2['result']['conversion'][30]['rate']
EuroDivisacolombiana=respuesta['result']['conversion'][30]['rate']
UsdToEU=t2['result']['conversion'][43]['rate']

print(EuroDivisacolombiana)
#data = pd.read_csv('Tasa_representativa_del_Mercado.csv', header=0)



# print(data)

#x = data['VALOR']
#y = data['VIGENCIADESDE']


#plt.plot(x, y, 'ro')
#plt.xlabel('Valor del dolar')
#plt.ylabel('Vigencia')


#plt.show


#def listadoDolar():
 #   datosDolar = []
#
 #   headers = {
  #      'content-type': 'json'
   ##df = pd.read_csv(url)
#
 #   for i in range(0, len(df)):
 #       datosDolar.append(float(df['VALOR'][i]), str(df['VIGENCIADESDE'][i]))
#
  #  datosDolar_json = json.dumps([ob.__dict__ for ob in datosDolar])
   # return Response(datosDolar_json, mimetype="json")
