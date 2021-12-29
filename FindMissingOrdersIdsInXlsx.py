import pandas as pd 

origin_file_path = './data/(Original)15-28Dezembro.xlsx'
metabase_file_path = './data/(Metabase)15-28Dezembro.xlsx' 

df_origin = pd.read_excel(origin_file_path)
df_metabase = pd.read_excel(metabase_file_path)
origin_order_ids = df_origin['NumeroPedido']
metabase_order_ids = df_metabase['NumeroPedido']

for origin_value in origin_order_ids.values:
    if origin_value not in metabase_order_ids.values:
        print('Valor de pedido não encontrado: ', origin_value)
