p = float(input('Peso de peixes: '))
if p > 50:
    excesso = p - 50
    multa = excesso * 4
    print(f'Multa: R${multa:.2f}')
else:
    excesso = multa = 0
    print('Não há excesso de peso')