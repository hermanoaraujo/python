'''
Escreva um programa que solicite ao usuário uma senha. Caso a senha digitada
esteja correta, o programa deverá mostrar senha correta. Caso contrário, o programa deverá
mostrar senha incorreta e pedir para o usuário tentar novamente digitar a senha correta. Mas, se o
usuário fornecer três senhas incorretas, o programa deverá encerrar a sua execução. (Sugestão:
Defina a senha como uma constante). 

'''
user_password = str(input("Digite uma senha:"))
senha = 12345
str(senha)


tentativa = 1

while (user_password != senha and tentativa < 4):
  if (str(user_password) == str(senha)):
    print("SENHA CORRETA")
    break
  else:
    print("SENHA INCORRETA!")
    print("VOCE POSSUI MAIS",4-tentativa,"TENTATIVAS")
    tentativa = (tentativa + 1)
    user_password = str(input("Digite uma senha:"))

if(tentativa == 4):    
  print("TENTATIVAS ENCERRARAM !!")