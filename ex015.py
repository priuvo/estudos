#Cálculo de valor a ser pago por km rodado
km = float(input("Informe a quantidade de km rodados: "))
d = int(input("Por quantos dias o carro foi alugado? "))

vd = 60
vkm = 0.15

vtotal = vd * d + vkm * km

print("O preço a pagar é de R$ {:.2f}.".format(vtotal))