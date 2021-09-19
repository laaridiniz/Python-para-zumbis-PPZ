'''1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
as funções max e min.'''

#Importando a biblioteca para gerar números aleatórios
from random import sample

#Criando a lista com os números sorteados
v = sample(range(100), 10)

#Variáveis para armazenar os números solicitados
maior = menor = v[0]
k = 1

#Descobrindo qual o maior e o menor número
while k < 10:
    if v[k] > maior: maior = v[k]
    if v[k] < menor: menor = v[k]
    k = k + 1

#Imprimindo os resultados
print(f'A lista criada é {v}.')
print(f'O menor número é {menor}.')
print(f'O maior número é {maior}.')