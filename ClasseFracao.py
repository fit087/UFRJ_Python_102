class Fracao(object):

    def __init__(self,numerador,denominador):
        if denominador == 0: raise ZeroDivisionError()
        self.__numerador = numerador
        self.__denominador = denominador

    def get_numerador(self):
        return self.__numerador
    def get_denominador(self):
        return self.__denominador
    def set_numerador(self,valor): 
        self.__numerador = valor
    def set_denominador(self,valor):
        if valor == 0: raise ZeroDivisionError()
        self.__denominador = valor

    def fracaoIrredutivel(self):
        mdc = calculaMDC(self.__numerador,self.__denominador)
        return Fracao(self.__numerador / mdc,self.__denominador / mdc)
    def __add__(self,f):
        novoNum = self.__numerador * f.get_denominador() + f.get_numerador() * self.__denominador
        novoDen = self.__denominador * f.get_denominador()
        return Fracao(novoNum,novoDen).fracaoIrredutivel()
    def __sub__(self,f):
        novoNum = self.__numerador * f.get_denominador() - f.get_numerador() * self.__denominador
        novoDen = self.__denominador * f.get_denominador()
        return Fracao(novoNum,novoDen).fracaoIrredutivel()
    def __mul__(self,f):
        novoNum = self.__numerador * f.get_numerador()
        novoDen = self.__denominador * f.get_denominador()
        return Fracao(novoNum,novoDen).fracaoIrredutivel()
    def __div__(self,f):
        novoNum = self.__numerador * f.get_denominador()
        novoDen = self.__denominador * f.get_numerador()
        return Fracao(novoNum,novoDen).fracaoIrredutivel()
    def __neg__(self):
        novoNum = -self.__numerador
        novoDen = self.__denominador
        return Fracao(novoNum,novoDen).fracaoIrredutivel()
    def __eq__(self,f): 
        n1 = self.fracaoIrredutivel().get_numerador()
        d1 = self.fracaoIrredutivel().get_denominador()
        n2 = f.fracaoIrredutivel().get_numerador()
        d2 = f.fracaoIrredutivel().get_denominador()
        return (n1==n2 and d1==d2)
    def __repr__(self):
        return str(self.__numerador) + "/" + str(self.__denominador)

    
def calculaMDC(dividendo,divisor):
    while divisor != 0:
        temp = divisor
        divisor = dividendo % divisor
        dividendo = temp
    return dividendo


class Funcionario(object):

    def __init__(self,nome,salario,n_dep):
        self.nome = nome
        self.salario = salario
        self.n_dep = n_dep

class Assistente(Funcionario):

    def __init__(self,nome,salario,n_dep,matricula):
        Funcionario.__init__(self,nome,salario,n_dep)
        self.matricula = matriula


                          

#f1 = Fracao(input("insira o numerador"),input("insira o denominador"))
