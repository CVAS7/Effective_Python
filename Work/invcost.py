import csv
import sys 
from report import read_inventory

def inventory_cost(filename):
    ive = read_inventory(filename)
    Total = 0.0
    for prod in ive:
        Total += prod['quant']*prod['price']
    return Total            

try:
    filename = sys.argv[1]
except IndexError:
    print('Filename is not given in the arugment, filename taken as Default Data/inventory.csv')
    filename = 'Data/inventory.csv'
cost = inventory_cost(filename)
print('Total cost:',cost)
