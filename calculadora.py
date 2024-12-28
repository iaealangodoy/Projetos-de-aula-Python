while True:

    numero_1 = input('Digite o primeiro número: ')
    operador = input('Digite um operador (+-x/): ')
    numero_2 = input('Digite o segundo número: ')
    
    float_numero_1 = float(numero_1)
    float_numero_2 = float(numero_2)
    operadores_validos = '+-x/'

    calculo_adicao = float_numero_1 + float_numero_2
    calculo_subtracao = float_numero_1 - float_numero_2
    calculo_multiplicacao = float_numero_1 * float_numero_2
    calculo_divisao = float_numero_1 / float_numero_2
    
    if len(operador) > 1:
        print('Você digitou mais de um operador!')
        continue
  
    if operador not in operadores_validos:
        print('Digite um operador válido (+-x/)')
        continue

    if operador == '+':
        print(f'O resultado da adição é {calculo_adicao}')

    elif operador == '-':
        print(f'O resultado da subtração é {calculo_subtracao}')

    elif operador == 'x':
        print(f'O resultado da multiplicação é {calculo_multiplicacao}')

    elif operador == '/':
        print(f'O resuldado da divisão é {calculo_divisao}')
        
    else:
        print('Você digitou algo errado, tente novamente!')
    
    
    continuar = input('Para sair da calculadora digite "S" ou "N" para continuar calculando.: ').lower().startswith('s')
    
    if continuar is True:
        break
    
               
