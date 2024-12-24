horario_dia = input('Digite aqui que horas são: ')

horario_dia_float = float(horario_dia)

bom_dia = horario_dia_float >= 0 and horario_dia_float <= 11
boa_tarde = horario_dia_float >= 12 and horario_dia_float <= 17
boa_noite = horario_dia_float >= 18 and horario_dia_float <= 23

if bom_dia:
    print(f'Bom dia, são {horario_dia}hrs.')

elif boa_tarde:
    print(f'Boa Tarde, são {horario_dia}hrs.')

elif boa_noite:
    print(f'Boa noite, são {horario_dia}hrs')

else:
    print('Você não digitou um horário valido.')