# -*- coding: latin1 -*-

"""
Created on Sun Mar 29 22:00:32 2015
    Lista de Exercicios:    Orientacao a objetos 02
    Curso:                      Computacao II (MAB225)
    Proffessor:                Igor Leao
@author: Adolfo Emmanuel Correa Lopez
"""

#import exer2_lib as lib
from exer2_lib import *


print ("\n\n\n***************************")
print ("\t1o Exercicio")
print ("***************************\n")

#cociente=lib.fracao(4,3)
cociente=fracao(4,3)
infinito=fracao(4,0)
indeterminado=fracao(0,0)

#print ("cociente.num=",cociente.num, end=" ")
print ("cociente.num=",cociente.num,)
print ("cociente.den=",cociente.den)

print ("cociente.get_num_den=",cociente.get_num_den())

print ("cociente.get_num_den[0]=",cociente.get_num_den()[0])
print ("cociente.get_num_den[1]=",cociente.get_num_den()[1])

print ("cociente.set_num_den(1,2)=",cociente.set_num_den(1,2))

print ("cociente.get_num_den=",cociente.get_num_den())

#print ("infinito.get_num_den=",infinito.get_num_den())

print ("euclides_mdc(27,9)= ",euclides_mdc(27,9))

print ("euclides_mdc(18,6)= ",euclides_mdc(18,6))

prueva=fracao(6,18)
prueva2=fracao(18,6)

print ("fra_irredutivel(6,18)= ",fra_irredutivel(prueva).get_num_den())

print ("fra_irredutivel(18,6)= ",fra_irredutivel(prueva2).get_num_den())