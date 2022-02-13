import time #para medir o tempo do algoritmo
import numpy as np


#matrixlist = [16,3,2,13,5,10,11,8,9,6,7,12,4,15,14,1]# Albrecht Dürer

inicio=datetime.datetime.now()

def confere(lista):
#    n = len(lista) #para qualquer lista quadrada
#    soma = int(n*(n**2 + 1)/2) #para qualquer lista quadrada
    n = 4
    soma = 34
    def soma_lin_col(lista,soma,n):
        for x in range(n):
            if sum(lista[x]) == soma:continue
            else:return False
        return True

    def inverte(lista):return(list(zip(*lista)))

    def reverte(lista,n):return[lista[x][::-1] for x in range(n)][::-1]

    def soma_diagonais(lista,soma,n):
        if (sum([lista[x][x] for x in range(n)])==soma) and (sum([[lista[x][::-1] for x in range(n)][x][x] for x in range(n)])==soma):return True
        else:return False
    
    if soma_diagonais(lista,soma,n):
        if soma_lin_col(inverte(lista),soma,n):
            if soma_lin_col(lista,soma,n):return True
            else:return False
        else:return False
    else:return False

#    matriz = [16,3,2,13,5,10,11,8,9,6,7,12,4,15,14,1] # Albrecht Dürer

def gerador(testes):
    base = np.arange(1,17)
    matriz = np.array([[a,b,c,d] for a in base for b in base for c in base for d in base if(a+b+c+d)==34 and len(list(set([a,b,c,d])))==4])#cria todas as combinações possiveis de 4 elementos não repetidos que somam 34
    a = 0
    for x in matriz:
        for w in matriz:
            if len(list(set(x+w)))==8:
                for y in matriz:
                    if len(list(set(x+w+y)))==12:
                        for z in matriz:
                            if len(list(set(x+w+y+z)))==16:
                                a += 1
                                #print("Confencia nº",a,[x,w,y,z])
                                if confere([x,w,y,z]):
                                    salva("matrizes.txt",[x,w,y,z])                                
                                if a == testes:return False
                


def salva(x,y):
    arquivo = open(x,"a")
    arquivo.write(str(y)+'\n')
    arquivo.close()

#testes = int(input("Digite o número de tentativas: "))
testes = 10**4 #define quantos testes irá fazer
gerador(testes)

#mostra as soluções encontradas
print("soluções: ",open("matrizes.txt",'r').read())

#mede performance
fim = datetime.datetime.now()
print("INI: ",inicio)
print("FIM: ",fim)
print("Tempo:           ",fim-inicio)
print("Performance:     ",(fim - inicio)/testes)

