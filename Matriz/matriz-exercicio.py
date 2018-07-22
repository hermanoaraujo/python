'''
Escreva um programa que preencha duas matrizes 2x3 com valores inteiros fornecidos pelo
usuário. O programa deverá somar as duas matrizes, armazenando o resultado em uma
terceira matriz, que deverá ser exibida. 

'''

A=[]
B=[]
C=[]
lin=2
col=3
print('\nLeitura da matriz A')
for i in range(lin):
    linha=[]
    for j in range(col):
        print('Elemento[',i,'][',j,']: ',end='')
        num=int(input())
        linha.append(num)
    A.append(linha)
print('matriz A',A)

print('\nLeitura da matriz B')
for i in range(lin):
    linha=[]
    for j in range(col):
        print('Elemento[',i,'][',j,']: ',end='')
        num=int(input())
        linha.append(num)
    B.append(linha)
print('matriz B',B)

print('\nSoma das matrizes A e B')
for i in range(lin):
    linha=[]
    for j in range(col):
        soma=A[i][j]+B[i][j]
        linha.append(soma)
    C.append(linha)
print('matriz C',C) 