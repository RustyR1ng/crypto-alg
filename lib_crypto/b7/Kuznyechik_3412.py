from pygost.gost3412 import GOST3412Kuznechik as Kuz
from pygost.utils import hexdec, hexenc

from ..utils.def_str import to_indexes, to_symbols, clear_text, is_hex
from ..utils.print import *

key = "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"


def get_key(key: str) -> bytes:
    if is_hex(key):
        key = hexdec(key)
    else:
        key = bytes(key, "utf-8")
    return key


def get_text(text: str) -> bytes:
    if type(text) == str:
        if is_hex(text):
            text = hexdec(text)
        else:
            text = bytes(text, "utf-8")
    return text


def get_chipher(key: str) -> Kuz:
    key = get_key(key)
    return Kuz(key)


def enc(text: str, key: str = key):

    chipher = get_chipher(key)

    byte_text = get_text(text)
    enc_bytes = chipher.encrypt(byte_text)

    enc_text = hexenc(enc_bytes)

    return enc_text


def dec(text: str, key: str = key, t: str = "str"):

    chipher = get_chipher(key)
    byte_text = get_text(text)
    dec_bytes = chipher.decrypt(byte_text)
    dec_text = ""

    if t == "hex":
        dec_text = hexenc(dec_bytes)

    else:
        dec_text = dec_bytes.decode("utf-8")

    return dec_text


def main():
    print_header("Пример из GOST_R_34_12-2015")
    text_example = "1122334455667700ffeeddccbbaa9988"
    enc_example = "7f679d90bebc24305a468d42b9d4edcd"

    key = "8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef"
    print_kv("Открытый текст", text_example)
    print_kv("Результат", enc_example)

    enc_text = enc(text_example, key)
    print_kv("Шифр", enc_text)

    dec_text = dec(enc_example, key, t="hex")
    print_kv("Расшифр.", dec_text)


if __name__ == "__main__":
    main()
