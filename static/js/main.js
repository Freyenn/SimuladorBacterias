window.cord_x = []
window.cord_y = []


function dibujar_circulo(x,y,color){
    ctx.beginPath();
    ctx.arc(x,y,10,0, 2 * Math.PI);
    ctx.fillStyle = color
    ctx.fill();
}

function getPosition(event){
    var rect = canvas.getBoundingClientRect();
    var x = event.clientX - rect.left;
    var y = event.clientY - rect.top;
    dibujar_circulo(x,y);
}

function oMousePos(canvas, evt) {
    var ClientRect = canvas.getBoundingClientRect();
    return { //objeto
      x: Math.round(evt.clientX - ClientRect.left),
      y: Math.round(evt.clientY - ClientRect.top)
    }
  }

function marcarCoords(output, x, y) {
    output.innerHTML = ("x: " + x + ", y: " + y);
    output.style.top = (y + 20) + "px";
    output.style.left = (x + 20) + "px";
    output.style.backgroundColor = "#FFF";
    output.style.border = "1px solid #d9d9d9"
   
  } 

  function limpiarCoords(output) {
    output.innerHTML = "";
    output.style.top = 0 + "px";
    output.style.left = 0 + "px";
    output.style.backgroundColor = "transparent"
    output.style.border = "none";
    
  }

   async function envio(){
    
        
        
  }

  function task(i) {
    setTimeout(function() {
        console.log(i);
    }, 2000 * i);
  }

  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  window.onload = function(){
    cv = document.getElementById("dibujo");
    ctx = cv.getContext("2d");
    var output = document.getElementById("output");
    btn_avanzar = document.getElementById("btn_avanzar");

    btn_avanzar.onclick = async function(){
        console.log("Cordenadas:", window.cord_x,window.cord_y);
        i=0;
        
        while(i<=20){
            // Proceso de encoding para datos 
        var datos = { 
            cord_x: window.cord_x,
            cord_y: window.cord_y,
        };

        var init = {
            // el método de envío de la información será POST
            method: "POST",
            headers: { // cabeceras HTTP
                // vamos a enviar los datos en formato JSON
                'Content-Type': 'application/json'
            },
            // el cuerpo de la petición es una cadena de texto
            // con los datos en formato JSON
            body: JSON.stringify(datos) // convertimos el objeto a texto
            };

            url='/comunicacion'
            let response = await fetch(url,init);
            data = await response.json();

            cord_x_resp = data.cord_x
            cord_y_resp = data.cord_y
            
            window.cord_x = cord_x_resp
            window.cord_y = cord_y_resp

            console.log(cord_x_resp,cord_y_resp)
            i++;
            ctx.clearRect(0,0,cv.width,cv.height)
            dibujar_circulo(cord_x_resp[0],cord_y_resp[0],"green");
            await delay(200);
            
        }
    }

    cv.ondblclick =  function(event){
        var rect = cv.getBoundingClientRect();
        x = event.clientX- rect.left;
        y = event.clientY- rect.top;

        window.cord_x.push(x)
        window.cord_y.push(y)

        dibujar_circulo(x,y,"green");
    }

    cv.onmousemove = function(event){
        var mousePos = oMousePos(cv, event); 
        marcarCoords(output, mousePos.x, mousePos.y)
    }

    cv.onmouseout = function(event){
        limpiarCoords(output);  
    }
  }