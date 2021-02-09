from product import Product
from fileparse import parse_csv

class Inventory:
    def __init__(self):
        self._products = []
    
    def __iter__(self):
        return self._products.__iter__()

    def __len__ (self):
        return len(self._products)

    def __getitem__(self,index):
        return self._products[index]

    def __contains__(self, name):
        return any(p.name == name for p in self._products)

    def append(self, product):
        if not isinstance(product, Product):
            raise TypeError('Expected Product instance')
        self._products.append(product)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        inventory = parse_csv(lines, select =['name', 'quant', 'price'], types = [str ,int, float],**opts)
        for p in inventory:
            self.append(Product(**p))

        return self

    @property
    def total_cost(self):
        return sum(p.cost for p in self._products)


    def tabulate_quants(self):
        from collections import Counter
        total_units = Counter()
        for p in self._products:
            total_units[p.name] += p.quant
        return total_units
