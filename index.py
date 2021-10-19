from os import replace
import re
from flask import Flask, render_template,request,flash
from flask.json import jsonify
import random

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

BUZZ = 10

def movimiento_brawmiano(x,y):
    dx = random.gauss(0, BUZZ)
    dy = random.gauss(0, BUZZ)
    y = int(y)+dy
    x = int(x)+dx
    if 680<x<710 :
        x = 640
    if -10<x<20:
        x = 40
    if -10<y<20 :
        y = 40
    if 480<y<510:
        y = 440
    return x,y

def dividir():
    probabilidad = random.gauss(0,100)
    if probabilidad >=70:
        return True
    return False

##Enrutamiento de directorio raiz retorna pagina home
@app.route('/', methods=['POST','GET'])
def home():
    return render_template('home.html')

##Enrutamento para conexión http
@app.route('/comunicacion',  methods=['POST','GET'])
def respuesta():
    ##Verificación de la petición POST
    if request.method == 'POST':
        ##Se obtiene el JSON enviado
        request_data = request.get_json()
        ##Se separa en los datos de interes
        cord_x = request_data.get('cord_x')
        cord_y = request_data.get('cord_y')
        
        ##Se imprime en consola de servido para verificar
        ##print("Cordenadas:",cord_x,cord_y)
        ##Incremento de coodenadas para simular movimiento
        cont=0
        for i in range(len(cord_y)+cont):
            cord_x[i],cord_y[i]=movimiento_brawmiano(cord_x[i],cord_y[i])
            if dividir():
                cord_x.append(cord_x[i]+10)
                cord_y.append(cord_y[i])
    ##Retorno de la petición POST; se regresan coordenadas actualizadas en un JSON
    return  jsonify({"cord_y":cord_y,"cord_x":cord_x})

##Incio del servidor
if __name__ == '__main__':
    app.run(debug = True)   

