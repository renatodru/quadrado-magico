#print(list(matrixdic.values()))
#print(list(matrixdic.keys()))
#print(list(matrixdic.items()))
#print(sum(matrixlist[0:4]))
#matrixdic = {1:16,2:3,3:2,4:13,5:5,6:10,7:11,8:8,9:9,10:6,11:7,12:12,13:4,14:15,15:14,16:1}
#matrixlist = [16,3,2,13,5,10,11,8,9,6,7,12,4,15,14,1]
import random
import datetime
inicio=datetime.datetime.now()

def confere(lista):
    n = len(lista)
    soma = int(n*(n**2 + 1)/2)
#    n = 4
#    soma = 34
    def soma_lin_col(lista,soma,n):
        for x in range(n):
            if sum(lista[x]) == soma:continue
            else:return False
        print("soma linha ou col")
        return True

    def inverte(lista):
        return(list(zip(*lista)))

    def reverte(lista,n):
        return[lista[x][::-1] for x in range(n)][::-1]

    def soma_diagonais(lista,soma,n):
        if (sum([lista[x][x] for x in range(n)])==soma) and (sum([[lista[x][::-1] for x in range(n)][x][x] for x in range(n)])==soma):return True
        else:return False
    
    if soma_diagonais(lista,soma,n):
        if soma_lin_col(inverte(lista),soma,n):
            if soma_lin_col(lista,soma,n):return True
            else:return False
        else:return False
    else:return False

def gerador():
#    matriz = [16,3,2,13,5,10,11,8,9,6,7,12,4,15,14,1]
    matriz = list(range(1,17,1))
    random.shuffle(matriz)
    nova_matriz = []
    matriz_int = []
    z = 0
    for y in matriz:
        matriz_int.append(y)
        z = z + 1
        if z == 4:
            nova_matriz.append(matriz_int)
            matriz_int = []
            z = 0
    return nova_matriz

def salva(y):
    arquivo = open("matrizes.txt","a")
    arquivo.write(str(y)+'\n')
    arquivo.close()

testes = 1000000
#abc = 0 global abc para ver quantas vezes entrou a soma diagonal

for x in range(testes):
    testando = gerador()
    if confere(testando):
        salva(testando)
print(open("matrizes.txt",'r').read())
fim = datetime.datetime.now()
print("INI: ",inicio)
print("FIM: ",fim)
print("Tempo:           ",fim-inicio)
print("Performance:     ",(fim - inicio)/testes)
