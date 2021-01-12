import csv
def parse_csv(filename):
    with open(filename) as f:
        rows =csv.reader(f)
        headers = next(rows)
        records = []
        for row in rows:
            if not row :
                continue
            record = dict(zip(headers,rows))
            records.append(record)

    return records
