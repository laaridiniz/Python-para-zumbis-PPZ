sa = float(input('Salário atual: '))
p = float(input('Porcentagem: '))
porcentagem = sa*p/100
novo = sa+porcentagem
print(f'Aumento: R$ {porcentagem:.2f}')
print(f'Novo salário: R$ {novo:.2f}')