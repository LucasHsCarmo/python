"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
"""

tam_metros = int(input("\nTamanho em metros que deverá ser pintado: "))

qtdade_litros = tam_metros / 3 # 1 l - 3 m
qtdade_latas = int(qtdade_litros / 18) 

if (qtdade_litros % 18 != 0): 
    qtdade_latas += 1
    
print("\nVocê deve comprar {} latas".format(qtdade_latas))
print("Valor total será: R$:{:.2f}".format(qtdade_latas*80))