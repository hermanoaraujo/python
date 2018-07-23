def cria_matriz(lin,col):
    mat=[]
    for i in range(lin):
        linha=[]
        for j in range(col):
            print('elemento[',i,'][',j,']:',end='')
            num=int(input())
            linha.append(num)
        mat.append(linha)
    return(mat)

def exibe(mat,lin,col):
    print('\nMatriz')
    for i in range(lin):
        for j in range(col):
            print('\t',mat[i][j],end='')
        print('')
              
        
lin=int(input('Num linhas: ' ))
col=int(input('Num colunas: '))
matriz=cria_matriz(lin,col)
exibe(matriz,lin,col)