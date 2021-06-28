import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('edited_data.csv')
pd.set_option('display.max_columns',None)
# print(data.head())

duplicates = data[data['Order ID'].duplicated(keep = False)] # finding duplicate values in ordered price column
# print(duplicates.head())
duplicates['Grouped'] = duplicates.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
duplicates = duplicates[['Order ID','Grouped']].drop_duplicates()
# print(duplicates.head())

# print(duplicates['Grouped'].unique())
count = duplicates.pivot_table(index=['Grouped'], aggfunc='size')
print(count.sort_values())