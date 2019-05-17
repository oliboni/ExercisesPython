"""Os alunos de uma turma foram muito mal em uma prova. O professor resolveu, então considerar a
maior nota como o 10.0 e transformar as demais notas em relação a esta nota da seguinte maneira:
nota do aluno * 10/ maior nota.
Faça uma função que receba a lista de notas dos alunos, calcule a nova nota dos alunos mostrando
as notas antigas e as novas na tela. Exemplo:
Notas originais: 3.0 4.0 5.0 6.0 3.0
maior nota: 6.0
Saída:
1 3.0 5.0 (3*10)/6
2 4.0 6.6
3 5.0 8.3
4 6.0 10.0
5 3.0 5.0"""

def notasOriginais():
	notas = []
	quantNotas = int(input("Quantas notas quer registar: "))
	for i in range(quantNotas):
		notas.append(float(input("Digite a {}º nota: ".format(i+1))))

	print (notas)
	return notas

def calculaNota(notas):
	maior = max(notas)
	novaNota = []
	for i in range(len(notas)):
		novaNota.append((notas[i]*10)/maior)
	print(maior)
	
	return novaNota

print(calculaNota(notasOriginais()))