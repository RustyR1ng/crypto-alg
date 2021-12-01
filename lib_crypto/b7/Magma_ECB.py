from pygost.gost3412 import GOST3412Magma
from pygost.utils import hexdec, hexenc
from pygost.gost3413 import ecb_encrypt, ecb_decrypt, pad2, unpad2


def encrypt_ecb(text: str, key: str) -> str:
    text, key = bytes(text, "utf-8"), hexdec(key)
    crypter = GOST3412Magma(key)

    res = ecb_encrypt(crypter.encrypt, crypter.blocksize, pad2(text, crypter.blocksize))

    return hexenc(res)


def decrypt_ecb(text: str, key: str) -> str:
    text, key = hexdec(text), hexdec(key)
    crypter = GOST3412Magma(key)

    res = ecb_decrypt(crypter.decrypt, crypter.blocksize, text)

    try:
        return unpad2(res, crypter.blocksize).decode()
    except ValueError:
        return res.decode()


def main():
    from ..utils.print import print_header, print_kv
    from ..utils.data import text_test, text_1000

    key = "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"

    print_header("Тест на пословице и 1000")

    enc = encrypt_ecb(text_test, key)
    dec = decrypt_ecb(enc, key)

    print_kv("Шифр пословицы", enc)
    print_kv("Расшифровка", dec)

    enc = encrypt_ecb(text_1000, key)
    dec = decrypt_ecb(enc, key)

    print_kv("Шифр 1000", enc)
    print_kv("Расшифровка", dec)


if __name__ == "__main__":
    main()
