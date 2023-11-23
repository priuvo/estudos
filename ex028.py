#Adivinhando o número que o PC pensou
from random import randint

pc = randint(0,5)
num = int(input("Tente adivinhar o número que pensei, entre 0 e 5...:"))

if num == pc:
    print ("PARABÉNS, ACERTOU! :D")
else: print("ERRÔOOO! *faustão")
