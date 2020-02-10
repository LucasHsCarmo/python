"""
Faça um programa que calcule as raízes de uma equação do segundo grau, 
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e 
fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do 
    segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    
    Se o delta calculado for negativo, a equação não possui raizes reais. 
    Informe ao usuário e encerre o programa;
    
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
    informe-a ao usuário;
    
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 
"""

import math

print("Equação do segundo grau...")

a = int(input("\nInforme o valor de A: "))

if(a == 0):
    print("\nEquação não é do segundo grau!")
    print("Programa será encerrado!")
else:
    b = int(input("Informe o valor de B: "))
    c = int(input("Informe o valor de C: "))

    delta = (math.pow(b,2)) - (4 * a * c)

    if(delta == 0):
        x1 = ((-b) + math.sqrt(delta)) / 2 * a
        print("\nA equação possui apenas uma raiz real!")
        print("X1 = {}".format(x1))
    elif(delta < 0):
        print("\nA equação não possui raizes reais!")
    else:
        x1 = ((-b) + math.sqrt(delta)) / (2 * a)
        x2 = ((-b) - math.sqrt(delta)) / (2 * a)
        print("\nA equação possui duas raizes reais!")
        print("X1 = {}".format(x1))
        print("X2 = {}".format(x2))