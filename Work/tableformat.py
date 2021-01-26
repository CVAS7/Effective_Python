class TableFormatter: # Parent class
    def headings(self, headers): 
        """
        Emit the table headings.
        """
        raise NotImplementedError()
    def row(self, rowdata): # Parent method
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()

class TextTableFormatter(TableFormatter): # Child class
    def headings(self, headers):
        #for h in headers:
            #print(f'{h:>10s}', end= ' ')
        print("{:>10s} {:>10s} {:>10s} {:>10s}".format(*headers))
        print()
        print(('-'*10+' ')*len(headers))

    def row(self, rowdata): # 
        for d in rowdata:
            print(f'{d:>10s}',end = ' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self,rowdata):
        print(','.join(rowdata))

class XMLTableFormatter(TableFormatter):
    def headings(self,headers):
        print("<tr><th>{}</th><th>{}</th><th>{}</th><th>{}</th></tr>".format(*headers))

    def row(self,rowdata):
        print("<tr><th>{}</th><th>{}</th><th>{}</th><th>{}</th></tr>".format(*rowdata))
