'''
Escreva um programa que leia os seguintes dados de um conjunto de alunos: matrícula, nome e as
duas notas que ele obteve em suas avaliações. A condição de parada será a digitação de uma
matrícula igual 0 (zero). O programa deverá mostrar, para cada aluno, as seguintes informações:
matrícula, nome, média e situação (aprovado, se a média for igual ou superior a 7 e, reprovado, se a
média for inferior a 7). 

'''

matricula=int(input("Matricula: "))
maiorM=0
menorM=11
while matricula!=0:
    nome=input("Nome: ")
    nota1=float(input("Nota 1: "))
    nota2=float(input("Nota 2: "))
    media=(nota1+nota2)/2
    if media>maiorM:
        maiorM=media
        nomeMaiorM=nome
    if media<menorM:
        menorM=media
        nomeMenorM=nome
    print("Media: ", media)
    if media>=7:
        print("Aprovado")
    else:
        print("Reprovado")
    print("==========================")
    matricula=int(input("Matricula: "))
print("Resultado final")
print("A Maior media foi de: ", nomeMaiorM,"-",maiorM)
print("A Menor media foi de: ", nomeMenorM,"-",menorM)