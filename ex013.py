#Cálculo de aumento %
s = float(input("Informe o salário atual: "))
a = 0.15
ns = s *(1+a)

print("O novo salário, considerando aumento de {}%, será de R$ {:.2f}.".format(a*100,ns))
