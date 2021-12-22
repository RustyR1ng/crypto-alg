from pygost.gost3412 import GOST3412Magma
from pygost.utils import hexdec, hexenc


def encrypt(text: str, key: str) -> str:
    text, key = hexdec(text), hexdec(key)
    crypter = GOST3412Magma(key)
    return hexenc(crypter.encrypt(text))


def decrypt(text: str, key: str) -> str:
    text, key = hexdec(text), hexdec(key)
    crypter = GOST3412Magma(key)
    return hexenc(crypter.decrypt(text))


def main():
    from ..utils.printing import print_header, print_kv

    print_header("Пример из ГОСТ Р 34.12-2015")

    m = "fedcba9876543210"
    key = "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"

    enc = encrypt(m, key)
    dec = decrypt(enc, key)

    print_kv("Сообщение", m)
    print_kv("Ключ", key)
    print_kv("Шифровка", enc)
    print_kv("Расшифровка", dec)


if __name__ == "__main__":
    main()
