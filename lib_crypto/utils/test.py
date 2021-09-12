#! /usr/bin/env python
# -*- coding: utf-8 -*-


def test_crypt(enc, dec):

    from .data import alph, text_1000, text_test

    _enc = enc(text_test, alph)
    print("Шифровка Тест:", _enc)

    _dec = dec(_enc, alph)
    print("Расшифровка Тест:", _dec)


"""
    _enc = enc(text_1000, alph)
    print("Шифровка 1000:", _enc)

    _dec = dec(_enc, alph)
    print("Расшифровка 1000:", _dec) """
