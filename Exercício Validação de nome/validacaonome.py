'''Cria um programa que peça ao utilizador para introduzir o seu nome completo. O programa deve validar se o nome contém apenas letras e espaços, a primeira letra do nome deve ser sempre maiúscula e a seguir ao espaço também, usando os códigos ASCII de cada caractere.
Exemplo:
Pedro Pereira 

Se o nome for válido, o programa deve exibir:
 "Nome válido!"
Caso contrário, deve exibir:
 "Nome inválido: contém caracteres não permitidos."

No caso de o programa encontrar um caractere invalido deve parar a execução.

Exemplos Inválidos:
Miguel PriMo
Luis AnseLmo
Guilherme ramos
'''
#valido = True
nome_completo = input("Introduza o seu nome completo: ")
for i in range(len(nome_completo)):
    
    #print(i, ord(nome_completo[i]))

    
    #se o cada caracte for:
    #              espaços          ou                  letras mauisculas                           ou                      letras minusculas
    if (ord(nome_completo[i]) == 32 or ord(nome_completo[i]) >= 65 and ord(nome_completo[i]) <= 90) or ord(nome_completo[i]) >= 97 and ord(nome_completo[i]) <= 122:
        #print("Nome só contém letras e espaços")
        valido = True
        #se a primeira letra for um espaço e a letra seguinte uma maíuscula
        if ord(nome_completo[i]) == 32 and ord(nome_completo[i+1]) >= 65 and ord(nome_completo[i+1] <= 90):
            #print("a posiçao 0 é um espaço e a letra seguinte é maiúscula")
            valido = True
      #  else:
        #    valido = False
    #se algum caracter não for espaço, letra maiúscula nem minuscula    
    else:
        valido = False


if valido:
    print("Nome válido!")
else:
    print("Nome inválido: contém caracteres não permitidos.")
    