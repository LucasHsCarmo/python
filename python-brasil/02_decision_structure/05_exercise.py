"""
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nt1 = float(input("\nInforme 1° nota: "))
nt2 = float(input("Informe 2° nota: "))

media = (nt1+nt2) / 2

if(media == 10):
    print("\nAprovado com Distinção.")
elif(media >= 7):
    print("\nAprovado.")
else:
    print("\nReprovado.")