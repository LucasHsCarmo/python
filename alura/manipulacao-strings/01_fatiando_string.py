print("\n")

argumento = "moedaorigem=real"
index = argumento.find("=")

#Fatiando da string "=" em diante --> Neste caso, será apresentado o REAL 
valor = argumento[index+1:]
print(valor)