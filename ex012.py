#Cálculo de desconto
p = float(input("Informe o preço do produto: "))

d= 0.05
np = p * (1-d)

print("O novo preço do produto, considerando {}% de desconto é de R$ {:.2f}.".format(d*100,np))