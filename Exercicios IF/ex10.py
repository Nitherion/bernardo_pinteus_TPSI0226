""" Exercício Loop: Identificar Números Pares e Ímpares
Enunciado:
 Leia 10 números e determine quantos são pares e quantos são ímpares.
Exemplo:
 Entrada: 2, 3, 5, 6, 8, 9, 10, 12, 14, 15
 Saída esperada:
 Pares: 6
 Ímpares: 4 """
 
num = [2, 3, 5, 6, 8, 9, 10, 12, 14, 15]
pares = 0
ímpares = 0

for n in num:
    if n % 2 == 0:
        pares += 1
    else:
        ímpares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {ímpares}")