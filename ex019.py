#Random
import random

a1 = input("Alune 1: ")
a2 = input("Alune 2: ")
a3 = input("Alune 3: ")
a4 = input("Alune 4: ")

alunos = [a1, a2, a3, a4]

escolhido = random.choice(alunos)

print("{} foi sorteade para apagar a louse.".format(escolhido))
