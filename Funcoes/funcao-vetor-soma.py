'''
Dado o vetor A = { 6,3,8,7,2,5 } , escreva um programa que informe a soma dos elementos do vetor A.
Crie uma função soma que receba um vetor e retorne a soma dos seus elementos.
'''
def soma(vetor):
  tam = len(vetor)
  soma = 0

  for i in range(tam):
    soma += vetor[i]
  return soma


v = [6,3,8,7,2,5]

print(soma(v))
    