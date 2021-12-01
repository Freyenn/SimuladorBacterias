//Variables globales en JS(similar a un self de python)
window.cord_x = [];
window.cord_y = [];
window.datos = [];
window.etiquetas = [];
window.repetir = "";
window.sustrato = 5000;
window.alimento = [];
window.contador_tick = [];
window.temperatura = 25;
window.primera_vez = [];
window.dup_tick = [];

const rango = document.querySelector("#customRange1")
const texto = document.querySelector("#range_text")

rango.oninput = () =>{
  texto.innerHTML = ": "+rango.value+" s/tick"
}

///////grafica
let miCanvas=document.getElementById("grafica").getContext("2d");

    var chart = new Chart(miCanvas,{
      type:"line",
      data:{
        labels:window.labels,
        datasets:[
          {
            label:"Cantidad",
            backgroundColor:"rgb(0,0,0)",
            data:window.data
          }
        ]
      },
      options: {
                responsive: false,
                plugins: {
                    title: {
                      display: true,
                      text: 'Crecimiento Bacteriano'
                    }
                  },
                  scales: {
                        /* xAxes: [{
                          gridLines: {
                            drawOnChartArea: false
                          }
                      }],
                      YAxes: [{
                        gridLines: {
                          drawOnChartArea: false
                        }
                    }], */
                    x:{
                      grid:{display:false}
                    },
                    y:{
                      grid:{drawBorder:false}
                    },
                    
                  }
            },
      
      
    })

    function updateChart(){
      chart.data.datasets[0].data = window.datos;
      chart.data.labels = window.etiquetas;
      chart.update();
    }
/////////////////////////////////////////////Funciones del canvas////////////////////////////////////////////////////////////
//Funcion encargada de dibujar un circulo en el canvas
function dibujar_circulo(x, y, color) {
  ctx.beginPath();
  ctx.arc(x, y, 3, 0, 2 * Math.PI);
  ctx.fillStyle = "black";
  ctx.fill();
  ctx.closePath();
  ctx.beginPath();
  ctx.arc(x, y, 1, 0, 2 * Math.PI);
  ctx.fillStyle = color;
  ctx.fill();
  ctx.closePath();
}




/////////////////////////////////////////////Finalizan Funciones del canvas////////////////////////////////////////////////////////////

//Funcion encargada de generar un delay entrada en ms
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

/////////////////////////////////////////////Funciones onload/////////////////////////////////////////////////////////////////////////
window.onload = function () {
  //////////Creación de elementos JS a traves de ID's HTML
  cv = document.getElementById("dibujo");
  ctx = cv.getContext("2d");
  var output = document.getElementById("output");
  btn_avanzar = document.getElementById("btn_avanzar");
  btn_parar = document.getElementById("btn_parar");
  cnt_elementos = document.getElementById("cnt_elementos");

  temp = document.getElementById("temp-medio");
  volumen = document.getElementById("volumen");

  btn_parar.onclick = function(){
    window.repetir=false;
  }
  //Funcion ejecutada al presionar el boton avanzar
  btn_avanzar.onclick = async function () {
    //Se escribe en consola las coordenadas de todos los puntos dibujados
    //console.log("Cordenadas:", window.cord_x, window.cord_y);
    //bucle para realizar avance del circulo dibujado
    window.repetir=true

    window.temperatura = parseInt(temp.value)
    window.sustrato = parseInt(volumen.value)

    if (window.temperatura >=48) { window.temperatura=0}
    console.log(window.temperatura)
    i = 0;

    while (window.repetir==true) {
      // Proceso de encoding para datos
      var datos = {
        cord_x: window.cord_x,
        cord_y: window.cord_y,
        sustrato: window.sustrato,
        alimento: window.alimento,
        contador_tick : window.contador_tick,
        temperatura : window.temperatura,
        primera_vez : window.primera_vez,
        dup_tick : window.dup_tick
      };

      var init = {
        // el método de envío de la información será POST
        method: "POST",
        headers: {
          // cabeceras HTTP
          // vamos a enviar los datos en formato JSON
          "Content-Type": "application/json",
        },
        // el cuerpo de la petición es una cadena de texto
        // con los datos en formato JSON
        body: JSON.stringify(datos), // convertimos el objeto a texto
      };

      //url la ruta en la que se realizara la peticion POST
      url = "/comunicacion";
      //Conexión http a traves de fetch
      let response = await fetch(url, init);
      
      //Se espera la respuesta del servidor y se almacena en data; se recibe un JSON
      data = await response.json();

      //Se recuperan los valores para las coordenadas X & Y
      cord_x_resp = data.cord_x;
      cord_y_resp = data.cord_y;
      sustrato_resp = data.sustrato;
      alimento_resp = data.alimento;
      primera_vez_resp = data.primera_vez;
      dup_tick_resp = data.dup_tick;
      contador_tick_resp = data.contador_tick;

      //Se actualizan los valores globales de coordenadas
      window.cord_x = cord_x_resp;
      window.cord_y = cord_y_resp;
      window.sustrato = sustrato_resp;
      window.alimento = alimento_resp;
      window.primera_vez = primera_vez_resp;
      window.dup_tick = dup_tick_resp;
      window.contador_tick = contador_tick_resp;

      //Se imprimen en consola
      //console.log(cord_x_resp, cord_y_resp);
      i++;
      //Se limpia el canvas
      ctx.clearRect(0, 0, cv.width, cv.height);
      //Se dibuja la nueva posicion del circulo
      for (var j = 0; j < cord_x_resp.length; j++) {
        dibujar_circulo(cord_x_resp[j], cord_y_resp[j], "green");
     }
      cnt_elementos.innerHTML ="Cantidad de elementos: " +cord_x_resp.length;
      window.datos.push(cord_x_resp.length);
      window.etiquetas.push(i.toString());
      updateChart();
      
      //Se genera un delay de 200ms entre cada iteración
     await delay(rango.value*1000);
    }
  };

  //Función responsiba al doble click sobre el canvas
  cv.ondblclick = function (event) {
    var rect = cv.getBoundingClientRect();
    console.log("Rect.Left: "+rect.left,"Rect.TOP: "+rect.top)
    console.log("event.clientX: "+event.clientX,"event.clientY: "+event.clientY)
    x = event.clientX - rect.left;
    y = event.clientY - rect.top;
    console.log("X: "+x,"Y: "+y)

    window.cord_x.push(x);
    window.cord_y.push(y);
    window.alimento.push(0);
    window.contador_tick.push(0);
    window.primera_vez.push("True");
    window.dup_tick.push(0);

    dibujar_circulo(x, y, "green");
  };

  //Función responsiva al movimiento del raton sobre el canvas
  
};
/////////////////////////////////////////////Termino Funciones onload/////////////////////////////////////////////////////////////////////////
