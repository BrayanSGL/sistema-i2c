# Interfaz gráfica para el control de 3 escalvos

> A continuación se explica a detalle el código de la tarjeta Nucleo L476RG y el del monitor (computadora).

## Código para tarjeta Nucleo L476RG (Manejo de los 3 esclavos)
Este proyecto consiste en un código escrito en C++ para utilizar en la tarjeta Nucleo L476RG con el objetivo de realizar diferentes acciones mediante la comunicación I2C y el puerto serial.

### Requisitos previos
Para poder utilizar este código es necesario tener instalado:

- Mbed CLI
- La librería mbed para trabajar con la tarjeta Nucleo L476RG
- La librería I2C para realizar la comunicación I2C entre dispositivos

### Descripción del código
El código incluye las siguientes funcionalidades:

- Lectura y escritura de la hora y fecha del reloj DS3231 mediante la comunicación I2C
- Lectura y escritura de datos en la memoria EEPROM mediante la comunicación I2C
- Recepción de comandos a través del puerto serial para encender el led, leer el voltaje del ADC o leer un dato específico de la memoria EEPROM

### Instrucciones de uso

Para utilizar este código, sigue estos pasos:

1. Conecta la tarjeta Nucleo L476RG a tu computadora mediante un cable USB
2. Abre una terminal y utiliza Mbed CLI para compilar y cargar el código en la tarjeta
3. Utiliza un programa como PuTTY o HyperTerminal para enviar comandos al puerto serial de la tarjeta
4. Presiona el botón conectado a la entrada PC_9 para leer y escribir la hora y fecha en la memoria EEPROM

### Códigos de comandos
Los comandos disponibles son:

- w: lee el voltaje del ADC y lo muestra en el puerto serial
- @: enciende el led conectado a la salida LED1
- 1, 2, 3, 4, 5, 6, 7, 8, 9, 0: lee el dato correspondiente al bloque indicado de la memoria EEPROM y lo muestra en el puerto serial. Por ejemplo, el comando 2 leería el segundo bloque de la memoria EEPROM.

## Código en python (Monitoreo de datos)
Este código se utiliza para monitorear y controlar distintos aspectos de un sistema a través de una interfaz gráfica de usuario (GUI) creada con Tkinter y de una conexión serial con otro dispositivo.

### Requisitos
Para utilizar este código, se deben cumplir los siguientes requisitos:

- Tener instalado Python 3.
- Tener instaladas las librerías tkinter, serial y numpy.
- Contar con un puerto serial disponible y conocer su nombre de puerto (en este caso, se utiliza 'COM3').
- Contar con el dispositivo al que se desea conectarse por medio del puerto serial y conocer los comandos necesarios para controlarlo.

### Uso
Para ejecutar este código, se debe abrir una consola y utilizar el comando python `main.py`. Esto abrirá la GUI de la aplicación.

La GUI incluye diversos botones y entradas de texto para enviar comandos y recibir y visualizar datos. Algunas de las funcionalidades disponibles son:

- Monitoreo y control del ADC del dispositivo.
- Encendido y apagado del LED del dispositivo.
- Consulta y configuración del reloj del dispositivo.
- Borrado de todos los datos almacenados en el dispositivo.
- Consulta y eliminación de datos específicos almacenados en el dispositivo.
- Monitoreo de la temperatura y humedad del dispositivo.

### Personalización
Este código puede ser personalizado para adaptarse a distintos sistemas y dispositivos, modificando los comandos utilizados para controlar dicho dispositivo y la estructura de los datos recibidos. También se pueden agregar o eliminar funcionalidades de la GUI según sea necesario.
