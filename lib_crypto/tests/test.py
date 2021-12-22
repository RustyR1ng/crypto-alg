# -*- coding: utf-8 -*-

import inspect
from types import FunctionType

from ..utils.printing import *


def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }


def test_crypt(enc: FunctionType, dec: FunctionType) -> None:
    from ..data import text_1000, text_test
    from ..utils.def_str import clear_text

    text_test = clear_text(text_test)
    text_1000 = clear_text(text_1000)

    print_header("Тест на пословице и тексте")

    print(get_default_args(enc))
    _enc = enc(text_test)
    print_kv("Шифровка пословицы", _enc)

    _dec = dec(_enc)
    print_kv("Расшифровка пословицы", _dec)

    _enc = enc(text_1000)
    print_kv("Шифровка 1000", _enc)

    _dec = dec(_enc)
    print_kv("Расшифровка 1000", _dec)
