""" Exercício 2: Encontrar o Maior e o Menor Valor entre 3 Números
Enunciado:
 Desenvolva um programa que analise 3 valores inteiros e informe qual o maior e qual o menor deles.
Exemplo:
 Entrada: num1 = 5, num2 = 2, num3 = 8
 Saída esperada:
 Maior: 8
 Menor: 2 """
 
num1=5
num2=2
num3=8
 
if num1>num2 and num2>num3:
    print (f"Maior: {num1}\nMenor: {num3}")
elif num1>num3 and num3>num2:
    print (f"Maior: {num1}\nMenor: {num2}")
elif num2>num1 and num1>num3:
    print (f"Maior: {num2}\nMenor: {num3}")
elif num2>num3 and num3>num1:
    print (f"Maior: {num2}\nMenor: {num1}")
elif num3>num1 and num1>num2:
    print (f"Maior: {num3}\nMenor: {num2}")
else:
    print (f"Maior: {num3}\nMenor: {num1}")
