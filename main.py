from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import *
from tkinter import ttk, font
import time
import threading
from turtle import color
from numpy import False_
import serial

root = tk.Tk()
root.title('Tercera entrega')
root.resizable(height=False, width=False)

data = ''
recibido = ''
selector = ''
comando = ''
comandoPantallaNuevo = ''
indexEspecifico=''
# --------------Configuración Serial----------------


def timer():
    global data
    global recibido
    global selector
    global comandoPantallaNuevo
    global indexEspecifico

    while True:
        nucleo = serial.Serial('COM3', 115200)
        rawString = str(nucleo.readline())
        rawString = rawString.strip("b'\.n")  # Ya tengo mi valor @Data# limpio
        # Limpieza y verificación del dato en Serial
        if(rawString.count('@') == 1) and (rawString.count('#') == 1):
            data = rawString.strip("@#")
            recibido = data
            print(data)
        print(rawString)

        ##

        register = Text(registerFrame, height=10, width=25, font=font.Font(
            family="Verdana", size=11,
        ))
        register.insert(INSERT, recibido)
        register.grid(
            row=2, column=0, columnspan=2, pady=10, padx=10)

        ##

        if selector == 'w' or comandoPantallaNuevo == 'S3L':  # ADC
            nucleo.write(b'w')
            selector = 0
            print('entre')

        elif selector == '@' or comandoPantallaNuevo == 'S3O' or comandoPantalla == 'S3A':  # LED
            nucleo.write(b'@')
            selector = 0
            print('entre')

        elif selector == 'r' or comandoPantallaNuevo == 'S1G':  # RTC
            nucleo.write(b'r')
            selector = 0
            print('entre')

        elif selector == 'e' or comandoPantallaNuevo == 'S2E':  # BorrarTodo
            nucleo.write(b'e')
            selector = 0
            print('entre')
####----------------------Especifico
        elif selector == '1' or comandoPantallaNuevo == 'S21':  # Especifico
            nucleo.write(b'1')
            selector = 0
            print('entre')

        elif selector == '2' or comandoPantallaNuevo == 'S22':  # Especifico
            nucleo.write(b'2')
            selector = 0
            print('entre')

        elif selector == '3' or comandoPantallaNuevo == 'S23':  # Especifico
            nucleo.write(b'3')
            selector = 0
            print('entre3')

        elif selector == '4' or comandoPantallaNuevo == 'S24':  # Especifico
            nucleo.write(b'4')
            selector = 0
            print('entre')

        elif selector == '5' or comandoPantallaNuevo == 'S25':  # Especifico
            nucleo.write(b'5')
            selector = 0
            print('entre')

#################
        elif selector == 't' or comandoPantallaNuevo == 'S2T':  # LeerTodo
            nucleo.write(b't')
            selector = 0
            print('entre')

        comandoPantallaNuevo = ''
        nucleo.close()
        time.sleep(0.1)  # 100ms


t = threading.Thread(target=timer)
t.start()


def obtenerCommand():
    global comandoPantalla
    global comandoPantallaNuevo
    comandoPantallaNuevo = comandoPantalla.get()
    print(comandoPantallaNuevo)


def test():
    print('me llamaron')


def OnOffLed():
    global selector
    selector = '@'

def ADC():
    global selector
    selector = 'w'

def leerTodo():
    global selector
    selector = 't'

def borrarTodo():
    global selector
    selector = 'e'

def datoEspecifico():
    global selector
    global indexCombo
    global indexEspecifico
    indexEspecifico = indexCombo.get()
    selector = indexEspecifico
    print(indexEspecifico)

# ------------------------Configuracion inicial de frames -------
buttonsFrame = tk.Canvas(root, width=350, height=200, bg='Light gray')
buttonsFrame.grid(row=0, column=0)
registerFrame = tk.Canvas(root, width=350, height=275, bg='Light gray')
registerFrame.grid(row=0, column=1)

# ---------------------Se establace la posicion de los botones----------
botonSaveInfo = Button(buttonsFrame, text='ENTREGA TRES', font=font.Font(
    family="Verdana", size=8
), width=28).grid(
    row=0, column=0, padx=5, pady=15, columnspan=2)
botonReadInfo = Button(buttonsFrame, text='Leer datos de la EEPROM',command=leerTodo, font=font.Font(
    family="Verdana", size=8
), width=28).grid(
    row=1, column=0, padx=5, pady=10, columnspan=2)
botonReadInfoEspecifico = Button(buttonsFrame, text='Dato especifico',command=datoEspecifico, font=font.Font(
    family="Verdana", size=8
), width=12).grid(
    row=2, column=0, padx=10, pady=15)
indexCombo=StringVar();
combo = Entry(buttonsFrame,textvariable=indexCombo, width=12).grid(row=2, column=1)

botonOffLed = Button(buttonsFrame, text='ON|OFF LED', command=OnOffLed, font=font.Font(
    family="Verdana", size=8
), width=12).grid(
    row=3, column=0, padx=8, pady=15)
borrar = Button(buttonsFrame, text='Borrar EEPROM',command=borrarTodo, font=font.Font(
    family="Verdana", size=8
), width=12).grid(
    row=3, column=1, padx=8, pady=15)
botonReadADC = Button(buttonsFrame, text='Leer ADC', command=ADC, font=font.Font(
                      family="Verdana", size=8
                      ), width=28).grid(
    row=4, column=0, padx=5, pady=15, columnspan=2)

# -----------------------Se establese el frame de registros y entrada de comandos

tk.Label(registerFrame, text='Comando:', bg='Light gray').grid(
    row=0, column=0, pady=10, padx=20)

label = Label(registerFrame, text='COMANDO:')
label.grid(row=0, column=0, pady=10, padx=8)
label.config(fg="Black", bg='Light gray', font=("Verdana", 12), justify='left')

comandoPantalla = StringVar()
entry = Entry(registerFrame, textvariable=comandoPantalla,
              font=font.Font(
                  family="Verdana",
                  size=11,
                  # weight=font.BOLD,   # Negrita.
                  slant=font.ITALIC,  # Cursiva.
                  overstrike=False,    # Tachado.
                  underline=False      # Subrayado.
              ), width=11,
              ).grid(row=0, column=1, padx='5')

botonComand = Button(registerFrame, text='Enviar comando',
                     width=33, command=obtenerCommand, font=font.Font(
                         family="Verdana", size=8,
                     )).grid(row=1, column=0, columnspan=2)
# entryComand.bind('<Return>', test())  # ('<Return>',funcionALlamar)

register = Text(registerFrame, height=10, width=25, font=font.Font(
    family="Verdana", size=11,))
register.grid(
    row=2, column=0, columnspan=2, pady=10, padx=10)

# start()
root.mainloop()
