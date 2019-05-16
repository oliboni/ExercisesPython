# 3. Faça uma função que receba duas listas e retorne True se têm os mesmos elementos ou False
# caso contrário ​ Observação ​ : Duas listas possuem os mesmos elementos quando são compostas
# pelos mesmos valores, mas não obrigatoriamente na mesma ordem.

lista1 = []
lista2 = []

for ind in range(5):
    lista1.append(int(input("Digite o {}º valor: ".format(ind + 1))))

print("Lista {} cadastrada com suecesso!\n".format(lista1))

for ind in range(5):
    lista2.append(int(input("Digite o {}º valor: ".format(ind + 1))))

aux = 0
for ind in range(5):
    if lista1[ind] in lista2:
        aux += 1

if aux == 5:
    print(True)
else:
    print(False)
