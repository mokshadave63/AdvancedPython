import pandas as pd

path = 'data.csv'
df = pd.read_csv(path)

#for missing values
print(df.isnull().sum())

#rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

#duplicates
print(df.duplicated().sum())

#Remove duplicates
df = df.drop_duplicates()

#correct data types
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Quantity'] = df['Quantity'].astype(int)
df['UnitPrice'] = df['UnitPrice'].astype(float)

# Group by CustomerID and aggregate data
customer_data = df.groupby('CustomerID').agg(
    TotalAmountSpent=pd.NamedAgg(column='Quantity', aggfunc=lambda x: (x * df.loc[x.index, 'UnitPrice']).sum()),
    TotalItemsPurchased=pd.NamedAgg(column='Quantity', aggfunc='sum'),
    LastPurchaseDate=pd.NamedAgg(column='InvoiceDate', aggfunc='max')
)

customer_data['AveragePurchaseValue'] = customer_data['TotalAmountSpent'] / customer_data['TotalItemsPurchased']

