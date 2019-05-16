# Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da média dos
# valores da lista.

def valProx(lst):
    avg = sum(lst) / len(lst)
    diffs = {value: abs(value - avg) for value in lst}

    return min(diffs, key=diffs.get)

lista = []
tam = int(input("Qual o tamanho da lista: "))
for i in range(tam):
    numero = float(input("\nDigite o {}º número: ".format(i + 1)))
    lista.append(numero)

media = sum(lista) / len(lista)
print("Valor da média: {} \nValor mais próximo da média: {}".format(media, valProx(lista)))