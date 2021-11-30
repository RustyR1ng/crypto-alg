import numpy as np
from ..utils.data import alph, grid_kardano
from ..utils.def_str import to_indexes, to_symbols, clear_text


def paste_values(text, template_grid, grid):
    indexes = np.argwhere(template_grid == 1)

    for row, col in indexes:
        grid[row][col] = text[0] if len(text) > 0 else "а"
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


def fill_grid(text, template_grid, grid):

    for template in get_templates(template_grid):
        grid, text = paste_values(text, template, grid)

    return grid


def enc(text, alph=alph, template_grid=grid_kardano, **kwargs):
    text = clear_text(text, alph)
    template_grid = np.array(template_grid)

    result = np.full(template_grid.shape, " ")

    result = fill_grid(text, template_grid, result)
    result = " ".join(["".join(row) for row in result])

    return result


def get_text(grid, template_grid):
    indexes = np.argwhere(template_grid == 1)
    text = ""
    for row, col in indexes:
        text += grid[row][col]
    return text


def dec(grid, alph=alph, template_grid=grid_kardano, **kwargs):
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
