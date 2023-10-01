import random

# Inicializa uma lista vazia para conter os números de 0 a 100 como strings
numeros = []

# Preenche a lista com números de 0 a 100 como strings
for i in range(101):
    numeros.append(str(i))


def adivinhar_numero():
    """
    Função que implementa o Jogo de Adivinhação de Números.

    Esta função permite ao jogador adivinhar um número aleatório dentro do intervalo de 0 a 100.

    Parâmetros:
    Nenhum.

    Retorna:
    None.
    """
    tentativas = 3  # Número de tentativas permitidas
    opcao = ['s', 'sim', 'n', 'nao', 'não']  # Opções válidas para continuar o jogo

    while True:
        numero_aleatorio = random.choice(numeros)  # Escolhe um número aleatório da lista

        if tentativas == 0:
            print(f'Você perdeu! O número era "{numero_aleatorio}"')
            break

        print(f'Tentativas restantes: {tentativas} \n')
        print('Escolha um número de 0 até 100')

        escolha = input('> ')

        if not escolha.isdigit():
            print('Insira uma opção válida. \n')
        else:
            escolha = int(escolha)

            if escolha == numero_aleatorio:
                print('\nParabéns! Você acertou.')

                print('Deseja continuar? [S/N]')

                continuar = input('> ')

                if continuar not in opcao:
                    print('Insira uma opção válida. \n')
                elif continuar in ['n', 'nao', 'não']:
                    print('\nPrograma encerrado.')
                    return False
                else:
                    continue
            else:
                print('Você errou! \n')
                tentativas -= 1
