import pandas as pd
import os # importing this so that i can list all the directories

# merging 12 months of data into a single file
# data1 = pd.read_csv('C:\\Users\\adwin\\PycharmProjects\\panda\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data\\Sales_April_2019.csv')
# print(data1.head())

files = [file for file in os.listdir('C:\\Users\\adwin\\PycharmProjects\\panda\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data')]
# print(files)
# this above line is used to access all the directories, that is all 12 months of data files
# i created a new list of files which contains all the 12 month files and now i need to concatenate all of these files in a single csv file

all_months = pd.DataFrame()
# here i am creating a empty dataframe so that i can append each month file here after reading that

# i will use for loop in files to access each months data
for file in files:
    data = pd.read_csv('C:\\Users\\adwin\\PycharmProjects\\panda\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data\\'+file)
    # this data reads one months data at a time
    all_months = pd.concat([all_months,data]) # this line appends new month data everytime to the allmonths

all_months.to_csv('all_months_data',index = False) # what this does is saves all_months as a new csv