
"""Foram anotadas as idades e alturas dos alunos de uma turma e armazenados em uma lista cujos
elementos são sublistas com dois elementos: o primeiro é a idade do aluno e o segundo a sua
altura. Faça uma função que receba esta lista e utilizando as funções abaixo, determina e mostra
quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
a. Faça a função MediaTurma (lista) que recebe a lista com idade e altura de cada um dos
aluno e retorna a média de altura da turma
b. Faça a função Conta_Baixinhos (lista, media), que recebe a lista com idade e altura de
cada um dos alunos e a média de altura da turma, retornando quantos alunos com mais de
13 anos estão abaixo da média de altura da turma"""



def MediaTurma(lista):
	total = 0
	for i in range(len(lista)):
		total += lista[i][1]

	media = total/(len(lista))
	return float(media)

def ContaBaixinhos(lista, media):
	baixinhos = 0
	for i in range(len(lista)):
		if lista[i][0] > 13 and lista[i][1] < media:
			baixinhos += 1
	return baixinhos


lista = [[10,1.3],[15,1.68],[17,1.5],[16,1.6],[15,1.49]]
media = MediaTurma(lista)

print("A média de altura dos alunos é {:.2f}m e existem {} alunos com mais de 13 anos e abaixo da média!"
      .format(media, ContaBaixinhos(lista,media)))
