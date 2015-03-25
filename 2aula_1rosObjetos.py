##class Fone:
##    __init__(self,volume):
##        self.volume=volume
##    def pegar_volume(self):
##        return self.volume


print ("\n\n\n***************************")
print ("\t1o Exercicio")
print ("***************************\n")

class quadrado:
    def __init__(self,lado=1):
        self.lado=lado

    def mudar_lado(self,nwlado):
        self.lado=nwlado

    def get_lado(self):
        return self.lado

    def area(self):
        return self.lado**2
        
#Print Python 2

#print ("\nQuadrado\n")
#quad1=quadrado(5)
#print "quadrado(5)=",quad1.get_lado()
#quad1.mudar_lado(20)
#print "quad1.mudar_lado(20)",quad1.get_lado()
#quad1.area()
#print "quad1.area()",quad1.area()

#Print Python 3

print ("\nQuadrado\n")
quad1=quadrado(5)
print ("quadrado(5)=",quad1.get_lado())
quad1.mudar_lado(20)
print ("quad1.mudar_lado(20)",quad1.get_lado())
quad1.area()
print ("quad1.area()",quad1.area())

print ("\n\n\n***************************")
print ("\t2o Exercicio")
print ("***************************\n")


class ponto:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

##class linha(ponto):
##    def
##
##    def comprimento(self):
##        return (x**2+y**2+z**2)**.5

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

print ("\nTriangulo\n")
        
print ("\nItem a)")
A=ponto(0,0,0)
B=ponto(1,1,0)
C=ponto(1,1,1)

#Print Python 2

#print "A=punto(0,0,0)=", A.x,A.y,A.z
#print "B=ponto(1,1,1)=", B.x,B.y,B.z
#print "C=ponto(1,1,0)=", C.x,C.y,C.z
#
#print ("\nItem b)")
#AB=linha(A,B)
#print "AB.comprimento() = ", AB.comprimento()
#
#print ("\nItem c)")
#ABC=Triangulo(A,B,C)
#print "ABC.lados() = ", ABC.lados()
#print "ABC.area() = ", ABC.area()

#Print Python 3
print ("A=punto(0,0,0)=", A.x,A.y,A.z)
print ("B=ponto(1,1,1)=", B.x,B.y,B.z)
print ("C=ponto(1,1,0)=", C.x,C.y,C.z)

print ("\nItem b)")
AB=linha(A,B)
print ("AB.comprimento() = ", AB.comprimento())

print ("\nItem c)")
ABC=Triangulo(A,B,C)
print ("ABC.lados() = ", ABC.lados())
print ("ABC.area() = ", ABC.area())


print ("\n\n\n***************************")
print ("\t3o Exercicio")
print ("***************************\n")

# class bombaCombustivel:
#     def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel=0):
#         self.tipoCombustivel=tipoCombustivel
#         self.valorLitro=valorLitro
#         self.quantidadeCombustivel=quantidadeCombustivel
#     def abastecerPorValor(self,recarga):
#         self.quantidadeCombustivel+=float(recarga)/self.valorLitro
#         return self.quantidadeCombustivel
#     def abastecerPorLitro(self,recarga):
#         self.quantidadeCombustivel+=recarga
#         return self.quantidadeCombustivel
#     def alterarValor(self,nwValor):
#         self.valorLitro=nwValor
#     def alterarCombustivel(self,nwtipo):
#         self.tipoCombustivel=nwtipo
#     def alterarQCombutivel(self,nwQuantidade):
#         self.quantidadeCombustivel=nwQuantidade


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


   
print ("\nBomba de Combustivel\n")

#Print Python 2

##Inicializacao
#bomba1=bombaCombustivel("Diesel",50.40,1000)
#print "\nBombaCombustivel(\"Diesel\",50.40,1000)=",\
#bomba1.tipoCombustivel,bomba1.valorLitro,bomba1.quantidadeCombustivel
#
##AbastecerPorLitro
#print "\nAbastecerPorLitro(20)= R$ ",bomba1.abastecerPorLitro(20)
#print "Bomba1= ", bomba1.tipoCombustivel,bomba1.valorLitro,\
#bomba1.quantidadeCombustivel
#
##AbastecerPorValor
#print "\nAbastecerPorValor(150)= Lts ",bomba1.abastecerPorValor(150)
#print "Bomba1= ", bomba1.tipoCombustivel,\
#bomba1.valorLitro,bomba1.quantidadeCombustivel
#
##AlterarValor
#print "\nAlterarValor(30.32)= R$ ",bomba1.alterarValor(30.32)
#print "Bomba1= ", bomba1.tipoCombustivel,bomba1.valorLitro,\
#bomba1.quantidadeCombustivel
#
##Alterar Tipo do Combustivel
#print "\nAlterarCombustivel(\"Gasolina\")",bomba1.alterarCombustivel("Gasolina")
#print "Bomba1= ", bomba1.tipoCombustivel,bomba1.valorLitro,\
#bomba1.quantidadeCombustivel

#Print Python 3

#Inicializacao
bomba1=bombaCombustivel("Diesel",50.40,1000)
print ("\nBombaCombustivel(\"Diesel\",50.40,1000)=",\
bomba1.tipoCombustivel,bomba1.valorLitro,bomba1.quantidadeCombustivel)

#AbastecerPorLitro
print ("\nAbastecerPorLitro(20)= R$ ",bomba1.abastecerPorLitro(20))
print ("Bomba1= ", bomba1.tipoCombustivel,bomba1.valorLitro,\
bomba1.quantidadeCombustivel)

#AbastecerPorValor
print ("\nAbastecerPorValor(150)= Lts ",bomba1.abastecerPorValor(150))
print ("Bomba1= ", bomba1.tipoCombustivel,\
bomba1.valorLitro,bomba1.quantidadeCombustivel)

#AlterarValor
print ("\nAlterarValor(30.32)= R$ ",bomba1.alterarValor(30.32))
print ("Bomba1= ", bomba1.tipoCombustivel,bomba1.valorLitro,\
bomba1.quantidadeCombustivel)

#Alterar Tipo do Combustivel
print ("\nAlterarCombustivel(\"Gasolina\")",bomba1.alterarCombustivel("Gasolina"))
print ("Bomba1= ", bomba1.tipoCombustivel,bomba1.valorLitro,\
bomba1.quantidadeCombustivel)

