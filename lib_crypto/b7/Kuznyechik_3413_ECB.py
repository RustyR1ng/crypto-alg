from pygost.gost3412 import KEYSIZE
from pygost.gost3412 import GOST3412Kuznechik as Crypter
from pygost.gost3413 import ecb_decrypt, ecb_encrypt, pad2, unpad2
from pygost.utils import hexdec, hexenc

from ..utils.def_bin import bytes_to_str, str_to_bytes
from ..utils.printing import *

HEX_KEY = "8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef"
BLOCK_SIZE = Crypter.blocksize


def get_key(key: str) -> bytes:
    key_bytes = str_to_bytes(key)
    assert len(key_bytes) == KEYSIZE
    return key_bytes


def encrypter(key: str = HEX_KEY):
    key_bytes = get_key(key)
    return Crypter(key_bytes).encrypt


def decrypter(key: str = HEX_KEY):
    key_bytes = get_key(key)
    return Crypter(key_bytes).decrypt


def get_text(text: str) -> bytes:

    b_text = str_to_bytes(text)
    if len(b_text) % BLOCK_SIZE != 0:
        b_text = pad2(b_text, BLOCK_SIZE)

    return b_text


def enc(text: str, key: str = HEX_KEY) -> str:
    b_text = get_text(text)
    enc_bytes = ecb_encrypt(encrypter(key), BLOCK_SIZE, b_text)

    return hexenc(enc_bytes)


def dec(text: str, key: str = HEX_KEY, _return: str = "str") -> str:

    b_text = hexdec(text)

    dec_bytes = ecb_decrypt(decrypter(key), BLOCK_SIZE, b_text)
    try:
        return bytes_to_str(unpad2(dec_bytes, BLOCK_SIZE), _return)
    except ValueError:
        return bytes_to_str(dec_bytes, _return)


def main():
    from ..tests.test import test_crypt

    print_header("Примеры из GOST_R_34_13-2015")
    print_kv("Ключ", HEX_KEY)
    plain_enc_dict = {
        "1122334455667700ffeeddccbbaa9988": "7f679d90bebc24305a468d42b9d4edcd",
        "00112233445566778899aabbcceeff0a": "b429912c6e0032f9285452d76718d08b",
        "112233445566778899aabbcceeff0a00": "f0ca33549d247ceef3f5a5313bd4b157",
        "2233445566778899aabbcceeff0a0011": "d0b09ccde830b9eb3a02c4c5aa8ada98",
    }  # открытый текст - шифр
    for i, (k, v) in enumerate(plain_enc_dict.items()):
        print_kv(i + 1, f"{k} -> {v}")
    for k, v in plain_enc_dict.items():
        enc_text = enc(k)

        print_kv("Шифр", enc_text)
        try:
            dec_text = dec(enc_text, _return="hex")
            print_kv("Расшифр.", dec_text)
        except:
            pass
    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
