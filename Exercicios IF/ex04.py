""" Exercício 4: Verificar se o Cheque Pode Ser Descontado
Enunciado:
 Desenvolva um Programa que leia o saldo inicial de um cliente de banco e leia também o valor de um cheque. Analise se o cheque pode ser descontado. Se o cheque não puder ser descontado, mostre essa informação, caso contrário, desconte o cheque e informe o saldo atualizado.
Exemplo:
 Entrada: Saldo = 500, Cheque = 300
 Saída esperada:
 Cheque descontado, saldo: 200 """
 
saldo = 500
cheque = 300

if cheque <= saldo:
    saldo -= cheque
    print(f"Cheque descontado, saldo: {saldo}")
else:
    print("Saldo insuficiente.")