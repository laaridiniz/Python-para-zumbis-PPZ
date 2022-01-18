'''Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
sortudos existem entre 18644 e 33087, incluindo os extremos?

Resposta: 7995'''

# Definindo o contador
c = 0

# Aplicando as repetições
for n in range(18644, 33088):
    if "2" in str(n) and "7" not in str(n):
        c = c + 1
print(f'Existem {c} números sortudos no intervalo entre 18644 e 33087.')
