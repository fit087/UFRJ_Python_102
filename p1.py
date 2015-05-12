def ObtemDoUsuario(txt):
    while True:
        try:
            x = input(txt)
            break
        except Exception,e:
            open("arquivo.txt","a").write(str(e) + "\n")

#y = ObtemDoUsuario("Digite um valor: ")


class VPet(object): 
    MAX = 100.0 
    MIN = 0.0 
    def __init__(self,n,f,i): 
        self.setNome(n) 
        self.setFome(f) 
        self.setIdade(i)

    def setNome(self,n):
        self.nome = n
        
    def setFome(self,f):
        if f < VPet.MIN:
            f = VPet.MIN
        if f > VPet.MAX:
            f = VPet.MAX
        self.fome = f
        
    def setIdade(self,i):
        self.idade = i
        if self.idade < VPet.MIN:
            self.idade = VPet.MIN

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getIdade(self):
        return self.idade

    def __repr__(self):
        s = object.__repr__(self) + "\n"
        s += "Nome: " + str(self.nome) + "\n"
        s += "F: " + str(self.fome) + "\n"
        s += "I: " + str(self.idade) + "\n"
        return s

    def gravar(self):
        try:
            s = "%s\n%s\n%s"%(self.nome,self.fome,self.idade)
            open("bichinho.txt","w").write(s)
        except Exception,e:
            print "Nao foi possivel salvar o bichinho. Ex: " + str(e)

    def carregar(self):
        try:
            lista = open("bichinho.txt","r").readlines()
            self.nome = str(lista[0][:-1])
            self.fome = float(lista[1][:-1])
            self.idade = int(lista[2]) 
        except Exception,e:
            print "Nao foi possivel salvar o bichinho. Ex: " + str(e)
        
    
def main(): 
    n=input("Nome do seu bichinho virtual: ") 
    pet = VPet(n,0.0,0) 
    continuar = True 
    while continuar: 
        print pet 
        pet.setFome(pet.getFome() + 10) 
        pet.setIdade(pet.getIdade() + 1) 
        acao = input("b=brincar; a=alimentar") 
        if acao=="b": 
            pet.setFome(pet.getFome() + 10) 
        elif acao=="a": 
            pet.setFome(pet.getFome() - 100)
        if pet.getIdade()>=100 or pet.getFome()==100.0: 
            continuar = False 
    print pet 
    print ("Seu bichinho viveu %d anos"%(pet.getIdade())) 
 
if __name__=="__main__": main()
