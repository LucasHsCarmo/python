"""
Faça um Programa que leia três números e mostre o maior deles. 
"""

num1 = int(input("\nDigite o 1° valor: "))
num2 = int(input("Digite o 2° valor: "))
num3 = int(input("Digite o 3° valor: "))

if(num1 > num2 and num1 > num3):
    print("\nO maior número é o {}".format(num1))
elif(num2 > num1 and num2 > num3):
    print("\nO maior número é o {}".format(num2))
else:
    print("\nO maior número é o {}".format(num3))