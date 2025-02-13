from funcionario import Funcionario
from gerente import Gerente

funcionario = Funcionario("João", "1235", 1518)
gerente = Gerente("Pedro", "5678", 3000, "gerente123", 1)

print(vars(funcionario))
print(vars(gerente))