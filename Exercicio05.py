""""
Faça um programa que percorre uma lista com o seguinte formato: [['Brasil', 'Italia', [10, 9]], ['Brasil',
'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez
em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O
programa deve imprimir na tela:
a. o total de faltas do campeonato
b. o time que fez mais faltas
c. o time que fez menos faltas
"""

lista = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7, 8]]]

def menos_faltas (lista):
    menos = lista[0][2][0]
    # for i in range(len(lista)):
        # print("teste")
    print(menos)
    return (menos)

def mais_faltas (lista):
    timeMais = lista[0][0]
    mais = lista[0][2][0]
    # for i in range(len(lista)):
    #     for j in range(2):
    #          if lista[i][2][j]>mais:
    #              mais = lista[i][2][j]
    #              timeMais = lista[i][j]
    # return timeMais

def total_faltas (lista):
    soma = 0
    for i in range(len(lista)):
        for j in range(2):
            soma += lista[i][2][j]
    return soma

print("Total de faltas: {}".format(total_faltas(lista)))
# print("O time que mais fez faltas foi: {}".format(mais_faltas(lista)))
# print("O time que menos fez faltas foi: {}".format(menos_faltas(lista)))

# menos = lista[0][2][0]
# mais = menos
# soma = 0
#
# # Total Faltas
# for i in range(len(lista)):
#     for j in range(2):
#         soma += lista[i][2][j]
#
# # Mais Faltas
# for i in range(len(lista)):
#     for j in range(2):
#         if lista[i][2][j] > mais:
#             mais = lista[i][2][j]
#             listaMais = lista[i][j]
#
#
# # Menas faltas
# for i in range(len(lista)):
#     for j in range(2):
#         if lista[i][2][j] < menos:
#             menos = lista[i][2][j]
#             listaMenos = lista[i][j]
#
#
#
# # print("O total de faltas do campeonato é {}".format(soma))
# # print("O lista que mais cometeu faltas foi o {}".format(listaMais))
# # print("O lista que menos cometeu falta foi o {}".format(listaMenos))
# print("O total de faltas do campeonato é {}".format(soma))
# print("O lista que mais cometeu faltas foi o {}".)
# print("O lista que menos cometeu falta foi o {}".format(listaMenos))