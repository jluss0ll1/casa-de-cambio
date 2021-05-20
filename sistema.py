from operacoes import Operacao 
from typing import List, Dict
from time import sleep
import pickle


registros: List[Operacao] = [] 

def main() -> None:
    menu()

def menu() -> None:
    print('=====================================================')
    print('================== MUITO DINHEIRO ===================')
    print('================== Casa de Câmbio ===================')
    print('=====================================================')

    print('Seja bem-vindo! Selecione uma opção: ')
    print('1 - Cadastrar Operação')
    print('2 - Listar Operações')
    print('3 - Buscar Operações por Cliente e Intervalo de Tempo')
    print('4 - Relatório: Valor Total das Operações')
    print('5 - Relatório: Valor Total das Taxas Cobradas')
    print('6 - Relatório: Valores por Cliente e Intervalo de Tempo')
    print('7 - Salvar Registros')
    print('8 - Carregar Registros')
    print('9 - Sair do Sistema')

 
    opcao: int = int(input('Selecione uma opção: '))

    if opcao == 1:
        cadastrar_operacao()

    elif opcao == 2:
        listar_operacoes()

    elif opcao == 3:
        nomecliente = input('Informe o nome do cliente: ')
        datainicial = input('Informe a data inicial do intervalo: ')
        datafinal = input('Informe a data final do intervalo: ')
        operacao: Operacao = busca_operacoes_por_cliente(nomecliente, datainicial, datafinal)
        print('----------')
        for o in operacao:
            print(o)
            print('----------')
        sleep(1)
        menu()

    elif opcao == 4:
        soma_op = round(total_operacoes(), 2)
        print(f'Valor total das operações: BRL {soma_op}')
        sleep(1)
        menu()

    elif opcao == 5:
        soma_taxas = round(total_taxas(), 2)
        print(f'Valor total das taxas cobradas: BRL {soma_taxas}')
        sleep(1)
        menu()

    elif opcao == 6:
        nomecliente = input('Informe o nome do cliente: ')
        datainicial = input('Informe a data inicial do intervalo: ')
        datafinal = input('Informe a data final do intervalo: ')
        operacao: Operacao = totais_por_cliente(nomecliente, datainicial, datafinal)
        print('----------')
        print(f'Valor total das operações realizadas pelo cliente {nomecliente} do dia {datainicial} até o dia {datafinal}:')
        print(f'BRL {operacao[0]}')
        print(f'Valor total das taxas cobradas do cliente {nomecliente} do dia {datainicial} até o dia {datafinal}:')
        print(f'BRL {operacao[1]}')
        print('----------')
        sleep(2)
        menu()

    elif opcao == 7:
        salvar_operacoes()

    elif opcao == 8:
        abrir_registros()

    elif opcao == 9:
        sair()

    else:
        print('Opção inválida. Tente novamente.')
        sleep(1)
        menu()


# Opção 1 - Cadastrar Operação
def cadastrar_operacao() -> None:
    print('Cadastro de Operação: ')
    print('======================')

    try:
        nome: str = input('Informe o nome do cliente: ')
        moeda_origem: str = input('Informe a moeda de origem: ')
        moeda_destino: str = input('Informe a moeda de destino: ')
        valor_original: float = input('Informe o valor original: ')

        operacao: Operacao = Operacao(nome, moeda_origem, moeda_destino, valor_original)

        registros.append(operacao)
        print('----------------')
        print(operacao)
        print(f'A operação para o cliente {operacao.nome} foi concluída com sucesso!')
        sleep(2)
        menu()
    except:
        print('Erro na operação! Favor tentar novamente.')
        sleep(1)
        menu()

# Opção 2 - Listar Operações
def listar_operacoes() -> None:
    if len(registros) > 0:
        print('Lista de operações') 
        print('==================')

        for registro in registros:
            print(registro)
            print('==================')
            sleep(1)
    else: 
        print('Não há operações registradas no sistema!')
    sleep(1)
    menu()

# Opção 3 - Buscar Operações por Cliente e Intervalo de Tempo
def busca_operacoes_por_cliente(nome: str, data_inicial: str, data_final: str) -> Operacao:
    o: Operacao = []

    for registro in registros:
        if (registro.nome == nome) and (registro.data_operacao >= data_inicial) and (registro.data_operacao <= data_final):
            o.append(registro)
    return o

# Opção 4 - Relatório: Valor Total das Operações
def total_operacoes():
    lista_op = []
    
    for registro in registros:
        lista_op.append(float(registro.valor_real))
    total_op = sum(lista_op)
    return total_op

# Opção 5 - Relatório: Valor Total das Taxas Cobradas
def total_taxas():
    lista_op = []
    
    for registro in registros:
        lista_op.append(float(registro.valor_real))
    total_taxas = (sum(lista_op))*registro.taxa_cobrada
    return total_taxas

# Opção 6 - Relatório: Valores por Cliente e Intervalo de Tempo
def totais_por_cliente(nome: str, data_inicial: str, data_final: str) -> Operacao:
    valores = []
    taxas = []

    for registro in registros:
        if (registro.nome == nome) and (registro.data_operacao >= data_inicial) and (registro.data_operacao <= data_final):
            valores.append(float(registro.valor_real))
            taxas.append(float(registro.taxa_operacao))
    total_valores = round(sum(valores), 2)
    total_taxas = round(sum(taxas), 2)
    return (total_valores, total_taxas)

# Opção 7 - Salvar Registros 
def salvar_operacoes():
    nome_arquivo = "registros.pkl"

    abrir_arquivo = open(nome_arquivo, "wb")
    for registro in registros:
        pickle.dump(registro, abrir_arquivo)
    abrir_arquivo.close()

    print('Salvo com sucesso!')
    sleep(3)
    menu()


# Opção 8 - Carregar Registros 
def abrir_registros():
    nome_arquivo = "registros.pkl"

    objetos = []
    with (open(nome_arquivo, "rb")) as openfile:
        while True:
            try:
                objetos.append(pickle.load(openfile))
            except EOFError:
                break

    for obj in range(len(objetos)):
        print('---------')
        print(objetos[obj])
        registros.append(objetos[obj])
    print('---------')
    sleep(1)
    menu()

# Opção 9 - Sair do Sistema 
def sair(): 
    exit('Volte sempre!')


if __name__ == '__main__':
    main()