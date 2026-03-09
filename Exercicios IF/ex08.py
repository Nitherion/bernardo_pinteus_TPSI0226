""" Exercício 8: Calcular a Média de 10 Notas e informar notas iguais ou acima da media 
Enunciado:
Crie um programa que leia a nota de 10 alunos (notas de 0 a 20), calcule a média das notas e mostre a média. Além disso, informe quantos alunos ficaram com a nota igual ou acima da média. 
 """
 
print ("Introduza as notas dos 10 alunos:")
notas = []

top_students = 0
for i in range(10):
    nota = int(input(f"Introduza a nota do aluno {i+1}: "))
    notas.append(nota)
    
media = sum(notas) / len(notas)
for nota in notas:
    if nota >= media:
        top_students += 1
        
print(f"Média: {media:.1f}")
print(f"Alunos com nota igual ou acima da média: {top_students}")