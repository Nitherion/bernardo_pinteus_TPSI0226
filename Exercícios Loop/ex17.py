#Exercícios 17: Elabore um programa que determine os múltiplos de 5 mas não múltiplos de 3 …. De 1 a 1000 deve ser a sequência.
for num in range(5,1001, 5):
    if num % 3 != 0:
        print(num)