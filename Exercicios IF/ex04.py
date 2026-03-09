""" Exercício 4: Verificar se o Cheque Pode Ser Descontado
Enunciado:
 Desenvolva um Programa que leia o saldo inicial de um cliente de banco e leia também o valor de um cheque. Analise se o cheque pode ser descontado. Se o cheque não puder ser descontado, mostre essa informação, caso contrário, desconte o cheque e informe o saldo atualizado.
Exemplo:
 Entrada: Saldo = 500, Cheque = 300
 Saída esperada:
 Cheque descontado, saldo: 200 """
 
print ("Introduza o saldo inicial:")
saldo = int(input())
print ("Introduza o valor do cheque:")
cheque = int(input())

if cheque <= saldo:
    saldo -= cheque
    print(f"Cheque descontado, saldo: {saldo}")
else:
    print("Saldo insuficiente.")