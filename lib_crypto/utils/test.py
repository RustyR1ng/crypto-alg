# -*- coding: utf-8 -*-

from .print import *


def test_crypt(enc, dec):

    from .data import alph, text_1000, text_test
    from .def_str import clear_text

    text_test = clear_text(text_test)
    text_1000 = clear_text(text_1000)

    print_header("Тест на пословице и тексте")

    _enc = enc(text_test)
    print_kv("Шифровка пословицы", _enc)

    _dec = dec(_enc)
    print_kv("Расшифровка пословицы", _dec)

    _enc = enc(text_1000)
    print_kv("Шифровка 1000", _enc)

    _dec = dec(_enc)
    print_kv("Расшифровка 1000", _dec)
