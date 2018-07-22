'''
O Brasil possui 5 estados. Escreva um programa para cadastrar todos os
estados. Depois do cadastro, o programa deverá obter de vários usuários qual é o estado
que ele acha mais interessante. O programa encerra quando for informado um estado que não foi
previamente cadastrado. Ao final, o programa deverá exibir qual foi o estado mais votado,
considere empate. 

'''

ve=[]
vv=[]
for i in range(5):
    estado=input('Digite estado: ')
    ve.append(estado)
    vv.append(0)

est=input('Estado que mais gosta: ')
while ve.count(est)!=0:
    ind=ve.index(est)
    vv[ind]+=1
    est=input('Estado que mais gosta: ')
print('Vetor de Estados =',ve)
print('Vetor de Votos =',vv)

#Procurando o maior elemento no vetor vv

maior=0
for i in range(5):
    if vv[i]>maior:
        maior=vv[i]

''' pode usar
maior=max(vv)
'''
print('O maior elemento e',maior)

#Procurar os estados com maior votação
print('Estados com maior Votação: ')
for i in range(5):
    if vv[i]==maior:
        print(ve[i],' ',end='')