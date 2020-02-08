"""
Faça um Programa que leia três números e mostre-os em ordem decrescente. 
"""

num1 = int(input("\nDigite o 1° valor: "))
num2 = int(input("Digite o 2° valor: "))
num3 = int(input("Digite o 3° valor: "))

if(num1 < num2 and num1 < num3 and num2 < num3):
    print("\nOrdem decrescente fica: {}, {} e {}".format(num1,num2,num3))
elif(num1 < num2 and num1 < num3 and num3 < num2):
    print("\nOrdem decrescente fica: {}, {} e {}".format(num1,num3,num2))
elif(num2 < num1 and num2 < num3 and num3 < num1):
    print("\nOrdem decrescente fica: {}, {} e {}".format(num2,num3,num1))
elif(num2 < num1 and num2 < num3 and num1 < num3):
    print("\nOrdem decrescente fica: {}, {} e {}".format(num2,num1,num3))
elif(num3 < num1 and num3 < num2 and num1 < num2):
    print("\nOrdem decrescente fica: {}, {} e {}".format(num3,num1,num2))
else:
    print("\nOrdem decrescente fica: {}, {} e {}".format(num3,num2,num1))