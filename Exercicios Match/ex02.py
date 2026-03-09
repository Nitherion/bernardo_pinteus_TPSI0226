""" 2. Classificação de nota
Lê uma nota (0-100) e retorna uma classificação:
90 ou mais → Excelente
70-89 → Bom
50-69 → Suficiente
Abaixo de 50 → Insuficiente
Exemplo:
Entrada → 70-89
Saída →  Bom
"""

print("Introduza a nota (0-100):")
nota = int(input())


match nota:
    case _ if nota >= 90:
        print("Excelente")
    case _ if nota >= 70:
        print("Bom")
    case _ if nota >= 50:
        print("Suficiente")
    case _ if nota >= 50:
        print("Insuficiente")
    case _:
        print("Introduza uma nota válida entre 0 e 100.")