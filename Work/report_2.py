import csv
from pprint import pprint
def read_inventory(filename):
    with open(filename,'rt') as FH:
        rows = csv.reader(FH)
        header = next(rows)
        inventory = []
        for r in rows:
            product = dict(zip(header, r))
#            print(product)
            product['quant'] = int(product['quant']) # updating the data type
            product['price'] = float(product['price']) # updating the date type
            inventory.append(product)
#    print(inventory)
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
#    print('dprices')
    return dprices


def make_report(inventory,prices):
    report = []
    for i in inventory:
        row = (i['name'],i['quant'],latest[i['name']],(latest[i['name']]-i['price'])) # This should be price or latest also works
        report.append(row)
#    print('report',report)
    return report
def print_report(report):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    dashs = ["-"*10, ]*len(headers)
    print('{:>10} {:>10} {:>10} {:>10}'.format(*headers))
    print('{:>10} {:>10} {:>10} {:>10}'.format(*dashs))
    for row in report:
            print('{:>10s} {:>10d} {:>10.2f} {:>10.2f}'.format(*row)) # what happens if length of name is more than 10 char
#read_prices('Data/prices.csv')
filename = 'Data/inventory.csv'
inventory = read_inventory(filename)
"""
total = 0.0
for i in inventory:
    total += i['quant'] * i['price']
#print('Total Cost',total)
"""
filename = 'Data/prices.csv'
latest = read_prices(filename)
"""
new_total = 0.0
for j in inventory:
    new_total += j['quant'] * latest[j['name']]

print('Total Gain',new_total-total)
"""
report = make_report(inventory,latest)
print_report(report)
