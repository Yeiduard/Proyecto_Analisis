
from pandas import pandas as pd
from matplotlib import pyplot as plt
from flask import Response
import numpy as np
import json


url = 'https://www.datos.gov.co/resource/g3ab-sax9.json'



data = pd.read_csv('Tasa_representativa_del_Mercado.csv', header=0)
# print(data)

x = data['VALOR']
y = data['VIGENCIADESDE']


plt.plot(x, y, 'ro')
plt.xlabel('Valor del dolar')
plt.ylabel('Vigencia')


plt.show


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
