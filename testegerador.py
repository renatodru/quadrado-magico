def gerador():#gera numero aleatorios
#    matriz = [16,3,2,13,5,10,11,8,9,6,7,12,4,15,14,1]
#    matrizini = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
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

def incrementador(inicial):
    incrementada=[None]*16
    for x, y in zip(inicial[::-1], range(16)):
        if x + 1>16:incrementada[y]=1
        else:incrementada[y]=x+1
    return incrementada[::-1]

def salva(y,archive):
    arquivo = open(archive,"a")
    arquivo.write(str(y)+'\n')
    arquivo.close()



testes = 10**6
inicial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]#menor valor de matriz possivel se concatenar os valores

print(inicial)
print(incrementador(inicial))

#for x in range(testes):
#    testando = gerador()
#    if confere(testando):
#        salva(testando,"matrizes.txt")
#print(open("matrizes.txt",'r').read())
#salva(testando,"orientagerador.txt")#salva a ultima matriz testada
#fim = datetime.datetime.now()