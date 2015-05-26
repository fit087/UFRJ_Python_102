# -*- coding: cp1252 -*-
# 26/05/2015
# TKinter
"""
Created on Tue May 26 10:20:32 2015
    Lista de Exercicios:        TKinter
    File:                       Slide TKinter.pdf
    Curso:                      Computacao II (MAB225)
    Proffessor:                 Igor Leao
@author: Adolfo Emmanuel Correa Lopez
"""

# 1st part
from Tkinter import *

#Pg. 34
### 2nd part
##about_message = "Hola"
####top = Toplevel()
##top = Tk()
##top.title("About this application...")
##
##msg = Message(top, text=about_message)
##msg.pack()
##
##button = Button(top,text="Dismiss",command=top.destroy)
##button.pack()
##
### 3ra part
##mainloop()

# Pg. 35

##class Application(Frame):
##    def __init__(self, master=None):
##        self.master = master
##        Frame.__init__(self, master)
##        self.msg = Label(self, text='Tiago')
##        self.msg.pack()
##        #self.bye = Button(self, text="Bye", command=self.quit)
##        #self.bye = Button(self, text="Bye", command=self.destroy)
##        self.bye = Button(self, text="Bye", command=master.destroy)
##        self.bye.pack()
##        self.pack()
##top = Tk()
##app = Application(top)
##mainloop()

# Pg. 38

###from Tkinter import *
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        lb1 = Label(text="MeuTexto")
##        lb1.pack()
##        self.pack()
##app = Application()
##mainloop()

# Pg. 39
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        var = StringVar()
##        label = Message(textvariable=var, relief=RAISED)
##        var.set("Hey!? How are you doing?")
##        label.pack()
##app = Application()
##mainloop()

# Pg. 40
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        self.btn = Button(self,text="Sair",command=self.quit) # quit � um callback
##        self.btn.pack()
##        self.pack()
##app = Application()
##mainloop()

# Pg. 41
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        entr = Entry()
##        entr.pack()
##        self.pack()
##        
##app = Application()
##mainloop()

# Pg. 42
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        checkb = Checkbutton(text="Me marque")
##        checkb.pack()
##        self.pack()
##app = Application()
##mainloop()

# Pg. 43
##class Application(Frame):
##    def __init__(self, master=None):
##        #Frame.__init__(self, master)
##        R1 = Radiobutton(text="Option 1", value=1)
##        R1.pack()
##        R2 = Radiobutton(text="Option 2", value=2)
##        R2.pack()
##        R3 = Radiobutton(text="Option 3", value=3)
##        R3.pack()
##        #self.pack()
##app = Application()
##mainloop()

# Pg. 44
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        Lb1 = Listbox()
##        Lb1.insert(1, "Python")
##        Lb1.insert(2, "Perl")
##        Lb1.insert(3, "C")
##        Lb1.insert(4, "PHP")
##        Lb1.insert(5, "JSP")
##        Lb1.insert(6, "Ruby")
##        Lb1.pack()
##        self.pack()
##app = Application()
##mainloop()

# Pg. 46
##class Application():
##    def __init__(self, master=None):
##        #Frame.__init__(self, master)
##        frame = Frame()
##        frame.pack()
##        bottomframe = Frame()
##        bottomframe.pack(side = BOTTOM)
##        redbutton = Button(frame, text="Red", fg="red", bg="green")
##        redbutton.pack(side = LEFT)
##        greenbutton = Button(frame, text="Brown", fg="brown")
##        greenbutton.pack(side = LEFT)
##        bluebutton = Button(frame, text="Blue", fg="blue")
##        bluebutton.pack(side = LEFT)
##        blackbutton = Button(bottomframe, text="Black", fg="black")
##        blackbutton.pack(side = BOTTOM)
##app = Application()
##mainloop()

# Pg. 47
# Funciona como a tela de um pintor onde � poss�vel desenhar outras formas
# envia uma mensagem para o canvas orientando-o
# a trocar algumas caracter�sticas do objeto texto
# canvas.itemconfig(texto, font=('SansSerif', '36'), fill='red', anchor=NW)
# ...
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        canvas = Canvas(master = None, background='white')
##        #canvas.pack()
##        texto = canvas.create_text(100, 75, text="Alo mundo!")
##        canvas.itemconfig(texto, font=('SansSerif', '36'), fill='red', anchor=NW)
##        canvas.pack()
##        bt = Button(master = None, text = "ola")
##        bt.pack(side=TOP)
##        bt.pack(side=LEFT)
##        bt["text"] = "alterado"
##        #bt.fg = "red"
##        bt["fg"] = "red"
###top = Tk()
###app = Application(top)
##app = Application()
##mainloop()

# Pg. 49
# Um painel de menu. Implementa menus de janela, pulldowns e popups
##class Application(Frame):
##    def __init__(self, master=Tk()):
##        Frame.__init__(self, master)
##        menubar = Menu()
##        filemenu = Menu(menubar, tearoff=0)
##        filemenu.add_command(label="New")
##        filemenu.add_command(label="Open")
##        filemenu.add_command(label="Save")
##        filemenu.add_command(label="Save as...")
##        filemenu.add_command(label="Close")
##        filemenu.add_separator()
##        filemenu.add_command(label="Exit", command=quit)
##        menubar.add_cascade(label="File", menu=filemenu)
##        master.config(menu=menubar)
##        self.pack()
##app = Application()
##mainloop()

# Pg. 50
# Permite especificar um valor atrav�s de um ponteiro em uma escala linear
##def sel():
##    selection = "Value = " + str(var.get())
##    label.config(text = selection)
##root = Tk()
##var = DoubleVar()
##scale = Scale( root, variable = var )
##scale.pack(anchor=CENTER)
##button = Button(root, text="Get Scale Value", command=sel)
##button.pack(anchor=CENTER)
##label = Label(root)
##label.pack()
##root.mainloop()

# Pg. 51
# Rolamento para widgets com superf�cie �til vari�vel (Text, Canvas, Entry, Listbox)
##root = Tk()
##scrollbar = Scrollbar(root)
##scrollbar.pack( side = RIGHT, fill=Y )
##
##mylist = Listbox(root, yscrollcommand = scrollbar.set )
##for line in range(100):
##    mylist.insert(END, "This is line number " + str(line))
##    
##mylist.pack( side = LEFT, fill = BOTH )
##scrollbar.config( command = mylist.yview )
##
##mainloop()

# Pg. 52
# Text:
# Exibe e permite editar texto formatado. Tamb�m suporta imagens e
# janelas embutidas
##root = None
###root = Tk()
##text = Text(root)
##text.insert(INSERT, "Hello.....")
##text.insert(END, "Bye Bye.....")
##text.pack()
##text.tag_add("here", "1.0", "1.4")
##text.tag_add("start", "1.8", "1.13")
##text.tag_config("here", background="yellow", foreground="blue")
##text.tag_config("start", background="black", foreground="green")
##
##mainloop()

# Pg. 53
# Toplevel: Uma janela separada

##root = Tk()
##top1 = Toplevel()
##top2 = Toplevel(bg="black")
##mainloop()

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.msg = Label(self, text='Tiago')
        self.msg.pack()
        self.bye = Button(self, text="Bye", command=self.quit)
        self.bye.pack()
        self.pack()
app = Application()
app.master.title("Catalogo do Mato")
app.master.geometry("100x200+900+500")
mainloop()
