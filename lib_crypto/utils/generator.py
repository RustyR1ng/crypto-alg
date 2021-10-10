def lcg(m, a, c, seed, _range):
    for _ in range(_range):
        seed = (a * seed + c) % m
        yield seed
