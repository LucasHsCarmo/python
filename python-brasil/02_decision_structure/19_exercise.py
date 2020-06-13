"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
Dica: utilize o operador módulo (resto da divisão). 
"""

num = int(input("\nInforme um número: "))

if(num % 2 == 0):
    print("Número PAR.")
else:
    print("Número ÍMPAR.")