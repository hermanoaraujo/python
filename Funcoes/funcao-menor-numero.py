'''
Escreva uma função chamada menor que receba 3 números e retorne o menor deles. Faça
também um programa para testar a função.
'''

def menor(n1,n2,n3):
  menor = 0

  if(n1 < n2 and n1 <n3):
    menor = n1
  elif(n2 < n1 and n2 < n3):
    menor = n2
  else:
    menor = n3
  
  return menor

#Testando a função
n1 = int(input("Digite n1:"))
n2 = int(input("Digite n2:"))
n3 = int(input("Digite n3:"))
print(menor(n1,n2,n3))