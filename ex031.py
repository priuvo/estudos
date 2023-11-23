#Cálculo km rodado
dist = int(input("Informe a distância da viagem em Km: "))

if dist <= 200:
    valor = dist * 0.5
else: valor = dist * 0.45

print("O preço da passagem será de R$ {:.2f}".format(valor))