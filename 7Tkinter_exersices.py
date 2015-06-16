# -*- coding: utf-8 -*-
"""
Spyder Editor
16/06/2015
This is a temporary script file.
"""

from Tkinter import *

# Exercise 1

class check_even_odd(object):
    def is_even(self, n):
        if n%2 == 0:
            return True
        else:
            return False
            
class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master = master)
        self.master = master
        self.pack()
        
        
#        self.fr1 = Frame(master = self)        
        self.lb1_descriptor = Label(master = self, text="Este programa verifica\
se um dado numero eh par ou impar")
        self.lb2_number = Label(master = self, text="Numero")
        self.lb3_number = Label(master = self, text="Numero")
        self.lb3_number = Label(master = self, text="Resultado")
        self.en1 = Entry(master = self)
        self.bt1 = Button(master = self, text = "Check", command = self.function_Bt1)
        
#        self.lb1.pack(side = TOP)
#        self.lb2.pack(side = TOP)
#        self.en1.pack(side = TOP)
#        self.bt1.pack(side = TOP)
#        self.lb3.pack(side = TOP)
        
        self.lb1_descriptor.pack(side = TOP)
        self.lb2_number.pack(side = TOP)
        self.en1.pack(side = TOP)
        self.bt1.pack(side = TOP)
        self.lb3_number.pack(side = TOP)

#        grid(row = 0, column = 0) # Grid elimina as colunas vazias, pois ficam
#        grid(row = 1, column = 0) # com largura e altura 0 (zero)
#        grid(row = 2, column = 0)
#        grid(row = 3, column = 0)
#        grid(row = 4, column = 0)
#        grid(row = 0, column = 1)
    
    def function_Bt1(self):
        value = 0
        try:
            value = int(self.en1.get())
            if checker.is_even(value):
                self.lb3_number["text"] = str(value) + " eh um numero par"
            else:
                self.lb3_number["text"] = str(value) + " eh um numero impar"
        except:
            self.lb3_number["text"] =" não é um numero"
        
        open("Resultado.txt", "w").write(str(self.lb3_number["text"]) + "\n")
#        open("Resultado.txt", "a").write(str(self.lb3["text"]))
            
    

main_window = Tk()
checker = check_even_odd()
app_frame = Application(main_window)
app_frame.pack()
mainloop()

#lb1_descriptor = Label(text="Este programa verifica se um dado número é par ou\
#                        impar")
                
class converte_temperature():
    def celsius2Fahrenheit(self,c):
        return (c*1.8)+32
    def Fahrenheit2celsius(self,c):
        return f-32.0/1.8


class Ex2(Frame):
    def __init__(self, master = None):
        Frame.__init__(master = self)
        self.master = master
        self.pack()
    def cmdbt1(self):
        valor = float(self.en1.get())
        valor = conv.celsius2Fahrenheit()
        en1.delete(0,END)
        en1.insert(0,str(valor))

class ex3_canvas(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master = master)
        self.pack(expand = True, fill = BOTH)
        self.canvas = Canvas(master = self, background = "white")
        self.canvas.pack(expand = True, fill = BOTH)
