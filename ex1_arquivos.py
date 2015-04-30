# Tue 28/04/2015
# Autor: Professor Igor Leao
import random

resultado = ""

for j in range(300):
    for i in range(10):
        resultado += chr(random.randint(ord("a"),ord("z")))
    resultado += "\n"

open("arquivo.txt","w").write(resultado)

def conta():
    alfabeto = [0 for i in range(26)]
    conteudo = open("arquivo.txt","r").readlines()
    #for l in conteudo:
    #    print l[:-2]
    for l in conteudo:
        for c in l[:-2]:
            alfabeto[ord(c) - ord("a")] += 1
            
    for i,j in enumerate(alfabeto):
        print chr(i + ord("a")) + ": " + str(j)

def copia():
    while True:
        origem = input("Entre com o nome do arquivo de origem: ")
        destino = input("Entre com o nome do arquivo de destino: ")
        conteudo = ""

        try:
            arq_origem = open(origem,"r")
            #arq_origem2 = open(origem,"r")
            #arq_origem2.close()
            conteudo = arq_origem.readlines()
            arq_origem.close()
            #conteudo = open(origem,"r").readlines()
            arq_destino = open(destino,"w")
            #arq_destino2 = open(destino,"w")
            #arq_destino2.write("alguma coisa")
            #arq_destino2.close()
            for i in conteudo:
                arq_destino.write(i)
            #arq_destino.write(str(conteudo))
            arq_destino.close()
            #open(destino,"w").write(conteudo)\
        except Exception,e:
            print "Tente novamente\n" + str(e)
        else:
            break

def copia_limpa():
    origem = input("Entre com o nome do arquivo de origem: ")
    destino = input("Entre com o nome do arquivo de destino: ")
    conteudo = ""

    arq_origem = open(origem,"r")
    conteudo = arq_origem.readlines()
    arq_origem.close()
    arq_destino = open(destino,"w")
    for i in conteudo:
        arq_destino.write(i)
    arq_destino.close()
        
def filtra():
    origem = input("Entre com o nome do arquivo de origem: ")
    destino = input("Entre com o nome do arquivo de destino: ")
    caract = input("Entre com o caracter: ")
    conteudo = ""

    arq_origem = open(origem,"r")
    conteudo = arq_origem.readlines()
    arq_origem.close()
    arq_destino = open(destino,"w")
    for i in conteudo:
        if caract in i[:-2]:
            arq_destino.write(i)
    arq_destino.close()
            
















    
    

    
    
