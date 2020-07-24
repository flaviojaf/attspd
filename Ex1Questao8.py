dinheiro = float(input('Quanto você ganha por hora? R$'))
hora = int(input('Quantas horas você trabalha no mês? '))
salario = (hora * dinheiro) * 23
print('O seu salário é de R${:.2f}.'.format(salario))
