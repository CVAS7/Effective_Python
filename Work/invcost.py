import csv
import sys 
from report import read_inventory

def inventory_cost(filename):
    #ive = read_inventory(filename)
    inventory = read_inventory(filename)
    return inventory.total_cost 

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} {inventory.csv}')
    
    try:
        filename = argv[1]
    except IndexError:
        print('Filename is not given in the arugment, filename taken as Default Data/inventory.csv')
    #filename = 'Data/inventory.csv'
    cost = inventory_cost(filename)
    print('Total cost:',cost)

if __name__ == "__main__":
    import sys
    main(sys.argv)
