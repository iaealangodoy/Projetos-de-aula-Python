horario_dia = input('Digite aqui que horas são: ')

try:

    horario_dia_float = float(horario_dia)

    if horario_dia_float >= 0 and horario_dia_float <= 11:
        print(f'Bom dia, são {horario_dia}hrs.')

    elif horario_dia_float >= 12 and horario_dia_float <= 17:
        print(f'Boa Tarde, são {horario_dia}hrs.')

    elif horario_dia_float >= 18 and horario_dia_float <= 23:
        print(f'Boa noite, são {horario_dia}hrs')

    else:
        print('Não conheço o horário que você digitou')

except:
    print('Você não digitou um horário!')