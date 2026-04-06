n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print(f'Soma:', n1 + n2)
if n1 > n2:
    print(f'Maior: {n1}')
elif n2 > n1:
    print(f'Maior: {n2}')
else:
    print('São iguais')