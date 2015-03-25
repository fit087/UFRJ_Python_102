class quadrado:
    def __init__(self,lado=1):
        self.lado=lado

    def mudar_lado(self,nwlado):
        self.lado=nwlado

    def get_lado(self):
        return self.lado

    def area(self):
        return self.lado**2

class linha:
    def __init__(self,A,B):
        self.A=A
        self.B=B

    def comprimento(self):
        x=self.B.x-self.A.x
        y=self.B.y-self.A.y
        z=self.B.z-self.A.z
        return (x**2+y**2+z**2)**.5
        
class Triangulo:
    def __init__(self,A,B,C):
        #Pontos
        self.A=A
        self.B=B
        self.C=C
    def lados(self):
        #Linhas
        lado1=linha(self.A,self.B)
        lado2=linha(self.B,self.C)
        lado3=linha(self.C,self.A)
        return lado1.comprimento(),lado2.comprimento(),\
               lado3.comprimento()
    def area(self):
        ab=self.lados()[0]
        bc=self.lados()[1]
        ca=self.lados()[2]
        p=(ab+bc+ca)/2
        area=(p*(p-ab)*(p-bc)*(p-ca))**0.5
        return area
        
class bombaCombustivel:
    """bombaCombustivel(T,x,y)

Trigonometric sine, element-wise.

Parameters
----------
T : String
    Tipo do Combustivel
x : float
    Valor do combustivel por litro.
y : float
    Quantidade no tanque.
    

Atributos
-------
T : String
    Tipo do Combustivel
x : float
    Valor do combustivel por litro.
y : float
    Quantidade no tanque.

Methods
--------

abastecerPorValor(x):
    x:  float
        Recarga em valor monetario.
abastecerPorLitro(x):
    x:  float
        Recarga em litros.
alterarValor(x):
    x:  float
        Novo Valor do combustivel por litro.
alterarCombustivel(T):
    T : String
         Novo Tipo do Combustivel
alterarQCombutivel(y):
    y : float
        Actualizacao da Quantidade no tanque.

Notes
-----
Exercicios da 2a Semana de Aula de Computacao UFRJ com o 
Professor Igor Leao.

Examples
--------
Inicializacao:

>>> bomba1=bombaCombustivel("Diesel",50.40,1000)


Print abastecimento por valor:

>>> bomba1.abastecerPorValor(150)

Print abastecimento por litro:

>>> bomba1.abastecerPorLitro(20)
"""
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel=0):
        self.tipoCombustivel=tipoCombustivel
        self.valorLitro=valorLitro
        self.quantidadeCombustivel=quantidadeCombustivel
    
    def abastecerPorValor(self,recarga):
        Lts=float(recarga)/self.valorLitro
        self.alterarQCombutivel(Lts)
        return Lts
        
    def abastecerPorLitro(self,recarga):
        self.alterarQCombutivel(recarga)
        pagar=recarga*self.valorLitro
        return pagar
        
    def alterarValor(self,nwValor):
        self.valorLitro=nwValor
        
    def alterarCombustivel(self,nwtipo):
        self.tipoCombustivel=nwtipo
        
    def alterarQCombutivel(self,saida):
        self.quantidadeCombustivel-=saida
