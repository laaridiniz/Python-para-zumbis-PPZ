'''7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.'''

#Inserindo o tamanho da área a ser pintada
m = float(input("Tamanho em metros: "))

#Definindo o rendimento de uma lata de tinta
l = 18 * 3

#Estabelecendo as condições para divisão inteira e para divisão com resto
if m % 54 == 0:
    latas = m / 54
else:
    latas = int(m / 54) + 1

#Calculando os valores e imprimindo as informações necessárias
valor = latas * 80
print(f'{latas} lata(s)')
print(f'Valor total: {valor: .2f}')
