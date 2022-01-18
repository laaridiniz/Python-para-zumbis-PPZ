'''Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
divisíveis por 7?

Resposta: 183'''

# Definindo o contador
cont = 0

# Aplicando as repetições
for n in range(1067, 3628):
    if n % 2 == 0 and n % 7 == 0:
        cont = cont + 1
print(f'Existem {cont} números pares e divisíveis por 7.')
