numero_1 = input('Digite o primeiro número: ')
multiplicador = input('Digite um multiplicador: ')
numero_2 = input('Digite o segundo número: ')

float_numero_1 = float(numero_1)
float_numero_2 = float(numero_2)

if multiplicador == '+':
    adicao = float_numero_1 + float_numero_2
    print(f'O resultado da adição é {adicao:.2f}')

elif multiplicador == '-':
    subtracao = float_numero_1 - float_numero_2
    print(f'O resultado da subtração é {subtracao:.2f}')

elif multiplicador == 'x':
    multiplicacao = float_numero_1 * float_numero_2
    print(f'O resultado da multiplicação é {multiplicacao:.2f}')

elif multiplicador == '/':
    divisao = float_numero_1 / float_numero_2
    print(f'O resuldado da divisão é {divisao:.2f}')

else:
    print('Você precisa digitar algum multiplicador "+", "-", "x" ou "/" para funcionar')