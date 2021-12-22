from pygost.gost3412 import GOST3412Magma
from pygost.gost3413 import ecb_decrypt, ecb_encrypt, pad3, unpad2
from pygost.utils import hexdec, hexenc

from ..utils.def_bin import bytes_to_str, str_to_bytes


def encrypt_ecb(text: str, key: str) -> str:
    text, key = str_to_bytes(text), hexdec(key)
    crypter = GOST3412Magma(key)

    res = ecb_encrypt(crypter.encrypt, crypter.blocksize, pad3(text, crypter.blocksize))

    return hexenc(res)


def decrypt_ecb(text: str, key: str, _return="str") -> str:
    text, key = hexdec(text), hexdec(key)
    crypter = GOST3412Magma(key)

    res = ecb_decrypt(crypter.decrypt, crypter.blocksize, text)

    try:
        return bytes_to_str(unpad2(res, crypter.blocksize), _return)
    except ValueError:
        return bytes_to_str(res, _return)


def main():
    from ..data import text_1000
    from ..utils.printing import print_header, print_kv

    key = "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"
    plaintext = "92def06b3c130a59"
    # plaintext += "db54c704f8189d20"
    # plaintext += "4a98fb2e67a8024c"
    # plaintext += "8912409b17b57e41"

    print_header("Тест ГОСТ режим простой замены")

    enc = encrypt_ecb(plaintext, key)
    dec = decrypt_ecb(enc, key, "hex")

    print_kv("Шифр", enc)
    print_kv("Расшифровка", dec)

    print_header("Тест на 1000")

    enc = encrypt_ecb(text_1000, key)
    dec = decrypt_ecb(enc, key)

    print_kv("Шифр 1000", enc)
    print_kv("Расшифровка", dec)


if __name__ == "__main__":
    main()
