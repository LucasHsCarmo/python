"""
Faça um programa que pergunte quanto você ganha por hora e o 
número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês. 
"""

ganha_hora = float(input("\nQual o valor que você ganha por horas R$: "))
horas_trabalhadas = int(input("Qual sua carga horaria de trabalho: "))

print("\nSeu salário é de R$: {}".format((ganha_hora*horas_trabalhadas)*22))