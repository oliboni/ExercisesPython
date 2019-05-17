""" 
Faça uma função que receba uma lista l e um valor, exiba a posição da 1ª ocorrência de valor em l.
Caso o valor não pertença à lista, a função deve retornar -1 e caso a lista esteja vazia, a função
deve retornar -2
a. considere que os elementos da lista são números
b. considere que os elementos da lista são números ou listas de números
"""

lista = [[1,2,3],[4,5,9], [9,2,8]]

def search(lista, valor):
	if len(lista) == 0:
		return -2
	var = [(lista.index(x), x.index(valor)) for x in lista if valor in x]
	if var:
		return var[0]
	else:
		return -1


print(search(lista,6))