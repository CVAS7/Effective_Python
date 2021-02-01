""" 
Define a prodcut class
"""
class Product:
    """ 
    Class to repreent a product consisting of name, quant, price
    """
    def __init__ (self, name, quant, price):
        """
        Returns the cost product
        """
        self.name = name
        self.quant = quant
        self.price = price

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
        return f'Product({self.name!r},{self.quant!r},{self.price!r})'

