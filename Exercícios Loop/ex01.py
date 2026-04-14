#Exercício 1: Crie um algoritmo que mostre os 30 primeiros números ímpares e pares.
"""
numeros = []
pares = []
impares = []
for n in range(60):
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
        
print("Números pares:", pares[:30])
print("Números ímpares:", impares[:30])
"""

num = 0
pares = []
impares = []
while len(pares) < 30 or len(impares) < 30:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
        num += 1
        
print("Números pares:", pares)
print("Números ímpares:", impares)