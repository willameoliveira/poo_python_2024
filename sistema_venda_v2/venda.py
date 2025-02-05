from datetime import datetime
from item_venda import Item_Venda
from produto import Produto

class Venda:

    def __init__(self, forma_pagamento: str, data_venda:datetime = datetime.now()):
        self._valor_total = 0
        self._forma_pagamento = forma_pagamento
        self._data_venda = data_venda
        self._itens = []
    
    @property
    def itens(self) -> list[Item_Venda]:
        return self._itens
    
    def adicionar_item(self, produto: Produto, quantidade: int):
        self._itens.append(Item_Venda(produto, quantidade))

    def calcular_valor_total(self) -> float:
        self._valor_total = sum(item.valor for item in self._itens)
        return self._valor_total

    def calcular_troco(self, valorPago: float) -> float:
        if self._valor_total > 0 and valorPago > 0:
            return valorPago - self._valor_total
        return 0.0

    def __str__(self):
        itens = ""
        for item in self.itens:
            itens += f"{item.produto.descricao}\t{item.quantidade}\tR$ {item.valor}\n"

        string = f"Venda realizada em: {self._data_venda.strftime('%d/%m/%y %H:%M')}\n" 
        string += itens
        string += f"Valor total: R$ {self.calcular_valor_total()}\n"
        string += f"Forma de pagamento: {self._forma_pagamento}"
        return string
    


