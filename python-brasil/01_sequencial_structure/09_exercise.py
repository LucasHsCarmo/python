"""
Faça um programa que peça a temperatura em graus Farenheit, 
transforme e mostre a temperatura em graus Celsius.
    C = (5 * (F-32) / 9). 
"""

graus_f = int(input("\nInforme a temperatura em F°: "))
print("\nConvertido em: {:.0f} C̣°".format((5*(graus_f-32))/9))