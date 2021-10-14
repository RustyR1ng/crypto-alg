# -*- coding: utf-8 -*-
import re
import copy
import sys


REG_X_LENGTH = 19
REG_Y_LENGTH = 22
REG_Z_LENGTH = 23

key_one = ""
reg_x = []
reg_y = []
reg_z = []


def loading_registers(key):
    """Loads registers using a 64-bit key as a parameter."""

    i = 0
    while i < REG_X_LENGTH:
        reg_x.insert(i, int(key[i]))  # takes first 19 elements from key
        i = i + 1
    j = 0
    p = REG_X_LENGTH
    while j < REG_Y_LENGTH:
        reg_y.insert(j, int(key[p]))  # takes next 22 elements from key
        p = p + 1
        j = j + 1
    k = REG_Y_LENGTH + REG_X_LENGTH
    r = 0
    while r < REG_Z_LENGTH:
        reg_z.insert(r, int(key[k]))  # takes next 23 elements from key
        k = k + 1
        r = r + 1


def set_key(key):
    """Sets the key and loads the registers if it contains 0's and 1's and if it's exactly 64 bits"""

    if len(key) == 64 and re.match("^([01])+", key):
        key_one = key
        loading_registers(key)
        return True
    return False


key = set_key("0101001000011010110001110001100100101001000000110111111010110111")


def get_key():  # gets the key
    return key_one


def to_binary(plain):
    """Converts plaintext to binary"""

    my_bin = [
        int(i)
        for i in "".join(block[2:] for block in map(bin, bytearray(plain, "utf-8")))
    ]

    # print("Text |", plain)
    # print("Binary Code |", my_bin)
    # print("Text |", bin_to_str("".join(str(i) for i in my_bin)))

    return my_bin


def bin_to_str(bits, encoding="UTF-8", errors="surrogatepass"):
    """Converts binary to string."""

    # print("Converting |", bits, type(bits))
    # print(*(bits[i * 8 : i * 8 + 8] for i in range(len(bits) // 8)))

    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode(encoding, errors) or "\0"


def get_majority(x, y, z):
    """
    Gets majority by adding up the x,y,and z values and if it's greater than 1 (e.g. two 1's and one 0), it returns the majority (1). Otherwise, if it's two 0's and one 1, the majority is returned as 0.
    """

    if x + y + z > 1:
        return 1
    else:
        return 0


def get_keystream(length):
    """Calculates the keystream by XOR-ing the appropriate indeces."""

    reg_x_temp = copy.deepcopy(reg_x)
    reg_y_temp = copy.deepcopy(reg_y)
    reg_z_temp = copy.deepcopy(reg_z)
    keystream = []
    i = 0
    while i < length:
        majority = get_majority(reg_x_temp[8], reg_y_temp[10], reg_z_temp[10])
        if reg_x_temp[8] == majority:
            new = reg_x_temp[13] ^ reg_x_temp[16] ^ reg_x_temp[17] ^ reg_x_temp[18]
            reg_x_temp_two = copy.deepcopy(reg_x_temp)
            j = 1
            while j < len(reg_x_temp):
                reg_x_temp[j] = reg_x_temp_two[j - 1]
                j = j + 1
            reg_x_temp[0] = new

        if reg_y_temp[10] == majority:
            new_one = reg_y_temp[20] ^ reg_y_temp[21]
            reg_y_temp_two = copy.deepcopy(reg_y_temp)
            k = 1
            while k < len(reg_y_temp):
                reg_y_temp[k] = reg_y_temp_two[k - 1]
                k = k + 1
            reg_y_temp[0] = new_one

        if reg_z_temp[10] == majority:
            new_two = reg_z_temp[7] ^ reg_z_temp[20] ^ reg_z_temp[21] ^ reg_z_temp[22]
            reg_z_temp_two = copy.deepcopy(reg_z_temp)
            m = 1
            while m < len(reg_z_temp):
                reg_z_temp[m] = reg_z_temp_two[m - 1]
                m = m + 1
            reg_z_temp[0] = new_two

        keystream.insert(i, reg_x_temp[18] ^ reg_y_temp[21] ^ reg_z_temp[22])
        i = i + 1
    return keystream


def enc(plain, key=key):
    """
    Takes in a plaintext, converts it to binary, gets the keystream after inputting the length of the binary, and appends the XOR values of the keystream and binary to a string
    """

    s = ""
    binary = to_binary(plain)
    keystream = get_keystream(len(binary))
    i = 0
    while i < len(binary):
        s = s + str(binary[i] ^ keystream[i])
        i = i + 1
    return s


def dec(cipher, key=key):
    """
    Takes in a cipher, gets the keystream from its length, cipher is XOR'd with keystream, and converted to string
    """

    s = ""
    binary = []
    keystream = get_keystream(len(cipher))
    i = 0
    while i < len(cipher):
        binary.insert(i, int(cipher[i]))
        stroke = str(binary[i] ^ keystream[i])

        s = s + stroke
        i = i + 1
    return bin_to_str(str(s))


# Example of 64-bit key: 0101001000011010110001110001100100101001000000110111111010110111
if __name__ == "__main__":
    from ..utils.test import test_crypt

    test_crypt(enc, dec)
