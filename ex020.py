#Shuffle
import random

a1 = input("Alune 1: ")
a2 = input("Alune 2: ")
a3 = input("Alune 3: ")
a4 = input("Alune 4: ")

alunos = [a1, a2, a3, a4]
random.shuffle(alunos)

print("A ordem de apresentação será:\n1- {}\n2- {}\n3- {}\n4- {}".format(alunos[0], alunos[1], alunos[2], alunos[3]))
