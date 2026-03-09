""" Exercício 5: Ler 3 Valores e Exibir em Ordem Crescente e Decrescente
Enunciado:
 Ler 3 valores inteiros e apresentar os valores dispostos em ordem crescente e decrescente.
Exemplo:
 Entrada: num1 = 4, num2 = 9, num3 = 2
 Saída esperada:
 Crescente: 2, 4, 9
 Decrescente: 9, 4, 2 """
 
print ("Introduza o primeiro número:")
num1 = int(input())
print ("Introduza o segundo número:")
num2 = int(input())
print ("Introduza o terceiro número:")
num3 = int(input())
 
if num1>num2 and num2>num3:
    print (f"Crescente: {num3}, {num2}, {num1}")
    print (f"Decrescente: {num1}, {num2}, {num3}")
elif num1>num3 and num3>num2:
    print (f"Crescente: {num2}, {num3}, {num1}")
    print (f"Decrescente: {num1}, {num3}, {num2}")
elif num2>num1 and num1>num3:
    print (f"Crescente: {num3}, {num1}, {num2}")
    print (f"Decrescente: {num2}, {num1}, {num3}")
elif num2>num3 and num3>num1:
    print (f"Crescente: {num1}, {num3}, {num2}")
    print (f"Decrescente: {num2}, {num3}, {num1}")
elif num3>num1 and num1>num2:
    print (f"Crescente: {num2}, {num1}, {num3}")
    print (f"Decrescente: {num3}, {num1}, {num2}")
else:
    print (f"Crescente: {num1}, {num2}, {num3}")
    print (f"Decrescente: {num3}, {num2}, {num1}")