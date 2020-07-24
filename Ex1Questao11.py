letra = str(input('Digite uma letra: ')).strip().upper()
if letra in 'A' 'E' 'I' 'O' 'U':
    print('{} é uma vogal.'.format(letra))
else:
    print('{} é uma consoante.'.format(letra))
