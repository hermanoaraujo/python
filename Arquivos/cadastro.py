'''
Escreva um programa que leia do teclado o nome, o sexo e a idade de várias pessoas e
armazene esses dados em um arquivo texto chamado CADASTRO.TXT, sendo uma pessoa por
linha e os dados separados por vírgula.
Obs: a leitura do nome vazio (string nula) encerra os dados de entrada

José Hermano
'''


#Ler nome, sexo, idade
nome = input("Digite o nome: ")
#Verifica se a string é vazia
while (nome != ''):
    #Pega os dados de Sexo e Idade
    sexo = input("Digite o sexo: ")
    idade = input("Idade: ")
    #Abre o arquivo Cadastro
    cadastro = open('CADASTRO.txt', 'a')
    #Escreve nos arquivos
    cadastro.write(nome+","+sexo+","+idade+"\n")
    #Fecha o arquivo cadastro
    cadastro.close()
    nome = input("Digite o nome: ")
print("Encerrado!")
