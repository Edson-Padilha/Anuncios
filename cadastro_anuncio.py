
# Edson Marciano Rodrigues Padilha

from time import sleep
# Funcao para imprimir linha
def linha():
    print("\033[34m= \033[m" * 35) 

# Funcao para inserir cabecalho
def cabecalho(txt):
    linha()
    print(txt.center(70))
    linha()

# Funcao para ler lista do menu
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont+=1
    linha()
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc

# Funcao para validar entrada menu
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO: Por favor, digite um numero inteiro válido.')
            continue
        else:
            return n

# Funcao para verificar se o arquivo existe
def arqExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


arq = ('cadastro.txt')

if arqExiste(arq):
    print('Arquivo encontrado com sucesso!!!')
else:
    print('Arquivo não encontrado...')
    sleep(2)


cabecalho('\033[1;33mSISTEMA DE ANUNCIOS\033[m')

while True:    
    opcao = menu(['Cadastrar anuncio', 'Relatório por cliente', 'Relatório por data','Sair do sistema'])
    if opcao == 1:
        cabecalho('Opção: 1')
    elif opcao == 2:
        cabecalho('Opção 2')
    elif opcao == 3:
        cabecalho('Opção 3')
    elif opcao == 4:
        cabecalho('Saindo do sistema...')
        break
    else:
        cabecalho('\033[31mERRO: Digite uma opção válida!\033[m')
    sleep(2)