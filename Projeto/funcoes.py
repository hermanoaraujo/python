def menu(opt):
    
    if(opt == 1):
        resposta = 'sim'
        while (resposta != 'n'):
            print('\n----- CADASTRAR USUARIO -----\n')
            nome = input("Digite o nome: ")
            sexo = input("Digite o sexo: ")
            idade = input("Digite a idade: ")
            cadastrarUser(nome,sexo,idade)
            resposta = input("Deseja cadastrar outro usuario? [S/n]: ")
    elif(opt == 2):
        print('\n----- LISTAR USUARIO -----\n')
        listarUsers()
    elif(opt == 3):
        limparUsers()
        
    elif(opt == 0):
        print('#'*40)
        print('')
        print('1 - Cadastrar Usuarios')
        print('2 - Listar Usuarios')
        print('3 - Deletar Usuarios')
        print('0 - Voltar')
        print('')
        print('#'*40)
        opt = int(input("Digite a opção: "))
        menu(opt)
        
        

def cadastrarUser(nome, sexo, idade):
    #Abre o arquivo Cadastro
    cadastro = open('CADASTRO.txt', 'a')
    #Escreve nos arquivos
    cadastro.write(nome+","+sexo+","+idade+"\n")
    #Fecha o arquivo cadastro
    cadastro.close()
    print(nome," Cadastrado com sucesso!")
    menu(0)


def listarUsers():

    #Abre o arquivo com a opção 'r' de read
    arquivo = open('CADASTRO.txt','r')

    #Ler a linha de um arquivo e retornar como string
    linha = arquivo.readline()
    #Criar um contador de linhas
    cont_linhas = 0

    while linha:
        print("Usuario",cont_linhas,":",linha)
        linha = arquivo.readline()
        #incrementar o contador
        cont_linhas += 1
        
    #fecha o arquivo
    arquivo.close()
    menu(0)

def limparUsers():
    #Abre o arquivo com a opção 'w' e limpa
    arquivo = open('CADASTRO.txt','w')
    #fecha o arquivo
    arquivo.close()
    print("Uusuarios Deletados! ")
    menu(0)
