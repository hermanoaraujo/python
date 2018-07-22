'''
Faça um programa que leia um número inteiro e determine se ele é par ou ímpar. Ao final, o
programa deve perguntar se o usuário deseja continuar (digitar outro número) ou sair. Se o usuário
quiser continuar, o programa deve repetir tudo de novo, caso contrário o programa deve ser
encerrado. 

'''
cont = "s"
while (cont == "s"):
  n = int(input("\nDigite um número: "))

  if (n%2 == 0):
    print (n,"é um numero PAR")
  else:
    print (n,"é um numero IMPAR")
  
  cont = input("\nDesejar Continuar? [S/N]").lower()
  
print ("Programa encerrado!")
