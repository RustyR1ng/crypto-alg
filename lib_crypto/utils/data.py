from os import path

basedir = path.abspath(path.dirname(__file__))


def get_text():
    text_1000 = ""
    with open(path.join(basedir, "1000.txt"), "r", encoding="utf-8") as stream:
        text_1000 = stream.read()

    return text_1000


text_1000 = get_text()


text_test = "Тот зпт кто хочет есть яйца зпт должен примириться с кудахтаньем тчк"


alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

grid_kardano = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
]

if __name__ == "__main__":
    print(text_1000)
