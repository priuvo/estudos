#Manipulando cadeias de caracteres

nome = input("Digite o seu nome completo: ")

print("NOME COM TODAS MAIÚSCULAS: " + nome.upper())
print("nome com todas as minúsculas: " + nome.lower())
print("Quantas letras tem ao todo: " + str(len(nome.replace(' ', ''))))
print ("Quantas letras tem o primeiro nome: " + str(len(nome.split()[0])))