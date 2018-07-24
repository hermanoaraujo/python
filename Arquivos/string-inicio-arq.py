'''
Escreva um programa que leia do teclado o nome de um arquivo texto e uma string, abra o
arquivo e inclua no início dele a string lida. 

José Hermano
'''

#Ler o nome do arquivo
nome_arq = input("Digite o nome do arquivo: ")

string = str(input("Digite um texto: "))

#Abre o arquivo com a opção 'r' de read
arquivo = open(nome_arq,'r')

#Salva o texto do arquivo em um variavel
texto = arquivo.read()
  
#fecha o arquivo
arquivo.close()

#Ler o arquivo com a opção 'w'
arquivo2 = open(nome_arq,'w')

#Coloca no inicio a string digitada pelo usuario
arquivo2.write(string+'\n'+texto)

#fecha o arquivo2
arquivo2.close()
print(string+'\n'+texto)



