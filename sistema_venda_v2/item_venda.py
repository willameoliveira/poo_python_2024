from produto import Produto

class Item_Venda:
    
    def __init__(self, produto:Produto, quantidade: int, valor:float=0):
        self._produto = produto
        self._quantidade = quantidade
        self._valor = valor
    
    @property
    def produto(self):
        return self._produto
    
    @property
    def quantidade(self):
        return self._quantidade

    @property
    def valor(self):
        if self._valor == 0:
            self._valor = self._produto.valor * self._quantidade
        return self._valor