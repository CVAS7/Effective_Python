from follow import follow
import csv
import report
import tableformat 

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func,val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_names(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def parse_product_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0,1,4])
    rows = convert_types(rows, [str,float,float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def ticker(filename, logfile, fmt):
    inventory = report.read_inventory(filename)
    rows = parse_product_data(follow(logfile))
#    rows = filter_names(rows, inventory)
    rows = (row for row in rows if row['name'] in inventory)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name','Price','Change'])
    for row in rows:
        name = row['name']
        price = row['price']
        change = row['change']
        rowdata = [name, f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

if __name__ == '__main__':

    lines = follow('Data/marketlog.csv')
    rows = parse_product_data(lines)
    for row in rows:
        print(row)
