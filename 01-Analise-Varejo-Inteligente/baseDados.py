import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

#Criar uma função com as informações de produtos
def bancoDados(numRegistros = 600):
    print(f"Iniciando a geração de {numRegistros} registros de vendas ...")
    #Cria-se um Dict com produtos, categorias e preços
    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Ácessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria':'Ácessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200},
        'Headset 7.1': {'categoria': 'Ácessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
}
    #Cria-se uma lista, capturando os nomes dos produtos
    listaProdutos = list(produtos.keys()) #Busca as chaves do dict

    #Criar um dict com os nomes das cidades e seus estados
    cidadeEstado = {
    'São Paulo': 'SP', 
    'Rio de Janeiro': 'RJ', 
    'Belo Horizonte': 'MG', 
    'Porto Alegre': 'RS',
    'Salvador': 'BA',
    'Curitiba': 'PR',
    'Fortaleza': 'CE'
}
    #Cria-se uma lista, capturando os nomes das cidades / estados   
    listaCidadesEstados = list(cidadeEstado.keys())
    #Lista que armazenará os registros de vendas
    dadosVendas = []
    #Define a data inicial dos pedidos
    dataInicial = datetime(2026,1,1)
    #Loop para gerar os produtos
    for registro in range(numRegistros):
        #Seleciona aleatoriamente um produto
        produto = random.choice(listaProdutos)
        #Seleciona aleatoriamente uma cidade
        cidade = random.choice(listaCidadesEstados)
        #Gera uma quantidade de produtos vendidos entre 1 e 7
        quantVendida = np.random.randint(1,8)
        #Calcula a data do pedido a partir da data inicial => dataInicial 
        dataPedido = dataInicial + timedelta(days= int(registro/5), hours= random.randint(0,23))
        #Se o produto for mouse ou teclado, deve aplicar um desconto de até 1%
        if produto in ['Mouse Vertical', 'Teclado Mecânico']:
            precoUn = produtos[produto] ['preco'] * np.random.uniform(0.9, 1.0)
        else:
            precoUn = produtos[produto] ['preco']
        #Adiciona um registro de venda à lista
        dadosVendas.append({
            'ID pedido': 1000 + registro, 
            'Data Pedido': dataPedido,
            'Nome Produto': produto,
            'Categoria': produtos[produto]['categoria'],
            'Preço Un.': round(precoUn, 2),
            'Quantidade': quantVendida,
            'ID Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidadeEstado[cidade]
            })
    #Retorna os dados no formado de Dataframe
    return pd.DataFrame(dadosVendas)

dt = bancoDados(1000) 

dt['Data Pedido'] = pd.to_datetime(dt['Data Pedido'])
#Engenharia de atributos - Faturamento
dt['Faturamento'] = dt['Preço Un.']  * dt['Quantidade']
#Engenharia de atributos - Status da entrega
dt['Status Entrega'] = dt['Estado'].apply(lambda estado: 'Rápida' if estado in ['SP', 'RJ', 'MG'] else 'Normal')
#Criar uma coluna de Mês
dt['Mês'] = dt['Data Pedido'].dt.to_period('M')
#Agrupa o mês e soma o faturamento
faturamentoMensal = dt.groupby('Mês')['Faturamento'].sum()

dt.to_csv('BD_Vendas.csv', index=False, encoding='utf-8-sig')

