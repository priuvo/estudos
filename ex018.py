#Seno, Cosseno e Tangente
import math
a = int(input("Digite um ângulo: "))

sen = math.sin(a)
cos = math.cos(a)
tg = math.tan(a)

print("Os valores de seno, cosseno e tangente do ângulo {}º são, respectivamente: {:.2f}, {:.2f} e {:.2f}.".format(a,sen,cos,tg))