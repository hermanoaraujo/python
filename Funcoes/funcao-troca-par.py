'''
Dado o vetor X = { 8,9,3,5,7,2,6,4,8 }, escreva programa que gere um vetor Y cujos elementos são os
elementos de X com os números pares substituídos por 99. Crie uma função par que receba um vetor e
substitua seus números pares por 99.
'''

def par(vetor):
  tam = len(vetor)

  for i in range(tam):
    if ((vetor[i]%2) == 0):
      vetor[i] = 99

  return vetor

vetor = [8,9,3,5,7,2,6,4,8]
print (par(vetor))