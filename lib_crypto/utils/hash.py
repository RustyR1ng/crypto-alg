from .def_str import to_indexes, clear_text


def hash(msg, p=11):
    h = 0
    h_list = []
    for symbol_code in to_indexes(msg):
        symbol_code += 1
        h = ((h + symbol_code) ** 2) % p
        h_list.append(h)
    return h


if __name__ == "__main__":
    print(hash(clear_text("МАША")))  # проверяем по примеру хеша
