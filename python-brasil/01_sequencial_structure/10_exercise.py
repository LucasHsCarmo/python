"""
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
 A)   o produto do dobro do primeiro com metade do segundo .
 B)   a soma do triplo do primeiro com o terceiro.
 C)   o terceiro elevado ao cubo. 
"""

num1 = int(input("\nInforme o 1° número: "))
num2 = int(input("Informe o 2° número: "))

num3 = ((num1*2) + (num2/2))
num3 = int(num3)

#A
print("\nProduto será: {}".format(num3))
#B
print("Calculado: {}".format((num1*3)+num3))
#C
print("Terceiro ao cubo: {}".format(num3**3))