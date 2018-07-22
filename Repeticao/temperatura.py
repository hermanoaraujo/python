'''
Faça um programa que, dadas as temperaturas dos 30 dias do mês de abril diga qual o dia mais
quente e o dia mais frio do mês (obs: suponha que não haja empates). 
'''

mes = str(input("Digite o Mes: "))
ano = "2018"
dias = int(input("Digite a Qtd. de dias: "))

diaQuent = 0
diaFrio = 0
tempMaisQuent = 0
tempMaisFrio = 100

for i in range(1,dias+1):
  if (i < 10):
    print("\n0"+str(i)+"/"+mes+"/"+ano)
    temperatura = int(input("Digite a Temperatura :"))
  else:
    print(str(i)+"/"+mes+"/"+ano)
    temperatura = int(input("Digite a Temperatura :"))
  
  if (temperatura > tempMaisQuent):
    tempMaisQuent = temperatura
    diaQuent = "0"+str(i)+"/"+mes+"/"+ano
  if (temperatura < tempMaisFrio):
    tempMaisFrio = temperatura
    diaFrio = "0"+str(i)+"/"+mes+"/"+ano

print("="*55)
print("\nDia mais Quente foi o dia",diaQuent,"Temperatura",tempMaisQuent,"Graus")
print("\nDia mais Frio foi o dia",diaFrio,"Temperatura",tempMaisFrio,"Graus")
print("="*55)