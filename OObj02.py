# -*- coding: latin1 -*-

"""
Created on Sun Apr 12 18:00:32 2015
    Lista de Exercicios:    Orientacao a objetos 02
    File:                   Lista_OO_2.pdf
    Curso:                  Computacao II (MAB225)
    Professor:              Igor Leao
@author: Adolfo Emmanuel Correa Lopez
"""

# ---------------Primer Exercicio------------------
class fraction(object):
    """
    This class allows represent and operate a fraction
    """

    def __init__(self, num, dem):
        """
        The constructor define the attributes numerator and denominator
        """
        if dem == 0: raise ZeroDivisionError()
        self.__num = num
        self.__dem = dem

    def get_num(self):
        """
        This method return the numerator
        """
        return self.__num

    def get_dem(self):
        """
        This method return the denominator
        """
        return self.__dem

    def get_cociente(self):
        """
        This method return the cociente
        """
        return float(self.__num)/self.__dem

    # Protected Function for use into the class and
    # subclass
    def _euclides_mdc(self, dividendo, divisor):
        """
        The Euclid algorithm to compute the
        greatest common divisor (gcd).
        """
        while divisor != 0:
            temp = divisor
            divisor = dividendo % divisor
            dividendo = temp
        return dividendo

    def _least_common_multiple(self, num1, num2):
        return num1 * num2 // self._euclides_mdc(num1, num2)


    def irreducible_fraction(self):
        divisor = self._euclides_mdc(self.__num,self.__dem)
        num = self.__num // divisor
        dem = self.__dem // divisor
        irreducible = fraction(num, dem)
        return irreducible

    def __repr__(self):
        return str(self.__num) + "/" + str(self.__dem)

    def __add__(self, op_2):
        #com_den = self.__dem * op_2.__dem // \
        #self._euclides_mdc(self.__dem, op_2.__dem)
        com_den = self._least_common_multiple(self.__dem, op_2.__dem)
        num = com_den // self.__dem * self.__num + com_den // op_2.__dem *\
        op_2.__num
        soma = fraction(num, com_den)
        soma = soma.irreducible_fraction()
        return soma

    def __sub__(self, op_2):
        com_den = self._least_common_multiple(self.__dem, op_2.__dem)
        num = com_den // self.__dem * self.__num - com_den // op_2.__dem *\
        op_2.__num
        subt = fraction(num, com_den)
        subt = subt .irreducible_fraction()
        return subt

    def __mul__(self, op_2):
        mulpl = fraction(self.__num * op_2.__num, self.__dem * op_2.__dem)
        mulpl = mulpl.irreducible_fraction()
        return mulpl

    def __div__(self, op_2):
        #div = fraction(self.__num * op_2.__dem, self.__dem * op_2.__num)
        #div = div.irreducible_fraction()
        #return self * (not op_2)
        return self * op_2.inv()
        #return self.__mul__(op_2.inv())

        #return div
# neg inversa()
    #def __neg__(self):
    #    aux = self.__num
    #    self.__num = self.__dem
    #    self.__dem = aux
    #    return self
    
    def inv(self):
        aux = self.__num
        self.__num = self.__dem
        self.__dem = aux
        return self

        
    def __neg__(self):
        return fraction(-self.__num, self.__dem)
        
# Funciona também mas achei melhor comparar os strings que representam as
# frações irreducíveis pois se reduz o erro de precisão na divisão
#    def __eq__(self, op_2):
#        # return self.irreducible_fraction() == op_2.irreducible_fraction()
#        # return cmp(self.irreducible_fraction(), op_2.irreducible_fraction())
#        #if self.irreducible_fraction().__num == op_2.irreducible_fraction().__num \
#        #    and self.irreducible_fraction().__dem == op_2.irreducible_fraction().__dem
#        #    op = True
#        #else:
#        #        op = False
#        #return op
#        return self.get_cociente() == op_2.get_cociente()

    def __eq__(self, op_2):
        #return self.irreducible_fraction.__repr__() == op_2.irreducible_fraction.__repr__() # Não funciona
        return repr(self.irreducible_fraction()) == repr(op_2.irreducible_fraction()) # Funciona
        #return str(self.irreducible_fraction()) == str(op_2.irreducible_fraction()) # Funciona


# ---------------Segundo Exercicio------------------
class funcionario(object):
    def __init__(self, name, salary, num_dependents):
        self.name = name
        self.salary = salary
        self.dependents = num_dependents
        
    def data_list(self):
        return str(self.name) + "\n" + \
                   str(self.salary) + "\n" + \
                   str(self.dependents) + "\n"
                   
class assistente(funcionario):
    def __init__(self, name, salary, matricula):
        super(assistente, self).__init__(name, salary, num_dependents=0)
        self.__matricula = matricula
        
    def get_matricula(self):
        return self.__matricula
        
    def data_list(self):
        func_data=super(assistente, self).data_list()
        return func_data+str(self.__matricula) + "\n"

class assistente_tecnico(assistente):
    def __init__(self, name, salary, matricula, bonus):
        super(assistente_tecnico, self).__init__(name, salary, matricula)
        self.__bonus = bonus
    def data_list(self):
        assis_data=super(assistente_tecnico, self).data_list()
        return assis_data + str(self.__bonus) + "\n"
        
class assistente_admin(assistente):
    def __init__(self, name, salary, matricula, turno):
        super(assistente_admin, self).__init__(name, salary, matricula)
        self.__turno = turno
    def data_list(self):
        assis_data=super(assistente_admin, self).data_list()
        return assis_data + str(self.__turno) + "\n"

# ---------------Tercer Exercicio------------------
# ----Item a-----
class Animal(object):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def caminha(self):
        return str(self.name) + " caminhando"

class dog(Animal):
    #def __init__(self, name, breed):
    #    super(cachorro, self).__init__(name, breed)
    def late(self):
        return str(self.name) + " latindo"

class cat(Animal):
    def mia(self):
        return str(self.name) + " miando"

# ----Item b-----        
class person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
class rich(person):
    def __init__(self, name, age, dinheiro):
        super(rich, self).__init__(name, age)
        self.dinheiro = dinheiro
    def buy(self):
        return str(self._name) + " faz compras"
        
class poor(person):
    def work(self):
        return str(self._name) + " trabalha"
        
class miserable(person):
    def beg(self):
        return str(self._name) + " mendiga"

# ---------------Quarto Exercicio------------------
class ingress(object):
    def __init__(self, value):
        self.__value = value
    
    def get_value(self):
        return self.__value

class vip(ingress):
    def __init__(self, value, prima):
        super(vip, self).__init__(value)
        self.__prima = prima

    def get_value(self):
        return super(vip, self).get_value() + self.__prima

class normal(ingress):
    pass
    
class camarote_inf(vip):
    def location(self):
        return "1ro andar do lado do palco"

class camarote_sup(vip):
    def __init__(self, value, prima1, prima2):
        super(camarote_sup, self).__init__(value, prima1)
        self.prima2 = prima2
    def location(self):
        return "2ro andar do lado do palco"
    
    def get_value(self):
        return super(camarote_sup, self).get_value() + self.prima2

# ---------------Quinto Exercicio------------------
class imovel(object):
    def __init__(self, adress, price):
        self.adress = adress
        self.price = price

class new(imovel):
    def __init__(self, adress, price, ad_price):
        imovel.__init__(self, adress, price)
        #imovel.__init__(adress, price)
        self.__ad_price = ad_price
    def set_ad_price(self, nw_ad_price):
        self.__ad_price = nw_ad_price
    def get_ad_price(self):
        return self.__ad_price
class old(imovel):
    def __init__(self, adress, price, desconto):
        imovel.__init__(self, adress, price)
        #imovel.__init__(adress, price)
        self.__desconto = desconto
    def set_desconto(self, nw_desconto):
        self.__desconto = nw_desconto
    def get_desconto(self):
        return self.__desconto

# ---------------Sexto Exercicio------------------
import random as rand



class vehicle(object):
    def __init__(self, code):
        self._code = code
    def locomover(self): pass
    
class air_vehicle(vehicle):
    def fly(self):
        return str(self)+" voando"
    
class military_vehicle(vehicle):
    #def __init__(self):
    def fire(self, alvo):
        return str(self)+" atirando em "+str(alvo)
    
class land_vehicle(vehicle):
    def run(self):
        return str(self)+" andando"

class civil_vehicle(vehicle):
    def axcidental_hit(self, oth_vehicle):
        return str(self)+" bateu com "+str(oth_vehicle)

class boeing(air_vehicle, civil_vehicle):
    "Avião de Passageiros"
    def __init__(self, code, n_passengers):
        vehicle.__init__(self, code)
        self.__n_passengers = n_passengers
    def __repr__(self):
        return "Boeing "+str(self._code)
        
class f_22(air_vehicle, military_vehicle):
    "Caça de combate"
    def __init__(self, code, n_missil):
        vehicle.__init__(self, code)
        self.__n_missil = n_missil
    def __repr__(self):
        return "F-22 "+str(self._code)
        
class tank(military_vehicle, land_vehicle):
    "Tanque"
    def __init__(self, code, shield):
        vehicle.__init__(self, code)
        self.__shield = shield
    def __repr__(self):
        return "Tank "+str(self._code)
        
class moto(land_vehicle, civil_vehicle):
    "Motocicleta"
    def __init__(self, code, gasoil):
        vehicle.__init__(self, code)
        self.__gasoil = gasoil
    def __repr__(self):
        return "Moto "+str(self._code)
        



if __name__ == '__main__':
    print ("\n\n\n***************************")
    print ("\t1o Exercicio")
    print ("***************************\n")
    
    TAN = fraction(15, 90)
    TAN1 = fraction(90, 15)
    TAN2 = fraction(5, 30)
    #TAN3 = fraction(1,0)
    TAN4 = fraction(3, 18)
    print ("TAN", TAN)
    print ("TAN1", TAN1)
    print ("TAN2", TAN2)
    #print ("TAN3", TAN3)
    print ("TAN4", TAN4)
    print ("TAN.irreducible_fraction()", TAN.irreducible_fraction())
    print ("TAN1.irreducible_fraction()", TAN1.irreducible_fraction())
    print ("TAN2.irreducible_fraction()", TAN2.irreducible_fraction())
    print ("TAN4.irreducible_fraction()", TAN4.irreducible_fraction())
    print ("TAN == TAN1", TAN == TAN1)
    print ("TAN == TAN2", TAN == TAN2)
    print ("TAN == TAN4", TAN == TAN4)
    print ("not TAN2", (not TAN2))
    print ("-TAN2",  -TAN2)
    
    print ("TAN2.inv()", TAN2.inv())
    print ("TAN + TAN1", TAN + TAN1)
    print ("TAN - TAN1", TAN - TAN1)
    print ("TAN * TAN1", TAN * TAN1)
    #print ("TAN / TAN1", TAN / TAN1) # Só funciona em python 2.x.x
    
    print ("\n\n\n***************************")
    print ("\t2o Exercicio")
    print ("***************************\n")
    
    director = funcionario("Javier", 10000, 5)
    asistent = assistente("Jorge", 1000, 5885698752)
    asis_admin = assistente_admin("Jose", 800, 4340987654, "Diurno")
    asis_tecnico = assistente_tecnico("Mario", 500, 4340998752, 400)
    
    print ("director.data_list()\n", director.data_list())
    print ("asistent.data_list()\n", asistent.data_list())
    print ("asistent.get_matricula()\n", asistent.get_matricula())
    print ("asis_admin.data_list()\n", asis_admin.data_list())
    print ("asis_tecnico.data_list()\n", asis_tecnico.data_list())
    
    print ("\n\n\n***************************")
    print ("\t3o Exercicio")
    print ("***************************\n")
    
    print ("\nItem a)")
    print ("\nAnimais\n")
    
    gato=cat("Orion", "siames")
    cachorro=dog("Tomy", "Labrador")
    
    print ("gato.mia()\t", gato.mia())
    print ("cachorro.late()\t", cachorro.late())
    print ("gato.caminha()\t", gato.caminha())
    print ("cachorro.caminha()\t", cachorro.caminha())
    
    print ("\nItem b)")
    print ("\nPessoas\n")
    
    rico = rich("Richard", 37, 1000000)
    pobre = poor("Joao", 40)
    mendigo = miserable("Alex", 27)
    
    print ("rico.buy()\t", rico.buy())
    print ("pobre.work()\t", pobre.work())
    print ("mendigo.beg()\t", mendigo.beg())

    print ("\n\n\n***************************")
    print ("\t4o Exercicio")
    print ("***************************\n")
    
    ingresso_vip = vip(10, 5)
    ingresso_comum = normal(10)
    ingresso_camsup = camarote_sup(10, 8, 6)
    ingresso_caminf = camarote_inf(10, 8)
    
    print ("ingresso_comum.get_value\t", ingresso_comum.get_value())
    print ("ingresso_vip.get_value\t", ingresso_vip.get_value())

    #opcao = int(input("Desea excecutar o programa? "))
    opcao = 0
    if opcao:

        while True:
            print ("\n\n\t***Menu: Venta de Ingressos***\n")
            print ("\t\t1: Normal\n")
            print ("\t\t2: VIP\n")
            opcao = input("\t\tOpcao: ")
            if opcao == "2":
                print ("\n\t\t1: Camarote Superior\n")
                print ("\t\t2: Camarote Inferior\n")
                opcao = input("\t\tOpcao: ")
                if opcao == "1":
                    print ("\n\tCamarote Superior\tValor: %.2f R$"%ingresso_camsup.get_value())
                if opcao == "2":
                    print ("\n\tCamarote Inferior\tValor: %.2f R$"%ingresso_caminf.get_value())
            else:
                #print ("\n\tIngresso comum\tValor: ", ingresso_comum.get_value())
                print ("\n\tIngresso comum\tValor: %.2f R$"%ingresso_comum.get_value())
            opcao = input ("Desea comprar outro ingrasso? (Y/N): ")
            if opcao.lower() == "y":
                continue
            break

    print ("\n\n\n***************************")
    print ("\t5o Exercicio")
    print ("***************************\n")

    imovel_velho = old("praia de copacabana", 50000, 10)
    imovel_novo = new("Fundao", 30000, 10)

    #opcao = int(input("Desea excecutar o programa? "))
    opcao = 0
    if opcao:

        while True:
            print ("\n\n\t***Menu: Venta de Inmovéis***\n")
            print ("\t\t1: Novo\n")
            print ("\t\t2: Velho\n")
            opcao = input("\t\tOpcao: ")
            if opcao == "1" or opcao == 1:
                    print ("\n\tVc comprou um imovel novo\tValor: %.2f R$"%imovel_novo.get_ad_price())    
            if opcao == "2" or opcao == 2:
                print ("\n\t\tVc comprou um imovel velho\n", imovel_velho.get_desconto())
            opcao = input ("Desea comprar outro imovel? (Y/N): ")
            if opcao.lower() == "y":
                continue
            break


    print ("\n\n\n***************************")
    print ("\t6o Exercicio")
    print ("***************************\n")

    print (rand.randint(0,10))

    #n_vehicles = int(input("Numero de vehiculos "))
    n_vehicles = 10
    lista=[0]*n_vehicles
    for it in range(n_vehicles):
        random_number = rand.randint(1,4)
        if random_number == 1:
            lista[it] = boeing(it, 200)
        elif random_number == 2:
            lista[it] = f_22(it, 5)
        elif random_number == 3:
            lista[it] = tank(it, 5)
        elif random_number == 4:
            lista[it] = moto(it, 5)

    print(lista)
#    print("\n\n",type(lista[0]))
#    print("\n\n",dir(lista[0]))
#    print("\n\n",dir(lista[0])[0])
#    print("\n\n",dir(lista[0])[4])
    #s = dir(lista[0])[4]
    #print("\n\n",lista[0].s)
    # Por turno
    # duvida 1 turno pode ser a ação de 1 veiculo ou a ação de todos
    # os veiculos e o jogo termina quando todos morirem.
    for vehicle in lista: # 1o Turno
        acao = rand.randint(1,3)
        #vehicle.dir(vehicle)[-1]
        #if repr(type(vehicle)) == "<class '__main__.boeing'>":
        if type(vehicle) is boeing:
            print(vehicle.fly())
            print(vehicle.axcidental_hit(vehicle))
        elif type(vehicle) is f_22:
            print(vehicle.fly())
            print(vehicle.fire(vehicle))
        elif type(vehicle) is tank:
            print(vehicle.run())
            print(vehicle.fire(vehicle))
        elif type(vehicle) is moto:
            print(vehicle.run())
            print(vehicle.axcidental_hit(vehicle))
    

# print(TAN._fraction__num) # quebrando o encapsulament
