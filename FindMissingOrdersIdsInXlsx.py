# source enviroment/bin/activate

import pandas as pd 

origin_file_path = './data/(Plataforma)list-orders-2022-01-06_14-52.xlsx'
metabase_file_path = './data/(Metabase)relatorio_de_pedido___dev_2022-01-06T14_53_15.945937Z.xlsx' 

df_origin = pd.read_excel(origin_file_path)
df_metabase = pd.read_excel(metabase_file_path)
origin_order_ids = df_origin['NumeroPedido']
metabase_order_ids = df_metabase['NumeroPedido']

totalOrders = 0
missingOrders = 0

for origin_value in origin_order_ids.values:
    if origin_value not in metabase_order_ids.values:
        print('Valor de pedido não encontrado: ', origin_value)
        missingOrders += 1
    totalOrders += 1

print('Total de pedidos: ', totalOrders)
if(missingOrders > 0):
    print('Total de pedidos faltando: ', missingOrders)
else:
    print('Todos os pedidos foram encontrados!')
