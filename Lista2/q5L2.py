a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a >= b and a >= c:
    print(f'Maior número: {a}')
elif b >= a and b >= c:
    print(f'Maior número: {b}')
else:
    print(f'Maior número: {c}')
if a <= b and a <= c:
    print(f'Menor número: {a}')
elif b <= c and b <= a:
    print(f'Menor número: {b}')
else:
    print(f'Menor número: {c}')