# 02/06/2015
# Exemplo professor Igor

from Tkinter import *

class Aplicacao(Frame):

    def __init__(self,m=None,w=500,h=500):
        Frame.__init__(self,master=m,width=w,height=h)
        self.m = m
        self.m.title("Minha Aplicacao")
        self.m.geometry("500x500+100+100")
        self.m.maxsize(800,400)
        self.place(x=0,y=0)
        
        self.bt = Button(master=self,text="Botao")
        self.bt["width"] = 10
        self.bt["height"] = 3
        self.bt["command"] = self.cb1
        self.bt["relief"] = 'sunken' # 'raised', 'ridge', 'sunken', 'groove' 
        self.bt["background"] = "red"
        self.bt.place(x=200,y=0)

        self.bt2 = Button(master=self,text="asfdadf")
        self.bt2["width"] = 50
        self.bt2["height"] = 50

        self.photo = PhotoImage(file="python.gif")
        self.bt2["image"] = self.photo
        #w = Label(parent, image=photo)
        #w.photo = photo
        self.bt2.place(x=0,y=0)     

    def cb1(self):
        self.bt["state"] = DISABLED
        self.novaJanela = Toplevel()
        

top = Tk()
app = Aplicacao(m=top,w=500,h=500)
mainloop()
