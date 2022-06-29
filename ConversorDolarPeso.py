import tkinter
import requests
from tkinter import *
from tkinter import ttk,font
class Ventana(object):
    __ventana=None
    __dolar=None
    __peso=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title('Conversor Dolar Peso')
        self.__ventana.configure(background='lightblue')
        fuente=font.Font(weight='normal')


        self.__dolar=StringVar()
        self.__peso=StringVar()
        self.__dolar.trace('w',self.calcular)


        self.dolaresEntry=ttk.Entry(self.__ventana,textvariable=self.__dolar,width=10)
        self.dolaresEntry.grid(column=0,row=0)

        ttk.Label(self.__ventana,background='lightblue',text='Dolares es igual a:',font=fuente,padding=(5,5)).grid(column=1,row=0)
        ttk.Label(self.__ventana,textvariable=self.__peso,background='lightblue').grid(column=0,row=1)
        ttk.Label(self.__ventana,background='lightblue',text='Pesos',font=fuente,padding=(5,5)).grid(column=1,row=1)
        ttk.Button(self.__ventana,text='Salir',command=self.destroy).grid(column=2,row=2)


    def calcular(self,*args):
        api=requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        api=api.json()
        valor= float(api[0]["casa"]["venta"].replace(",", "."))
        if self.dolaresEntry.get() != '':
           try:
               dolar=float(self.dolaresEntry.get())
               self.__peso.set(valor*dolar)
           except ValueError:
                messagebox.showerror(title='Error de tipo',
                message='Debe ingresar un valor numérico')
                self.__dolar.set('')
                self.__peso.set('')
                self.dolarEntry.focus()
        else:
            self.__peso.set('')



    def destroy(self):
        self.__ventana.destroy()
    def ejecutar(self):
        self.__ventana.mainloop()
if __name__=='__main__':
    ventana=Ventana()
    ventana.ejecutar()
