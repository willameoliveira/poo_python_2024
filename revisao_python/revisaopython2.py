#Faça um programa que recebe 10 notas e, ao final, imprime a média de todas as notas.

soma = 0.0
for cont in range(10):
    soma += float(input(f"Digite a nota {cont+1}: "))

media = soma / 10

print(f"\nMédia do aluno: {media:.1f}")
