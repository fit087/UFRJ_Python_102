# 23/06/2015
# Lista Tkinter
#from Tkinter import *  # Tkinter para python 2
from tkinter import *   # Tkinter para python 3

# Exercise 4

##top = Tk()
##
##def exibir():
##    caminho = en.get()
##    if caminho != "":
##        try:
##            im = PhotoImage(file = caminho)
##            cv.create_image(0,0,image=im)
##            #im = PhotoImage(file = caminho)
##            #lb.configure(image = im)
##        #except:
##        except Exception, e:
##                print ("Arquivo nao encontrado")
##                print (e)
##    else:
##        print ("Caminho Nulo")
##
##en = Entry(master=top)
###en.insert(0, "img1.gif")
##en.insert(0, "./img1.gif")
##en.pack()
##bt = Button(master = top, text = "Exibir Imagem", command = exibir)
##bt.pack()
###lb = Label(master = top, image = PhotoImage(file="img1.gif"))
###lb = Label(master = top, image = PhotoImage(file="./img1.gif"))
###lb.pack()
##cv = Canvas(master=top, background="white")
##cv.pack(expand=True, fill=BOTH)#, background="white")
##btSair = Button(master = top, text = "Sair", command = top.destroy)
##btSair.pack()
##
##mainloop()

# Exercise 5
import time

##top = Tk()
##
##largura = 500
##altura = 500
##d = 450.0
##
##centro_x= largura /2.0
##centro_y= altura /2.0
##
##cv = Canvas(master=top, background="white", width=largura, height=altura)
##cv.pack(expand=True, fill=BOTH)#, background="white")
##btSair = Button(master = top, text = "Sair", command = top.destroy)
##btSair.pack()
##circulos = []
##while True:
##    # Constroe os circulos concentricos
##    for i in range(50):
##        x1,y1,x2,y2 = centro_x - d/2.0, centro_y-d/2.0, centro_x + d/2.0, \
##                      centro_y+d/2.0
##        #cv.create_oval(x1,y1,x2,y2)
##        circulos.append(cv.create_oval(x1,y1,x2,y2)) # Salva as referencias dos circulos
##                                                        # para destroir depois
##        #d = 450.0 - 50.0*i
##        d = 450.0 - 9.0*i
##        cv.update()
##        time.sleep(0.2)
##
##    for i in circulos[::-1]:
##        cv.delete(i)
##        cv.update()
##        time.sleep(0.2)
##
##    
##
##mainloop()

# Exercise 6

def clique(e):
    cv.delete(ALL)
    x1=e.x-l_ret/2.0
    y1=e.y-a_ret/2.0
    x2=e.x+l_ret/2.0
    y2=e.y+a_ret/2.0
    global ret
    #cv.move(ret,e.x,e.y)
    ret = cv.create_rectangle(x1,y1,x2,y2, fill="black")
    cv.update()

top = Tk()

largura = 500
altura = 500
l_ret = 50
a_ret = 30
#d = 450.0
d = 45.0

centro_x= largura /2.0
centro_y= altura /2.0

cv = Canvas(master=top, background="white", width=largura, height=altura)
cv.pack(expand=True, fill=BOTH)#, background="white")

cv.bind("<Button-1>",clique)

btSair = Button(master = top, text = "Sair", command = top.destroy)
btSair.pack()

x1,y1,x2,y2 = centro_x - d/2.0, centro_y-d/2.0, centro_x + d/2.0, \
                      centro_y+d/2.0
cv.create_rectangle(x1,y1,x2,y2, fill='black')
cv.update()
 
cv.update()
time.sleep(0.2)

ret = None
    

mainloop()
