""" 4. Tipo de dado
Analisa um valor e retorna o seu tipo:
Número inteiro
Número decimal
String numérica
String textual
Lista
Tipo desconhecido
Exemplo:
Entrada → [10, 20, 30]
Saída → Lista """

valor = [10, 20, 30]

match valor:
    case int():
        print(f"Número inteiro")
    case float():
        print(f"Número decimal")
    case str() if valor.isdigit():
        print(f"String numérica")
    case str():
        print(f"String textual")
    case list():
        print(f"Lista")
    case _:
        print(f"Tipo desconhecido")