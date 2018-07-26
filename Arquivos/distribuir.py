'''
Escreva um programa que leia o arquivo gerado na questão 8 e copie os nomes distribuindo
para dois novos arquivos: machos.txt e femeas.txt (sendo um nome por linha).

José Hermano
'''

arquivo = open('CADASTRO.txt','r')
linhas = arquivo.readline()
while linhas:
    lista = linhas.split(",")
    print(lista[0])
    linhas = arquivo.readline()

    if (lista[1] == "Masculino"):
        machos = open('machos.txt','a+')
        machos.write(lista[0]+"\n")
        machos.close()
    else:
        femeas = open('femeas.txt','a+')
        femeas.write(lista[0]+"\n")
        femeas.close()

