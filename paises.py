import random

todos_os_paises = [
    # Países com A
    'Abecásia',
    'Afeganistão',
    'África do Sul',
    'Albânia',
    'Alemanha',
    'Andorra',
    'Angola',
    'Antígua e Barbuda',
    'Arábia Saudita',
    'Argélia',
    'Argentina',
    'Armênia',
    'Austrália',
    'Áustria',
    'Azerbaijão',

    # Países com B

    'Bahamas',
    'Bahrein',  # (ou Barein, ou Barém)
    'Bangladesh',
    'Barbados',
    'Bélgica',
    'Belize',
    'Benim',
    'Bielorrússia',
    'Bolívia',
    'Bósnia e Herzegovina',
    'Botswana',  # (ou Botsuana)
    'Brasil',
    'Brunei',
    'Bulgária',
    'Burkina Faso',  # (ou Burquina Faso)
    'Burundi',
    'Butão',

    # Países com C

    'Cabo Verde',
    'Camarões',
    'Camboja',
    'Canadá',
    'Catar',  # (ou Qatar)
    'Cazaquistão',
    'Chade',
    'Chile',
    'China',
    'Chipre',
    'Cingapura',  # (ou Singapura)
    'Colômbia',
    'Comores',
    'Congo',
    'Coreia do Norte',
    'Coreia do Sul',
    'Costa do Marfim',
    'Costa Rica',
    'Croácia',
    'Cuba',

    # Países com D

    'Dinamarca',
    'Djibouti',  # (ou Djibuti)
    'Dominica',

    # Países com E

    'Egito',
    'El Salvador',
    'Emirados Árabes Unidos',
    'Equador',
    'Eritreia',
    'Escócia',
    'Eslováquia',
    'Eslovênia',
    'Espanha',
    'Estados Federados da Micronésia',
    'Estados Unidos da América',
    'Estônia',
    'Eswatini',  # (ou Essuatíni, ou Suazilândia)
    'Etiópia',

    # Países com F

    'Fiji',
    'Filipinas',
    'Finlândia',
    'França',

    # Países com G

    'Gabão',
    'Gâmbia',
    'Gana',
    'Geórgia',
    'Granada',
    'Grécia',
    'Guatemala',
    'Guiana',
    'Guiné',
    'Guiné-Bissau',
    'Guiné Equatorial',

    # Países com H

    'Haiti',
    'Holanda',  # (ou Países Baixos)
    'Honduras',
    'Hungria',

    # Países com I

    'Iêmen',
    'Índia',
    'Indonésia',
    'Inglaterra',
    'Irã',  # (ou Irão)
    'Iraque',
    'Irlanda do Norte',
    'Irlanda',
    'Islândia',
    'Israel',
    'Itália',

    # Países com J

    'Jamaica',
    'Japão',
    'Jordânia',

    # Países com K

    'Kiribati',  # (ou Quiribati)
    'Kosovo',
    'Kuwait',

    # Países com L

    'Laos',
    'Lesoto',
    'Letônia',
    'Líbano',
    'Libéria',
    'Líbia',
    'Liechtenstein',  # (ou Listenstaine)
    'Lituânia',
    'Luxemburgo',

    # Países com M

    'Macedônia do Norte',
    'Madagascar',  # (ou Madagáscar)
    'Malásia',
    'Malawi',  # (ou Malauí)
    'Maldivas',
    'Mali',
    'Malta',
    'Marrocos',
    'Marshall',
    'Maurícia',
    'Mauritânia',
    'México',
    'Mianmar',
    'Micronésia',
    'Moçambique',
    'Moldávia',
    'Mônaco',
    'Mongólia',
    'Montenegro',

    # Países com N

    'Namíbia',
    'Nauru',
    'Nepal',
    'Nicarágua',
    'Níger',
    'Nigéria',
    'Noruega',
    'Nova Zelândia',

    # Países com O

    'Omã',
    'Ossétia do Sul',

    # Países com P

    'País de Gales',
    'Países Baixos',  # (ou Holanda)
    'Palau',
    'Palestina',
    'Panamá',
    'Papua-Nova Guiné',
    'Paquistão',
    'Paraguai',
    'Peru',
    'Polônia',
    'Portugal',

    # Países com Q

    'Qatar',  # (ou Catar)
    'Quênia',
    'Quirguistão',
    'Quiribati',  # (ou Kiribati)

    # Países com R

    'República Árabe Saaraui Democrática',
    'República Centro-Africana',
    'República Democrática do Congo',
    'República do Congo',
    'República Dominicana',
    'República Tcheca',  # (ou Tchéquia)
    'República Turca de Chipre do Norte',
    'Romênia',
    'Ruanda',
    'Rússia',

    # Países com S

    'Salomão',
    'Samoa',
    'San Marino',  # (ou São Marinho)
    'Santa Lúcia',
    'São Cristóvão e Névis',  # (ou São Cristóvão e Neves)
    'São Tomé e Príncipe',
    'São Vicente e Granadinas',
    'Senegal',
    'Serra Leoa',
    'Sérvia',
    'Seychelles',  # (ou Seicheles)
    'Singapura',  # (ou Cingapura)
    'Síria',
    'Somália',
    'Sri Lanka',
    'Suazilândia',  # (ou Eswatini, ou Essuatíni)
    'Sudão do Sul',
    'Sudão',
    'Suécia',
    'Suíça',
    'Suriname',

    # Países com T

    'Tailândia',
    'Taiwan',
    'Tajiquistão',  # (ou Tadjiquistão)
    'Tanzânia',
    'Tchéquia',  # (ou República Tcheca)
    'Timor-Leste',
    'Togo',
    'Tonga',
    'Trinidad e Tobago',
    'Tunísia',
    'Turcomenistão',  # (ou Turquemenistão)
    'Turquia',
    'Tuvalu',

    # Países com U

    'Ucrânia',
    'Uganda',
    'Uruguai',
    'Uzbequistão',

    # Países com V

    'Vanuatu',
    'Vaticano',
    'Venezuela',
    'Vietnã',  # (ou Vietname)

    # Países com Z

    'Zâmbia',
    'Zimbábue'

]

paises_mais_conhecidos = [
    'Estados Unidos da América',
    'China',
    'Rússia',
    'Índia',
    'Brasil',
    'Alemanha',
    'França',
    'Inglaterra',
    'Canadá',
    'Japão',
    'Austrália',
    'Itália',
    'Espanha',
    'México',
    'Argentina'
]


def adivinhar_pais():
    tentativas = 3
    opcao = ['s', 'sim', 'n', 'nao', 'não']  # Opções válidas para continuar o jogo

    while True:

        print('Escolha uma das opções abaixo:')
        print('1 - Todos os países')
        print('2 - Países mais conhecidos')

        op = input('>')

        if not op.isdigit():
            print('Insira uma opção válida \n')

        else:
            if op == '1':
                while True:
                    pais_aleatorio_1 = random.choice(todos_os_paises).lower()

            elif op == '2':
                while True:
                    pais_aleatorio_2 = random.choice(paises_mais_conhecidos).lower()

            else:
                print('Insira uma opção válida \n')
