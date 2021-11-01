import time #para medir o tempo do algoritmo
import numpy as np

def gerador_old(testes):
    base = list(range(1,17))
    matriz = [[a,b,c,d] for a in base for b in base for c in base for d in base if(a+b+c+d)==34 and len(list(set([a,b,c,d])))==4]#cria todas as combinações possiveis de 4 elementos não repetidos que somam 34
    achado = []
    a = 0
    for x in matriz:
        for w in matriz:
            if len(list(set(x+w)))==8:
                for y in matriz:
                    if len(list(set(x+w+y)))==12:
                        for z in matriz:
                            if len(list(set(x+w+y+z)))==16:
                                a += 1
                                achado.append([x,w,y,z])
                                if a == testes:return achado



def gerador_np(testes):
    base = list(range(1,17))
    matriz = np.array([[a,b,c,d] for a in base for b in base for c in base for d in base if(a+b+c+d)==34 and len(list(set([a,b,c,d])))==4])#cria todas as combinações possiveis de 4 elementos não repetidos que somam 34
#    achado = np.array([[[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]])
    achado = np.empty((0,4,4),dtype=int)
    a = 0
    for x in matriz:
        for w in matriz:
            if np.unique(np.concatenate((x, w))).size==8:
                for y in matriz:
                    if np.unique(np.concatenate((x, w, y))).size==12:
                        for z in matriz:
                            if np.unique(np.concatenate((x, w, y, z))).size==16:
                                a += 1
                                achado = np.concatenate((achado,np.reshape(np.concatenate((x,w,y,z)),(1,4,4))))
                                if a == testes:return achado

testes=100
#########################
inicio = time.time()
gerador_np(testes)
print("Tempo np  :",time.time() - inicio)
##########################
inicio = time.time()
gerador_old(testes)
print("Tempo old :",time.time() - inicio)
