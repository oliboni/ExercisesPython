# 2. Faça uma função que receba duas listas e retorne True se são iguais ou False caso contrário.
# Observação ​ : Duas listas são iguais se possuem os mesmos valores e na mesma ordem.

lista1 = []
lista2 = []
for ind in range(5):
    lista1.append(input("Digite o {}º valor: ".format(ind + 1)))
print("Lista {} cadastrada com sucesso!\n".format(lista1))

for ind in range(5):
    lista2.append(input("Digite o {}º valor: ".format(ind + 1)))
print("Lista {} cadastrada com sucesso!\n".format(lista2))

cont = 0
for ind in range(5):
    if lista1[ind] == lista2[ind]:
        cont += 1

if(cont == 5):
    print(True)
else:
    print(False)

