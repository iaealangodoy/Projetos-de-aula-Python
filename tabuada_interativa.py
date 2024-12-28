tabuada = input('Digite qual tabuada que você quer calcula: ')
num_inicio = input('Digite qual número a tabuada deve iniciar: ')
num_final = input('Digite qual número a tabuada deve finalizar: ')

int_tabuada = int(tabuada)
int_num_inicio = int(num_inicio)
int_num_final = int(num_final)

numeros = range(int_num_inicio, (int_num_final + 1))

for tabuada_final in numeros:
    print(f'{tabuada} + {tabuada_final} = {int_tabuada * tabuada_final}')

