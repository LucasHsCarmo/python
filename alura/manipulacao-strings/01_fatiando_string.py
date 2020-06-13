print("\n")

argumento = "moedaorigem=real"
index = argumento.find("=")

#Fatiando da string "=" em diante --> Neste caso, será apresentado o REAL 
valor = argumento[index+1:]
print(valor)

#Apenas pegando o valor do código de área
celular = "(41)96574-1728"
indiceInicialCodigoArea = celular.find("(")
indiceFinalCodigoArea   = celular.find(")")
valor2 = celular[indiceInicialCodigoArea+1:indiceFinalCodigoArea]
print(valor2)