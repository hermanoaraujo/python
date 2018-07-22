'''
Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Faça um
programa que leia um número e determine se ele é ou não primo. 

'''
n=int(input("Digite numero: "))
cont_div=0
for i in range(n,0,-1):
    div=n%i
    if (div==0):
        cont_div=cont_div+1
if (cont_div==2):
    print("e primo")
else:
    print("nao e primo")