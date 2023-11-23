#separando os dígitos de uma cadeia de números
num = int(input("digite um número qualquer entre 0 e 9999: "))

if num >= 0 and num <= 9999:
    snum = str(num)
    if len(snum) == 1:
        print("unidade: " + snum[0])
    elif len(snum) == 2:
        print("unidade: " + snum[1] + "\ndezena: " + snum[0])
    elif len(snum) == 3:
        print("unidade: " + snum[2] + "\ndezena: " + snum[1] + "\ncentena: " + snum[0])
    elif len(snum) ==4:
        print("unidade: " + snum[3] + "\ndezena: " + snum[2] + "\ncentena: " + snum[1] + "\nmilhar: " + snum[0])
else: print("Número digitado não corresponde às regras.")