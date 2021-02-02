class Inventory:
    def __init__(self, products):
        self._products = products
    
    def __iter__(self):
        return self._products.__iter__()

    def __len__ (self):
        return len(self._products)

    def __getitem__(self,index):
        return self._products[index]

    def __contains__(self, name):
        return any([p.name == name for p in self._products])

    @property
    def total_cost(self):
        return sum([p.cost for p in self._products])


    def tabulate_quants(self):
        from collections import Counter
        total_units = Counter()
        for p in self._products:
            total_units[p.name] += p.quant
        return total_units
