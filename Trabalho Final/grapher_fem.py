# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:40:25 2015
    Project of a grapher program to Finite Elements Models
@author: adolfo.correa
"""

from tkinter import *
#from Tkinter import *

#class menu(Menu):
#    def __init__(self, master = Tk()):
#        menu_bar = Menu.__init__(self, master)
#        #Menu.__init__(self, master)
#        file_menu = Menu(menu_bar, tearoff = 0)
#        #file_menu = Menu(self, tearoff = 0)
#        file_menu.add_command(label = "Open")
#        file_menu.add_command(label = "Save")
#        file_menu.add_command(label = "Save as")
#        file_menu.add_command(label = "Close")
#        file_menu.add_separator()
#        file_menu.add_command(label = "Exit", command = quit)
#        menu_bar.add_cascade(label = "File", menu = file_menu)
#        help_menu = menu(menu_bar, tearoff = 1)
#        #help_menu = menu(self, tearoff = 1)
#        help_menu.add_command(label = "About it")
#        menu_bar.add_cascade(label = "Help", menu = help_menu)
##        master.config(menu=menu_bar)
#        self.pack()
#
#menu = menu()
##mainloop()
#menu.mainloop()


#class menus(Frame):
#    def __init__(self, master = Tk()):
#        #menu_bar = Menu.__init__(self, master)
#        Frame.__init__(self, master)
#        #Menu.__init__(self, master)
#        menu_bar = Menu()
#        
#        
#        file_menu = Menu(menu_bar, tearoff = 100)
#        #file_menu = Menu(self, tearoff = 0)
#        
#        
#        file_menu.add_command(label = "Open")
#        file_menu.add_command(label = "Save")
#        file_menu.add_command(label = "Save as")
#        file_menu.add_command(label = "Close")
#        file_menu.add_separator()
#        file_menu.add_command(label = "Exit", command = quit)
#        
#        menu_bar.add_cascade(label = "File", menu = file_menu)
#        help_menu = Menu(menu_bar)
#        #help_menu = menu(self, tearoff = 1)
#        help_menu.add_command(label = "About it")
#        menu_bar.add_cascade(label = "Help", menu = help_menu)
#        
#        
#        master.config(menu=menu_bar)
#        self.pack()
#
##top = Tk()
##menu = menu(top)
#menu = menus()
##top.mainloop()
##mainloop()
#menu.mainloop()
##menu.mainloop()


class menus(Menu):
    #def __init__(self, master = Tk()):
    def __init__(self, master = None):
        #menu_bar = Menu.__init__(self, master)
        
        #Frame.__init__(self, master)
        Menu.__init__(self, master)
        
        #menu_bar = Menu()
        
        
        #file_menu = Menu(menu_bar, tearoff = 100)
        file_menu = Menu(self, tearoff = False)
        
        
        file_menu.add_command(label = "Open")
        file_menu.add_command(label = "Save")
        file_menu.add_command(label = "Save as")
        file_menu.add_command(label = "Close")
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = quit)
        
        #menu_bar.add_cascade(label = "File", menu = file_menu)
        self.add_cascade(label = "File", menu = file_menu)
        #help_menu = Menu(menu_bar)
        help_menu = Menu(self, tearoff = False)
        help_menu.add_command(label = "About it")
        #menu_bar.add_cascade(label = "Help", menu = help_menu)
        self.add_cascade(label = "Help", menu = help_menu)
        
        
        #master.config(menu=menu_bar)
        master.config(menu=self)
        self.pack()

#class application(Tk):
#class application(Frame):
#    def __init__(self, barra_menus=False):
#        #Tk.__init__(self, master.geometry = "100x200+900+500")
#        #Tk.__init__(self)
#        Frame.__init__(self)
#        self.master.geometry("600x400+300+100")
#        self.master.title("Grapher Finite Elements Models")
#        self.barra_menus = barra_menus
#        self.pack()

#class application(Tk):
#class main_frame(Frame):
#    #def __init__(self, barra_menus=False):
#    def __init__(self):
#        #Tk.__init__(self, master.geometry = "100x200+900+500")
#        #Tk.__init__(self)
#        Frame.__init__(self)
#        self.master.geometry("600x400+300+100")
#        self.master.title("Grapher Finite Elements Models")
#        #self.barra_menus = barra_menus
#        self.pack()

       
class application():
    def __init__(self):
        top = Tk()
        top.title("Grapher Finite Elements Models")
        top.geometry("600x400+300+100")
        #top = Tk()
        #top.master.title("Grapher Finite Elements Models")
        menu = menus(top)
        #top.pack()
        #menu.pack()
        
app = application()
app.mainloop()
    
"""    
#top = Tk()
#menu = menu(top)
menu = menus()
#top.mainloop()
#mainloop()
menu.mainloop()
#menu.mainloop()
"""
"""app = application()
#menu = menus()
menu = menus(app)
#app = application(menu)
app.mainloop()
#mainloop()
#menu.mainloop()"""