'''
Em uma pesquisa foram coletados os seguintes dados de um conjunto de 100 pessoas: nome, idade,
sexo, estado civil e salário. Neste contexto, escreva um programa que leia os dados coletados
durante a pesquisa, determine e mostre:
a) A quantidade de mulheres entrevistadas
b) A quantidade de homens entrevistados 
c) A quantidade de pessoas solteiras
d) A quantidade de pessoas casadas
e) O salário médio das mulheres entrevistadas
f) A idade média dos homens entrevistados
g) A quantidade de mulheres solteiras que ganham acima de R$ 2.000,00
h) A quantidade de homens com mais de 35 anos que ganham acima de R$ 2.000,00
'''

qtdPessoas = int(input("Digite a quantidade de pessoas: "))
mulheresEntrevistadas = 0
homensEntrevistados = 0
pessoasSolteiras = 0
pessoasCasadas = 0
salarioMulheres = 0
idadeHomens = 0
MulherAcima = 0
HomensAcima = 0

Homens = []
Mulheres = []
Solteiras = []
Casados = []

for i in range(1,qtdPessoas+1):
  print ("\nDados da",i,"Pessoa")
  nome = input("Digite o Nome: ")
  idade = int(input("Digite a idade:"))
  sexo = input("Digite o sexo (M/F):").lower()
  
  #Tratamento de Caracteres
  while (sexo != "m" and sexo != "f"):
    print("Caracter Invalido!!")
    sexo = input("Digite o sexo (M/F):").lower()
  ec = input("Estado Civil (S = solteiro / C = casado): ").lower()
  
  #Tratamento de Caracteres
  while (ec != "s" and ec != "c"):
    print("Caracter Invalido!!")
    ec = input("Estado Civil (S = solteiro / C = casado): ").lower()
  
  salario = int(input("Digite o salario: "))
  
  if (sexo == "f"):
    mulheresEntrevistadas = mulheresEntrevistadas + 1
    salarioMulheres = salarioMulheres + salario
    Mulheres.append(nome)
  elif (sexo == "m"):
    homensEntrevistados = homensEntrevistados + 1
    idadeHomens = idadeHomens + idade
    Homens.append(nome)
  
  if (ec == "s"):
    pessoasSolteiras = pessoasSolteiras + 1
    Solteiras.append(nome)
  elif (ec == "c"):
    pessoasCasadas = pessoasCasadas + 1
    Casados.append(nome)
  
  if (sexo == "f" and ec =="s" and salario > 2000):
    MulherAcima = MulherAcima + 1
  
  if (sexo == "m" and idade > 35 and salario > 2000):
    HomensAcima = HomensAcima + 1
    

if (qtdPessoas == 1):
  print("\n---- ",qtdPessoas," Pessoa Entrevistada ----")

else:
  print("\n---- ",qtdPessoas," Pessoas Entrevistadas ----")

print("Total de Mulheres Entrevistadas: ",mulheresEntrevistadas)
if (mulheresEntrevistadas > 0):
  print(Mulheres)
print("Total de Homens Entrevistados: ",homensEntrevistados)
if (homensEntrevistados > 0):
  print(Homens)
print("Total de Pessoas Solteiras: ",pessoasSolteiras)
print(Solteiras)
print("Total de Pessoas Casadas: " ,pessoasCasadas)
print(Casados)


# Calculo Idade Media homens
if (homensEntrevistados > 0):
  mediaIdadeHomens = (idadeHomens/homensEntrevistados)
  print("Idade Media dos Homens:",mediaIdadeHomens, "anos")
  print("Total de Homens > 35 Anos e Salario > 2000: ",HomensAcima)
if (mulheresEntrevistadas > 0):
  # Calculo Salario Mulheres
  mediaSalarioMulheres = (salarioMulheres/mulheresEntrevistadas)
  print("Total de Mulheres Solteiras com salario > 2000: ",MulherAcima)
  print("Media Salarial das Mulheres:",mediaSalarioMulheres)