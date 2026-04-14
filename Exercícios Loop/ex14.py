#Exercício 14: Altere o programa anterior para que mostre todas as tabuadas de 1 a 100. (ciclos for).

for num in range(1,101):
    print(f"\nTabuada do {num}")
    for n in range(1,11):
        print(f"{num} x {n} = {num * n}")
    num += 1