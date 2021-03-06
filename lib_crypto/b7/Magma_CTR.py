from pygost.gost3412 import GOST3412Magma as Magma
from pygost.gost3413 import ctr
from pygost.utils import hexdec, hexenc

from ..utils.def_bin import bytes_to_str, str_to_bytes


def ctr_encrypt(text: str, key: str, iv: str) -> str:
    key, iv = hexdec(key), hexdec(iv)
    crypter = Magma(key)
    text = str_to_bytes(text)

    res = ctr(crypter.encrypt, crypter.blocksize, text, iv)

    return hexenc(res)


def ctr_decrypt(text: str, key: str, iv: str, _return="str") -> str:
    key, iv, text = hexdec(key), hexdec(iv), hexdec(text)
    crypter = Magma(key)

    res = ctr(crypter.encrypt, crypter.blocksize, text, iv)

    return bytes_to_str(res, _return)


def main():
    from ..data import text_1000
    from ..utils.printing import print_header, print_kv

    key = "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"
    IV = "12345678"

    plaintext = "92def06b3c130a59"
    plaintext += "db54c704f8189d20"
    plaintext += "4a98fb2e67a8024c"
    plaintext += "8912409b17b57e41"

    print_header("Тест ГОСТ гаммирование")

    enc = ctr_encrypt(plaintext, key, IV)
    dec = ctr_decrypt(enc, key, IV, "hex")

    print_kv("Шифр", enc)
    print_kv("Расшифровка", dec)

    print_header("Тест на 1000")
    enc = ctr_encrypt(text_1000, key, IV)
    dec = ctr_decrypt(enc, key, IV)

    print_kv("Шифр 1000", enc)
    print_kv("Расшифровка", dec)


if __name__ == "__main__":
    main()
