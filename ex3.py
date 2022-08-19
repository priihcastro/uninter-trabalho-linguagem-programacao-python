# III Realizar o upload do arquivo STORES.csv.  Renomear todas as colunas do arquivo STORES.csv, onde os respctivos
# nomes sejam compactados (Exemplo: Daily_Customer_Count foi renomeado para Visitantes). Após isto, para se analisar o
# desempenho das lojas de supermercado/mercado do arquivo STORES.csv encontre os valores mínimo, máximo, médio e desvio
# padrão das seguinte colunas: "Items_Available"; "Daily_Customer_Count"; e "Store_Sales". Para resultar nos valaros de
# minímo, máximo, média e desvio padrão deverá utilizar o comando groupby.
# Algumas informações extras sobre a tabela do arquivo STORES.csv:
# 	Store ID: (Índice) ID da loja específica.
# 	Store_Area: Área Física da loja em pátio.
# 	Itemns_Avaliable: Número de itens diferentes disponíveis na loja correspondente.
# 	DailyCustomerCount: Número de clientes que visitaram as lojas em média ao longo do mês.
# 	Store_Sales: Vendas em (US$) que as lojas realizaram.

# Importando a biblioteca "Pandas".
import pandas as pd

# Abrindo arquivo csv que será utilizado.
df = pd.read_csv('C:/Users/prisc/Área de Trabalho/Pri/UNINTER/Engenharia de Software/3º Semestre/Modulo B - Fase I/'
                 'Linguagem de Programação/Trabalho de Ling. de Programação/Stores.csv',
                 sep=',')
print('\n-----  Tabela Original  -----\n', df)

# Renomeando colunas da tabela.
df = df.rename(columns={'Daily_Customer_Count': 'Visitantes', 'Store ID ': 'ID', 'Items_Available': 'Estoque',
                        'Store_Sales': 'Faturamento', 'Store_Area': 'Loja'})
print('\n-----  Tabela com Colunas Renomeadas  -----\n', df)

# Filtrando tabela e armazenando somente os valores das colunas 'Estoque', 'Visitantes' e 'Faturamento'.
dfColunas = ['Estoque', 'Visitantes', 'Faturamento']
dfFiltrado = df.filter(items=dfColunas)

# Criando dicionario para armazenar os valores min, max, media e desvio padrão da tabela filtrada.
estatisticas = ({'Estoque': [(dfFiltrado['Estoque'].min()), (dfFiltrado['Estoque'].max()),
                             (dfFiltrado['Estoque'].mean()), (dfFiltrado['Estoque'].std())],
                 'Visitantes': [(dfFiltrado['Visitantes'].min()), (dfFiltrado['Visitantes'].max()),
                                (dfFiltrado['Visitantes'].mean()), (dfFiltrado['Visitantes'].std())],
                 'Faturamento': [(dfFiltrado['Faturamento'].min()), (dfFiltrado['Faturamento'].max()),
                                 (dfFiltrado['Faturamento'].mean()), (dfFiltrado['Faturamento'].std())]})

estatisticas = pd.DataFrame(estatisticas)  # transformando o dicionário em uma tabela.

# renomeando o "nome" de cada linha da tabela.
estatisticas = estatisticas.rename(index={0: 'min', 1: 'max', 2: 'media', 3: 'desvio pd'})

print('\n-----  Tabela Filtrada e Estatísticas  -----')
print(estatisticas.groupby('Estoque').head())  # Exibindo a tabela com o groupby.
