#Seno, Cosseno e Tangente
import math
a = int(input("Digite um ângulo: "))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))

print("Os valores de seno, cosseno e tangente do ângulo {}º são, respectivamente: {:.2f}, {:.2f} e {:.2f}.".format(a,sen,cos,tg))