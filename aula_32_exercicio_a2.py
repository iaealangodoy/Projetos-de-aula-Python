numero = input('Digite um número inteiro para saber se ele é par ou ímpar: ')

try:
    numero_float = float(numero)
    par_impar = numero_float % 2 == 0
    par_impar_texto = 'ÍMPAR'

    if par_impar:
        par_impar_texto = 'PAR'
    
    print(f'O número que você digitou {numero_float }, é {par_impar_texto}')

except:
    print('Você não digitou um número inteiro')