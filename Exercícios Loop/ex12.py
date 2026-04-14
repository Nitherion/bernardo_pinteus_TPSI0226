# Exercício 12: Elabore um programa que leia quantos números quer que se efetue a soma, subtrações, divisões, multiplicações e no fim por meio de um acumulador diga quantas operações foram efetuadas. Exemplo introduzindo o número 60 o programa deve apresentar 60 a somar, dividir multiplicar e subtrair por todos os números menores que ele.
num = int(input("Introduza um númmero:"))
add, sub, mult, div = 0, 0, 0, 0
for n in range(1,num):
    print(f"{num} + {n} = {num + n}")
    add += 1
    print(f"{num} - {n} = {num - n}")
    sub += 1
    print(f"{num} * {n} = {num * n}")
    mult += 1
    print(f"{num} / {n} = {num / n}")
    div += 1
print(f"Contador de operações\nSomas: {add}\nSubtrações: {sub}\nMultiplicações: {mult}\nDivisões: {div}")