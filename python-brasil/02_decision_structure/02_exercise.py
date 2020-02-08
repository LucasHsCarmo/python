"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

num = int(input("\nInforme um número: "))

if(num >= 0):
    print("\nO número {} é positivo.".format(num))
else:
    print("\nO número {} é negativo.".format(num))