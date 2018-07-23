'''
Escreva um programa que leia 100 números inteiros e armazene no vetor L. Leia um número N e informe
se ele está no vetor L. Crie uma função acha que retorna True se um determinado número pertence a
um vetor e False, caso contrário.
'''

def acha(vetor,num):
  tam = len(vetor)

  for i in range(tam):
    if(vetor[i]==num):
      return True    
  return False


v = []
print("Vetor atual: ",v)
for i in range(3):
  num = int(input("Digite o numero "+str(i)+": "))
  v.append(num)
  print("Vetor atual: ",v)

n = int(input("Digite o numero a procurar: "))
print (acha(v,n))

