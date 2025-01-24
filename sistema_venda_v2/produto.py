class Produto:
    
    def __init__(self, descricao: str, valor: float, estoque: int=0):
        self._descricao = descricao
        self._valor = valor
        self._estoque = estoque
    
    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        if descricao:
            self._descricao = descricao

    @property
    def valor(self):
        return self._valor    
    
    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self._valor = valor

    @property
    def estoque(self):
        return self._estoque

    def incrementar_estoque(self, quantidade: int):
        if quantidade > 0:
            self._estoque += quantidade
    
    def decrementar_estoque(self, quantidade: int) -> bool:
        if quantidade > 0 and quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        else:
            return False