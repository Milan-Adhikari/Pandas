import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('all_months_data.csv')
#data.dropna(axis = 0,inplace=True) # dropping null rows
pd.set_option('display.max_columns',None)
# print(data.head())

# removing NAN values and cleaning data
nan_data = data[data.isna().any(axis=1)]
# print(nan_data)
data.dropna(axis = 0,inplace = True)
# nana = data[data.isna().any(axis=1)] # checking to see if any NAN values are still left
# print(data)
data = data.loc[data['Quantity Ordered'] != 'Quantity Ordered'] # some rows contained column names as data, so removing those rows from the dataset
# that is, columns had strings in them, so i couldnt convert those columns to float, so i removed those strings

# find the month with largest amount of sales
data['Total'] = data['Quantity Ordered'].astype('float32')* data['Price Each'].astype('float32') # adding new total column
data['Month'] = data['Order Date'].str[0:2].astype('int32') # yesma chai, tyo order date column lai maile string ma convert gardiye, ani 1st 2 letters month ko
# extract garey, ani teslai int ma convert garera naya column ma haldiye
# print(data)
sales_by_month =data.groupby('Month').sum() # here i have grouped the data with respect to month and summed them
# print(sales_by_month)
months = range(1,13)
# plt.bar(months,sales_by_month['Total'])
# plt.show()


# which city had the highest number of sales?
# print(data['Purchase Address'])
split_purchase_adress = data['Purchase Address'].str.split(',', expand = True) # i separated comma separeated values inside columns into diff columns
data['City'] = split_purchase_adress[1]+''+(split_purchase_adress[2].str.split(' ',expand = True)[1]) # i created a new column with cities from splited
# purchase adress. pachi tya city ko code hatauna lai, space sanga nih split garera, city ko name code matra nih leko chu
# data = pd.concat([data,data2],axis =0)
# data['City'] = data2[1]
city = data.groupby('City').sum()
# print(city)
# cities = data['City'].unique() this code can find the city names too, but order gets mimatched when plotting so below line code was used
cities = [city for city,data in  data.groupby('City')]
# plt.bar(cities,city['Total'])
# plt.xticks(cities,rotation = 'vertical',size = 6)
# plt.show()


# what time should we display advertisements

data['Order Date'] = pd.to_datetime(data['Order Date']) # converting into date time
data['Hour'] = data['Order Date'].dt.hour # order data bata hour nikalera naya column ma rakheko
# print(data.head())
hours = [hour for hour,df in data.groupby('Hour')] # yesma for use garera data frame use garnu ko euta matra karan vaneko so that the sequence of
# hours remains the same as in groupby, natra data yeta uta huncha. so hours ra, groupby ma same sequence hos vbanera groupby use gareko
plt.plot(hours,data.groupby('Hour').count())
plt.grid()
plt.show()







