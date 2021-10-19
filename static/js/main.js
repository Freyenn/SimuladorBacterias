//Variables globales en JS(similar a un self de python)
window.cord_x = [];
window.cord_y = [];
window.datos = [];
window.etiquetas = [];




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
  ctx.arc(x, y, 7, 0, 2 * Math.PI);
  ctx.fillStyle = "black";
  ctx.fill();
  ctx.closePath();
  ctx.beginPath();
  ctx.arc(x, y, 5, 0, 2 * Math.PI);
  ctx.fillStyle = color;
  ctx.fill();
  ctx.closePath();
}

//Funcion encargada de obtener las coordenadas del mouse dentro del canvas
function oMousePos(canvas, evt) {
  var ClientRect = canvas.getBoundingClientRect();
  return {
    //objeto
    x: Math.round(evt.clientX - ClientRect.left),
    y: Math.round(evt.clientY - ClientRect.top),
  };
}

//Funcion encargada de marcar las coordenadas en un recuadro cerca del raton
function marcarCoords(output, x, y) {
  output.innerHTML = "x: " + x + ", y: " + y;
  output.style.top = y + 20 + "px";
  output.style.left = x + 20 + "px";
  output.style.backgroundColor = "#FFF";
  output.style.border = "1px solid #d9d9d9";
}

//Funcion encargada de limpiar las coordenadas en el recuadro cerca del raton
function limpiarCoords(output) {
  output.innerHTML = "";
  output.style.top = 0 + "px";
  output.style.left = 0 + "px";
  output.style.backgroundColor = "transparent";
  output.style.border = "none";
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
  cnt_elementos = document.getElementById("cnt_elementos");

  //Funcion ejecutada al presionar el boton avanzar
  btn_avanzar.onclick = async function () {
    //Se escribe en consola las coordenadas de todos los puntos dibujados
    console.log("Cordenadas:", window.cord_x, window.cord_y);
    //bucle para realizar avance del circulo dibujado
    i = 0;
    while (i <= 30) {
      // Proceso de encoding para datos
      var datos = {
        cord_x: window.cord_x,
        cord_y: window.cord_y,
        
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

      //Se actualizan los valores globales de coordenadas
      window.cord_x = cord_x_resp;
      window.cord_y = cord_y_resp;

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
     await delay(100);
    }
  };

  //Función responsiba al doble click sobre el canvas
  cv.ondblclick = function (event) {
    var rect = cv.getBoundingClientRect();
    x = event.clientX - rect.left;
    y = event.clientY - rect.top;

    window.cord_x.push(x);
    window.cord_y.push(y);

    dibujar_circulo(x, y, "green");
  };

  //Función responsiva al movimiento del raton sobre el canvas
  cv.onmousemove = function (event) {
    var mousePos = oMousePos(cv, event);
    marcarCoords(output, mousePos.x, mousePos.y);
  };

  //Funcion responsiva al quitar el raton del canvas
  cv.onmouseout = function (event) {
    limpiarCoords(output);
  };
};
/////////////////////////////////////////////Termino Funciones onload/////////////////////////////////////////////////////////////////////////
