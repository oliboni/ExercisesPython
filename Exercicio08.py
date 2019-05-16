"""Faça uma função que receba uma lista de inteiros qualquer e retorne True se ela está ordenada ou
False, caso contrário."""

def verificaOrde(lista):
    valor = lista[0]
    for i in range(len(lista)):
        if valor <= lista[i]:
            valor = lista[i]
        else:
            return 0

    return 1

lista = [1,2,4,4,5,6,7,8,9,10]

if verificaOrde(lista):
    print("A fila esta ordenada!")
else:
    print("A fila não está ordenada!")