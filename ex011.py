#Cálculo de área
b = float(input("Informe a largura da parede, em metros: "))
h = float(input("Informe a altura da parede, em metros: "))

a = b*h
tinta = a/2

print("A área total da parede é de {}m² e é necessário {:.2f} litros de tinta para pintá-la.".format(a,tinta))