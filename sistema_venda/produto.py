class Produto:
    
    def __init__(self, descricao: str, valor: float, estoque: int=0):
        self.descricao = descricao
        self.valor = valor
        self.estoque = estoque
    
    def incrementar_estoque(self, quantidade: int):
        if quantidade > 0:
            self.estoque += quantidade
    
    def decrementar_estoque(self, quantidade: int) -> bool:
        if quantidade > 0 and quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            return False