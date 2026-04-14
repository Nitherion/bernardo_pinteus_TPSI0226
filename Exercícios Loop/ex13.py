#Exercício 13: Elabore um programa que leia um número e mostre a tabuada. (multiplicar de 1 a 10)
num = int(input("Introduza um número: "))
print(f"Tabuada do {num}")
for n in range(1,11):
    print(f"{num} x {n} = {num * n}")