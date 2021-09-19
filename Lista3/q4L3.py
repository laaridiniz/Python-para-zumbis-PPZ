n = int(input('Digite um número inteiro: '))
a, b = 1, 1
cont = 0
while cont <= n - 2:
    a, b = b, a + b
    cont = cont + 1
print(b)