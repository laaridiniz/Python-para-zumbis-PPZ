nota = int(input('Digite uma nota de 0 a 10: '))
while nota < 0 or nota > 10:
    print('Valor inválido.')
    nota = int(input('Por favor, digite uma nota válida: '))
print(f'A nota digitada foi {nota}.')