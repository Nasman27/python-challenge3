import csv
import os
fin_data="Resources\\budget_data.csv"

# with open(fin_data) as csvfile:
#     csvreader = csv.reader(csvfile)
#     header = next(csvreader)
#     first_row = next(csvreader)
#     total_month=1

#     for i in csvreader:
#         total_month+=1
# print('The total number of months is,', total_month)

# with open(fin_data) as csvfile:
#     csvreader = csv.reader(csvfile)
#     header = next(csvreader)
#     first_row = next(csvreader)
#     NPL=0
#     for row in csvreader:
#         amount=int(row[1])
#         NPL += amount
# print("The net profit/loss is, ", NPL)

with open(fin_data) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    first_row = next(csvreader)
    profit_loss=[]
    changes=[]

    for line in csvreader:
        amount =(line[1])
        if len(amount)==2:
            profit_loss.append(int(amount))

        
        # amount = int(line[1])
        # if len(line[1])==2:
        #     profit_loss.append(line[1])

# import pandas as pd
# df=pd.read_csv('Resources\\budget_data.csv')
# print(df)
# df["Average Change"]=df['Profit/Losses'].pct_change()
# print(df)

