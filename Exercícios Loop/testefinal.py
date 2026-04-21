'''Teste Final:
Elabore um programa que:
    - leia um valor de entrada e 
    - mostre para cada valor até ao 1 se é número Primo, Quantos divisores e números perfeitos
    - o Programa deve validar entradas entre 1 e 30.000, e
    - parar de 10 em 10 valores com instrução para parar ou continuar.

No mesmo programa:
    - use um menu e
    - Elabore uma calculadora simples (+,-,*,/) com a função extra tabuada.
    - Validar entradas de 1 a 1000 (nota a tabuada deve apresentar todas as multiplicações de 1 ate ao máximo introduzido) e 
    - deve parar de 20 em 20 valores.

# Ex4: primos; Ex10: qts divisores; Ex18: nrs perfeitos; Ex12: calculadora; Ex13: tabuada
'''

num = int(input("Introduza um número: "))
contador = 0

while num < 1 or num > 30000:
    num = int(input("Número inválido. Introduza um número entre 1 e 30000: "))

#percorrer todos os números entre 1 e num
for n in range(num,0,-1):
    print()
    divisores = []
    contador += 1
#Divisores
    for i in range(1,n+1):  
        primo = True
        
        #guardar os divs na lista    
        if n % i == 0:
            divisores.append(i) 
                       
            #verificar se é primo
            if len(divisores) > 2 or n == 1:
                primo = False   

    if n > 0:
        print(f"{n} tem {len(divisores)} divisores: {divisores}")
        if primo:
            print(f"{n} é primo")
        else:
            print(f"{n} não é primo")
            
        #Num perfeito
        if (sum(divisores) - n) == n:
            print(f"{n} é um número perfeito")
            
    if contador % 10 == 0:
            continuar = input("\nContinuar?\n1 - Sim\n2 - Não\n")
            if continuar == "2":
                break
            elif continuar == "1":
                continue
            else:
                while continuar != "1" and continuar != "2":
                    continuar = input("Escolha inválida.\nContinuar?\n1 - Sim\n2 - Não\n")
            

 
    
#----CALCULADORA----
while True:
    print("\nCALCULADORA\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Tabuada\n6 - Sair\n")
    calc_choice = int(input())
    
    match calc_choice:
        case 1:
            num1 = int(input("Introduza o 1o número: "))
            num2 = int(input("Introduza o 2o número: "))
            print(f"{num1} + {num2} = {num1 + num2}")
        
        case 2:
            num1 = int(input("Introduza o 1o número: "))
            num2 = int(input("Introduza o 2o número: "))
            print(f"{num1} - {num2} = {num1 - num2}")
            
        case 3:
            num1 = int(input("Introduza o 1o número: "))
            num2 = int(input("Introduza o 2o número: "))
            print(f"{num1} * {num2} = {num1 * num2}")
            
        case 4:
            num1 = int(input("Introduza o 1o número: "))
            num2 = int(input("Introduza o 2o número: "))
            print(f"{num1} / {num2} = {num1 / num2}")
            
        case 5:
            num1 = int(input("Introduza um número: "))
            if num1 < 1 or num1 > 1000:
                num1 = int(input("Número inválido.\nIntroduza um número entre 1 e 1000: "))
            
            print(f"Tabuada do {num1}")
            for n in range(1,num1+1):
                print(f"{num1} x {n} = {num1 * n}")
                
                if n % 20 == 0:
                 #   print(f"{num1} x {n} = {num1 * n}")
                    continuar = input("Continuar?\n1 - Sim\n2 - Não\n")
                    if continuar == "2":
                        break
                    elif continuar == "1":
                        continue
                    else:
                        while continuar != "1" and continuar != "2":
                            continuar = input("Escolha inválida.\nContinuar?\n1 - Sim\n2 - Não\n")             
        case 6:
            exit()
        case _:
            continue