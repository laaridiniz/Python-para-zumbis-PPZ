'''2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas.'''

#Importando a biblioteca para gerar números aleatórios
from random import sample

#Criando a lista aleatória
v = sample(range(100), 20)

#Armazenando os números em listas específicas
par = []
ímpar = []
for x in v:
    if x % 2 == 0:
        par.append(x)
    else:
        ímpar.append(x)

#Imprimindo as listas
print(f'A lista criada é {v}.')
print(f'Os números pares sorteados são {par}.')
print(f'Os números ímpares sorteados são {ímpar}.')