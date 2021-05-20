from datetime import date
import calculadora

from helper import data_para_str, str_para_data


class Operacao:

    def __init__(self: object, nome: str, moeda_origem: str, moeda_destino: str, valor_original: float) -> None:
        self.__nome: str = nome 
        self.__moeda_origem: str = moeda_origem
        self.__moeda_destino: str = moeda_destino
        self.__data_operacao: date = date.today()
        self.__valor_original: float = valor_original
        self.__taxa_cobrada: float = self.taxa_cobrada
        self.__valor_convertido: float = self.valor_convertido   
        self.__taxa_operacao: float = self.taxa_operacao
        self.__valor_real: float = self.valor_real

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def moeda_origem(self: object) -> str:
        return self.__moeda_origem    

    @property
    def moeda_destino(self: object) -> str:
        return self.__moeda_destino  

    @property
    def data_operacao(self: object) -> str:
        return data_para_str(self.__data_operacao)

    @property
    def valor_original(self: object) -> float:
        return self.__valor_original

    @property
    def taxa_cobrada(self: object) -> float:
        taxa = 0.1
        return taxa

    @property 
    def valor_convertido(self: object) -> float:
        valor = float(self.__valor_original)
        moeda_origem = str(self.__moeda_origem)
        moeda_destino = str(self.__moeda_destino)
        return calculadora.converter_moedas(valor, moeda_origem, moeda_destino)

    @property
    def valor_real(self: object) -> float:
        valor = float(self.__valor_original)
        moeda_origem = str(self.__moeda_origem)
        return calculadora.converter_moedas(valor, moeda_origem, 'BRL')

    @property 
    def taxa_operacao(self: object) -> float:
        valor = self.valor_real
        return round(valor * self.__taxa_cobrada, 2)

    def __str__(self: object) -> str:
        return f'Nome do cliente: {self.nome} \nMoeda de Origem: {self.moeda_origem} \nMoeda de Destino: {self.moeda_destino} \nData da Operação: {self.data_operacao} \nValor original: {self.moeda_origem} {self.valor_original} \nValor convertido: {self.moeda_destino} {self.valor_convertido} \nTaxa cobrada pela operação: BRL {self.taxa_operacao}'


