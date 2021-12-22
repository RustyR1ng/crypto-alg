from .def_str import clear_text, to_indexes


def kv_hash(msg: str, p: int = 11) -> int:
    h = 0
    h_list = []
    for symbol_code in to_indexes(msg):
        symbol_code += 1
        h = ((h + symbol_code) ** 2) % p
        h_list.append(h)
    return h


if __name__ == "__main__":
    print(kv_hash(clear_text("МАША")))  # проверяем по примеру хеша
