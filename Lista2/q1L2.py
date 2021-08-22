a = float(input('Medida do primeiro lado: '))
b = float(input('Medida do segundo lado: '))
c = float(input('Medida do terceiro lado: '))
if a > b + c or b > a + c or c > a + b:
    print(f'Esta figura não pode ser um triângulo')
elif a == b == c:
    print (f'É um triângulo equilátero')
elif a == b or b == c or a == c:
    print(f'É um triângulo isósceles')
else:
    print (f'É um triângulo escaleno')