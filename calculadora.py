numero_1 = input('Digite o primeiro número: ')
multiplicador = input('Digite um multiplicador: ')
numero_2 = input('Digite o segundo número: ')

float_numero_1 = float(numero_1)
float_numero_2 = float(numero_2)

calculo_adicao = float_numero_1 + float_numero_2
calculo_subtracao = float_numero_1 - float_numero_2
calculo_multiplicacao = float_numero_1 * float_numero_2
calculo_divisao = float_numero_1 / float_numero_2

if multiplicador == '+':
    print(f'O resultado da adição é {calculo_adicao:.2f}')

if multiplicador == '-':
    print(f'O resultado da subtração é {calculo_subtracao:.2f}')

if multiplicador == 'x':
    print(f'O resultado da multiplicação é {calculo_multiplicacao:.2f}')

if multiplicador == '/':
    print(f'O resuldado da divisão é {calculo_divisao:.2f}')

else:
    print('Você precisa digitar algum multiplicador "+", "-", "x" ou "/" para funcionar')