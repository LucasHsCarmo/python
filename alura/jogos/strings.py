"""
Interpolação {:02d}
               {} -> Aonde vou passar a variavel
               :  -> Define a quantidade de decimais
               0  -> Primeiro numerador (qual numero deverá aparecer no print)
               2  -> Quantidade de casas que serão respeitados
               d  -> Tipo da variável 
"""         
#print("Data {:02d}/{:02d}/{:4d}".format(10,3,2020))

#print("R$: {:7.2f}".format(1234.8))

#built in python são módulos que já são pré-definidos no python

frutas = ['Maça', 'Melância', 'Uva']

fruta_buscada = input("Informe a fruta que está procurando: ")

if(fruta_buscada in frutas):
    print("Parabéns, você encontrou a fruta desejada.")
else:
    print("A fruta {} não consta no sistema".format(fruta_buscada))


#List Comprehension. 
lista = [1,2,3,4,5,6]

quadrado = [n*n for n in lista]
print(quadrado)

"""
inteiros = [1,2,3,4,5,6,7,8,9,10]
pares = []
for numero in inteiros:
    if(numero % 2 == 0):
        pares.append(numero)
"""

inteiros = [1,2,3,4,5,6,7,8,9,10]
pares = [numero for numero in inteiros if numero % 2 == 0]
print(pares)