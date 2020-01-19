"""
Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58 
"""

altura = float(input("\nInforme sua altura: "))
print("O peso ideal é: {:.2f}kg".format((72.7*altura)-58))