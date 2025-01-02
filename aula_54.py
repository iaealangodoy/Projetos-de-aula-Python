import os

lista = []

while True:
    print('Selecione uma opção:')
    opcoes = input('[i]nserir [a]pagar [l]istar: ').strip().lower()

    if not opcoes or opcoes[0] not in ['i', 'a', 'l', ]:
        print('Você digitou uma opção inválida. Tente novamente!')
        continue
        

    if opcoes[0] == 'i':
        os.system('cls' if os.name == 'nt' else 'clear')
        valor = input('Valor: ').strip()
        lista.append(valor)

    elif opcoes[0] == 'l':
        if not lista:
            print('A lista está vazia.')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            for indice, nome in enumerate(lista):
                print(f'{indice}: {nome}')

    elif opcoes[0] == 'a':
        if not lista:
            print('A lista está vazia. Não há nada para apagar.')
        
        else:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                apagar = int(input('Escolha um índice para apagar: '))
                if 0 <= apagar < len(lista):
                    lista.pop(apagar)
                    print('Item removido com sucesso!')
                else:
                    print('Índice fora do intervalo.')
            
            except ValueError:
                print('Por favor, insira um número válido.')

