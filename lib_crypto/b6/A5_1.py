# -*- coding: utf-8 -*-
from re import match
from operator import xor
from functools import reduce
from ..utils.def_bin import to_binary, bin_to_str
from dataclasses import dataclass
from typing import List


@dataclass
class Reg:
    length: int
    main_pos: int
    takt_pos: tuple

    def __post_init__(self):
        assert all(i < self.length for i in [self.main_pos, *self.takt_pos])


REGS_CONF = [
    Reg(19, 8, (18, 17, 16, 13)),
    Reg(22, 10, (21, 20)),
    Reg(23, 10, (22, 21, 20, 7)),
]


class Crypter:
    def __init__(self, conf: List[Reg]):
        self.conf = conf
        self.regs = None

    def configure(self, len_msg: int, key: str):
        key = set_key(key)
        regs = get_registers(key, self.conf)
        keystream = get_keystream(len_msg, regs, self.conf)

        return keystream

    def enc(
        self,
        msg: str,
        key: str = "0101001000011010110001110001100100101001000000110111111010110111",
    ):
        binary = to_binary(msg)
        keystream = self.configure(len(binary), key)
        res = [binary[i] ^ keystream[i] for i in range(len(binary))]

        return "".join(list(map(str, res)))

    def dec(
        self,
        msg: str,
        key: str = "0101001000011010110001110001100100101001000000110111111010110111",
    ) -> str:
        """
        Takes in a cipher, gets the keystream from its length, cipher is XOR'd with keystream, and converted to string.
        """
        keystream = self.configure(len(msg), key)

        res = [bit ^ keystream[i] for i, bit in enumerate(list(map(int, msg)))]

        return bin_to_str("".join(list(map(str, res))))


def get_registers(key: List[int], reg_confs: List[Reg]) -> List[List[int]]:
    """Loads registers using a 64-bit key as a parameter."""
    lens = [conf.length for conf in reg_confs]
    regs = []

    for i in range(len(lens)):
        start = sum(lens[:i])

        regs.append(key[start : start + lens[i]])

    return regs


def set_key(key: str) -> List[int]:
    """Sets the key and loads the registers if it contains 0's and 1's and if it's exactly 64 bits."""

    assert len(key) == 64
    assert match("^([01])+", key)

    key = list(map(int, key))

    return key


def get_majority(x: int, y: int, z: int) -> int:
    """
    Gets majority by adding up the x,y,and z values and if it's greater than 1 (e.g. two 1's and one 0), it returns the majority (1). Otherwise, if it's two 0's and one 1, the majority is returned as 0.
    """
    return x & y | x & z | y & z


def get_keystream(
    length: int, registers: List[List[int]], reg_confs: List[Reg]
) -> List[int]:
    """Calculates the keystream by XOR-ing the appropriate indeces."""

    regs_temp = registers[:]

    keystream = []
    keystream_xor = []

    for _ in range(length):
        majority = get_majority(
            *(regs_temp[i][reg_confs[i].main_pos] for i in range(len(regs_temp)))
        )

        for temp, conf in zip(regs_temp, reg_confs):
            if temp[conf.main_pos] == majority:
                new = reduce(xor, (temp[i] for i in conf.takt_pos))

                temp[1:] = temp[:-1]
                temp[0] = new
                keystream_xor.append(temp[conf.takt_pos[0]])

        keystream.append(reduce(xor, keystream_xor))

        keystream_xor.clear()
    return keystream


# Example of 64-bit key: 0101001000011010110001110001100100101001000000110111111010110111


def main():

    from ..utils.test import test_crypt

    crypter = Crypter(REGS_CONF)
    test_crypt(crypter.enc, crypter.dec)

if __name__ == "__main__":
    main()
