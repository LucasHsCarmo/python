"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e 
lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o 
    seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, 
    informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. 
"""

salario = float(input("\nInforme o seu salário R$: "))

aumento_20 = salario * 0.2
aumento_15 = salario * 0.15
aumento_10 = salario * 0.1
aumento_05 = salario * 0.05

if(salario > 0 and salario <= 280):
    print("\nSalário antes do reajuste R$: {:.2f}".format(salario))
    print("Percentual do aumento é de 20%")
    print("Valor do aumento R$: {:.2f}".format(aumento_20))
    print("Salário com o reajuste R$:{:.2f}".format(salario+aumento_20))
elif(salario > 280 and salario < 700):
    print("\nSalário antes do reajuste R$: {:.2f}".format(salario))
    print("Percentual do aumento é de 15%")
    print("Valor do aumento R$: {:.2f}".format(aumento_15))
    print("Salário com o reajuste R$:{:.2f}".format(salario+aumento_15))
elif(salario >= 700 and salario < 1500):
    print("\nSalário antes do reajuste R$: {:.2f}".format(salario))
    print("Percentual do aumento é de 10%")
    print("Valor do aumento R$: {:.2f}".format(aumento_10))
    print("Salário com o reajuste R$:{:.2f}".format(salario+aumento_10))
elif(salario >= 1500):
    print("\nSalário antes do reajuste R$: {:.2f}".format(salario))
    print("Percentual do aumento é de 5%")
    print("Valor do aumento R$: {:.2f}".format(aumento_05))
    print("Salário com o reajuste R$:{:.2f}".format(salario+aumento_05))
else:
    print("\nSalário Inválido!")
