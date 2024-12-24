nome = input('Digite aqui o seu nome: ')

nome_len = len(nome)

nome_curto = nome_len >= 1 and nome_len <= 4
nome_normal = nome_len >= 5 and nome_len <= 6
nome_longo = nome_len > 6

if nome_curto:
    print('Seu nome é curto!')

if nome_normal:
    print('Seu nome é normal!')

if nome_longo:
    print('Seu nome é longo!')

else:
     print('Você não digitou um nome!')