# SimuladorBacterias
Simulador de Bacterias desarrollado usando python, html y js

En este repositorio se encuentran los archivos generados para el simulador bacteriano desarrollado a lo largo del curso de Inteligencia Artificial de la Maestría en ingeniería Electrónica de la Benemérita Universidad Autónoma de Puebla.

El simulador desarrollado permite observar el crecimiento bacteriano de E. Coli en diferentes condiciones de temperatura y con diferentes cantidades de alimento disponible en el medio de cultivo. 

# ¿Cómo usarlo?
Para ejecutar el simulador de forma local es necesario contar con Python 3.9.7 o superior. Se recomienda utilizar Visual Studio Code pero cualquier editor de codigo de su preferencia es util. 
El archivo princial es:
- *index.py*

A traves de este archivo se inicializa el servidor local para realizar la prueba del simulador, se puede acceder desde cualquier navegador en *http://localhost:5000*.

El archivo HTML principal se encuentra en */templates/home.html* dentro de este repositorio. En la Sección */static* se encuentran los archivos CSS en */static/CSS*, JavaScript en */static/JS* e imagenes en */static/img*.

Por ultimo en la raíz del repositorio se encuentra el archivo -*bacteia.py* el cual corresponde a la entidad agente que se utiliza para realizar la simulación, esta contiene todas las rutinas que realiza la bacteria para moverse, comer, dividirse y morir.

## Propiedades del Agente

| Nombre | Descripción | Tipo de dato |
| ------------- | ------------- |------------- |
| Self.X | Valor en posición X | Entero |
| Self.Y | Valor en posición Y | Entero |
| Self.Estado | Estado de vida | Booleano |
| Self.EstadoDiv | Bandera para realizar división | Booleano |

## Memoria del Agente

| Nombre | Descripción | Tipo de dato |
| ------------- | ------------- |------------- |
| Self.dupTick | Ticks necesarios para dividirse | Entero |
| Self.contadorTick | Conteo de ticks | Entero |
| Self.Alimento | Cantidad de alimento ingerido | Flotante |

# Funcionamiento

En la figura 1 se muestra el diagrama de flujo del funcionamiento para el simulador. Donde la simulación no se inicia hasta que se presiona un botón de inicio. Cuando este botón es presionado se procede a crear las bacterias iniciales, mientras no se presione el botón de paro la simulación sigue en ejecución para ello, se evalúa cada bacteria sí esta bacteria se divide se añade una nueva bacteria a la lista y se procede a evaluar la siguiente, cuando no quedan bacterias por evaluar se re-dibujan las bacterias y se repite el procedimiento.

<img src="https://github.com/Freyenn/SimuladorBacterias/blob/main/static/img/flujo_1.png" width="1000" >
Figura 1.- Diagrama de flujo del simulador.

Para evaluar a la bacteria primero es necesario comprobar si esta vive o muere, en caso de que muera no se realiza ninguna acción y termina la evaluación. Por el contrario si vive, se realiza un movimiento, se alimenta y se genera o no una división. En la figura 2 se muestra el diagrama de flujo correspondiente a este proceso. 

<img src="https://github.com/Freyenn/SimuladorBacterias/blob/main/static/img/flujo_2.jpg" width="500" >
Figura 2.- Diagrama de flujo del bloque evaluar bacteria.

Para evaluar si vive o muere se comprueba la cantidad de alimento que tiene el agente en su memoria, si esta cantidad es menor que el parámetro establecido se asigna al parámetro Estado un False siendo así que se considera que la bacteria muere, caso contrario se asigna un True para marcarla como viva, en la figura 3 se muestra el diagrama para este proceso.

<img src="https://github.com/Freyenn/SimuladorBacterias/blob/main/static/img/flujo_vivir.jpg" width="300" >
Figura 3.- Diagrama de flujo del bloque evaluar si vive o muere la bacteria.

En la figura 4 se encuentra el diagrama de flujo para el movimiento del agente, el cual se realiza creando un dx y un dy con un numero aleatorio pequeño, estos se suman con la propiedad X y Y del agente, así al redibujar la bacteria se genera un movimiento.

<img src="https://github.com/Freyenn/SimuladorBacterias/blob/main/static/img/flujo_mov.jpg" width="200" >
Figura 4.- Diagrama de flujo del bloque moverse.

Se tiene el proceso por el cual el agente se alimenta, en este primero se verifica si la cantidad de sustrato actual es mayor a cero, si no lo es decrementa la cantidad de alimento del agente y termina. Si el sustrato es mayor a cero entonces se evalúa cuanto alimento tiene el agente, si este es igual a uno se restablece a cero y se decrementa el sustrato, si no es igual a uno el alimento se incrementa y se procede a decrementar el sustrato, en la figura 5 se encuentra el diagrama correspondiente. Y por ultimo para realizar la división se verifica el contador de ticks es igual a la cantidad de ticks necesarios para la duplicación si esto se cumple se activa la bandera de duplicación si no, se mantiene desactivada, en la figura 6 se tiene el diagrama de flujo.

<img src="https://github.com/Freyenn/SimuladorBacterias/blob/main/static/img/flujo_com.jpg" width="400" >
Figura 5.- Diagrama de flujo del bloque comer.

<img src="https://github.com/Freyenn/SimuladorBacterias/blob/main/static/img/flujo_divi.jpg" width="400" >
Figura 6.- Diagrama de flujo del bloque dividir.

# Más Información
Si desea conocer con mayor detalle el desarrollo de este simulador puede contactarse con cualquiera de los desarrolladores mediante correo electrónico.
- S.E. Ayala-Raggi - saraggi@gmail.com
- L.E. López-García - luis.lopezga@alumno.buap.mx
- J.M. Roa-Escalante - jesus.roae@alumno.buap.mx
