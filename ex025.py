#Verificar sobrenome Silva
nome = input("Digite o nome completo: ")

lista = nome.split()

silva = False
for i in lista:
    if i.lower() == "silva":
        silva = True

if silva == True:
    print("o nome da pessoa tem o sobrenome SILVA.")
else: print("o nome da pessoa não tem o sobrenome SILVA.")