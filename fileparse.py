import csv
def parse_csv(filename, select=None, types=None, has_headers=True,delimiter=','):
    with open(filename) as f:
        rows =csv.reader(f,delimiter = delimiter)
        if has_headers:
            headers = next(rows)

            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

        records = []
        for row in rows:
            if not row :
                continue

            if select:
                row = [row[index] for index in indices]

            if types:
                row = [func(value) for func, value in zip(types, row)]

            if has_headers:
                record = dict(zip(headers,row))
            else:
                record = tuple(row)
            records.append(record)

    return records