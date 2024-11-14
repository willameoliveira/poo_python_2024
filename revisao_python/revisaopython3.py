#Faça um programa que guarda 10 nomes em uma lista e, ao final, sorteia um dos nomes.
import random
nomes = []
for cont in range(10):
    nomes.append(input(f"Digite o nome {cont + 1}: "))

#melhorando o programa adicionando sorteios em loop
resposta = "s"
while resposta == "s":
    print(f"\nO nome sorteado é: {random.choice(nomes)}")
    resposta = input("Sortear outro? (s|n)").lower()