import numpy as np

from ..utils.data import alph, grid_kardano
from ..utils.def_str import REPLACES, clear_text, random_char


def paste_values(text, template_grid, grid, alph=alph):
    indexes = np.argwhere(template_grid == 1)

    for row, col in indexes:
        if grid[row][col] != " ":
            raise ValueError("Введите другую решетку")
        grid[row][col] = text[0] if len(text) > 0 else random_char(alph)
        text = text[1:]
    return grid, text


def get_templates(grid):
    templates = [
        grid,
        np.rot90(grid, 2),
        np.flip(grid, axis=0),
        np.rot90(np.flip(grid, axis=0), 2),
    ]
    return templates


def fill_grid(text, template_grid, grid, alph=alph):

    for template in get_templates(template_grid):
        grid, text = paste_values(text, template, grid, alph)

    return grid


def enc(text, alph=alph, template_grid=grid_kardano, **kwargs):
    size = len(template_grid) * len(template_grid[0])

    assert (
        np.count_nonzero(template_grid) == size // 4
    ), "Количество ячейк должно = (строк*столбцов)/4"

    text = clear_text(text, alph)

    return ",".join(enc_block(text[i : i + size]) for i in range(0, len(text), size))


def enc_block(text, alph=alph, template_grid=grid_kardano, **kwargs):
    text = clear_text(text, alph)
    template_grid = np.array(template_grid)

    result = np.full(template_grid.shape, " ")

    result = fill_grid(text, template_grid, result, alph)
    result = " ".join(["".join(row) for row in result])

    return result


def get_text(grid, template_grid):
    indexes = np.argwhere(template_grid == 1)
    text = ""
    for row, col in indexes:
        text += grid[row][col]
    return text


def dec(grids, alph=alph, template_grid=grid_kardano, **kwarg):
    grids = grids.split(",")
    return "".join(dec_block(grid, alph, template_grid) for grid in grids)


def dec_block(grid, alph=alph, template_grid=grid_kardano, **kwargs):
    grid = [list(row) for row in grid.split()]
    template_grid = np.array(template_grid)

    result = ""
    for template in get_templates(template_grid):
        result += get_text(grid, template)

    return result


def main():
    from ..utils.test import test_crypt

    test_crypt(enc, dec)


if __name__ == "__main__":
    main()
