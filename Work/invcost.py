import csv
import sys 
def inventory_cost(filename):
    Total = 0
    
    with open(filename,'rt') as FH:
        rows = csv.reader(FH)
        headers = next(rows)
        for idx,row in enumerate(rows,start=1):
            record = dict(zip(headers, row))
            try:
                quant = int(record['quant'])
                price = float(record['price'])
                Total += quant*price
            except ValueError:
                print(f"Row {idx} :Bad Row {row}")
    return Total            
try:
    filename = sys.argv[1]
except IndexError:
    print('Filename is not given in the arugment, filename taken as Default Data/inventory.csv')
    filename = 'Data/inventory.csv'
cost = inventory_cost(filename)
print('Total cost:',cost)
