from datetime import datetime
from produto import Produto

class Venda:

    def __init__(self, produto: Produto, quantidade_vendida: int, forma_pagamento: str, data_venda:datetime = datetime.now()):
        self.produto = produto
        self.valor_total = 0
        self.quantidade_vendida = quantidade_vendida
        self.forma_pagamento = forma_pagamento
        self.data_venda = data_venda
    
    def calcular_valor_total(self) -> float:
        self.valor_total = self.produto.valor * self.quantidade_vendida
        return self.valor_total

    def calcular_troco(self, valorPago: float) -> float:
        return valorPago - self.calcular_valor_total()

    def __str__(self):
        return (f"Venda realizada em: {self.data_venda} \nValor total: R${self.calcular_valor_total()}"
                f"\nProduto: {self.produto.descricao} \nQuantidade de itens: {self.quantidade_vendida}"
                f"\nForma de pagamento: {self.forma_pagamento}")
    


