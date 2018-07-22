'''
Escreva um programa que, dada uma matriz quadrada de ordem N, de elementos inteiros,
exiba os elementos da diagonal principal, isto é, os elementos onde I = J.
Obs: N será lido (N <= 10). 


'''

A=[]
n=int(input('Ordem da matriz:'))
for i in range(n):
    linha=[]
    for j in range(n):
        print('Elemento[',i,'][',j,']:', sep='', end='')
        num=int(input())
        linha.append(num)
    A.append(linha)
print('\nmatriz A')
for i in range(n):
    for j in range(n):
        print('{0:4d}'.format(A[i][j]),end='')
    print('')
#Exibindo a diagonal principal (versão 1)
print('\nElementos da diagonal principal (versao 1)')
for i in range(n):
    for j in range(n):
        if i==j:
            print(A[i][j],' ',end='')
#Exibindo a diagonal principal (versão 2)
print('\nElementos da diagonal principal (versao 2)')
for i in range(n):
    print(A[i][i],' ', end='')