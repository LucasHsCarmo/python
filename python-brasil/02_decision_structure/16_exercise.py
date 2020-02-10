"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e 
determine se a mesma é uma data válida. 
"""

print("\nFormato da data dd/mm/aaaa")

dia = int(input("Informe o dia: "))
if(dia <= 0 or dia >= 32):
    print("Dia incorreto...")
else:
    mes = int(input("Informe o mês: "))
    if(mes <= 0 or mes >= 13):
        print("Mês incorreto...")
    else:
        ano = int(input("Informe o ano: "))
        if(ano <= 0):
            print("Ano incorreto...")
        else:
            print("A data é: {:02d}/{:02d}/{:04d}".format(dia,mes,ano))