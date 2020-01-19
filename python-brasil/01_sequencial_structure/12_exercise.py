"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""

altura = float(input("\nInforme sua altura: "))
print("O peso ideal para homens:   {:.2f}kg".format((72.7*altura)-58))
print("O peso ideal para mulheres: {:.2f}kg".format(((62.1*altura)-44.7)))