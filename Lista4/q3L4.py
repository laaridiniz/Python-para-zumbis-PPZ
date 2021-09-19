'''3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três vetores.'''

#Importando a biblioteca para gerar números aleatórios
from random import randint, sample

#Criando as listas para armazenar os números sorteados
v1 = []
v2 = []
v3 = []

#Sorteando números aleatórios entre 1 e 100 e incluindo-os na lista composta
for k in range(10):
    x = randint(1, 100)
    v1.append(x)
    v3.append(x)
    x = randint(1, 100)
    v2.append(x)
    v3.append(x)

#Imprimindo as listas com os números sorteados
print(f'A primeira lista é {v1}.')
print(f'A segunda lista é {v2}.')
print(f'A lista composta é {v3}.')