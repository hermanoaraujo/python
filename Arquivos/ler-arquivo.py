'''
Escreva um programa que exiba na tela um arquivo texto cujo nome será lido pelo teclado. 
'''

nome_arq = input("Digite o nome do arquivo: ")
arquivo = open(nome_arq,'w')
arquivo.write('Arquivo criado com sucesso!: '+nome_arq)
print('Arquivo criado com sucesso!: '+nome_arq)
arquivo.close()
