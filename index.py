from os import replace
import re
from flask import Flask, render_template,request,flash
from flask.json import jsonify




app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['POST','GET'])
def home():

    #Recepción de datos por metodo POST
    
        
    ## Retorno de pagina HTML 
    return render_template('home.html')

@app.route('/comunicacion',  methods=['POST','GET'])
def respuesta():
    if request.method == 'POST':
        request_data = request.get_json()
        cord_x = request_data.get('cord_x')
        cord_y = request_data.get('cord_y')
        print("Cordenadas:",cord_x,cord_y)
        for i in range(len(cord_y)):
            cord_y[i] = int(cord_y[i])
            cord_x[i] = int(cord_x[i])+5
        
    return  jsonify({"cord_y":cord_y,"cord_x":cord_x})

if __name__ == '__main__':
    app.run(debug = True)   

