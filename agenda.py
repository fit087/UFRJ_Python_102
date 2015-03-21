# -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This temporary script file is located here:
#C:\Users\Aluno\.spyder2\.temp.py
##Inserir contato
##Alterar
##Remover
##Nome
##Telefone
##ID
#
##Deve ser utilizado uma lista
#"""

#contatos=[]

#contatos=[["",""],["",""]]

contatos=[['Joao',"1234-5678"],["Jose","9 9999-9999"]]


def search(name):
    pos=-1
    for r,c in enumerate(contatos):
        print (r,c)
        print ('c[0]=',c[0],'==name=',name,c[0]==name)
        if c[0]==name:
            pos=r
    return pos


def inserir(name,tel):
#    id+=1
#    contatos.append(name,tel,id)
    contatos.append([name,tel])
    print ("Contato Inserido com sucesso")
    print (contatos[-1])
    print ("\v")
    
def view():
    print (contatos)
    
def deletar(name):
    pos=search(name)
    if pos>=0:
        contatos.pop(pos)
        #del contatos[pos]
    else:
        print ("Contato nao achado")
    

def alterar(name,newtel):
    pos=search(name)
    if pos>=0:
        contatos[pos][1]=newtel
    else:
        print ("Contato nao achado")


while True:
    #print "Escolha uma opcao:\n"
    print ("0. Visualizar"               )
    print ("1. Inserir um contato"   )
    print ("2. Remover um contato")
    print ("3. Alterar um contato")
    print ("4. Sair do programa"  )
    print ("Escolha uma opcao: " )
    opcao=int(input())
    
    if opcao==0:
        view()
    elif opcao==1:
        
        #Python2
        #name=raw_input("Nome: ")
        #name=name[:len(name)-1]
        #inserir(raw_input("Nome: "),str(input("Telefone: ")))
        
        #Python3
        inserir(input("Nome: "),input("Telefone: "))
        
        #Se presenta um erro quando se escreve um nome sem ""
    elif opcao==2:
        #Python2
        name=raw_input("Nome: ")
        name=name[:len(name)-1]
        
        #Python3
        #name=input("Nome: ")
        
        deletar(name)
        #pass    
    elif opcao==3:
        #Python2
        #name=raw_input("Nome: ")
        #name=name[:len(name)-1]
        #Python3
        name=input("Nome: ")
        #name=name[:len(name)-1]
        #name.pop()
        alterar(name,input("Tel.: "))
        #pass        
    elif opcao==4:
        break
    else:
        print ("Opcao invalida, tente novamente\n")