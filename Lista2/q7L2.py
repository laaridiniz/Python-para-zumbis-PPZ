m = float(input("Tamanho em metros: "))
l = 18 * 3
if m % 54 == 0:
    latas = m / 54
else:
    latas = int(m / 54) + 1

valor = latas * 80
print(f'{latas} lata(s)')
print(f'Valor total: {valor: .2f}')