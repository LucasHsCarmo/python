"""
Faça um Programa que peça dois números e imprima o maior deles. 
"""

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if(num1 > num2):
    print("\n{} é maior que o {}".format(num1,num2))
else:
    print("\n{} é maior que o {}".format(num2,num1))