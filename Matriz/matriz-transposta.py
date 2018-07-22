'''
Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma dada
matriz. Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será representada
por Ct de ordem n x m onde cada elemento de Ct [i,j] = C [j,i]. 

'''

a=[]
lin=2
col=3
#leitura da matriz
for i in range(lin):
    linha=[]
    for j in range(col):
        n=int(input('digite numero: '))
        linha.append(n)
    a.append(linha)
#Gerando a matriz transposta
at=[]
for i in range(col):
    linha=[]
    for j in range(lin):
        linha.append(a[j][i])
    at.append(linha)
print(a)
print(at)    