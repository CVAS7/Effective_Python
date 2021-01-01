import csv
from pprint import pprint
def read_inventory(filename):
    with open(filename,'rt') as FH:
        rows = csv.reader(FH)
        header = next(rows)
        inventory = []
        for r in rows:
            product = {'name':str(r[0]),
                           'quant':int(r[1]),
                           'value':float(r[2])}
            inventory.append(product)
    return inventory
#    print(inventory)
#read_inventory('Data/inventory.csv')

def read_prices(filename):
    with open(filename,'rt') as FH:
        rows = csv.reader(FH)
        dprices = {}
        for line in rows:
            try:
                dprices[line[0]] = float(line[1])
            except IndexError:
                continue

#    print(dprices)
    return dprices




#read_prices('Data/prices.csv')
filename = 'Data/inventory.csv'
inventory = read_inventory(filename)
total = 0.0
for i in inventory:
    total += i['quant'] * i['value']
print('Total Cost',total)

filename = 'Data/prices.csv'
latest = read_prices(filename)
new_total = 0.0
for j in inventory:
    new_total += j['quant'] * latest[j['name']]

print('Total Gain',new_total-total)

