'''
Exercício 11: Elabore um ciclo for para produzir o seguinte output.
	1
	22
	333
	4444
	55555
'''
num = 1
while num<=5:
    numstr = str(num)
    print(num*numstr)
    num += 1