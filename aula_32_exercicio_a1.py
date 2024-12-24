numero = input('Digite um número inteiro para saber se ele é par ou ímpar: ')

numero_int= int(numero)

calculo_par_ou_impar = numero_int % 2

par = calculo_par_ou_impar == 0
impar = calculo_par_ou_impar == 1

if par:
    print(f'Você digitou {numero}, ele é um número PAR!')

elif impar:
    print(f'Você digitou o {numero}, ele é um número ÍMPAR!')

else:
    print('Você não digitou um número!')
