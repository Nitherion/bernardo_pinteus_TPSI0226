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
valido = True
nome_completo = input("Introduza o seu nome completo: ")

#verifica input vazio
if nome_completo.strip() == "":
    valido = False   
    
#65 = A, 90 = Z, a = 97, 122 = z, espaço = 32

#verifica se o primeiro caracter (não) é letra maiúscula nem um espaço
elif (ord(nome_completo[0]) < 65 or ord(nome_completo[0]) > 90) and ord(nome_completo[0]) != 32:
    valido = False

else: 
    for i in range(1, len(nome_completo)):
        #
        #se o caracter nao for uma letra MAIÚSCULA                      e           nao for letra minúscula e não for espaço
        if (ord(nome_completo[i]) < 65 or ord(nome_completo[i]) > 90 ) and (ord(nome_completo[i]) < 97 or ord(nome_completo[i]) > 122) and ord(nome_completo[i]) != 32:
            valido = False
            break
        
        #se o caracter anterior nao for um espaço    E          for letra MAIÚSCULA
        if ord(nome_completo[i-1]) != 32 and (ord(nome_completo[i]) >= 65 and ord(nome_completo[i]) <= 90):
            valido = False
            break
        
        #se o caracter anterior for um espaço E nao for letra MAIÚSCULA
        if ord(nome_completo[i-1]) == 32 and (ord(nome_completo[i]) < 65 or ord(nome_completo[i]) > 90) and ord(nome_completo[i]) != 32: 
            valido = False
            break

if valido:
    print("Nome válido!")
else:
    print("Nome inválido: contém caracteres não permitidos.")