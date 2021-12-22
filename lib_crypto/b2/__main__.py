#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ..tests.test import test_crypt
from .Tritemi import dec, enc

print("--------------------ТРИТЕМИЙ--------------------")

test_crypt(enc, dec)

from .Belazo import dec, enc

print("--------------------Belazo--------------------")

test_crypt(enc, dec)

from .Vizhiner import dec, enc

print("--------------------Vizhiner--------------------")

test_crypt(enc, dec)
