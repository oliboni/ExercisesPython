"""4) Crie uma função que recebe uma lista de strings e
 a. retorne o elemento com mais caracteres
 b. retorne a média de vogais nos elementos (soma do no de vogais de cada elemento/no de
 elementos)
 c. retorne o número de ocorrências do primeiro elemento da lista
 d. retorne a palavra lexicograficamente maior
 e. conte o número de ocorrências de palavras compostas
 f. retorne a quantidade de vizinhos iguais"""


def Anykey():
    msg = input("Pressione Enter para continuar...")

def Menu():
    cod = 1
    lista = []

    while cod == 1:
        # Recebendo a lista
        tamanho = int(input("Informe o tamanho da lista: "))

        for i in range(tamanho):
            lista.append(input("Digite a {} string: ".format(i+1)))

        print("\nLista {} cadastrada com sucesso!".format(lista))

        # -------------------------------------------------------------------
        # a) retorne o elemento com mais caracteres
        for i in range(len(lista)):
            if i == 0:
                maior = lista[i]
            elif len(lista[i]) > len(maior):
                maior = lista[i]
        
        print("O elemento com mais caracter é {}".format(maior))

        # --------------------------------------------------------------------
        # b)  retorne a média de vogais nos elementos (soma do no de vogais de cada elemento/no de elementos)
        for i in range(tamanho):
            tam = 0
            for letra in lista[i]:
                if letra.lower()in 'aáâãeéêiíoóõôuú':
                    tam += 1
            media = tam/len(lista[i])
            print("A média de vogal da string {} é {:.2f}".format(lista[i].upper(), media))

         # -------------------------------------------------------------------
         # c) retorne o número de ocorrências do primeiro elemento da lista
        print("O número de ocorrências do elemento {} é de {}".format(lista[0], lista.count(lista[0])))

        # --------------------------------------------------------------------
        # d) retorne a palavra lexicograficamente maior
        maior = 0
        total = 0
        strMaior = []
        for i in range(len(lista)):
            total = 0
            for j in range(len(lista[i])):
                if lista[i][j].isalpha():
                    total += 1
            if total > maior:
                maior = total
                strMaior = lista[i]
        print(strMaior)

        # --------------------------------------------------------------------
        print("\n\n1 = SIM - 0 = Não")
        cod = int(input("Executar novamente? "))

Menu()