""" 6. Estado do servidor
Recebe um dicionário com as chaves "status" e "tempo_resposta".
Retorna:
“Servidor ativo” se o status for “ok”
“Servidor lento” se o status for “ok” e o tempo de resposta for maior que 200 ms
“Servidor indisponível” se o status for “erro”
“Estado desconhecido” caso contrário
Exemplo:
Entrada → {"status": "ok", "tempo_resposta": 350}
Saída → Servidor lento
 """

print("Introduza o status do servidor:")
status = input().lower()

if status == "erro":
    print("Servidor indisponível")
    server_status = {"status": status, "tempo_resposta": "-"}
    #se o status for "erro", não pede input do tempo de resposta
else:
    print("Introduza o tempo de resposta do servidor:")
    tempo_resposta = int(input())
    server_status = {"status": status, "tempo_resposta": tempo_resposta}
    
    match server_status:
        case {"status": "erro"}:
            print("Servidor indisponível")
        case {"status": "ok", "tempo_resposta": tempo} if tempo > 200:
            print("Servidor lento")
        case {"status": "ok"}:
            print("Servidor ativo")
        case _:
            print("Estado desconhecido")