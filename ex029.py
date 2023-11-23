#Velocidade de um carro
vel = int(input("Escreva a velocidade do carro, em Km/h: "))

if vel > 80:
    print("Você foi multado. O valor da multa é de R$ {:.2f}".format(vel*7))
else: print("Vai na paz irmão.")