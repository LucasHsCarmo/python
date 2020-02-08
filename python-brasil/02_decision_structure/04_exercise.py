"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
"""

letra = input("\nDigite uma letra: ")

if(letra.upper() == 'A' or letra.upper() == 'E' or letra.upper() == 'I' or letra.upper() == 'O' or letra.upper() == 'U'):
    print("\nLetra digitada é vogal.")
else:
    print("\nLetra digitada é consoante.")