import emoji
global lista

# Função para
def Anykey():
    msg = input("Pressione Enter para continuar...")

def valProx(lst):
    avg = sum(lst) / len(lst)
    diffs = {value: abs(value - avg) for value in lst}

    return min(diffs, key=diffs.get)

# Questão 1
def Menu():
    cod = 1
    media = None
    lista = []

    while cod == 1:
        print("\n" * 130)
        print(emoji.emojize("""
		-------------------------------------
		|1 - Cadastrar Lista                |
		|2 - Verificar maior número         |
		|3 - Soma dos elementos		    |
		|4 - Ocorrências do 1º elmento      |
		|5 - Média dos elementos            |
		|6 - Valor mais próximo da média    |
		|7 - Negativar os elementos         |
		|8 - Quantidades Vizinhos iguais    |
		|                                   |
		|10 - Ver lista                     |
		|0 - Sair		:thumbsup:          |
		|00 - Limpar Lista                  |
		-------------------------------------
		""", use_aliases=True))

        op = input("\nOque deseja fazer: ")



        if op == "1":
            # Lendo a lista
            print("----------------------------------------------")
            tamLista = input("\nQual o tamanho da lista: ")


            for i in range(int(tamLista)):
                numero = int(input("\nDigite o {}º número: ".format(int(i) + 1)))
                lista.append(numero)

            print("A lista {} foi criada com sucesso".format(lista))
            Anykey()

        elif op == "2":
            # a) Retornar maior elemento
            maior = max(lista)

            print("\nO maior número é {}".format(maior))

            Anykey()

        elif op == "3":
            # b) Soma dos valores
            soma = sum(lista)
            print("\nA soma dos números é {}".format(soma))

            Anykey()

        elif op == "4":
            #     c) retorne o número de ocorrências do primeiro elemento da lista
            ocor = lista.count(lista[0])
            print("O número de ocorrências do valor {} é {}".format(lista[0], ocor))

            Anykey()

        elif op == "5":
            media = sum(lista) / len(lista)
            print("A média dos números dentro da lista é {:.2f}".format(media))

            Anykey()

        elif op == "6":
            # e) retorne o valor mais próximo da média dos elementos
            if media:
                print("Valor da média: {} \nValor mais próximo da média: {}".format(media, valProx(lista)))
            else:
                print("Some a média primeiro")

            Anykey()

        elif op == "7":
            # f) retorne a soma dos elementos com valor negativo
            for aux in range(len(lista)):
                lista[aux] = lista[aux] * (-1)

            print("Lista de valores negativos: {}".format(lista))

            Anykey()

        elif op == "8":
            # g) retorne a quantidade de vizinhos iguais
            ant = lista[0]+1
            vizinho = 0
            for aux in range(len(lista)):
                if lista[aux] == ant:
                    vizinho += 1
                ant = lista[aux]
            print("A quantidade de vizinhos é {}".format(vizinho))

            Anykey()

        elif op == "10":
            print("Lista: {}".format(lista))
            Anykey()

        elif op == "0":
            print("\nAté mais...")
            cod = 0

        elif op == "00":
            lista = []
            print("Lista zerada")
            Anykey()

        else:
            print("\n\nOpção inválida")
            Anykey()


Menu()
