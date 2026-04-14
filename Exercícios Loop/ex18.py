#Exercícios 18: Elabore um programa que leia uma entrada e diga quantos números perfeitos existem. Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial. 6=3+2+1 .

nperf = []
num = int(input("Introduza um número: "))

for n in range(1,num+1):      #iterar até ao número introduzido(num)
    divisores = []
    for i in range(1,n):            #iterar até ao número correspondente a cada iteração(n), para verificar os seus divisores
        if n % i == 0:              #verificar se o número é divisor de n,
            divisores.append(i)     #adicionar o divisor à lista de divisores
    if sum(divisores) == n:         #verificar se n é número perfeito
        nperf.append(n)             #adicionar o número perfeito à lista

if nperf == []:
    print("Não existem números perfeitos")
else:
    print(f"Números perfeitos: {len(nperf)}\n{nperf}")


