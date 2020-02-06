"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no 
mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa 
que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo: 
    
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido. 
"""

ganha_hora = float(input("\nQual o valor que você ganha por horas R$: "))
horas_trabalhadas = int(input("Qual sua carga horaria de trabalho: "))

salario_bruto = (ganha_hora*horas_trabalhadas)*22
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - (ir+inss+sindicato)

print("\n+ Seu salário bruto é de R$: {:.2f}".format(salario_bruto))
print("- IR R$: {:.2f}".format(ir))
print("- INSS R$: {:.2f}".format(inss))
print("- Sindicato R$: {:.2f}".format(sindicato))
print("= Salário Líquido R$: {:.2f}".format(salario_liquido))
