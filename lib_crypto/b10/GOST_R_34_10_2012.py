from pygost.gost3410 import GOST3410Curve, sign, verify
from pygost.utils import bytes2long, hexdec, hexenc

from lib_crypto.utils.def_str import clear_text, is_hex
from lib_crypto.utils.hash import hash as h
from lib_crypto.utils.print import print_header, print_kv


def get_hash(msg_or_hash):
    if is_hex(msg_or_hash):
        msg_hash = hexdec(msg_or_hash)
    else:
        msg_hash = bytes(h(clear_text(msg_or_hash)))
    return msg_hash


def gen_ecp(curve: GOST3410Curve, d: str, msg_or_hash: str, k: str) -> str:
    msg_hash = get_hash(msg_or_hash)
    d = bytes2long(hexdec(d))  # prv
    k = hexdec(k)  # rand
    return hexenc(sign(curve, d, msg_hash, k))


def check_ecp(
    curve: GOST3410Curve,
    x_point_public: str,
    y_point_public: str,
    msg_or_hash: str,
    ecp: str,
) -> bool:
    x, y = x_point_public, y_point_public
    x, y = bytes2long(hexdec(x)), bytes2long(hexdec(y))
    msg_hash = get_hash(msg_or_hash)
    ecp = hexdec(ecp)
    return verify(curve, (x, y), msg_hash, ecp)


def main():
    from ..utils.data import text_1000

    curve = GOST3410Curve(
        p=bytes2long(hexdec("8000000000000000000000000000000000000000000000000000000000000431")),
        q=bytes2long(hexdec("8000000000000000000000000000000150FE8A1892976154C59CFC193ACCF5B3")),
        a=bytes2long(hexdec("0000000000000000000000000000000000000000000000000000000000000007")),
        b=bytes2long(hexdec("5FBFF498AA938CE739B8E022FBAFEF40563F6E6A3472FC2A514C0CE9DAE23B7E")),
        x=bytes2long(hexdec("0000000000000000000000000000000000000000000000000000000000000002")),
        y=bytes2long(hexdec("08E2A8A0E65147D4BD6316030E16D19C85C97F0A9CA267122B96ABBCEA7E8FC8")),
    )  # fmt: skip

    d = "7A929ADE789BB9BE10ED359DD39A72C11B60961F49397EEE1D19CE9891EC3B28"
    e = "2DFBC1B372D89A1188C09C52E0EEC61FCE52032AB1022E8E67ECE6672B043EE5"
    k = "77105C9B20BCD3122823C8CF6FCC7B956DE33814E95B7FE64FED924594DCEAB3"

    ecp = gen_ecp(curve, d, e, k)

    print_header("Пример из ГОСТ")

    print_kv("Подпись", ecp)

    Qx = "7F2B49E270DB6D90D8595BEC458B50C58585BA1D4E9B788F6689DBD8E56FD80B"
    Qy = "26F1B489D6701DD185C8413A977B3CBBAF64D1C593D26627DFFB101A87FF77DA"

    check = check_ecp(curve, Qx, Qy, e, ecp)

    print_kv("Проверка", check)

    print_header("Подпись 1000")

    ecp = gen_ecp(curve, d, text_1000, k)
    check = check_ecp(curve, Qx, Qy, text_1000, ecp)

    print_kv("Подпись", ecp)
    print_kv("Проверка", check)


if __name__ == "__main__":
    main()
