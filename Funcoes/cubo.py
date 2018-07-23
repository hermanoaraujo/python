'''
Escreva uma função chamada cubo que receba um valor do tipo float e retorne a potência
elevado a 3 do mesmo. Faça também um programa para testar a função. 

'''

def cubo(valor):
  return valor**3


v = float(input("Digite o valor: "))
print(v," ao cubo ",cubo(v))
