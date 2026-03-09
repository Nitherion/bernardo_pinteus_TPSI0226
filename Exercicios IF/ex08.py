""" Exercício 8: Calcular a Média de 10 Notas e informar notas iguais ou acima da media 
Enunciado:
Crie um programa que leia a nota de 10 alunos (notas de 0 a 20), calcule a média das notas e mostre a média. Além disso, informe quantos alunos ficaram com a nota igual ou acima da média. 
 """
 
notas = [12, 15, 18, 10, 20, 8, 14, 17, 19, 11]

media = sum(notas) / len(notas)
print(f"Média: {media:.1f}")

top_students = 0
for nota in notas:
    if nota >= media:
        top_students += 1

print(f"Alunos com nota igual ou acima da média: {top_students}")