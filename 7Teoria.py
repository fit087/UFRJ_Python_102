# -*- coding: utf8 -*-
# 28/05/2015
from Tkinter import *

class Aplicacao(Frame):
    def __init__(self, master = None):
        self.f = Frame.__init__(self, master, relief = "groove", border=10)
        self.m = master
        self.m.title("My App")#; self.m.geometry("500x500+100+100")
        #self.m.geometry("500x500+100+100")
        #Frame.__init__(self, master)
        #self.m.pack() # Err1_1 Só com isso aqui que resolve
        #self.pack()   # Err2 Não aparece o botao
        #self.m.pack()
        
        # Adicionando um Botao
        self.bt = Button(master = self, text = "Botao", width = 10, height = 3)
        #self.bt = Button(text = "Botao", width = 10, height = 3, command=self.callback_function1)
        #self.bt = Button(master = self.m, text = "Botao", width = 10, height = 3)
        #self.bt = Button(master = self.m, text = "Botao", width = 10, height = 3, command=self.callback_function1)
        self.bt = Button(master = self.f, text = "Botao", command=self.callback_function1)
        #self.bt.pack()
        #self.bt["command"] = self.callback_function1 # Assim eu vejo o frame
        self.bt.pack()
        
        
        self.pack()
        self.m.pack() # Err2_1 Resolve colacar aqui no final
        #self.pack()
        
    def callback_function1(self):
        self.nw_window = Toplevel()
        #self.nw_window.pack()
        #self.m.destroy()
        #self.bt["state"] = DISABLE

top = Tk()
app = Aplicacao(master = top) #Err1 Utilizando essa sentencia o tamanho da janela é só
                              # a barra de fechar e minimizar
mainloop()
#app.mainloop()
        