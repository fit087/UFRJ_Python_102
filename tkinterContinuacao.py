# 09/06/2015
# Aula Pratica. Slide TKinter Continuacao

#from Tkinter import *
from tkinter import *

def cb2():
    top.deiconify # visualizar de novo

def cb():
    t = Toplevel()
    top.withdraw() # Minimiza a janela atual
    x = Button(master = t, text = "voltar", command = cb2)
    x.pack()

top = Tk()
f = Frame(master = top)
f.pack()
b = Button(master = f, text = "Abrir", command = cb)
b.pack()

top.mainloop()
