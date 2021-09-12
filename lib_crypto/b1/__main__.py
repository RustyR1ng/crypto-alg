#! /usr/bin/env python
# -*- coding: utf-8 -*-

from utils.data import alph, text_1000, text_test
from utils.test import test_crypt

from .Atbash import dec, enc

print("--------------------АТБАШ--------------------")

test_crypt(enc, dec)


from .Cesar import dec, enc

print("--------------------ЦЕЗАРЬ--------------------")

test_crypt(enc, dec)


from .Polibiy import dec, enc

print("--------------------ПОЛИБИЙ--------------------")

test_crypt(enc, dec)