"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado 
de download do arquivo usando este link (em minutos). 
"""

tam_aquivo = int(input("\nTamanho do arquivo em MB: "))
link_internet = float(input("Velocidade do link de internet: "))

tempo = tam_aquivo * link_internet

print("\nTempo aproximado para download será de: {:.0f}min".format(tempo))