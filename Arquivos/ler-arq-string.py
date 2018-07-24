'''
Escreva um programa que leia do teclado o nome de um arquivo texto e uma string, abra o
arquivo e inclua no final dele a string lida. 

José Hermano
'''

#Ler o nome do arquivo
nome_arq = input("Digite o nome do arquivo: ")
#Ler uma string
string = str(input("Digite um texto: "))

#Abre o arquivo com a opção 'a' de adição
arquivo = open(nome_arq,'a')
#Adiciona a string no final do arquivo
arquivo.write(string+"\n")
#fecha o arquivo
arquivo.close()
print(string+" adicionado no final do arquivo: "+nome_arq)

