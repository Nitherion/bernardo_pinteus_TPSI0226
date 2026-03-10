""" 7. Classificação de produto
Recebe um dicionário com as chaves "categoria" e "preco".
Retorna:
“Produto de luxo” se categoria for “eletrônico” e preço acima de 1000
“Produto comum” se categoria for “eletrônico” e preço até 1000
“Produto alimentar” se categoria for “alimento”
“Categoria desconhecida” caso contrário
Exemplo:
Entrada → {"categoria": "eletrônico", "preco": 1500}
Saída → Produto de luxo
 """

print("Introduza a categoria do produto:")
categoria = input()

print("Introduza o preço do produto:")
preco= float(input())

produto = {"categoria": categoria, "preco": preco}

match (produto):
    case {"categoria": "eletronico", "preco": preco} if preco > 1000:
        print("Produto de luxo")
    case {"categoria": "eletronico", "preco": preco} if preco <= 1000:
        print("Produto comum")
    case {"categoria": "alimento", "preco": preco}:
        print("Produto alimentar")
    case _:
        print("Categoria descconheida")