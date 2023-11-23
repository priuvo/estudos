#Verificando a letra A no texto
frase = input ("Digite uma frase qualquer: ")

lista = list(frase)
pos = 0
contador = 0
primeira = 0
ultima = 0

for i in lista:
    pos = pos + 1
    if i == "a" or i == "A":
        contador = contador + 1
        if contador == 1:
            primeira = pos
        else: ultima = pos

print ("A letra 'A' aparece " + str(contador) + " vezes na frase. A primeira vez que ela aparece é na posição " + str(primeira) + ", a última é na posição " + str(ultima) + ".")