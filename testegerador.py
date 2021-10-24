
def identific4d0r():
    base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    return[[a,b,c,d] for a in base for b in base for c in base for d in base if(a+b+c+d)==34 and len(list(set([a,b,c,d])))==4]

def combin4t0r(lista):
    


    
def salva(y,archive):
    arquivo = open(archive,"a")
    arquivo.write(str(y)+'\n')
    arquivo.close()

inicial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] #menor valor de matriz possivel se concatenar os valores


for i in range(300):
    print(inicial)

    inicial = limpa(incrementador(inicial))


#list(set(inicial))#remove duplicados de uma lista 

#testes = 10**6
#for x in range(testes):
#    testando = gerador()
#    if confere(testando):
#        salva(testando,"matrizes.txt")
#print(open("matrizes.txt",'r').read())
#salva(testando,"orientagerador.txt")#salva a ultima matriz testada
#fim = datetime.datetime.now()

#def limpa(lista): # substitui elemento repetido pelo elemento não encontrado
#    nova = []
#    base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#    for x in range(16):
#        if lista.count(lista[x])>1 and lista[x] not in nova :
#            nova.append(list(set(base) ^ set(lista))[0])
#            return nova+lista[x+1:16]
#        else:nova.append(lista[x])