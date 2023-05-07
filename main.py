#Calculadora con Tkinter
#Tkinter Calculator

#Realizada por Bryan Delgado
#Fecha de Desarrollo: 5-5-2023
#Proyecto para portafolio

from tkinter import *
from tkinter import ttk

#Definimos las funciones de las operaciones matematicas
def limpiar():
    num1.set(" ")
    num2.set(" ")

def sumar():
    num3.set(float(num1.get()) + float(num2.get()))
    limpiar()

def sumar():
   num3.set(float(num1.get()) - float(num2.get()))
   limpiar()


#Determinamos las caracteristicas de la ventana
window = Tk()
window.geometry("300x300")
window.iconbitmap(bitmap='icon.ico')
window.resizable(0,0) #No hay redimension
window.title('Tkinter Calculated v 1.0')

#Definimos las variables para albergar los datos
num1 = StringVar()
num2 = StringVar()
num3 = StringVar()

#Definimos los titulos y entradas de las operaciones
title1 = Label(window, text="Ingrese su primer valor: ")
title1.pack()
input1 = ttk.Entry(window, justify="center", textvariable=num1)
input1.pack()

title2 = Label(window, text="Ingrese su segundo valor: ")
title2.pack()
input2 = ttk.Entry(window, justify="center", textvariable=num2)
input2.pack()

title_general = Label(window, justify="center", text="Seleccione la operacion a realizar: ")
title_general.pack()

#Definimos los botones de operaciones
boton1 = ttk.Button(window, text="Sumar", command=sumar)
boton1.pack()

boton2 = ttk.Button(window, text="Restar", command=sumar)
boton2.pack()


#Definimos casilla de resultado
title3 = Label(window, text="Su resultado es: ")
title3.pack()
input3 = ttk.Entry(window, justify="center", textvariable=num3)
input3.pack()

#Definimos loop principal del programa
window.mainloop()