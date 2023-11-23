#aumento de salário
salario = float(input("informe salário atual: "))

if salario > 1250:
    novoSalario = salario * 1.1
else: novoSalario = salario * 1.15

print ("O aumento será de R$ {:.2f}.".format(novoSalario-salario))