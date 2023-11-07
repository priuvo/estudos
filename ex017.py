#Pitágoras
import math
co = float(input("Informe o comprimento do Cateto Oposto: "))
ca = float(input("Informe o comprimento do Cateto Adjacente: "))

h = math.sqrt((math.pow(ca,2) + math.pow(co,2)))

print("O valor da hipotenusa é {:.2f}".format(h))