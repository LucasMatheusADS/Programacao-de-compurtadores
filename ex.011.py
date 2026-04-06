n = int(input('Digite um numero: '))
if n % 2 == 0 and n > 0:
    print('par positivo')
elif n % 2 == 0 and n < 0:
    print('par negativo')
else:
    print('impar')