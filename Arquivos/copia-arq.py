'''
Escreva um programa que copie um arquivo texto (cujo nome será lido pelo teclado) para um
novo arquivo chamado COPIA.TXT, porém substituindo todos os brancos contidos no arquivo
pelo ponto.

José Hermano
'''

#Ler o nome do arquivo
nome_arq = input("Digite o nome do arquivo: ")
#Abre o arquivo com a opção 'r' de read
arquivo = open(nome_arq,'r')
#Retorna todas os caracters do arquivo com a função read() para a variavel linha
linha = arquivo.read()
#Substitui o espaço por um .
nova_linha = linha.replace(' ','.')
#fecha o arquivo
arquivo.close()
print("Texto: ",linha," do arquivo: ",nome_arq," modificado em : copia.txt")
#cria um novo arquivo copia.txt substituindo o que tem nele com o 'w'
arquivo2 = open('copia.txt','w')
#escreve no arquivo a nova_linha
arquivo2.write(nova_linha)
#fecha o arquivo2
arquivo2.close()
