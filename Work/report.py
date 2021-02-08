import csv
from pprint import pprint
from fileparse import parse_csv 
from product import Product
from inventory import Inventory
import tableformat

def read_inventory(filename):
    with open(filename) as FH:
        inventory = parse_csv(FH, select =['name', 'quant', 'price'], types = [str ,int, float])
        #prodinv =[Product(p['name'],p['quant'], p['price']) for p in inventory]
        prodinv =[Product(**p) for p in inventory]
    return Inventory(prodinv)

def read_prices(filename):
    with open(filename) as FH:
        pricelist = parse_csv(FH, types =[str, float], has_headers=False)
    pricesdict = dict(pricelist)
    return pricesdict

def make_report(inventory,prices):
    report = []
    for i in inventory:
        row = (i.name,i.quant,prices[i.name],(prices[i.name]-i.price)) 
        report.append(row)
        
    return report

def print_report(report, formatter):
    #headers = ('Name', 'Quantity', 'Price', 'Change')
    #dashs = ["-"*10, ]*len(headers)
    #print('{:>10} {:>10} {:>10} {:>10}'.format(*headers))
    #print('{:>10} {:>10} {:>10} {:>10}'.format(*dashs))
    formatter.headings(['Name','Quant','Price','Change'])
    for name, quant, price, change in report:
        rowdata = [name, str(quant),f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)
    
    #for row in report:
            #print('{:>10s} {:>10d} {:>10.2f} {:>10.2f}'.format(*row))

def inventory_report(inventory_filename,price_filename,fmt = 'txt'):
    inventory = read_inventory(inventory_filename)
    latest = read_prices(price_filename)
    report = make_report(inventory,latest)
    #if fmt == 'txt':
        #formatter = tableformat.TextTableFormatter()
        #print_report(report,formatter)

    #if fmt == 'csv':
        #formatter = tableformat.CSVTableFormatter()
        #print_report(report,formatter)

    #if fmt == 'html':
        #formatter = tableformat.HTMLTableFormatter()
        #print_report(report,formatter)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) != 4:
        raise SystemExit(f'Usage: {argv[0]} ' 'invfile pricefile format')
    invfile = argv[1]
    pricefile = argv[2]
    fmt = argv[3]
    inventory_report(invfile,pricefile,fmt)

if __name__ == "__main__":
    import sys
    main(sys.argv)
