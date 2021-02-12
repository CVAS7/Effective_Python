""" 
Define a prodcut class
"""
from typedproperty import typedproperty

class Product:
    name = typedproperty('name', str)
    quant = typedproperty('quant',int)
    price = typedproperty('price', float)

    #__slots__ = ('name', '_quant', 'price')

    def __init__ (self, name, quant, price):
        self.name = name
        self.quant = quant
        self.price = price

    """    
    @property
    def quant(self):
        return self._quant

    @quant.setter
    def quant(self,value):
        if not isinstance(value, int):
            raise('Expected as int')
        self._quant = value
    """

    @property
    def cost(self):
        """
        Returns the cost product
        """
        return self.quant*self.price
    
    def sell(self, sold):
        """
        Sell few units of the prdduct
        """
        self.quant = self.quant - sold

    def __repr__(self):
        return f'Product({self.name},{self.quant!r},{self.price})'

