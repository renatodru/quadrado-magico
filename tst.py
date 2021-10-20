


def limpa(lista):
    lista = lista[::-1]
    nova = []
    base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for x in range(16):
        if lista.count(lista[x])>1 and lista[x] not in nova :
            nova.append(list(set(base) ^ set(lista))[0])
            return (nova+lista[x+1:16])[::-1]
        else:nova.append(lista[x])

lista = [15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 2]

print(limpa(lista))

