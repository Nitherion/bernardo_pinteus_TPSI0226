""" Exercício 2: Ler 10 números, e determinar se o número par e número impar. """

numeros = []
for i in range(1,11):
    print(f"Introduza o {i}o número:")
    numeros.append(int(input()))
    
for numero in numeros:    
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
