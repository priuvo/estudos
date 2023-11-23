#Primeiro e último nome
nome = input("Digite o nome completo: ")

tamanho = len(nome.split())

if tamanho > 1:
    print("Primeiro nome: " + nome.split()[0])
    print("Último nome: " + nome.split()[tamanho-1])
else: print("Nome completo requer nome E sobrenome.")