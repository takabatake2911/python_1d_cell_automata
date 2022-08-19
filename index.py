from typing import List
import unittest


# configurable constants
RULES_DICT = {
    (1, 1, 1): 0,
    (1, 1, 1): 0,
    (1, 1, 0): 1,
    (1, 0, 1): 0,
    (1, 0, 0): 1,
    (0, 1, 1): 0,
    (0, 1, 0): 1,
    (0, 0, 1): 1,
    (0, 0, 0): 0,
}
DEFAULT_DEPTH = 10
WIDTH = 30
DEPTH = 20


def main():
    row = [0] * WIDTH
    row[WIDTH // 2] = 1
    draw_cells_recursive(row, DEPTH)


def next_cell(left: int, curr: int, right: int) -> int:
    return RULES_DICT[(left, curr, right)]


def next_row(row: List[int]) -> List[int]:
    w = len(row)
    tmp = [0] * w
    for i in range(w):
        tmp[i] = next_cell(row[i - 1], row[i], row[(i + 1) % w])
        pass
    return tmp


def conv_row_01_to_sign(row: List[int]) -> List[str]:
    width = len(row)
    tmp: list[str] = [""] * width
    for i in range(width):
        if row[i] == 0:
            tmp[i] = "_"
        else:
            tmp[i] = "#"
    return tmp


class TestNextCell(unittest.TestCase):
    def test_111(self):
        self.assertEqual(next_cell(1, 1, 1), 0)

    def test_110(self):
        self.assertEqual(next_cell(1, 1, 0), 1)

    def test_101(self):
        self.assertEqual(next_cell(1, 0, 1), 0)

    def test_100(self):
        self.assertEqual(next_cell(1, 0, 0), 0)

    def test_011(self):
        self.assertEqual(next_cell(0, 1, 1), 0)

    def test_010(self):
        self.assertEqual(next_cell(0, 1, 0), 1)

    def test_001(self):
        self.assertEqual(next_cell(0, 0, 1), 1)

    def test_000(self):
        self.assertEqual(next_cell(0, 0, 0), 0)


class TestNextRow(unittest.TestCase):
    def test_row1(self):
        self.assertEqual(next_row([1, 1, 1, 0]), [0, 0, 1, 0])

    def test_row2(self):
        self.assertEqual(next_row([1, 1, 1, 0, 0]), [0, 0, 1, 0, 1])


def draw_cells_recursive(row: List[int], depth=DEFAULT_DEPTH) -> None:
    if depth == 0:
        return
    print(*conv_row_01_to_sign(row))
    draw_cells_recursive(next_row(row), depth - 1)


if __name__ == "__main__":
    main()
    # unittest.main()
