"""
Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 
"""
#Base and high
b = int(input("\nInforme o valor da base: "))
h = int(input("Informe o valor da altura: "))

a = (b*h)

print("O dobro desta área é: {}".format(a*a))