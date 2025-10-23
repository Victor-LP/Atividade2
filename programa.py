from funcoes import *

# Inicializa frota
frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

navios = {
    "porta-aviões": {"quantidade": 1, "tamanho": 4},
    "navio-tanque": {"quantidade": 2, "tamanho": 3},
    "contratorpedeiro": {"quantidade": 3, "tamanho": 2},
    "submarino": {"quantidade": 4, "tamanho": 1}
}

# Porta-aviões
for navio, infos in navios.items():
    for i in range(infos["quantidade"]):
        lin, col = 0, 0
        ori = ""
        while not posicao_valida(frota, lin, col, ori, infos["tamanho"]):
            print(f"Insira as informações referentes ao navio {navio} que possui tamanho {infos['tamanho']}")
            lin = int(input("Linha: "))
            col = int(input("Coluna: "))
            if navio != "submarino":
                ori_input = int(input("[1] Vertical [2] Horizontal >"))
                ori = "vertical" if ori_input == 1 else "horizontal"
            else:
                ori = "horizontal"
            if not posicao_valida(frota, lin, col, ori, infos["tamanho"]):
                print("Esta posição não está válida!")
        frota = preenche_frota(frota, navio, lin, col, ori, infos["tamanho"])

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
while afundados(frota_oponente, tabuleiro_oponente) < 10:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    while True:
        lin =  int(input("Jogador, qual linha deseja atacar? "))
        while lin < 0 or lin > 9:
            print("Linha inválida!")
            lin = int(input("Jogador, qual linha deseja atacar? "))
        col =  int(input("Jogador, qual coluna deseja atacar? "))
        while col < 0 or col > 9:
            print("Coluna inválida!")
            col =  int(input())
        if tabuleiro_oponente[lin][col] in ['X', '-']:
            print(f"A posição linha {lin} e coluna {col} já foi informada anteriormente!")
            continue
        break
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, lin, col)
print("Parabéns! Você afundou todos os navios do oponente!")