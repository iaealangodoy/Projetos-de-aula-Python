import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls' if os.name == 'nt' else 'clear')
        valor = input('Valor: ')
        lista.append(valor)
    
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]

        except ValueError:
            print('Por favor digite número inteiro')

        except IndexError:
            print('Índice não existente na lista')

        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system('cls' if os.name == 'nt' else 'clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i,valor)
    
    else:
        print('Por favor, escolha i, a ou l.')