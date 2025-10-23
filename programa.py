from funcoes import *

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []}

navios = {
    "porta-aviões": {"quantidade": 1, "tamanho": 4},
    "navio-tanque": {"quantidade": 2, "tamanho": 3},
    "contratorpedeiro": {"quantidade": 3, "tamanho": 2},
    "submarino": {"quantidade": 4, "tamanho": 1}}

for nome_navio, info in navios.items():
    for i in range(info["quantidade"]):
        linha, coluna = -1, -1
        orientacao = ""
        while not posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {info['tamanho']}")
            while True:
                linha = int(input("Linha: "))
                if 0 <= linha <= 9:
                    break
                print("Linha inválida!")
            while True:
                coluna = int(input("Coluna: "))
                if 0 <= coluna <= 9:
                    break
                print("Coluna inválida!")
            if nome_navio != "submarino":
                orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if orientacao_input == 1 else "horizontal"
            else:
                orientacao = "horizontal"
            if not posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
                print("Esta posição não está válida!")
        frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, info["tamanho"])

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

total_navios_oponente = 0
for lista in frota_oponente.values():
    total_navios_oponente += len(lista)
montar = True

jogando = True
while jogando:
    if montar:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    montar = True
    while True:
        lin = int(input("Jogador, qual linha deseja atacar? "))
        if 0 <= lin <= 9:
            break
        print("Linha inválida!")

    while True:
        col = int(input("Jogador, qual coluna deseja atacar? "))
        if 0 <= col <= 9:
            break
        print("Coluna inválida!")

    if str(tabuleiro_oponente[lin][col]) in "X-":
        print(f"A posição linha {lin} e coluna {col} já foi informada anteriormente!")
        montar = False
    else:
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, lin, col)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios_oponente:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False