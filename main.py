import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import threading
import serial

root = tk.Tk()
root.title('Tercera entrega')
root.resizable(height=False, width=False)

# ------------------------Configuracion inicial de frames -------
buttonsFrame = tk.Canvas(root, width=350, height=200, bg='Light gray')
buttonsFrame.grid(row=0, column=0)
registerFrame = tk.Canvas(root, width=350, height=220, bg='Light gray')
registerFrame.grid(row=0, column=1)

# ---------------------Se establace la posicion de los botones----------
botonSaveInfo = Button(buttonsFrame, text='Guardar datos RTC').grid(
    row=0, column=0, padx=5, pady=15,columnspan=2)
botonReadInfo = Button(buttonsFrame, text='Leer datos de la EEPROM').grid(
    row=1, column=0, padx=5, pady=15, columnspan=2)
botonReadInfoEspecifico = Button(buttonsFrame, text='Dato especifico').grid(
    row=2, column=0, padx=10, pady=15)
combo = ttk.Combobox(buttonsFrame,values=["Bloque 1","Bloque 2","Bloque 3","Bloque 4","Bloque 5"],width=5)
combo.grid(row =2, column = 1)
botonOffLed = Button(buttonsFrame, text='Apagar LED').grid(
    row=3, column=0, padx=8, pady=15)
botonOnLed = Button(buttonsFrame, text='Encender LED').grid(
    row=3, column=1, padx=8, pady=15)
botonReadADC = Button(buttonsFrame, text='Leer ADC').grid(
    row=4, column=0, padx=5, pady=15,columnspan=2)



# start()
root.mainloop()
