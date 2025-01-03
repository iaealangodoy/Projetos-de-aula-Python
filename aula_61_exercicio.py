cpf = '746.824.890-70'
cpf_limpo = cpf.replace('.','').replace('-','')
nove_digitos = cpf_limpo[: 9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)


'''caracteres_individuais = list(nove_digitos)

cal_01 = int(caracteres_individuais[0]) * 10
cal_02 = int(caracteres_individuais[1]) * 9
cal_03 = int(caracteres_individuais[2]) * 8
cal_04 = int(caracteres_individuais[3]) * 7
cal_05 = int(caracteres_individuais[4]) * 6
cal_06 = int(caracteres_individuais[5]) * 5
cal_07 = int(caracteres_individuais[6]) * 4
cal_08 = int(caracteres_individuais[7]) * 3
cal_09 = int(caracteres_individuais[8]) * 2

soma = cal_01 + cal_02 + cal_03 + cal_04 + cal_05 + cal_06 + cal_07 + cal_08 + cal_09
multiplicacao = soma * 10
div_resto = multiplicacao % 11

div_resto if div_resto > 9  else 0

print(nove_digitos)
print(cal_01)
print(cal_02)
print(cal_03)
print(cal_04)
print(cal_05)
print(cal_06)
print(cal_07)
print(cal_08)
print(cal_09)
print(soma)
print(multiplicacao)
print(div_resto)
print(div_resto if div_resto < 9  else 0)'''