p = float(input('Preço original: '))
d = float(input('Desconto: '))
print(f'Desconto: R$ {d/100*p}')
print(f'Preço a pagar: R$ {p-(d/100*p)}')