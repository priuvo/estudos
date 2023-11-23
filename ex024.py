#Verificar nome da cidade SANTO
nome = input("Digite o nome da cidade: ")

lista = nome.split()

santo = False
if lista[0].lower() == "santo":
        santo = True

if santo == True:
    print("o nome da cidade começa com o nome SANTO.")
else: print("o nome da cidade não começa com o nome SANTO.")