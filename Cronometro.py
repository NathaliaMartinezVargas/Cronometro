#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Natalia
#
# Created:     06/05/2020
# Copyright:   (c) Natalia 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
import tkinter as tk

def main():
    pass

if __name__ == '__main__':
    main()

    def click_boton(cronometro):
        return


    def cronometro():
        for hora in range (0,24):
            for minuto in range (0,60):
                for segundo in range (0,60):
                    print("Hora: ", hora, "Minutos: ", minuto, "Segundos: ", segundo )
                    time.sleep(1)



    #interfaz
    #ventana
    ventana =tk.Tk()
    ventana.title("Cronometro")
    ventana.geometry("250x300")
    ventana.config(bg="grey")
    var=tk.StringVar()

    #boton
    botoniniciar=tk.Button(ventana,text="Iniciar", bg="black", fg="white", command = lambda:click_boton(cronometro))
    botoniniciar.pack(side=tk.TOP)

    #etiqueta hora
    e1=tk.Label(ventana,text="Hora: ", bg="black", fg="white")
    e1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
    entradahora=tk.Label(ventana, bg="white", textvariable=cronometro)
    entradahora.pack(padx=5, pady=6, ipadx=5, ipady=5, fill=tk.X)

    #etiqueta minutos
    e2=tk.Label(ventana,text="Minutos: ", bg="black", fg="white")
    e2.pack(padx=5, pady=7, ipadx=5, ipady=5, fill=tk.X)
    entradaminuto=tk.Label(ventana, bg="white", textvariable=cronometro)
    entradaminuto.pack(padx=5, pady=8, ipadx=5, ipady=5, fill=tk.X)

    #etiqueta segundos
    e3=tk.Label(ventana,text="Segundos: ", bg="black", fg="white")
    e3.pack(padx=5, pady=9, ipadx=5, ipady=5, fill=tk.X)
    entradasegundo=tk.Label(ventana, bg="white", textvariable=cronometro)
    entradasegundo.pack(padx=5, pady=10, ipadx=5, ipady=5, fill=tk.X)


    ventana.mainloop()

    print ("iniciar")
    cronometro()
