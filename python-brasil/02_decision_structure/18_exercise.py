"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do 
saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o 
máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na 
máquina.

  A) Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
     uma nota de 50, uma nota de 5 e uma nota de 1;

  B) Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
     uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. 
"""

print("\nValor mínimo R$:10,00 e Valor máximo R$:600,00")
print("Notas disponíveis para o saque R$: 1, 5, 10, 50 e 100.")

saque = float(input("\nDigite o valor do saque R$: "))

if(saque < 10 or saque > 600):
    print("\nSaque inválido.")
else:
    cem = int(saque // 100)
    cinquenta = int(saque - (cem*100)) // 50
    dez = int((saque - (cem*100)) - (cinquenta*50)) // 10
    cinco = int(((saque - (cem*100)) - (cinquenta*50)) - (dez*10)) // 5
    um = int(((saque - (cem*100)) - (cinquenta*50)) - (dez*10)) - (cinco*5)

    print("Para sacar a quantia de R$:{:.2f}, o programa fornece {} nota(s) de 100, {} nota(s) de 50, {} nota(s) de 10, {} nota(s) de 5 e {} nota(s) de 1".format(saque,cem,cinquenta,dez,cinco,um))