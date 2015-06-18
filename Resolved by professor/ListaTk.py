# -*- coding: utf-8 -*-
# 16/06/2015
"""
Created on Tue Jun 16 14:20:32 2015
    Lista de Exercicios:        Tkinter
    File:                       lista Tkinter.pdf
    Curso:                      Computacao II (MAB225)
    Proffessor:                 Igor Leao
@author: Adolfo Emmanuel Correa Lopez

Obs: No ultimo exercício, o problema era simples. As propriedades width e height 
não podiam ser acessadas como self.canvas["width"] e self.canvas["height"], pois 
essas propriedades não são atualizadas dinamicamente quando o canvas é redimensionado.
A melhor forma de acessar a largura e altura do canvas é através de 
self.canvas.winfo_width() e self.canvas.winfo_height().
 
Ou seja, o que estava acontecendo até o ponto em que fomos em sala de aula é que a
cada redimensionamento do canvas os losangos estavam sendo desenhados sobrepostos na
posição baseada na largura/altura inicial do canvas. Com essa alteração (e também a
adição de uma chamada à função de deletar todos os itens existentes no canvas antes
de desenhar o losango) é possível perceber o deslocamento do losango. Ressaltando 
que o evento a ser associado à função on_resize é o <Configure>. Ele é disparado
sempre que alguma propriedade do widget é alterada, como no caso é a largura e
altura durante o redimensionamento.

"""


#from Tkinter import * # for python2
from tkinter import * # for python3

class VerifParNumero():
    def ehNumeroPar(self,n):
        if n%2 == 0:
            return True
        else:
            return False

class Ex1(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master=master)
        self.pack()

        self.fr1 = Frame(master=self)
        self.lb1 = Label(master=self,text="Este programa verifica se um dado numero e par ou impar")
        self.lb2 = Label(master=self.fr1,text="Numero: ")
        self.lb3 = Label(master=self,text="Resultado")
        self.en1 = Entry(master=self.fr1)
        self.bt1 = Button(master=self,text="Verificar",command=self.funcaoBt1)

        self.lb1.pack(side=TOP)
        self.fr1.pack(side=TOP)
        self.bt1.pack(side=TOP)
        self.lb3.pack(side=TOP)

        self.lb2.pack(side=LEFT)
        self.en1.pack(side=RIGHT)
        
    def funcaoBt1(self):
        valor = 0
        try:
            valor = int(self.en1.get())
            if ver.ehNumeroPar(valor):
                self.lb3["text"] = str(valor) + " e um numero par"
            else:
                self.lb3["text"] = str(valor) + " e um numero impar"
        except:
            self.lb3["text"] = "O valor digitado nao e um numero"

        open("resultado.txt","a").write(str(self.lb3["text"]+"\n"))

class ConverteTemperatura():
    def ConverteCelsiusFahrenheit(self,c):
        return (c*1.8)+32
    def ConverteFahrenheitCelsius(self,f):
        return (f-32.0)/1.8
    
class Ex2(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master=master)
        self.pack()
        self.lb1 = Label(master=self,text="Graus Fahrenheit: ")
        self.lb2 = Label(master=self,text="Graus Celsius: ")
        self.en1 = Entry(master=self)
        self.en2 = Entry(master=self)
        self.bt1 = Button(master=self,text="F -> C",command=self.cmdbt1)
        self.bt2 = Button(master=self,text="C -> F",command=self.cmdbt2)

        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)
        self.en1.grid(row=0,column=1)
        self.en2.grid(row=1,column=1)
        self.bt1.grid(row=0,column=2)
        self.bt2.grid(row=1,column=2)

    def cmdbt1(self):
        valor = float(self.en1.get())
        valor = conv.ConverteFahrenheitCelsius(valor)
        self.en2.delete(0,END)
        self.en2.insert(0,str(valor))
        
    def cmdbt2(self):
        valor = float(self.en2.get())
        valor = conv.ConverteCelsiusFahrenheit(valor)
        self.en1.delete(0,END)
        self.en1.insert(0,str(valor))

class Ex3(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master=master)
        self.pack(expand=True,fill=BOTH)
        self.canvas = Canvas(master=self,background="white")
        self.canvas.pack(expand=True,fill=BOTH)

        self.canvas.bind("<Configure>", self.on_resize)

        self.desenhaLosango(50.0)
        
    def desenhaLosango(self,tamanho):
        cx = float(self.canvas.winfo_width())/2.0 
        cy = float(self.canvas.winfo_height())/2.0
        t = tamanho/2.0
        pontos = [cx,cy-t,cx+t,cy,cx,cy+t,cx-t,cy]
        self.canvas.delete(ALL)
        return self.canvas.create_polygon(pontos, outline='red', fill='green', width=2)

    def on_resize(self,e):
        self.desenhaLosango(50.0)
        
        
        
        

        
top = Tk()
ver = VerifParNumero()
conv = ConverteTemperatura()
#app = Ex1(top)
#app = Ex2(top)
app = Ex3(top)

mainloop()
