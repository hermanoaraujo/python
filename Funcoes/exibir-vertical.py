'''
Escreva uma função que receba como parâmetro uma string e a exiba na vertical, ou seja, com uma
letra em cada linha. Faça também um programa para testar a função.
'''

def exibirVertical(string):
  tam = len(string)
  for i in range(tam):
    print(string[i])

exibirVertical("teste")

