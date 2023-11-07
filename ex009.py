#Tabuada
n = int(input("Digite um número inteiro: "))

print("{0} x 0 = {1}\n{0} x 1 = {2}\n{0} x 2 = {3}".format(n, n*0, n*1, n*2, n*3))
print("{} x 3 = {}".format(n, n*3))
for i in range(5,11):
    print("{} x {} = {}".format(n, i, n*i))