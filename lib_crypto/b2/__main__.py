#! /usr/bin/env python
# -*- coding: utf-8 -*-

from utils.data import alph, text_1000, text_test
from utils.test import test_crypt

from .Tritemi import dec, enc

print("--------------------ТРИТЕМИЙ--------------------")

test_crypt(enc, dec)
