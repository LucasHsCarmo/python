"""
Faça um Programa que peça um número correspondente a um determinado ano e 
em seguida informe se este ano é ou não bissexto.
"""

ano = int(input("\nInforme o ano da sua preferencia: "))

if(ano % 6 == 0):
    print("\nO ano {} é bissexto.".format(ano))
else:
    print("\nO ano {} não é bissexto.".format(ano))