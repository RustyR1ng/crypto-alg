def to_indexes(text, alph):
    return [alph.index(symbol) for symbol in text]


def to_symbols(nums, alph):
    return "".join([alph[num] for num in nums])


def clear_text(text, alph):
    return "".join([symbol for symbol in text.lower() if symbol in alph])
