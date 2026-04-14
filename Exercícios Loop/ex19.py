#Exercícios 19:Escreva um programa que mostre os primeiros 60 números da serie bonatchi.

fibonacci = [0,1]
for i in range(2,60):
    fibonacci.append(fibonacci[i-1] + fibonacci [i-2])
print(fibonacci)
print(len(fibonacci))

""" 
0+1=1
1+1=2
2+1=3
3+2=5
5+3=8
8+5=13
0+1 = fib[i]
fib[i-1] + fib[i-2] = fib[i]

 """
