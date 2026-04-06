n = int(input('Digite um número inteiro: '))
if n > 0:
    if n % 2 == 0 and n % 3 == 0:
        print('Múltiplo de 2 e 3')
    else:
        print('Não atende')
else:
    print('Número inválido')