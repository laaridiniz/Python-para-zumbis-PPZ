n1 = int(input('Digite um número inteiro positivo: '))
n2 = int(input('Digite outro número inteiro positivo: '))
while n1 % n2 != 0:
    n1, n2 = n2, n1 % n2
print(f'O MDC desses números é {n2}.')
