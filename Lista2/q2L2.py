'''2. Determine se um ano é bissexto.'''

#Inserindo o ano a ser analisado
ano=int(input('Ano: '))

#Verificando se o ano é bissexto e retornando o resultado
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('É ano bissexto')
else:
    print('Não é ano bissexto')
