import pandas as pd

df = pd.read_csv('cars_data.csv')
print(df.head())

df['total_price'] = df['passings'] * df['price_per_unit']

df['Price/2'] = df['price_per_unit']/2
df['passings*2'] = df['passings']*2

print(df)

# filter rows
filtered_passings = df[df['passings'] > 4]
filtered_total_price = df[df['price_per_unit'] > 40000]

print(filtered_passings)
print(filtered_total_price)

# save the updated csv
df.to_csv('updated_cars_data.csv', index=False)