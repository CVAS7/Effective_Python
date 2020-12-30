"""
import pandas as pd
import numpy

df = pd.read_csv('Data/inventory.csv',skiprows=0,delimiter=",")
#name,quant,price
Product = df['quant']*df['price']
Total = sum(Product)
print('Total',Total)

"""
import csv
product = []
with open('Data/inventory.csv','rt') as FH:
    csvreader = csv.reader(FH)
    fields = next(csvreader)
    for row in csvreader:
        product.append(int(row[1])*float(row[2]))

print("Total",sum(product))
