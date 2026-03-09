""" 1. Tipo de dia
Cria um programa que receba o nome de um dia da semana e diga se é dia útil ou fim de semana.
Exemplo:
Entrada → domingo
Saída → Fim de semana """

print("Introduza o nome de um dia da semana:")
dia = input().lower()

match dia:
    case "segunda"|"terça"|"quarta"|"quinta"|"sexta":
        print (f"{dia} é um dia útil")
    case "sábado"|"domingo":
        print(f"{dia} é dia de fim de semana")