# Importação de Bibliotecas
from forex_python.converter import CurrencyRates


# Parâmetro
c = CurrencyRates()


# Funções 
def converter_moedas(valor, moeda_origem, moeda_destino):
    """
    -> Converte um valor monetario pela taxa de cambio entre duas moedas fornecidas pelo usuário e retorna a conversao.

    Args:
        valor ([float]): [Valor monetario que se deseja converter]
        moeda_origem ([str]): [Moeda de origem, escrita conforme norma ISO 4217]
        moeda_destino ([str]): [Moeda de destino, escrita conforme norma ISO 4217]
    """
    taxa_cambio = c.get_rate(moeda_origem, moeda_destino)
    conversao = round(valor * taxa_cambio, 2)
    return conversao

def converter_lista(valor, lista_origem, lista_destino):
    """
    -> Converte um valor monetario pela taxa de cambio entre duas moedas fornecidas pelo usuário e retorna a conversao na tela.

    Args:
        valor ([float]): [Valor monetario que se deseja converter]
        lista_origem ([list]): [Lista de moedas de origem, escritas conforme norma ISO 4217]
        lista_destino ([list]): [Lista de moedas de destino, escritas conforme norma ISO 4217]
    """
    for o in lista_origem:
        for d in lista_destino:
            taxas_cambio = c.get_rate(o, d)
            valores_convertidos = {round(taxas_cambio * float(valor), 2)} 
            return valores_convertidos

converter_moedas(2700.13, 'BRL', 'USD')