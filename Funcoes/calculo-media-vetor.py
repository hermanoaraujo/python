'''
Escreva um programa que leia N números inteiros (máximo 20) e armazene em um vetor X. Calcule a
média dos elementos do vetor e informe quantos elementos estão abaixo da média do conjunto. Crie
uma função que faça a leitura dos elementos de um vetor; uma função que retorne a média dos
elementos de um vetor; e, finalmente, outra função que receba um vetor e um número (float), e retorne
quantos elementos do vetor estão abaixo desse número.
'''

def media(vetor):
  tam = len(vetor)
  soma = 0
  
  for i in range(tam):
    soma += vetor[i]
  
  media = soma/tam
  return media

def lerVetor(n):
  vetor = []
  for i in range(n):
    n = int(input("Digite o numero "+str(i)+" : "))
    vetor.append(n)
  return vetor

def abaixoMed(vetor,media):
  tam = len(vetor)
  abaixo = []

  for i in range(tam):
    if (vetor[i]<media):
      abaixo.append(vetor[i])
  
  return abaixo
  
vetor = lerVetor(3)
media = media(vetor)

print("Meu vetor é: ",vetor)
print("A media do Vetor é: ",media)
print("Abaixo da media é: ",abaixoMed(vetor,media))