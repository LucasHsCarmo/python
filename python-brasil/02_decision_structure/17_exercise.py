"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a 
quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros.
    Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 
    326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 
"""

num = int(input("\nInforme um número: "))

if(num < 0 or num > 999):
    print("Valor inválido!")
else:
    centena = num // 100
    dezena  = (num - (centena*100)) // 10
    unidade = (num - (centena*100)) - (dezena*10)

    print("{} centenas, {} dezenas e {} unidades.".format(centena,dezena,unidade))