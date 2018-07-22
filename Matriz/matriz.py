lin = int(input("Digite a qtd de linhas: "))
col = int(input("Digite a qtd de colunas: "))

matriz = [] #Inicia a matriz

for i in range(lin): #For na quantidade de linhas
  linha = [] #Inicia a lista de linha
  for j in range(col):
    num=int(input("Digite um número M["+str(i)+"]["+str(j)+"]: "))
    linha.append(num)

  matriz.append(linha) #Adiciona na matriz a linha

print('\n\t\t'"MATRIZ ")
for i in range(lin):
  for j in range(col):
    print('\t',matriz[i][j],end='')
  print('')



