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
def inventory_cost(filename):
    product = []
    
    with open(filename,'rt') as FH:
        csvreader = csv.reader(FH)
        fields = next(csvreader)
        for row in csvreader:
            product.append(int(row[1])*float(row[2]))
    return sum(product)            

cost = inventory_cost('Data/inventory.csv')
print('Total cost:',cost)
