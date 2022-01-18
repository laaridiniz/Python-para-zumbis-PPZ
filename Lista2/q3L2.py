'''3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. 
Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. 
Caso contrário mostrar tais variáveis com o conteúdo ZERO.'''

#Inserindo a quantidade de peixes pescada
p = float(input('Peso de peixes: '))

#Analisando a quantidade inserida e calculando eventual multa
if p > 50:
    excesso = p - 50
    multa = excesso * 4
    print(f'Multa: R${multa:.2f}')
else:
    excesso = multa = 0
    print('Não há excesso de peso')
