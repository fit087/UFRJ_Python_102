### Exercicio 2 ###
def printArquivo(NomeArquivo):
    try: 
        arquivo = open(NomeArquivo, "r")
        linhas = arquivo.readlines()  
        for linha in linhas:
            # pequeno detalhe da , eh a gambiarra que faz o print nao pular linha.
            # tente tirar a virgula e veja...
            print linha, 
        arquivo.close()
    except IOError:
        # aqui voce pode tratar seu erro como preferir inclusive 
        # so dando print de uma mensagem para o usuario
        print "Este arquivo nao existe."
                      

#printArquivo("exemplo.txt")


### Exercicio 3 -  parte 1 ###
def somaColuna(NomeArquivo):
    somatorio = 0
    try:
        arquivo = open(NomeArquivo, "r")              
    except IOError:
        print "Este arquivo nao existe."
         

    linhas = arquivo.readlines()  
    for linha in linhas:
        # tenta converter a linha em um inteiro ja que linhas 
        # na realidade eh uma lista de STRINGS.
        # ignora o que nao for uma string que representa um numero.
        try: 
            somatorio += int(linha)
        except:
            pass
    arquivo.close()
    return somatorio
    
#print somaColuna("ex2.txt")


### Exercicio 3 - parte 2 ###

def somaTodos(NomeArquivo):
    somatorio = 0
    try: 
        arquivo = open(NomeArquivo, "r")              
    except IOError:
        print "Este arquivo nao existe."
        

    linhas = arquivo.readlines()  
    for linha in linhas:
        for caracter in linha.split():
            try: 
                somatorio += int(caracter)
            except:
                pass
    arquivo.close()
    return somatorio
    
#print somaTodos("ex2.txt")
 
### Exercicio 4 ###   
def leColuna(NomeArquivo, numColuna):
    coluna = ""
    try:
        arquivo = open(NomeArquivo, "r")
        linhas = arquivo.readlines()  
        for linha in linhas:
            linhaSeparada = linha.split()
            if 0 < numColuna and numColuna <= len(linhaSeparada):
                coluna += linhaSeparada[numColuna-1] + "\n"
        arquivo.close()
        return coluna              
    except IOError:
        print "Este arquivo nao existe."
   
#print leColuna("ex2.txt",2)
   
### Exercicio 5 ###   
def enumera(NomeArquivo):
    try: 
        arquivo = open(NomeArquivo, "r")
        linhas = arquivo.readlines()  
        for num, linha in enumerate(linhas):
            print str(num) + "| " + linha, 
        arquivo.close()
    except IOError:
        print "Este arquivo nao existe."
    
#enumera("exemplo.txt") 
    
### Exercicio 6 ###   
def contaLinhas(NomeArquivo):
    contador = 0
    try: 
        arquivo = open(NomeArquivo, "r")
        linhas = arquivo.readlines()
        
        for linha in linhas:
            if linha.strip() == "":
                continue
            else:
                if linha.strip()[0] != "#":
                    contador += 1            
        arquivo.close()
        return contador
    except IOError:
        print "Este arquivo nao existe."
        
# print contaLinhas("exemplo.txt")    
     
### Exercicio 7 ###
import random 

def jogoForca(NomeArquivo):
    erro = 0
    erromax = 5
    try:
        arquivo = open(NomeArquivo, "r")
        palavras = arquivo.readlines()
        while True:
            sorteada = random.choice(palavras)
            sorteada = sorteada.strip("\n").strip()
            if sorteada != "": break        
        arquivo.close()                 
    except IOError:
        print "Este arquivo nao existe."
    except IndexError:
        print "O arquivo nao possui palavras para serem sorteadas"     
    else:    
        revelada = "-"*len(sorteada.strip())
        while True:
            letra = raw_input("Insira uma letra: ")
            if len(letra) > 1: 
                print "Somente uma letra por vez!\n"
                continue
            if letra.isalpha() == False: 
                print "Somente insira LETRAS.\n"
                continue
            
            umaSubstituicao = False # ajuda a saber se alguma letra foi substituida
            for i in range(len(sorteada)):
                if sorteada[i] == letra:
                    revelada = revelada[:i] + letra + revelada[i+1:]
                    umaSubstituicao = True
                    
            # se nao substituiu nenhuma letra entao conta um erro
            if umaSubstituicao == False:
                erro += 1
                print "Voce desperdicou %s de um total de %s\n" %(erro, erromax) 
            else:
                if revelada == sorteada: # se revelou todas as letras vive
                    print "PARABENS! Voce continua vivo e a palavra era < %s >." %sorteada
                    break
                else: 
                    print "< %s >\n" %revelada
                    
            # se atingiu o numero maximo de erros eh enforcado  
            if erro == erromax:
                print "ADEUS MUNDO CRUEEEEEL!...\nVoce acaba de ser enforcado.\n"
                break
       
        
jogoForca("ex2.txt")       
            
        
        
    
    
    