#triângulo a partir de 3 retas
t1 = float(input("Digite o valor da primeira reta: "))
t2 = float(input("Digite o valor da segunda reta: "))
t3 = float(input("Digite o valor da terceira reta: "))

if t1 < t2+t3 and t2 < t1+t3 and t3 < t1+t2:
    print("As medidas de retas informadas podem formar triângulo.")
else: print("não rolou.")