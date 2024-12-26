continuartrue = True

while continuartrue:

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
        print(f'O resultado da adição é {calculo_adicao}')

    elif multiplicador == '-':
        print(f'O resultado da subtração é {calculo_subtracao}')

    elif multiplicador == 'x':
        print(f'O resultado da multiplicação é {calculo_multiplicacao}')

    elif multiplicador == '/':
        print(f'O resuldado da divisão é {calculo_divisao}')
        
    else:
        print('Você precisa digitar algum multiplicador "+", "-", "x" ou "/" para funcionar')
    
    continuar = input('Para continuar calculando digite "S" para sim ou "N" para não:')
    
    if continuar == 'S':
        continuartrue = True
    else:
        break
    
               
