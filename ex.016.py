valor = input('Digite um valor: ')
if valor.isnumeric():
    n = int(valor)
    print('Número válido')
    print(f'Quadrado: {n ** 2}')
else:
    print('Não é numérico')