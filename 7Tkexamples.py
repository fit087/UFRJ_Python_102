# -*- coding: utf8 -*-
# 28/05/2015
from Tkinter import *

class Aplicacao(Frame):
    def __init__(self, master = None):
        self.f = Frame.__init__(self, master, relief = "groove", border=5)
        self.m = master
        self.m.title("My App")#; self.m.geometry("500x500+100+100")
        self.m.geometry("500x500+100+100")
        #Frame.__init__(self, master)
        #self.m.pack() # Err1_1 Só com isso aqui que resolve
        #self.pack()   # Err2 Não aparece o botao
        #self.m.pack()
        
        # Adicionando um Botao
        self.bt_ex_pg69 = Button(master = self, text = "Exemplo pg. 69", width = 20, height = 2)
        self.bt_ex_pg69["command"] = self.callback_function1 # Assim eu vejo o frame
        self.bt_ex_pg69.pack()
        
        
        self.pack()
        self.m.pack() # Err2_1 Resolve colacar aqui no final
        #self.pack()
        
    def callback_function1(self):
        self.nw_window = Toplevel()
        #self.nw_window.pack()
        #self.m.destroy()
        #self.bt["state"] = DISABLE
        b = Button(self.nw_window, text="Incrementa",command=self.inc)
        b.pack()
        self.rotulo = Label(self.nw_window, text="0")
        self.rotulo.pack()
        
    def inc(self):
        n=int(self.rotulo.configure("text")[4])+1
        print self.rotulo.configure("text") # Retorna os datos que o configure coleta do widget
        self.rotulo.configure(text=str(n))

top = Tk()
app = Aplicacao(master = top) #Err1 Utilizando essa sentencia o tamanho da janela é só
                              # a barra de fechar e minimizar
mainloop()
#app.mainloop()
        