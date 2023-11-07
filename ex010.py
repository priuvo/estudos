#Conversão de moedas
n = float(input("Informe quantos reais você tem na carteira: "))
txc = 3.27

us = n/txc

print("Com R$ {:.2f} você pode comprar US$ {:.2f}.".format(n,us))