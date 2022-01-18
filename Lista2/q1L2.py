'''1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.'''

# Pedindo as medidas da figura a ser analisada
a = int(input('Medida do primeiro lado: '))
b = int(input('Medida do segundo lado: '))
c = int(input('Medida do terceiro lado: '))

# Analisando a possibilidade de ser um triângulo
if a > b + c or b > a + c or c > a + b:
    print(f'Esta figura não pode ser um triângulo')
    
# Informando qual o tipo de triângulo
elif a == b == c:
    print (f'É um triângulo equilátero')
elif a == b or b == c or a == c:
    print(f'É um triângulo isósceles')
else:
    print (f'É um triângulo escaleno')
