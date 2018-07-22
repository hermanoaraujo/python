'''
 Faça um programa que apresente o menu de opções abaixo:
OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM
O programa deve ler a opção do usuário e exibir, para cada opção, a respectiva mensagem:
1 - Olá. Como vai?
2 - Vamos estudar mais.
3 - Meus Parabéns!
0 - Fim de serviço.

'''
print ("########################")
print ("\nOPÇÕES")
print ("1 - SAUDAÇÃO")
print ("2 - BRONCA")
print ("3 - FELICITAÇÃO")
print ("4 - FIM")
print ("\n########################")

opt = int(input("Digite uma opção: "))
while (opt != 0 and opt != 1 and opt != 2 and opt != 3 ):
  print("Opcao invalida")
  opt = int(input("Digite uma opção: "))

if (opt == 1):
  print ("1 - Olá. Como vai?")
elif (opt == 2):
  print ("2 - Vamos estudar mais.")
elif (opt == 3):
  print ("3 - Meus Parabéns!")
else:
  print("0 - Fim de serviço")

