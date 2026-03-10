""" 8. Operação matemática
Recebe uma operação (em texto) e dois números.
Operações válidas: "soma", "subtrai", "multiplica", "divide".
Exemplo:
Entrada →
Operação: "divide"
Número 1: 20
Número 2: 4
Saída → 5 """

print("Introduza a operação (soma, subtrai, multiplica, divide):")
operacao = input()

print("Introduza o primeiro número:")
num1 = float(input())

print("Introduza o segundo número:")
num2 = float(input())

match (operacao):
    case "soma":
        print(num1 + num2)
    case "subtrai":
        print(num1 - num2)
    case "multiplica":
        print(num1 * num2)
    case "divide":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        print("Operação inválida.")