'''
Escreva um programa que abra um arquivo texto e o exiba na tela com todas as suas linhas
numeradas sequencialmente. 

José Hermano
'''

#Ler o nome do arquivo
nome_arq = input("Digite o nome do arquivo: ")

#Abre o arquivo com a opção 'r' de read
arquivo = open(nome_arq,'r')

#Ler a linha de um arquivo e retornar como string
linha = arquivo.readline()
#Criar um contador de linhas
cont_linhas = 0

while linha:
    print("Linha",cont_linhas,":",linha)
    linha = arquivo.readline()
    #incrementar o contador
    cont_linhas += 1
    
#fecha o arquivo
arquivo.close()


