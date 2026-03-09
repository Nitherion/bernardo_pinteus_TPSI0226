
""" 
Exercício 1: Converter Segundos em Horas, Minutos e Segundos 

Enunciado: 
Desenvolva um programa que assuma uma entrada em segundos e a converta para horas, minutos e segundos. 

Exemplo: 
Entrada: 3665 segundos 
Saída esperada: 1 hora, 1 minuto e 5 segundos.  
"""
print ("Introduza o tempo em segundos:")
tempo = int(input())
if(tempo > 0):
    horas=int(tempo/3600)
    resto = tempo%3600
    minutos = int(resto/60)
    segundos = resto%60
    print(f"{tempo} segundos = {horas}h{minutos}m{segundos}s")
else:
    print("Tempo inválido. Por favor, insira um número positivo.")
