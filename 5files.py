# -*- coding: utf8 -*-
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
import sys
import os.path


# Own Library

def name_file_func():
    fn = input("Name of file: ").strip()
    
#    if not os.path.exists(fn):
#        print ("Tente outra vez...")
#        sys.exit()
    while not (os.path.exists(fn)):
        print ("Tente outra vez...")
        print (fn)
        fn = input("Name of file: ").strip()
        #sys.exit()
        
    # Numerando as linhas
    #for i, s in enumerate(open(fn)):
    #    print (i + 1, s, end='')
    return fn

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
        print (chr(i + ord("a")) + ":" + str(j))
        
    # Exercise 2
def visualize_file(file_named):
    print (open(file_named).readlines())
    
def visualize_file2(file_named):
    with open(file_named) as file:
        for line in file:
            sys.stdout.write(line)

    
    # Exercise 3
def sum_column(name_file):
    file = open(name_file, 'r')
    sum = 0
    for line in file:
        sum += int(line)
    file.close()
    return sum

def sum_all(name_file):
    file = open(name_file, 'r')
    sum = 0
    for line in file:
        list_line = str.split(line)
        #print (list_line)
        for i_list_line in list_line:
            #print (i_list_line)
            sum += int(i_list_line)
    file.close()
    return sum

    # Exercise 4
def read_column(name_file, column_n = 0):
    with open(name_file, 'r') as file:
        #all_lines = file.readlines()
        column = []
        for line in file:
            line = line.split()
            #print (line)
            column.append(line[column_n])
            #print file.seek()
    return column
    
    # Exercise 5
#def enumerate_lines(name_file = name_file()):

def enumerate_lines(name_file):
    #name_file = name_file_func()
        
    # Numerando as linhas
    for i, s in enumerate(open(name_file)):
        print (i + 1, s, end="")      

     # Exercise 6
def non_commented_lines(name_file):
    with open(name_file, 'r') as file:
        counter = 0
        for line in file:
            #if not (line[0] == "#" or line[0] == "\n"):
            #line = str.split(line)
            line = line.split()
            #print (line)
            if len(line):
                if not (line[0][0] == "#"):
                    counter += 1
                    #print("hello")
    return counter
    
    # Exercise 7
def gallows_game(name_file, type_of_file = True):
    with open(name_file) as file:
        data = file.readlines()
    #if type_of_file:
    word = data[random.randint(0, len(data)-1)].strip()
    characters = []
    characters.extend(word)
    char2print = characters[:]
    #characters[:] = word
    #print(characters)
    #print (range(int(len(characters)/2)))
    #position = random.randint(0, len(characters))
    
    # Oculta alguns caracteres aleatoriamente e guarda uma lista
    # com as solucoes
    solution = []
    positions_list = []
    for i in range(int(len(characters)/2)):
        position = random.randint(0, len(characters)-1)
        #print(position, end = ' ')
        #while position in positions_list:
        #    position = random.randint(0, len(characters))
        #positions_list.append(position)
        solution.append(characters[position])
        char2print[position] = "_."
    print (''.join(char2print))
    print (word)
    chances = 5
    #while len(resposta):
    while solution and chances:
        chances -= 1
        resposta = input("Digite a letra: ")
        if resposta in solution:
            solution.remove(resposta)
            char2print[characters.index(resposta)] = resposta
            print (''.join(char2print))
        else:
            print ("Try again...")
    print (word)
        


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
    
    # Exercise 3
    print ("\n\n\n***************************")
    print ("\t3o Exercicio")
    print ("***************************\n")
    visualize_file("5file3Exc.txt")
    print("sum_column(\"5file3Exc.txt\")", sum_column("5file3Exc.txt"))
    visualize_file("5file3Exc_2.txt")
    print("sum_column(\"5file3Exc_2.txt\")", sum_all("5file3Exc_2.txt"))
    
    # Exercise 4
    print ("\n\n\n***************************")
    print ("\t4o Exercicio")
    print ("***************************\n")
    visualize_file2("5file4Exc.txt")
    print("\nread_column(\"5file4Exc.txt\")", read_column("5file4Exc.txt"))
    print("\nread_column(\"5file4Exc.txt\")", read_column("5file4Exc.txt", 5))
    
    # Exercise 5
    print ("\n\n\n***************************")
    print ("\t5o Exercicio")
    print ("***************************\n")
    #enumerate_lines(name_file = "5file.txt")
    enumerate_lines("5file.txt")
    
    # Exercise 6
    print ("\n\n\n***************************")
    print ("\t6o Exercicio")
    print ("***************************\n")
    print("\n non_commented_lines(\"5.2aula_lib - Prova.py\")", 
        non_commented_lines("5.2aula_lib - Prova.py"))
        
    # Exercise 7
    print ("\n\n\n***************************")
    print ("\t7o Exercicio")
    print ("***************************\n")
    gallows_game("5file.txt")

    
    

