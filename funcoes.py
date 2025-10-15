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