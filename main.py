from re import L
from tkinter import *
from math import *
import tkinter
import time
from tkinter.ttk import *
from datetime import datetime
CANTIDAD = 10
TIEMPOAVISO = 1

from tabulate import tabulate

#backend
fichero = open('ficha.txt', 'w')

lista_jugadoresA= []
lista_jugadoresB=[]


class jugadorA():
    def __init__(self, equipo, numero, puntos=0, faltas=0, faltasTecnicas=0):
        self.equipo = equipo
        self.numero = numero
        self.puntos = puntos
        self.faltas = faltas
        self.faltasTecnicas = faltasTecnicas

    def EnterData(self):
        self.numero=int(input('Numero:'))

class jugadorB():
    def __init__(self, equipo, numero, puntos=0, faltas=0, faltasTecnicas=0):
        self.equipo = equipo
        self.numero = numero
        self.puntos = puntos
        self.faltas = faltas
        self.faltasTecnicas = faltasTecnicas

    def EnterData(self):
        self.numero=int(input('Numero:'))
        

    

print('-------EQUIPO A---------')
for i in range(CANTIDAD):
    j = jugadorA('A', 0, 0, 0, 0)
    j.EnterData()
    lista_jugadoresA.append(j)

print('-------EQUIPO B---------')
for i in range(CANTIDAD):
    j = jugadorB('B', 0, 0, 0, 0)
    j.EnterData()
    lista_jugadoresB.append(j)

#frontend

#ventana prncipal
window = Tk()
window.geometry('600x700')
window.resizable(False, False)
window.title('App')

puntosTotalesA = 0
puntosTotalesB = 0

#sumar puntps
def sumarPuntosA(variable, suma):
    global puntosTotalesA
    lista_jugadoresA[variable].puntos = lista_jugadoresA[variable].puntos + suma
    fichero.write(str(lista_jugadoresA[variable].equipo) + str(lista_jugadoresA[variable].numero) + '   +' + str(suma)+ '\n')
    fichero.flush()
    puntosTotalesA = puntosTotalesA + suma
    labelA.config(text=str(puntosTotalesA))




#ventanas jugadores


def faltas(variable):
    lista_jugadoresA[variable].faltas =  lista_jugadoresA[variable].faltas +1
    fichero.write(str(lista_jugadoresA[variable].equipo) + str(lista_jugadoresA[variable].numero) + '    falta\n')
    if lista_jugadoresA[variable].faltas == 5: 
        aviso1a = Label(window, text = 'El jugador ' + str(lista_jugadoresA[variable].numero) + ' está expulsado')
        aviso1a.place(relx=0.5, rely= 0.9)
        time.sleep(TIEMPOAVISO)
        aviso1a = Label(window, text = ' ')
        fichero.write(str(lista_jugadoresA[variable].equipo) + str(lista_jugadoresA[variable].numero) + '    expulsado\n')
        fichero.flush()



def faltasTecnicas(variable):
    lista_jugadoresA[variable].faltasTecnicas = lista_jugadoresA[variable].faltasTecnicas + 1
    fichero.write(str(lista_jugadoresA[variable].equipo) + str(lista_jugadoresA[variable].numero)+ '    falta tecnica/antideportiva\n')
    fichero.flush()

    if lista_jugadoresA[variable].faltasTecnicas == 2:
        aviso2a = Label(window, text = 'El jugador ' + str(lista_jugadoresA[variable].numero) + ' está expulsado')
        aviso2a.place(relx=0.5, rely= 0.9)
        fichero.write(str(lista_jugadoresA[variable].equipo) + str(lista_jugadoresA[variable].numero) + '    expulsado\n')
        fichero.flush()


def abrirVentanaA(variable):
    ventanaA = Toplevel(window)
    ventanaA.title('Ventana jugadores equipo A')
    ventanaA.resizable(False,False)
    ventanaA.geometry('400x300')
    #botones
    Amas1 = Button(ventanaA, text = '+1', command= lambda: sumarPuntosA(variable, 1))
    Amas1.pack()
    Amas2 = Button(ventanaA, text = '+2', command=  lambda: sumarPuntosA(variable, 2))
    Amas2.pack()
    Amas3 = Button(ventanaA, text= '+3', command= lambda:  sumarPuntosA(variable, 3))
    Amas3.pack()
    Afalta = Button(ventanaA, text = 'FALTA', command= lambda: faltas(variable))
    Afalta.pack()
    Aantideportiva = Button(ventanaA, text = 'Atideportiva', command=lambda:faltasTecnicas(variable))
    Aantideportiva.pack()
    Atecnica = Button(ventanaA, text = 'TÉCNICA',  command= lambda: faltasTecnicas(variable))
    Atecnica.pack()
##


def sumarPuntosB(variable, suma):
    global puntosTotalesB
    lista_jugadoresB[variable].puntos = lista_jugadoresB[variable].puntos + suma
    fichero.write(str(lista_jugadoresB[variable].equipo) + str(lista_jugadoresB[variable].numero) + '   +' + str(suma) + '\n')
    fichero.flush()
    puntosTotalesB = puntosTotalesB + suma
    labelB.config(text = str(puntosTotalesB))


def faltasB(variable):
    lista_jugadoresB[variable].faltas =  lista_jugadoresB[variable].faltas +1
    fichero.write(str(lista_jugadoresB[variable].equipo) + str(lista_jugadoresB[variable].numero) + '   falta\n')
    fichero.flush()
    if lista_jugadoresB[variable].faltas == 5: 
        aviso1B = Label(window, text = 'El jugador ' + str(lista_jugadoresB[variable].numero) + ' está expulsado')
        aviso1B.place(relx=0.5, rely= 0.9)
        fichero.write(str(lista_jugadoresB[variable].equipo) + str(lista_jugadoresB[variable].numero) + '   expulsado\n')
        fichero.flush()



def faltasTecnicasB(variable):
    lista_jugadoresB[variable].faltasTecnicas = lista_jugadoresB[variable].faltasTecnicas + 1
    fichero.write(str(lista_jugadoresB[variable].equipo) + str(lista_jugadoresB[variable].numero) + '   falta tecnica/antideportiva\n')
    fichero.flush()

    if lista_jugadoresB[variable].faltasTecnicas == 2:
        aviso2B = Label(window, text = 'El jugador ' + str(lista_jugadoresB[variable].numero) + ' está expulsado')
        aviso2B.place(relx=0.5, rely= 0.9)
        fichero.write(str(lista_jugadoresB[variable].equipo) + str(lista_jugadoresB[variable].numero) + '   expulsado\n')
        fichero.flush()


def abrirVentanaB(variable):
    ventanaB = Toplevel(window)
    ventanaB.title('Ventana jugadores equipo B')
    ventanaB.resizable(False,False)
    ventanaB.geometry('400x300')
    #botones
    Bmas1 = Button(ventanaB, text = '+1', command= lambda: sumarPuntosB(variable, 1))
    Bmas1.pack()
    Bmas2 = Button(ventanaB, text = '+2', command=  lambda: sumarPuntosB(variable, 2))
    Bmas2.pack()
    Bmas3 = Button(ventanaB, text= '+3', command= lambda:  sumarPuntosB(variable, 3))
    Bmas3.pack()
    Bfalta = Button(ventanaB, text = 'FALTA', command= lambda: faltasB(variable))
    Bfalta.pack()
    Bantideportiva = Button(ventanaB, text = 'Atideportiva', command=lambda:faltasTecnicasB(variable))
    Bantideportiva.pack()
    Btecnica = Button(ventanaB, text = 'TÉCNICA',  command= lambda: faltasTecnicasB(variable))
    Btecnica.pack()


        
#TEMPORIZADOR
counter = 0
running = False


def counter_label(label):
    def count():
        if running:
            global counter 
            global string
            if counter == 0:
                display = '00:00:00'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string
    
            label['text'] = display
            label.after(1000, count)
            counter += 1 
    count()
    
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'
    
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False
    

def Reset(label):
    global counter
    counter = 0
    if not running:
        reset['state'] = 'disabled'
        label['text'] = '00:00:00'
    else:
        label['text'] = '00:00:00'


window.minsize(width=250, height=70)
label = tkinter.Label(window, text='00:00:00', fg='black', font='Verdana 30 bold')
label.pack()
f = tkinter.Frame(window)
start = tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
stop = tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')

##


etiquetainfo1 = Label(window, text = 'EQUIPO A', font = ('arial', 30), width = 9)
etiquetainfo1.place(relx=0.2, rely=0.15, anchor='center')
etiquetainfo2 = Label(window, text = 'EQUIPO B', font = ('arial', 30), width = 9)
etiquetainfo2.place(relx=0.8, rely=0.15, anchor='center')

#contador a
labelA = Label(window, text = str(puntosTotalesA))
labelA.place(relx=0.2, rely=0.2, anchor='center')
#contador b
labelB = Label(window, text = puntosTotalesB)
labelB.place(relx=0.8, rely=0.2, anchor='center')

#botones a
a1 = Button(window, text = lista_jugadoresA[0].numero, command = lambda: abrirVentanaA(0))
a1.place(relx=0.2, rely=0.35, anchor='center')

a2 = Button(window, text = lista_jugadoresA[1].numero, command =  lambda: abrirVentanaA(1))
a2.place(relx=0.2, rely=0.4, anchor='center')
a3 = Button(window, text = lista_jugadoresA[2].numero, command =  lambda: abrirVentanaA(2))
a3.place(relx=0.2, rely=0.45, anchor='center')
a4 = Button(window, text = lista_jugadoresA[3].numero, command =  lambda: abrirVentanaA(3))
a4.place(relx=0.2, rely=0.5, anchor='center')
a5 = Button(window, text = lista_jugadoresA[4].numero, command =  lambda: abrirVentanaA(4))
a5.place(relx=0.2, rely=0.55, anchor='center')
a6 = Button(window, text = lista_jugadoresA[5].numero, command =  lambda: abrirVentanaA(5))
a6.place(relx=0.2, rely=0.6, anchor='center')
a7 = Button(window, text = lista_jugadoresA[6].numero, command =  lambda: abrirVentanaA(6))
a7.place(relx=0.2, rely=0.65, anchor='center')
a8 = Button(window, text = lista_jugadoresA[7].numero, command =  lambda: abrirVentanaA(7))
a8.place(relx=0.2, rely=0.7, anchor='center')        
a9 = Button(window, text = lista_jugadoresA[8].numero, command = lambda:  abrirVentanaA(8))
a9.place(relx=0.2, rely=0.75, anchor='center')        
a10 = Button(window, text = lista_jugadoresA[9].numero, command =  lambda: abrirVentanaA(9))
a10.place(relx=0.2, rely=0.8, anchor='center')                        

#botones b
b1 = Button(window, text = lista_jugadoresB[0].numero, command = lambda: abrirVentanaB(0))
b1.place(relx=0.8, rely=0.35, anchor='center')
b2 = Button(window, text = lista_jugadoresB[1].numero, command = lambda: abrirVentanaB(1))
b2.place(relx=0.8, rely=0.4, anchor='center')
b3 = Button(window, text = lista_jugadoresB[2].numero, command = lambda: abrirVentanaB(2))
b3.place(relx=0.8, rely=0.45, anchor='center')
b4 = Button(window, text = lista_jugadoresB[3].numero, command = lambda: abrirVentanaB(3))
b4.place(relx=0.8, rely=0.5, anchor='center')
b5 = Button(window, text = lista_jugadoresB[4].numero, command = lambda: abrirVentanaB(4))
b5.place(relx=0.8, rely=0.55, anchor='center')
b6 = Button(window, text = lista_jugadoresB[5].numero, command = lambda: abrirVentanaB(5))
b6.place(relx=0.8, rely=0.6, anchor='center')
b7 = Button(window, text = lista_jugadoresB[6].numero, command = lambda: abrirVentanaB(6))
b7.place(relx=0.8, rely=0.65, anchor='center')
b8 = Button(window, text = lista_jugadoresB[7].numero, command = lambda: abrirVentanaB(7))
b8.place(relx=0.8, rely=0.7, anchor='center')
b9 = Button(window, text = lista_jugadoresB[8].numero, command = lambda: abrirVentanaB(8))
b9.place(relx=0.8, rely=0.75, anchor='center')
b10 = Button(window, text = lista_jugadoresB[9].numero)
b10.place(relx=0.8, rely=0.8, anchor='center')     

#tabla
def crear_fichero():
    data = [
    ['A' + str(lista_jugadoresA[0].numero), lista_jugadoresA[0].puntos, 'B' + str(lista_jugadoresB[0].numero), lista_jugadoresB[0].puntos], 
        ['A' + str(lista_jugadoresA[1].numero), lista_jugadoresA[1].puntos, 'B' + str(lista_jugadoresB[1].numero), lista_jugadoresB[1].puntos], 
        ['A' + str(lista_jugadoresA[2].numero), lista_jugadoresA[2].puntos, 'B' + str(lista_jugadoresB[2].numero), lista_jugadoresB[2].puntos], 
        ['A' + str(lista_jugadoresA[3].numero), lista_jugadoresA[3].puntos, 'B' + str(lista_jugadoresB[3].numero), lista_jugadoresB[3].puntos], 
        ['A' + str(lista_jugadoresA[4].numero), lista_jugadoresA[4].puntos, 'B' + str(lista_jugadoresB[4].numero), lista_jugadoresB[4].puntos], 
        ['A' + str(lista_jugadoresA[5].numero), lista_jugadoresA[5].puntos, 'B' + str(lista_jugadoresB[5].numero), lista_jugadoresB[5].puntos], 
        ['A' + str(lista_jugadoresA[6].numero), lista_jugadoresA[6].puntos, 'B' + str(lista_jugadoresB[6].numero), lista_jugadoresB[6].puntos], 
        ['A' + str(lista_jugadoresA[7].numero), lista_jugadoresA[7].puntos, 'B' + str(lista_jugadoresB[7].numero), lista_jugadoresB[7].puntos], 
        ['A' + str(lista_jugadoresA[8].numero), lista_jugadoresA[8].puntos, 'B' + str(lista_jugadoresB[8].numero), lista_jugadoresB[8].puntos], 
        ['A' + str(lista_jugadoresA[9].numero), lista_jugadoresA[9].puntos, 'B' + str(lista_jugadoresB[9].numero), lista_jugadoresB[9].puntos], 
        ['PUNTOS TOTALES', puntosTotalesA, ' ', puntosTotalesB]
    ]

    #nombres columnas
    col_names = ["JUGADORES A", "PUNTOS", 'JUGADORES B', 'PUNTOS']
  
    #display table
    print(tabulate(data, headers=col_names, tablefmt="grid"))
  


crear = Button(window, text = 'CREAR TABLA', command = crear_fichero)
crear.place(relx=0.15, rely=0.9, anchor='center')

window.mainloop()