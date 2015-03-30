# -*- coding: latin1 -*-

"""
Created on Sun Mar 29 22:00:32 2015
    Lista de Exercicios:    Orientacao a objetos 02
    Curso:                      Computacao II (MAB225)
    Proffessor:                Igor Leao
@author: Adolfo Emmanuel Correa Lopez
"""

#---------------Primer Exercicio------------------

class fracao:

    def __init__(self,num,den):
        if den!=0:
            self.num=num
            self.den=den
            
    def get_num_den(self):
        return self.num,self.den
        
    def set_num_den(self,num,den):
        self.__init__(num,den)
        
        
#Calcula MDC
def euclides_mdc(dividendo, divisor):
    """Calcula o Maximo divisor comum
        int, int --> int"""
    while divisor <> 0:
        temp = divisor
        divisor = dividendo % divisor
        dividendo = temp
    return dividendo
    
def fra_irredutivel(fracao):
    """Fracao irredutivel
        fracao (obj) --> fracao (obj)"""
    mdc=euclides_mdc(fracao.get_num_den()[0],fracao.get_num_den()[1])
    fra_irred=map(lambda x: x/mdc,fracao.get_num_den())
    #fra_irred=[x/mdc for x in fracao.get_num_den()]
      
    #num,den=fracao.get_num_den()[0]/mdc,fracao.get_num_den()[1]/mdc
    #fracao.set_num_den(num,den)
    
    fracao.set_num_den(fra_irred[0],fra_irred[1])
    #fracao.set_num_den(fra_irred[:])
    return fracao

#-------------Segundo Exercicio------------------