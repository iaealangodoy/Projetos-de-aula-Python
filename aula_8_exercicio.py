nome = str(input('Qual é o seu nome? '))
sobrenome = str(input('Qual é o seu sobrenome? '))
idade = int(input('Qual é a sua idade? '))
ano_nascimento = int(2024 - idade)
maior_de_idade = bool(idade >= 18)
altura_metros = float(input('Qual é a sua altura em metros? '))
print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Ano de nascimento: ', ano_nascimento)
print('É maior de idade? ', maior_de_idade)
print('Altura em metros: ', altura_metros)