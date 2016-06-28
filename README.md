# Simulación de Líneas de Espera
## Proyecto Final Métodos Cuantitativos y Simulación

#### Integrantes:
##### Fredele Sentíes Lozano   
- A00343822

##### Eric Reyes Cruz      
- A01228077

##### Ney González Mejía   
- A01224019


### Líneas de Espera
Las líneas de espera son estudiadas por la teoría de colas. Estas se encargan de analizar procesos, generalmente industriales o de servicios, y obtener datos estadísticos a partir de dicho análisis. Los datos obtenidos ayudan a evaluar el costo y eficiencia del sistema.

Los procesos tienen tres componentes básicos:

- Llegadas
- Instalaciones de Servicio
- Línea de Espera

Existen también diversos modelos dentro de estos sistemas, estos utilizan distribuciones distintas y sus fórmulas funcionan ligeramente diferente. Estos modelos pueden variar según su número de ocurrencias, tasa determinística, distribución general y varianza conocidas. Su estructura tiene la siguiente forma:

-Distribución de llegadas/Distribución de tiempo de servicio/Número de canales abiertos

Dicha estructura utiliza letras para representar las distribuciones de probabilidad:

- M = Distribución de Poisson del número de ocurrencias
- D = Tasa constante (determinística)
- G = Distribución general con media y varianza conocidas

### Cálculos

Los cálculos que se pueden obtener de los modelos previamente mostrados son los siguientes:

## P0:

![p0 uno](https://raw.githubusercontent.com/ericreyes/Waiting_Queue/master/1.png)

## L:

![L](https://raw.githubusercontent.com/ericreyes/Waiting_Queue/master/2.png)

## W:

![W](https://raw.githubusercontent.com/ericreyes/Waiting_Queue/master/3.png)

## Lq:

![Lq](https://raw.githubusercontent.com/ericreyes/Waiting_Queue/master/4.png)

## Wq:

![Wq](https://raw.githubusercontent.com/ericreyes/Waiting_Queue/master/5.png)

## Rho:

![Rho](https://raw.githubusercontent.com/ericreyes/Waiting_Queue/master/6.png)


### Datos sobre el Proyecto

Para el presente proyecto, se utilizó el modelo M/M/D. La simulación se creó utilizando el lenguaje de programación Python, utilizando la versión PyQt4 para tener mayor facilidad al crear la interfaz gráfica.

La manera en que se creó la simulación se demuestra en el siguiente diagrama de estados:

![estados](https://raw.githubusercontent.com/ericreyes/Waiting_Queue/master/estados.png)

El proyecto consta de 2 clases:

- `WQ.io`: Clase especializada en la parte gráfica y de diseño del programa
- `project.py`: Clase ejecutable en la que se encuentra la parte lógica del programa

La siguiente imagen es una captura de pantalla del programa corriendo al momento de ejecutarse.

![pantalla normal](https://raw.githubusercontent.com/ericreyes/Waiting_Queue/master/pic.png)

En este se tienen:

- *3 campos de input:*
```
inputLambda
inputMiu
inputServers
```

- *6 etiquetas para las fórmulas*
```
outputP0
outputL
outputW
outputLq
outputWq
outputRo
```
- *2 botones*
```
botonCalcular
botonReset
```
Y

- *1 etiqueta para errores*
```
errorLabel
```

Al ingresar los datos, el programa realiza los cálculos utilizando las fórmulas mencionadas previamente y los arroja en los espacios inferiores. En la parte superior derecha, es donde se genera la simulación gráfica para analizar el comportamiento del sistema de manera más clara. A continuación se muestra una imagen posterior a ingresar valores y obtener los resultados finales:

![Sim](https://raw.githubusercontent.com/ericreyes/Waiting_Queue/master/7.png)

Una vez finalizada, el usuario puede decidir reajustar los valores y continuar realizando cálculos, o simplemente cerrar el programa.
