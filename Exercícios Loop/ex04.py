#Exercício 4: Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não.
num = int(input("introduza um número: "))
primo = True
for n in range(2,num):
    if num % n == 0:
        primo = False
        break
  
if primo:
    print(num, "é primo")
else:
    print(num, "não é primo")