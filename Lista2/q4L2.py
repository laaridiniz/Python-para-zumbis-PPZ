'''4. Faça um Programa que leia três números e mostre o maior deles.'''

#Inserindo os valores a serem comparados
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

#Comparando os valores e imprimindo o maior deles
if a >= b and a >= c:
    print(f'Maior número: {a}')
elif b >= a and b >= c:
    print(f'Maior número: {b}')
else:
    print(f'Maior número: {c}')
