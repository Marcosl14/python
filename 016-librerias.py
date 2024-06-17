from random import randint, uniform, random, choice, shuffle, sample

print(randint(1,50)) # devuelve un integer aleatorio
print(uniform(1,5)) # devuelve un float aleatorio
print(random()) # devuelve un float aleatorio entre 0 y 1

print(choice([1,2,3,4,5])) # selecciona aleatoriamente un elemento de la lista

numeros = [1,2,3,4,5]

print(sample(numeros, 3)) # toma una muestra de 3 valores

shuffle(numeros)
print(numeros) # desordena la lista aleatoriamente
