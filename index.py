from os import replace
import re
from flask import Flask, render_template,request,flash
from flask.json import jsonify
import random
import sys

from numpy.lib.function_base import append

sys.path.insert(1, 'src/static/python')
from bacteria import bacteria

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


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
        sustrato = request_data.get('sustrato')
        alimento = request_data.get('alimento')
        contador_tick = request_data.get('contador_tick')
        temperatura = request_data.get('temperatura')
        primera_vez = request_data.get('primera_vez')
        dup_tick = request_data.get('dup_tick')
        ##Se imprime en consola de servido para verificar
        ##print("Cordenadas:",cord_x,cord_y)
        
        print("temperatura",temperatura)
        #Instanciación de bacterias
        list_bacterias = []
        estado = []
        for i in range(len(cord_y)):
            list_bacterias.append(bacteria(cord_x[i],cord_y[i],contador_tick[i],temperatura,primera_vez[i],dup_tick[i]))
            

        ##Comportamiento para cada bacteria en cada TICK
        #print("Cantidad de bacterias",len(list_bacterias))
        
        for i in range(len(list_bacterias)):
            cord_x[i],cord_y[i],sustrato,alimento[i],divid,est,primera_vez[i],dup_tick[i],contador_tick[i]=list_bacterias[i].principal(sustrato,alimento[i])
            #cord_x[i],cord_y[i],sustrato,alimento[i]=list_bacterias[i].movimiento_brawmiano()
            #sustrato,alimento[i]=list_bacterias[i].comer(sustrato,alimento[i])
            estado.append(est)


            if divid:
                cord_x.append(cord_x[i]+10)
                cord_y.append(cord_y[i])
                alimento.append(0)
                estado.append(True)
                primera_vez.append(True)
                dup_tick.append(0)
                contador_tick.append(0)

            """ if list_bacterias[i].dividir(alimento[i]):
                cord_x.append(cord_x[i]+10)
                cord_y.append(cord_y[i])
                alimento.append(0) """

        cord_x_temp = [];cord_y_temp = [];alimento_temp=[];estado_temp = []; contador_tick_temp =[]; primera_vez_temp=[]; dup_tick_temp = []     
        
        for i in range(len(estado)):    
            if estado[i]:
                
                    cord_x_temp.append(cord_x[i])
                    cord_y_temp.append(cord_y[i])
                    alimento_temp.append(alimento[i]) 
                    estado_temp.append(estado[i])
                    primera_vez_temp.append(primera_vez[i])
                    dup_tick_temp.append(dup_tick[i])
                    contador_tick_temp.append(contador_tick[i])

        print("Estado len",len(estado))
        print("Estado temp len",len(estado_temp))
        cord_x = cord_x_temp;cord_y=cord_y_temp;alimento=alimento_temp;estado=estado_temp;primera_vez=primera_vez_temp
        dup_tick = dup_tick_temp; contador_tick = contador_tick_temp
                           
    ##Retorno de la petición POST; se regresan coordenadas actualizadas en un JSON
    return  jsonify({"cord_y":cord_y,"cord_x":cord_x,"sustrato":sustrato,"alimento":alimento,"primera_vez":primera_vez,"dup_tick":dup_tick,"contador_tick":contador_tick})

##Incio del servidor
if __name__ == '__main__':
    app.run(debug = True)   

