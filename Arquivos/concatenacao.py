'''
Escreva um programa que crie um arquivo texto resultante da concatenação de dois outros
arquivos.

José Hermano
'''

#Ler o nome do primeiro arquivo
arquivo1 = input("Digite o nome do arquivo 1: ")

#Ler o nome do segundo arquivo
arquivo2 = input("Digite o nome do arquivo 2: ")

#Abre o arquivo 1 com a opção 'r' de read
arquivo1 = open(arquivo1,'r')

#Salva o texto do arquivo 1 em um variavel
texto1 = arquivo1.read()
  
#fecha o arquivo 1
arquivo1.close()

#Abre o arquivo 2 com a opção 'r' de read
arquivo2 = open(arquivo2,'r')

#Salva o texto do arquivo 2 em um variavel
texto2 = arquivo2.read()
  
#fecha o arquivo 2
arquivo2.close()

#Cria um novo arquivo com a opcao 'w'
arquivo3 = open('concatenacao.txt','w')

#Coloca no inicio a string digitada pelo usuario
arquivo3.write(texto1+'\n'+texto2)

#fecha o arquivo2
arquivo3.close()
print(texto1+'\n'+texto2)
