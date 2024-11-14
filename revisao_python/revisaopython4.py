#Faça função que calcula o fatorial de um numero x
def calcular_fatorial(x):
    if x < 0:
        print("Informe um número positivo.")
        return 0
    else:
        resultado = 1
        for num in range(1, x+1):
            resultado *= num
        return resultado