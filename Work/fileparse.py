import csv
def parse_csv(lines, select=None, types=None, has_headers=True,delimiter=',', silent_erros=False):
    if isinstance (lines,str):
        raise RuntimeError('lines argument should be a file or a list')

    if select and not has_headers:
        raise RuntimeError("select header requires headers")

    #with open(filename) as f:
    rows = csv.reader(lines,delimiter = delimiter)
    if has_headers:
        headers = next(rows)
        
        if select:
            print(select)
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

    records = []
    for idx,row in enumerate(rows):
        if not row :
            continue

        if select:
            row = [row[index] for index in indices]

        if types:
            try:
                row = [func(value) for func, value in zip(types, row)]
            except ValueError as e:
                if silent_errors == False:
                    print(f"Row {idx}: Could`t covert {row}")
                    print(f"Row {idx}: Reason {e}")
                continue

        if has_headers:
            record = dict(zip(headers,row))
        else:
            record = tuple(row)
        records.append(record)

    return records
