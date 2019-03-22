from flask import Flask
app = Flask(__name__)

from flask import request
from flask import render_template


@app.route('/')
def index():
	 name ='Yeisson'
	 return render_template("index.html",name=name)


@app.route('/client')
def client():
	list_name=["t1","t2","t3"]
	return render_template("client.html",list= list_name)




#@app.route('/usuarios/<name>')
#def usuario(name="yeisson"):
#	age=19
#	lista_edad=[1,2,3,4,5]
#	return render_template("index.html", nombre=name,age=age,lista=lista_edad)

#@app.route("/params/")
#@app.route("/params/<name>")#ruta de acceso
#def params(name="default"):
#	param=request.args.get("params1","no contiene parametro")
#	return " el parametro es {} ".format(name)#peticion de parametro 

	

app.run(debug =True ,port = 5000)    