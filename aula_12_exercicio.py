nome = str(input('Qual é o seu nome? '))
altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
imc = peso / (altura * altura)

print('{} tem {} de altura, \npesa {} quilos e seu IMC é\n{:.2f}'.format(nome, altura, peso, imc))