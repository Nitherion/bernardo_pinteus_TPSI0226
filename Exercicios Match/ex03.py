'''
3. Tipo de pedido
Recebe um dicionário com as chaves "tipo" e "valor".
Exibe:
“Compra de X€” se tipo for “compra”
“Venda de X€” se tipo for “venda”
“Pedido desconhecido” caso contrário
Exemplo:
Entrada → {"tipo": "venda", "valor": 250}
Saída → Venda de 250€
'''

print("Introduza o tipo do pedido:")
tipo = input().lower()
print("Introduza o valor do pedido:")
valor = float(input())

pedido = {"tipo": tipo, "valor": valor}

match pedido:
    case {"tipo": "compra", "valor": valor} | {"tipo": "venda", "valor": valor}:
        print(f"{tipo} de {valor:.2f}€")
    case _:
        print("Pedido desconhecido")
        

