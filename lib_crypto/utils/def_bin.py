from typing import List

from pygost.utils import hexdec, hexenc

from .def_str import is_hex


def to_binary(plain: str) -> List[int]:
    """Converts plaintext to binary"""

    binary = [
        int(i)
        for i in "".join(block[2:] for block in map(bin, bytearray(plain, "utf-8")))
    ]

    return binary


def bin_to_str(
    bits: str, encoding: str = "UTF-8", errors: str = "surrogatepass"
) -> str:
    """Converts binary to string."""

    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode(encoding, errors) or "\0"


def str_to_bytes(text: str) -> bytes:

    if is_hex(text):
        b_text = hexdec(text)
    else:
        b_text = bytes(text, "utf-8")

    return b_text


def bytes_to_str(b_text: bytes, _return: str = "str") -> str:

    if _return == "str":
        text = b_text.decode("utf-8")
    else:

        text = hexenc(b_text)
    return text


def count_bits_in_num(num):
    binary = bin(num)[2:]
    return len(binary)
