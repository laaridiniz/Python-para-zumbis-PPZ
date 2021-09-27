'''6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. 
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$ .'''

#Inserindo o valor do salário e das horas trabalhadas
s = float(input('Digite o valor do seu salário por hora: '))
h = float(input('Digite as horas trabalhadas no mês: '))

#Calculando o salário bruto
sb = s * h

#Calculando os descontos
IR = 0.11 * sb
INSS = 0.08 * sb
sind = 0.05 * sb
desc = IR + INSS + sind

#Calculando o salário líquido
sl = sb -  desc

#Imprimindo os valores encontrados
print(f'Seu salário bruto neste mês é R$ {sb:.2f}.')
print(f'O desconto de IR foi de R$ {IR:.2f}.')
print(f'O desconto de INSS foi de R$ {INSS:.2f}.')
print(f'O desconto do sindicato foi de R$ {sind:.2f}.')
print(f'O total de descontos foi de R$ {desc:.2f}.')
print(f'Seu salário líquido totalizou R$ {sl:.2f}.')
