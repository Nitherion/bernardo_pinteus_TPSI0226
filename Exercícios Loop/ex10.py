# Exercício 10: Elabore um programa que lê um número e escreve quantos divisores ele possui.

num = int(input("Introduza um número: "))
divisores = 0

for n in range(1,num+1):
    if num % n == 0:
        divisores += 1

print(f"O número {num} tem {divisores} divisores")