sph = float(input('Salário por hora: '))
h = float(input('Horas trabalhadas: '))
salario = (sph*h)
INSS = 8/100*salario
Sind = 5/100*salario
IR = 11/100*salario
total = salario - IR - INSS - Sind
print(f'Salário bruto: {salario:.2f}')
print(f'IR: {IR:.2f}')
print(f'INSS: {INSS:.2f}')
print(f'Sindicato: {Sind:.2f}')
print(f'Salário líquido: {total:.2f}')