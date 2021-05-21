<h1 align = 'center'> 
    <img src = 'https://i.ibb.co/W58n6fw/thumbnail-moeda.png'> 
    <br>MUITO DINHEIRO
    <br>Casa de Câmbio</br>
</h1>


## 📃 Indice
___

- [Sobre](#-sobre)
- [Instruções de Instalação](#-instruções-de-instalação)
- [Como usar](#-como-usar)

##  💰 Sobre
___

<br>Programa desenvolvido em Python para realizar conversões entre moedas e registrar as operações em um banco de dados. </br>  
  
<br>O cadastro inclui o nome do cliente, moeda de origem, moeda de destino e valor original. O programa cadastra automaticamente a operação com a data atual e contém em seu código-fonte uma taxa de 10% que é cobrada sobre as conversões. O sistema possibilita a execução de relatórios com o valor total das operações e valor total das taxas cobradas. Também é possível filtrar as operações pelo nome do cliente e intervalo de tempo.</br>

<br>O banco de dados pode ser salvo em um arquivo pickle e carregado posteriormente.</br>

## 💻 Instruções de Instalação
___

<br>Recomendo  bifurcar o repositório e cloná-lo localmente usando a função **git clone** no terminal. Instruções sobre como fazer isso podem ser acessadas [aqui](
https://docs.github.com/pt/github/getting-started-with-github/fork-a-repo).
</br>

``` bash
# Clonar repositório
git clone https://github.com/jluss0ll1/casa-de-cambio
```
Outra alternativa é clicar no botão verde "clone or download" neste repositório e então clicar em "Download ZIP". Em seguida, extrair o arquivo ZIP no local que você desejar editar ou executar o código.

Para as conversões de câmbio é utilizado o módulo [forex-python](https://pypi.org/project/forex-python/). Instale-o diretamente usando o comando:

```bash
pip install forex-python
```

## 📝 Como usar
___

Para executar o programa acesse a pasta com o projeto salvo e use o comando: 

```bash
python sistema.py
```

Ao executar o programa, é aberto automaticamente um menu com as opções disponíveis. O usuário do sistema deve digitar o número da opção desejada e pressionar a tecla Enter para executá-la.

**1 - Cadastrar Operação**

Solicita ao usuário o nome do cliente, a moeda de origem e a moeda de destino em três letras conforme ISO 4217 (ex.: BRL, USD, EUR), e o valor a ser convertido (valor original). Retorna o registro da operação com o nome do cliente, data da operação, moeda de origem, moeda de destino, valor original, valor convertido e taxa cobrada pela operação em Reais [BRL], e salva no banco de dados provisoriamente, podendo ser salvo permanentemente através da função 7 - Salvar Registros.

**2 - Listar Operações**

Retorna todas as operações registradas no sistema.

**3 - Buscar Operação por Nome e Intervalo de Tempo**

Solicita ao usuário do sistema o nome cadastrado do cliente, a data inicial e a data final do intervalo de tempo no formato DD/MM/AAAA. Retorna todas as operações para o cliente informado naquele intervalo de tempo.

**4 - Relatório: Valor Total das Operações**

Retorna a soma de todos os valores registrados no sistema, convertido para Reais [BRL].

**5 - Relatório: Valor Total das Taxas Cobradas**

Retorna a soma das taxas cobradas de todos os clientes registrados no sistema, convertido para Reais [BRL].

**6 - Relatório: Valores Totais por Cliente e Intervalo de Tempo**

Solicita ao usuário do sistema o nome cadastrado do cliente, a data inicial e a data final do intervalo de tempo. Retorna a soma dos valores e taxas cobradas para o cliente no intervalo de tempo informado, em Reais [BRL].

**7 - Salvar Registros**

Salva os cadastros realizados no sistema em um arquivo pickle.

**8 - Carregar Registros**

Carrega um arquivo pickle com as operações previamente salvas.

**9 - Sair do Sistema.** 

Finaliza o programa, apagando todos os registros que não foram salvos.

## 🔖 Licenças
---

**Logo**

Creative Commons Attribution 3.0 Unported (CC BY 3.0) License


