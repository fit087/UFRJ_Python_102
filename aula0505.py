#lista OO2
#exercicio 6

class GeradorCodigosUnicos():
    def __init__(self):
        self.atual = 0
    def getCodigoUnico(self):
        self.atual += 1
        return self.atual
    
class Veiculo():
    def __init__(self):
        self.atrib = G.getCodigoUnico()
    def locomover(self):
        return "Estou me locomovendo"

class Veiculoterrestre(Veiculo):
    def __init__(self,moto):
        Veiculo.__init__(self)
        self.atrib = "Veiculoterrestre" + str(self.atrib)
        self.moto = moto
    def get_atrib(self):
        return self.atrib
    def __repr__(self):
        return self.moto
    def andar(self):
        print "Estou andando"
class Veiculomilitar(Veiculo):
    def __init__(self,tanque):
        Veiculo.__init__(self)
        self.tanque = tanque
    def __repr__(self):
        return self.tanque
    def atirar(self,Veiculo):
        print "Estou atirando em "+ str(Veiculo)
class Veiculoaereo(Veiculo):
    def __init__(self,boeing):
        Veiculo.__init__(self)
        self.boeing = boeing
    def __repr__(self):
        return self.boeing
    def voar(self):
        print "Estou voando"
class F_22(Veiculomilitar,Veiculoaereo):
    pass

#para dar um numero aleatorio para cada veiculo acompanhado do seu nome
G = GeradorCodigosUnicos()

lista = []
for i in range(100):
    lista.append(Veiculomilitar("tanque"))
for i in range(100):
    lista.append(Veiculoterrestre("moto"))
for i in range(100):
    lista.append(Veiculoaereo("boeing"))
