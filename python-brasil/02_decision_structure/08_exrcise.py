"""
Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 
"""

pd1 = float(input("\nInforme o preço do 1° produto R$: "))
pd2 = float(input("Informe o preço do 2° produto R$: "))
pd3 = float(input("Informe o preço do 3° produto R$: "))

if(pd1 < pd2 and pd1 < pd3):
    print("\nO produto mais barato custa R$:{:.2f}".format(pd1))
elif(pd2 < pd1 and pd2 < pd3):
    print("\nO produto mais barato custa R$:{:.2f}".format(pd2))
else:
    print("\nO produto mais barato custa R$:{:.2f}".format(pd3))