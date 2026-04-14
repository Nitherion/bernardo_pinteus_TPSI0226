#Exercícios 15: Elabore um programa que escreva no ecrã todas as linhas de código ASCII(0 a 255) e o código correspondente. Dispor de 20 em 20 com a condição de continuação ou saída do programa.

for n in range(0,256):
    print(f"{n}: {chr(n)}")
    if int(n)%20 == 0 and n != 0:
            continuar = input("Deseja continuar?\n1 - Sim\n2 - Não\n\n")
            if continuar == "2":
                break
            elif continuar == "1":
                continue
            else:
                print("Opção inválida\n")
                continuar = input("Deseja continuar?\n1 - Sim\n2 - Não\n\n")
                if continuar == "2":
                    break