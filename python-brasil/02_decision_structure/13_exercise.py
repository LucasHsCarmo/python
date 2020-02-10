"""
Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados 
    for maior que o terceiro;
    
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; 
"""

ld1 = int(input("\nInforme o 1° lado do triângulo: "))
ld2 = int(input("Informe o 2° lado do triângulo: "))
ld3 = int(input("Informe o 3° lado do triângulo: "))

if(ld1 == ld2 and ld1 == ld3 and ld2 == ld3):
    print("\nTriângulo Equilátero!")
elif((ld1 == ld2) or (ld1 == ld3) or (ld2 == ld3)):
    print("\nTriângulo Isósceles!")
elif((ld1 != ld2) and (ld1 != ld3) and (ld2 != ld3)):
    print("\nTriângulo Escaleno!")