from csv import DictReader, DictWriter

counter = amount = 0

file = str(input('Informe o nome do arquivo: ')).strip().lower()

# Se o usuario salvar como .csv, apenas recebe arquivo
if file [:-4] == '.csv':
    file_name = file
# Caso não, será incluido .csv
else:
    file_name = file.replace(' ','_') + '.csv'
   
#-----------------------Mostrar arquivo---------------------------------

try:
    with open(file_name) as doc:
        reading = DictReader(doc)

        print('| CLIENTE | ANUNCIO | DATA_INICIO | DATA_TERMINO | INVESTIMENTO_DIA |')

        for line in reading:
            print(f"| {line['CLIENTE']:<10} | {line['ANUNCIO']:^12} | {line['DATA_INICIO']:^5} | {line['DATA_TERMINO']:^17} | {line['INVESTIMENTO_DIA']:^7} | ")

        parameter = 'a'
except FileNotFoundError:
    parameter = 'w'
    print()

#--------------CONDICAO---------------------

condition = str(input('Realizar cadastro? [S / N]: ')).strip().lower()
if condition == 's':
    amount = int(input('Quantos: '))

#----------------------Cria arquivo-------------------------
with open(file_name, parameter) as doc:
    header = ['CLIENTE', 'ANUNCIO', 'DATA_INICIO', 'DATA_TERMINO', 'INVESTIMENTO_DIA']

    writing = DictWriter(doc, fieldnames=header)

    if parameter == 'w':
        writing.writeheader()

    while counter < amount:
        for counter in range(amount):
            print('\n','{:-^34}'.format(f'{counter + 1}'' Anuncio'))

            first_name = input('Digite o NOME ou Sair para encerrar: ').title()

            if first_name != 'Sair':
                nm_anuncio = str(input('Nome do anuncio: ')).title()
                dt_inicio = int(input('Data de inicio: '))
                dt_termino = int(input('Data término: '))
                vlr_dia = float(input('Valor investido dia: R$ '))

# ------------------Populando dicionário--------------------------

            writing.writerow (
                {
                    'CLIENTE': first_name,
                    'ANUNCIO': nm_anuncio,
                    'DATA_INICIO': dt_inicio,
                    'DATA_TERMINO': dt_termino,
                    'INVESTIMENTO_DIA': vlr_dia,
                                    
                }
            )
    counter +=1
print('----------Arquivo Salvo-------------')






