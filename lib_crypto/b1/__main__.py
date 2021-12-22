#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ..tests.test import test_crypt
from .Atbash import dec, enc

print("--------------------АТБАШ--------------------")

test_crypt(enc, dec)


from .Cesar import dec, enc

print("--------------------ЦЕЗАРЬ--------------------")

test_crypt(enc, dec)


from .Polibiy import dec, enc

print("--------------------ПОЛИБИЙ--------------------")

test_crypt(enc, dec)
