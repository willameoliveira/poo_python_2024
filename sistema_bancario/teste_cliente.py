from cliente import Cliente
from datetime import date

data_nasc = date.fromisoformat("2000-12-06")
cliente1 = Cliente("José", "098.678.543-35", "Rua X", "86988996655", data_nasc)
print(f"Idade: {cliente1.calcular_idade()} anos")
