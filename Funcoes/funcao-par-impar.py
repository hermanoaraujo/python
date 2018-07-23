'''
Escreva uma função chamada par que receba um número inteiro e retorne True se o número
for par ou False se for ímpar. Escreva também um programa que leia vários números inteiros
(encerrado com a leitura do valor 0) e, usando a função criada, informe quantos números pares
e quantos números ímpares foram lidos.
'''

def par(n1):
  if (n1%2 == 0):
    return True
  else:
    return False

numero = int(input("Digite um inteiro: "))
nPares = 0
nImpares = 0

while (numero !=0):
  
  if(par(numero) == True):
    nPares += 1
  else:
    nImpares += 1
  numero = int(input("Digite um inteiro: "))
  

print("Numeros Pares: ",nPares)
print("Numeros impares: ",nImpares)