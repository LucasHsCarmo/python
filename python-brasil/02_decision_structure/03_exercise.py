"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
"""

print("\nEscolha sua opção: ")
letra = input("Feminino - F ou Masculino - M: ")

if(letra.upper() == 'F'):
    print("\nSexo Feminino.")
elif(letra.upper() == 'M'):
    print("\nSexo Masculino.")
else:
    print("\nSexo Inválido.")