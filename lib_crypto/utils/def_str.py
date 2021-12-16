from .data import alph

REPLACES = {
    ",": "ЗПТ",
    ".": "ТЧК",
    "-": "ТИРЕ",
    ";": "ТЧКИЗПТ",
}


def to_indexes(text, alph=alph):
    return [alph.index(symbol) for symbol in text]


def to_symbols(nums, alph=alph):
    return "".join([alph[num] for num in nums])


def clear_text(text, alph=alph):
    import re

    text = replace_special(text, alph)
    text = text.lower()
    text = re.sub(f"[^{alph}]", "", text)
    return text


def replace_special(text, alph=alph, replaces=REPLACES):

    for key, value in replaces.items():
        text = text.replace(key, value)
    return text


def is_hex(s):
    import string

    try:
        return all(c in string.hexdigits for c in s)
    except:
        return False


def random_char(alph=alph):
    from random import choice

    return choice(alph)


if __name__ == "__main__":
    test = "Это тестовая строка, тут есть все: запятые, КАПС, тире(-), и многое другое... That`s awesome!"
    print(clear_text(test))
