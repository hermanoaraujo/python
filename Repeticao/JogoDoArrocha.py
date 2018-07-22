'''
Jogo do Arrocha! Esse é um jogo que consiste em tentar adivinhar um número (previamente
escolhido), que está representado dentro de um intervalo de números inteiros.
Inicialmente, o jogador 1 prepara o jogo, definindo um intervalo e escolhendo um número (secreto)
que está dentro desse intervalo, esse número escolhido não pode ser os números limites do
intervalo.
Uma vez preparado o jogo, o jogador 2 tentará adivinhar esse número “chutando” valores até
acertar (ganha) ou arrochar o número (perde), ou informar valor inválido (perde). Um número é
considerado inválido se estiver fora do intervalo do jogo. 

'''
import random

inter_1 = int(input("JOGADOR 1 - Digite o 1 intervalo: "))
inter_2 = int(input("JOGADOR 1 - Digite o 2 intervalo: "))
num_Secret = random.randint(inter_1,inter_2)
   
## arrochado
arrochado_1 = num_Secret - 1
arrochado_2 = num_Secret + 1
   

while (num_Secret == inter_1 or num_Secret == inter_2):
  print("ERRO!! O NÚMERO SECRETO NAO PODE SER O INTERVALO.")
  num_Secret = random.randint(inter_1,inter_2)

print("\n  --- JOGO CONFIGURADO ---\n")
chute = 0

while(chute != num_Secret):
  
  if (arrochado_1 == inter_1 and arrochado_2 == inter_2):
    print ("\n----------------------------------")
    print("--- VOCE PERDEU ARROCHADO ---")
    print("--- Itervalo de",inter_1,"até",inter_2," ---")
    print("--- JOGADOR 1 VENCEU! ---")
    print ("\n----------------------------------")
    break
  
  print("--- Itervalo de",inter_1,"até",inter_2," ---")
  chute = int(input("JOGADOR 2 - Chute um número: "))
  
  if (chute == inter_1 or chute == inter_2):
    print ("\n----------------------------------")
    print("        --- VOCE PERDEU ---")
    print("        --- JOGADOR 1 VENCEU! ---")
    print ("\n----------------------------------")
    break
  
  elif (chute != num_Secret and chute < num_Secret and chute > inter_1):
    print("\n       --- ERROU --- ")
    inter_1 = chute
    
  elif (chute != num_Secret and chute > num_Secret and chute < inter_2):
   print("\n        --- ERROU ---")
   inter_2 = chute
   
  elif (chute < inter_1 or chute > inter_2):
    print ("\n----------------------------------")
    print ("\n VOCÊ PERDEU! FORA DO INTERVALO")
    print (" PRESTE MAIS ATENÇÃO!")
    print ("\n----------------------------------")
    break

  else:
    print ("\n----------------------------------")
    print ("\n---- PARABENS VOCÊ GANHOU ! ---- ")
    print ("\n----------------------------------")
    break