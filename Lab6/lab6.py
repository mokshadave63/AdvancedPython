import pandas as pd

data_jan = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Store ID': ['Store001', 'Store001', 'Store002', 'Store002'],
    'Product ID': ['ProdA', 'ProdB', 'ProdA', 'ProdC'],
    'Quantity sold': [10, 5, 7, 8]
}
df_jan = pd.DataFrame(data_jan)
df_jan.to_csv('sales_data_2023-01.csv', index=False)

data_feb = {
    'Date': ['2023-02-01', '2023-02-01', '2023-02-02', '2023-02-02'],
    'Store ID': ['Store001', 'Store001', 'Store002', 'Store002'],
    'Product ID': ['ProdA', 'ProdB', 'ProdA', 'ProdC'],
    'Quantity sold': [12, 6, 9, 10]
}
df_feb = pd.DataFrame(data_feb)
df_feb.to_csv('sales_data_2023-02.csv', index=False)

product_names = {
    'Product ID': ['ProdA', 'ProdB', 'ProdC'],
    'Product Name': ['Widget A', 'Widget B', 'Widget C']
}
df_products = pd.DataFrame(product_names)
df_products.to_csv('product_names.csv', index=False) 
