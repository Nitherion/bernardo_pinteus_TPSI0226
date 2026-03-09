""" Exercício 6: Desconto de Compra
Enunciado:
 Uma loja oferece descontos de acordo com o valor da compra:
10% para compras até 200,00€.
15% para compras entre 200,01€ e 500,00€.
20% para compras acima de 500,00€.
 Desenvolva um Programa que leia o nome do cliente e o valor da compra e mostre o valor do desconto e o valor total a pagar.
Exemplo:
 Entrada: Cliente: João, Compra: 350
 Saída esperada:
 Nome: João
 Compra: 350,00€
 Desconto: 52,50€
 Total a pagar: 297,50€ """
 
print ("Introduza o nome do cliente:")
cliente = input()
print ("Introduza o valor da compra:")
compra = float(input())

if compra <= 200:
    desconto = compra * 0.10
elif compra > 500:
    desconto = compra * 0.20
else:
    desconto = compra * 0.15

print(f"Nome: {cliente}")
print(f"Compra: {compra:.2f}€")
print(f"Desconto: {desconto:.2f}€")
print(f"Total a pagar: {compra - desconto:.2f}€")