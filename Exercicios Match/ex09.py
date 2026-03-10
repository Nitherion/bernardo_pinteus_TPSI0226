""" 9. Processamento de requisição
Recebe um dicionário com as chaves "metodo" e "conteudo".
Retorna:
“Requisição GET recebida” se o método for “GET”
“Requisição POST com dados válidos” se o método for “POST” e o conteúdo não estiver vazio
“Requisição POST sem dados” se o método for “POST” e o conteúdo estiver vazio
“Método não suportado” caso contrário
Exemplo:
Entrada → {"metodo": "POST", "conteudo": ""}
Saída → Requisição POST sem dados """

print("Introduza o método da requisição (GET ou POST):")
metodo = input().lower()

print("Introduza o conteúdo da requisição:")
conteudo = input().lower()

requisicao = {"metodo": metodo, "conteudo": conteudo}

match (requisicao):
    case {"metodo":"get"}:
        print("Requisição GET recebida")
    case {"metodo":"post", "conteudo": conteudo} if conteudo != "":
        print("Requisição POST com dados válidos")
    case {"metodo":"post", "conteudo": conteudo} if conteudo == "":
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")