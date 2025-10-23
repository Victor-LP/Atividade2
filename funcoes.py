def define_posicoes (lin,col,ori,siz):
    ret = []
    for i in range(siz):
        ret.append([lin+i,col]) if ori == "vertical" else ret.append([lin,col+i])
    return ret

def preenche_frota (fr,na,lin,col,ori,siz):
    if na not in fr:
        fr[na] = []
    fr[na].append(define_posicoes(lin,col,ori,siz))
    return fr

def faz_jogada (grid,lin,col):
    if grid[lin][col] == 1:
        grid[lin][col] = 'X'
    else:
        grid[lin][col] = '-'
    return grid

def posiciona_frota (fr):
    grid = [
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10
    ]
    for val in fr.values():
        for bar in val:
            for pos in bar:
                grid[pos[0]][pos[1]] = 1
    return grid
def afundados(fr, tab):
    afundado = 0
    pos = []
    i = 0
    while i < 10:
        j = 0
        while j < 10:
            if tab[i][j] == 'X':
                pos.append([i, j])
            j += 1
        i += 1
    for val in fr.values():
        for bar in val:
            cont = 0
            for p in bar:
                if p in pos:
                    cont += 1
            if cont == len(bar):
                afundado += 1
    return afundado
def posicao_valida (fr,lin,col,ori,siz):
    posicoes = define_posicoes(lin,col,ori,siz)
    for p in posicoes:
        if p[0] < 0 or p[0] > 9 or p[1] < 0 or p[1] > 9:
            return False
    for val in fr.values():
        for bar in val:
            for p in posicoes:
                if p in bar:
                    return False
    return True
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto