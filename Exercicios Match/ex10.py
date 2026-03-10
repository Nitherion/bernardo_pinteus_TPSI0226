'''
10. Jogo: Pedra, Papel ou Tesoura
Cria um programa que receba duas jogadas:
Jogador 1
Jogador 2
Usa match para determinar o resultado:
Pedra ganha de Tesoura
Tesoura ganha de Papel
Papel ganha de Pedra
Se forem iguais, é Empate
Exemplo:
Entrada →
Jogador 1: pedra
Jogador 2: tesoura
Saída → Jogador 1 venceu
'''
print("--------------\nPedra, Papel ou Tesoura?\n--------------")
print("Jogador 1:")
p1 = input().lower()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Jogador 2:")
p2 = input().lower()

match(p1, p2):
    case ("pedra","tesoura") | ("tesoura","papel") | ("papel","pedra"):
        print("Vencedor: Jogador 1")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Vencedor: Jogador 2")
    case ("pedra", "pedra") | ("tesoura", "tesoura") | ("papel","papel"):
        print("Empate")
    case _:
        print("Jogada inválida. Insira pedra, papel ou tesoura.")