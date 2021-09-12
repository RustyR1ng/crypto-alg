from ..utils.data import alph


def alph_to_sq(alph, cols=6):

    from math import ceil, sqrt

    n = ceil((sqrt(len(alph))))  # получение размера квадратной матрицы
    sq = [[char for char in alph[i * n : (i + 1) * n]] for i in range(n)]

    return sq


def enc(text, alph=alph, **kwargs):

    answer = []
    sq = alph_to_sq(alph)

    for sym in text:
        sym = sym.lower()

        for row in sq:
            if sym not in row:
                continue
            num = str(sq.index(row) + 1) + str(row.index(sym) + 1)
            answer.append(num)

    return " ".join(answer)


def dec(text, alph=alph, **kwargs):
    text = text.split()
    sq = alph_to_sq(alph)

    return "".join([sq[int(sym[0]) - 1][int(sym[1]) - 1] for sym in text])
