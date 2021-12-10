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
