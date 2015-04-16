# -*- coding: latin1 -*-
# 14/04/2015
"""
Created on Tue Apr 14 10:20:32 2015
    Lista de Exercicios:  Execoes
    File:                         lista Excecoes.pdf
    Curso:                      Computacao II (MAB225)
    Proffessor:                Igor Leao
@author: Adolfo Emmanuel Correa Lopez
"""
import sys

# Exercise 1

#class MinhaExcecao(Exception): pass
#class Exc2(MinhaExcecao): pass
#
#try:
#    sys.exit()
#    a = eval(input("Entre com um numero "))
#    b = eval(input("Entre com outro numero "))
#    if b==500:
#        raise Exc2("Não pode dividir por 500")
#    if b == 1000:
#        raise MinhaExcecao("Não pode dividir por 1000")
#    print(a, "/", b, "=", a/b)
#    print("Essa linha nao executa se b=0")
#except ZeroDivisionError:
#    print("Ooops, divisão por zero")
#except TypeError:
#    print("Ooops, você não deu um número")
#except MinhaExcecao as e:
#    print(e)
#except Exception as e:
#    print("Deu um bode qualquer:",e)
#except:
#    #raise Exc2("Ola")
#    print("Deu um bode qualquer")
#    #raise
#    raise Exc2("Ola estou no bloco except")
#else:
#    print("Nenhum except disparou")
#finally:
#    print("sempre executado")
#    #raise MinhaExcecao
#    #raise MinhaExcecao("Mensagem que eu escrevi")
#
#print ("Olá, o programa continua")

# Exercise 2

#class entradaInvalida(ValueError): pass
class entradaInvalida(Exception): pass


def obtem_do_usuario(text):
    #flag = True
    #while flag:
    while 1:
        try:
            entrada = float(input(text))
         #   flag = False
            break
        #except entradaInvalida as e:
        except Exception as e:
            print ("Bloco except ", e)
 #       else:
 #           flag = False
    return entrada

    
    
    
def exemplo():
    lst = []
    for i in range(3):
        while 1:
            try:
                lst.append(int(input('Digite um valor: ')))
                break
            except:
                print ('Digite somente numeros!!!')

# Exercise 7

#class MinhaExcecao(Exception):
#    def __init__(self, x): # sobre escreve o metodo nativo init
#        #Exception.__init__(self) # Para nao apagar o conteudo do metodo init
#        self.x = x
#
#def funcaoA():
#    try:    
#        funcaoB()
#    except MinhaExcecao as e: # para capturar a excecao
#        print(e.x)
#        e.x = 2
#        raise
#               
#    
#def funcaoB():
#    raise MinhaExcecao(x = 1) # Levanta uma exceção, é um instanciacao, criou um obj de excecao,
#                                            # vai jogar esse objteto como excecao
#        
#    
#try:
#    funcaoA()
#except MinhaExcecao as e: # Captura a excecao mais externa
#    print(e.x)
#    print(dir(e))
#    #e.x = 2
#    #raise
#
#
#dir(Exception)
## e.message

if __name__ == '__main__':
         #print (obtem_do_usuario("Ingresa un valor: "))
         obtem_do_usuario("Ingresa un valor: ")
         #exemplo()
