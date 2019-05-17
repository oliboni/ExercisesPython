"""Faça uma função que receba o resultado da última megasena e uma lista onde cada elemento é
composto pelo CPF de um jogador e sua aposta. Esta função deve exibir o CPF dos jogadores que
ganharam a megasena."""


ganhador = []
for i in range(6):
	ganhador.append(input("Qual foi o {}º valor sorteado: ".format(i+1)))

tamLista = int(input("Qual o número de apostas: "))
lista = []
aposta = []
for i in range(tamLista):
	listaAposta = []
	cpf = input("Qual o CPF do apostador: ")
	for j in range(6):
		aposta.append(input("Qual o {}º número apostado: ".format(j+1)))
	listaAposta.append(cpf)
	listaAposta.append(lista)
	lista.append(listaAposta)

print(lista)