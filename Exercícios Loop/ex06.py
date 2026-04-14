#Exercício 6: Crie um algoritmo que mostre os 10 primeiros números primos.
primos=0
num = 2
while primos < 10:
    primo = True
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            primo = False
            break
    if primo:
        primos += 1
        print(num)
    num+=1

