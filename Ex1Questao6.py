from math import pow
raio = float(input('Digite o raio do circulo: '))
ar = 3.14 * pow(raio, 2)
print('A area deste circulo é {:.2f}.'.format(ar))