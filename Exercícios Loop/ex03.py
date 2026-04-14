#Exercício 3: Ler a nota de 10 alunos, calcular a media e mostrar essa média.
total = 0
for i in range(1,11):
    nota = float(input(f"Introduza a {i}a nota: "))
   
    while nota < 0 or nota > 20:
        print(f"Nota inválida. Introduza uma nota entre 0 e 20.")
        nota = float(input(f"Introduza a {i}a nota: "))
        
    total += nota

print(f"Média = {total/10}")
