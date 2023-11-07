#Convertendo medidas
n = float(input("Digite um valor em metros: "))

cm = n*100
mm = n*1000

print("{}m equivalem a {:.2f}cm ou a {:.2f}mm.".format(n,cm,mm))