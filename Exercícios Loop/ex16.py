#Exercícios 16: Elabore um programa que constitua a média de 30 números pares que sejam introduzidos. Validando a entrada de números inteiros entre 1 e 50.
pares = []
while len(pares) < 30:
    num = int(input("Introduza um número inteiro par entre 1 e 50: "))
    if num < 1 or num > 50 or num % 2 != 0:
        print("\nNúmero inválido.")
        num = int(input("Introduza um número inteiro par entre 1 e 50: "))
    else:
        pares.append(num)
        
print(f"Média: {sum(pares) / len(pares)}")