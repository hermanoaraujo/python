'''
Escreva um programa que leia o arquivo gerado na questão 8 e calcule a média de idade dos
homens e a média de idade das mulheres.

José Hermano
'''

#Ler as linhas do arquivo CADASTRO.txt com o readline()
arquivo = open('CADASTRO.txt','r')
linhas = arquivo.readline()

#Inicializa os contadores
contMasc = 0
somaMasc = 0
contMulh = 0
somaMulh = 0

#Enquanto houver linhas..
while linhas:
    
    #Transforma as linhas em listas
    lista = linhas.split(",")
    linhas = arquivo.readline()

    #Se o campo 1 da lista for = Masculino então incrementa
    if (lista[1] == "Masculino"):
        contMasc += 1
        somaMasc += int(lista[2])
    else:
        contMulh += 1
        somaMulh += int(lista[2])

#Calculo das medias
mediaHomens = (somaMasc/contMasc)
mediaMulher = (somaMulh/contMulh)

print("A Media da idade dos homens é de :",mediaHomens)
print("A Media da idade das mulheres é de :",mediaMulher)


