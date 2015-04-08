
"""
Created on Mon Apr 08 10:53:32 2015
    Slide da aula 2. Metodos nativos das classes do python
@author: adolfo.correa
"""
class Carro:
    def __init__(self,nr):
        self.__nrodas = nr
    def __add__(self,car):
        return self.__nrodas + car.get_nr()
    def __repr__(self):
        return "Eu sou um carro de %d rodas!" % self.__nrodas
    def __cmp__(self, car):
        return cmp(self.__nrodas, car.get_nr())
    def get_nr(self):
        return self.__nrodas

a=Carro(4);b=Carro(6)
print a + b
print a>b
print a

#a + b
#a>b
#a

class objeto(object):
    pass

obj=objeto()
