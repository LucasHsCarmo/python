"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:

  A)  "Telefonou para a vítima?"
  B)  "Esteve no local do crime?"
  C)  "Mora perto da vítima?"
  D)  "Devia para a vítima?"
  E)  "Já trabalhou com a vítima?" 
  
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como 
"Inocente". 
"""

print("\nPerguntas investigativas...")
print("As respostas devem ser com 'S' (sim) ou 'N' (não)!\n")

pg1 = str(input("Telefonou para a vítima? -> "))
pg2 = str(input("Esteve no local do crime? -> "))
pg3 = str(input("Mora perto da vítima? ->"))
pg4 = str(input("Devia para a vítima? -> "))
pg5 = str(input("Já trabalhou com a vítima? -> "))

