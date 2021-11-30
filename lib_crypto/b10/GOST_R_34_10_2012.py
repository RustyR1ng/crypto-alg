from pygost.gost3410 import GOST3410Curve, sign, verify
from pygost.utils import hexenc, hexdec, bytes2long


def main():
    curve = GOST3410Curve(
        p=bytes2long(hexdec("8000000000000000000000000000000000000000000000000000000000000431")),
        q=bytes2long(hexdec("8000000000000000000000000000000150FE8A1892976154C59CFC193ACCF5B3")),
        a=bytes2long(hexdec("0000000000000000000000000000000000000000000000000000000000000007")),
        b=bytes2long(hexdec("5FBFF498AA938CE739B8E022FBAFEF40563F6E6A3472FC2A514C0CE9DAE23B7E")),
        x=bytes2long(hexdec("0000000000000000000000000000000000000000000000000000000000000002")),
        y=bytes2long(hexdec("08E2A8A0E65147D4BD6316030E16D19C85C97F0A9CA267122B96ABBCEA7E8FC8")),
    )  # fmt: skip
    d = bytes2long(
        hexdec(
            "7A929ADE789BB9BE10ED359DD39A72C11B60961F49397EEE1D19CE9891EC3B28"
        )  # prv
    )
    e = hexdec(
        "2DFBC1B372D89A1188C09C52E0EEC61FCE52032AB1022E8E67ECE6672B043EE5"
    )  # digest
    k = hexdec(
        "77105C9B20BCD3122823C8CF6FCC7B956DE33814E95B7FE64FED924594DCEAB3"
    )  # rand
    signature = sign(curve, d, e, k)

    print(hexenc(signature))

    # r = "41aa28d2f1ab148280cd9ed56feda41974053554a42767b83ad043fd39dc0493"
    # s = "01456c64ba4642a1653c235a98a60249bcd6d3f746b631df928014f6c5bf9c40"

    Qx = bytes2long(
        hexdec("7F2B49E270DB6D90D8595BEC458B50C58585BA1D4E9B788F6689DBD8E56FD80B")
    )
    Qy = bytes2long(
        hexdec("26F1B489D6701DD185C8413A977B3CBBAF64D1C593D26627DFFB101A87FF77DA")
    )
    check = verify(curve, (Qx, Qy), e, signature)
    print(check)


if __name__ == "__main__":
    main()
