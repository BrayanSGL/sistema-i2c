import tkinter as tk
from tkinter import *
import time
import threading
import serial

root = tk.Tk()
root.title('Tercera entrega')
root.resizable(height=False, width=False)

# ------------------------Configuracion inicial de frames -------
buttonsFrame = tk.Canvas(root, width=300, height=300, bg='Gray')
buttonsFrame.grid(row=0, column=0)
registerFrame = tk.Canvas(root, width=350, height=300, bg='Gray')
registerFrame.grid(row=0, column=1)

# ---------------------Se establace la posicion de los botones----------
botonSaveInfo = Button(buttonsFrame, text='Save RTC').grid(
    row=0, column=0, padx=10, pady=10)
botonReadInfo = Button(buttonsFrame, text='Read EEPROM').grid(
    row=1, column=0, padx=10, pady=10)
botonOnOffLed = Button(buttonsFrame, text='on | off Led').grid(
    row=2, column=0, padx=10, pady=10)
botonReadADC = Button(buttonsFrame, text='Read ADC').grid(
    row=3, column=0, padx=10, pady=10)

# start()
root.mainloop()
