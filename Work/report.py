import csv
from pprint import pprint
from fileparse import parse_csv 

def read_inventory(filename):
    inventory = parse_csv(filename, select =['name', 'quant', 'price'], types = [str ,int, float])
    return inventory

def read_prices(filename):
    pricelist = parse_csv(filename, types =[str, float], has_headers=False)
    pricesdict = dict(pricelist)
    return pricesdict

def make_report(inventory,prices):
    report = []
    for i in inventory:
        row = (i['name'],i['quant'],prices[i['name']],(prices[i['name']]-i['price'])) 
        report.append(row)
        
    return report

def print_report(report):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    dashs = ["-"*10, ]*len(headers)
    print('{:>10} {:>10} {:>10} {:>10}'.format(*headers))
    print('{:>10} {:>10} {:>10} {:>10}'.format(*dashs))
    
    for row in report:
            print('{:>10s} {:>10d} {:>10.2f} {:>10.2f}'.format(*row))

def inventory_report(inventory_filename,price_filename):
    inventory = read_inventory(inventory_filename)
    latest = read_prices(price_filename)
    report = make_report(inventory,latest)
    print_report(report)

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'invfile pricefile')
    invfile = argv[1]
    pricefile = argv[2]
    inventory_report(invfile,pricefile)

if __name__ == "__main__":
    import sys
    main(sys.argv)
