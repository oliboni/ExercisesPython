# Para instalar bibliotecas utiliza sudo pip3 install biblioteca
"""
# sys é uma função com método de entrada.
import sys

# Também pode ser usado o input
nome = input("Digite seu Nome: ")
sobrenome = "Oliboni"
Idade = 22
print("DIgite seu sexo: ")
sexo = sys.stdin.readline()

print ("Meu nome começa com a letra ", nome[0])

print("Nome:"+nome + "\n" + "Sexo: %s Idade: %s" %(sexo,idade))
"""
# -------------------------------------------------------------------------------------------------------
# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]
"""
numero = input ("Digite um número: ")
print (numero)
"""

# ---------------------------------------------------------------------------------------------------------
# Faça um Programa que peça dois números e imprima a soma
"""
num1 = input ("Digite o número 1: ")
num2 = input ("Digite o número 2: ")

# Como a entrada é uma string, temos que converter em int
print ("Resultado: ", int(num1) + int(num2))
"""

# ---------------------------------------------------------------------------------------------------------
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# Todo cálculo que for fazer tem que converter a entrada para o formato desejado
"""
bim1 = input ("Média 1 bimestre: ") 
bim2 = input ("Média 2 bimestre: ")
bim3 = input ("Média 3 bimestre: ")
bim4 = input ("Média 4 bimestre: ")
media = (float(bim1)+float(bim2)+float(bim3)+float(bim4))/4

print ("Média: ", media)
"""

# ---------------------------------------------------------------------------------------------------------
# Faça um Programa que converta metros para centímetros

"""
def transforma(metros):
	centimetros = int(metros)*100
	return int(centimetros)

metros = input("Digite o valor em Metros: ")
centimetros = transforma(metros)
print ("Convertendo para centimetros o valor de %d" %int(metros)+ "m ficaria %d"%(centimetros)+ "cm.")
"""

# ---------------------------------------------------------------------------------------------------------
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
def area(raio)
	pi = float(3.14)
	A = pi*(raio*raio)

	return float(A)

raio = input("Qual o raio do círculo: ")

print ("A Área do círculo é ", area(float(raio)))
"""

# ---------------------------------------------------------------------------------------------------------
# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
def area(l1):
	A = l1*l1
	return float(A)*int(2)

l1 = input("Qual é o Lado do Quadrado: ")

print ("O dobro da área do Quadrado é ", area(float(l1)))
"""

# ----------------------------------------------------------------------------------------------------------
"""meu_nome = "Rodrigo Oliboni"
meu_nick = "slayer"
# Método upper deixa todas as letras em caixa alta
print("Nome: %s, nick: %s" %(meu_nome.upper(), meu_nick))
print("Meu nome começa com a letra ", meu_nome[0])
# Método lower deixa as letras minúsculas
print("Meu nome comeca com a letra ", meu_nome[0].lower())
print("My first_name is ", meu_nome[0:6])
print(meu_nome[0])
print(meu_nome[1])
print(meu_nome[2])
print(meu_nome[3])
print(meu_nome[4])
print(meu_nome[5])
print(meu_nome[6])"""

# ---------------------------------------------------------------------------------------------------------
# Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.
i = int(input)
n = int(1)

while n<=i:
	if(n%2 == 0):
		n += 1
	else:
		print (n)
		n += 1			

