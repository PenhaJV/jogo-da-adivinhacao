import random


def escolher_entre_todos():
    with open('todos os paises.txt', 'r', encoding='utf-8') as arquivo:
        lista_de_paises = arquivo.read().splitlines()

    pais_escolhido = random.choice(lista_de_paises)

    print(pais_escolhido)


def escolher_entre_os_mais_conhecidos():
    with open('paises mais conhecidos.txt', 'r', encoding='utf-8') as arquivo:
        lista_de_paises = arquivo.read().splitlines()

    pais_escolhido = random.choice(lista_de_paises)

    print(pais_escolhido)
