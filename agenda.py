# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Aluno\.spyder2\.temp.py
"""

#Inserir contato
#Alterar
#Remover
#Nome
#Telefone
#ID

#Deve ser utilizado uma lista

#contatos=[]

#contatos=[["",""],["",""]]

contatos=[["Joao","1234-5678"],["Jose","9 9999-9999"]]

#id=0

def inserir(name,tel):
#    id+=1
#    contatos.append(name,tel,id)
    contatos.append([name,tel])
    print "Contato Inserido com sucesso"
    print contatos[-1]
    print "\v"

def view():
    print contatos

#def deletar(name):
#    contatos.
#    contatos.remove

#def alterar(name,tel):
#    contatos.
#    contatos.remove

def alterar(name,newtel):
    pass
#    contatos.
#    contatos.remove


#inserir('hola',12314234)
#print contatos

while True:
    print "Escolha uma opcao:\n"
    print "0. Visualizar"
    print "1. Inserir um contato"
    print "2. Remover um contato"
    print "3. Alterar um contato"
    print "4. Sair do programa"
    print "Escolha uma opcao "
    opcao=input()

    if opcao==0:
        view()
    elif opcao==1:
#        name=raw_input("Digite o nome do contato")
#        tel=input("Digite o telefone do contato")
#        inserir(name,tel)
        inserir(str(input("Nome: ")),str(input("Telefone: ")))
    elif opcao==2:
#        deletar(name)
        deletar(str(input("Nome: ")))
        pass
    elif opcao==3:
        alterar()
        pass
    elif opcao==4:
        break
    else:
        print "Opcao invalida, tente novamente\n"
