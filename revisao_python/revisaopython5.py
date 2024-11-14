from revisaopython4 import calcular_fatorial
num = 0
while num >= 0:
    num = int(input("Digite um número: "))
    if num >= 0:
        print(f"Fatorial de {num} é {calcular_fatorial(num)}\n")
