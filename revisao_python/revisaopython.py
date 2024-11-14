#Crie um programa que recebe três notas de um aluno e imprime a média com uma casa decimal.
#Depois do programa deve imprimir o resultado do aluno.
#Se a média for maior ou igual a 7, aluno aprovado. Senão, se a média for menor do que 7 e
#maior ou igual a 4, aluno de prova final. E se a média for menor do que 4, aluno reprovado.

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media = (nota1 + nota2 + nota3) / 3

print(f"Média do aluno: {media:.1f}")

if media >= 7:
    print("Resultado: Aluno aprovado.")
elif media >= 4:
    print("Resultado: Aluno de prova final.")
else:
    print("Resultado: Aluno reprovado.")