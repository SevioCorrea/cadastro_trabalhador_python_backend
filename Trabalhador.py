from datetime import datetime

# Armazena os dados em um Dicionário
dados = dict()

# Lê os dados
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 - Não Tem): '))

# Verifica se tem CTPS
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Sexo'] = str(input('Sexo: [F/M]: ')).upper()

# Verificando o Sexo
    if dados['Sexo'] == 'M':
        if dados['idade'] >= 61:
            print('Você tem idade para se Aposentar.')
        else:
            tempo_restante = 61 - dados['idade']
            print(
                f'{dados["nome"]}, faltam {tempo_restante} anos para se aposentar.')

    elif dados['Sexo'] == 'F':
        if dados['idade'] >= 56:
            print(f'{dados["nome"]}, Você tem idade para se Aposentar.')
        else:
            tempo_restante = 56 - dados['idade']
            print(
                f'{dados["nome"]}, faltam {tempo_restante} anos para se aposentar.')
