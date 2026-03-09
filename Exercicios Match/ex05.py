""" 5. Análise de mensagem
Recebe uma mensagem e retorna:
“Saudação” se for “olá” ou “bom dia”
“Pergunta” se terminar com “?”
“Despedida” se contiver “tchau” ou “adeus”
“Mensagem genérica” caso contrário
Exemplo:
Entrada → “Tudo bem?”
Saída → Pergunta
 """
print("Introduza uma mensagem:")
mensagem = input().lower()

match mensagem:
    case "olá" | "bom dia":
        print("Saudação")
    case _ if mensagem.endswith("?"):
        print("Pergunta")
    case _ if "tchau" in mensagem or "adeus" in mensagem:
        print("Despedida")
    case _:
        print("Mensagem genérica")