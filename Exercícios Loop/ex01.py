""" Exercício 1: Crie um algoritmo que mostre os 30 primeiros números ímpares e pares. """

numeros = []
pares = []
impares = []
for n in range(100):
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
        
print("Números pares:", pares[:30])
print("Números ímpares:", impares[:30])