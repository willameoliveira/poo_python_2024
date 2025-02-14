from funcionario import Funcionario
from gerente import Gerente

funcionario = Funcionario("João", "1235", 1000)
gerente = Gerente("Pedro", "5678", 2000, "gerente123", 1)

print(vars(funcionario))
print(vars(gerente))

print(f"Bonificação do funcionario: {funcionario.get_bonificacao()}")
print(f"Bonificação do gerente: {gerente.get_bonificacao()}")