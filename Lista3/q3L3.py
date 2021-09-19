A = 80000
B = 200000
anos = 0
while A <= B:
    anos = anos + 1
    A = A + A * 0.03
    B = B + B * 0.015
print(f'Será necessário {anos} anos.')