import csv
from pprint import pprint
def read_inventory(filename):
    with open(filename,'rt') as FH:
        rows = csv.reader(FH)
        header = next(rows)
        inventory = []
        for r in rows:
            product = dict(zip(header, r))
            product['quant'] = int(product['quant']) # updating the data type
            product['price'] = float(product['price']) # updating the date type
            inventory.append(product)
    return inventory

def read_prices(filename):
    with open(filename,'rt') as FH:
        rows = csv.reader(FH)
        prices = {}
        for line in rows:
            try:
                prices[line[0]] = float(line[1])
            except IndexError:
                continue
    return prices
def make_report(inventory,prices):
    report = []
    for i in inventory:
        row = (i['name'],i['quant'],prices[i['name']],(prices[i['name']]-i['price'])) # This should be price or latest also works
        report.append(row)
    return report
def print_report(report):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    dashs = ["-"*10, ]*len(headers)
    print('{:>10} {:>10} {:>10} {:>10}'.format(*headers))
    print('{:>10} {:>10} {:>10} {:>10}'.format(*dashs))
    for row in report:
            print('{:>10s} {:>10d} {:>10.2f} {:>10.2f}'.format(*row)) # what happens if length of name is more than 10 char
#read_prices('Data/prices.csv')
def inventory_report(inventory_filename,price_filename):
    inventory = read_inventory(inventory_filename)
    latest = read_prices(price_filename)
    report = make_report(inventory,latest)
    print_report(report)

inventory_report('Data/inventory.csv','Data/prices.csv')
