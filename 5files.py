# -*- coding: latin1 -*-
# 16/06/2015
"""
Created on Thu Apr 16 14:20:32 2015
    Lista de Exercicios:        Arquivos
    File:                       lista Arquivos.pdf
    Curso:                      Computacao II (MAB225)
    Proffessor:                 Igor Leao
@author: Adolfo Emmanuel Correa Lopez
"""

import random

# Exercise 1

def random_txt():
    "Make a file with random lines"
    resultado = ""
    for linha in range(300):
            for i in range(10):
                    resultado += chr(random.randint(ord("a"),ord("z")))
            resultado += "\n"

    open("5file.txt", "w").write(resultado)

def conta():
    "Count the frequency of any letter in the file"
    #alfabeto = [0]*26
    alfabeto = [0 for i in range(26)]
    conteudo = open("5file.txt", "r").readlines()
    for l in conteudo:
        for c in l[:-2]: #l[:-2] # tem um \n (newline) q foi lido p/ readlines
            alfabeto[ord(c) - ord("a")] += 1
    return alfabeto

def print_dic(lista_dic):
    "Print in format of dictionary"
    for i, j in enumerate(lista_dic):
        print chr(i + ord("a")) + ":" + str(j)
        
    # Exercise 2
def visualize_file(file_named):
    print (open(file_named).readlines())
    
if __name__ == '__main__':

 # Exercise 1
    print ("\n\n\n***************************")
    print ("\t1o Exercicio")
    print ("***************************\n")
    random_txt()
    valores = conta()
    print_dic(valores)
    
    # Exercise 2
    print ("\n\n\n***************************")
    print ("\t2o Exercicio")
    print ("***************************\n")
    
    visualize_file("5file.txt")
    #visualize_file(NomeArquivo) 
