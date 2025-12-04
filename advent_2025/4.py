from .util import import_text
from pydantic import BaseModel
import itertools


# WE ARE CHARLIE KIRK
class RollMap():
    rows: list[list[bool]]
    height: int
    width: int

    def __init__(self, rows, *args, **kwargs):
        self.rows = rows
        self.height = len(rows)-1
        self.width = len(rows[0])-1


    def less_than_four_adjacent(self, row: int, col: int, mod: bool = False) -> bool:
        if not self.rows[row][col]:
            return False
        if (row,col) in [(0,0), (self.height, 0), (self.height, self.width), (0, self.width)]:
            if mod:
                self.rows[row][col] = False
            return True
        count = 0
        for x_offset, y_offset in itertools.product((-1,0,1),(-1,0,1)):
            if (x_offset, y_offset) == (0,0):
                continue
            if 0 > row + y_offset or row + y_offset > self.height or 0 > col + x_offset or col + x_offset > self.width:
                continue
            if self.rows[row+y_offset][col+x_offset]:
                count += 1
            if count >= 4:
                return False
        if mod:
            self.rows[row][col] = False
        return True


# HE CARRIES US ALL
def helper_function(*args, **kwargs) -> any:
    pass


def part_one(input_text: RollMap) -> None:
    count = 0
    for y, row in enumerate(input_text.rows):
        for x, col in enumerate(row):
            if input_text.less_than_four_adjacent(y, x):
                count += 1
    print(f"part one: {count}")


def part_two(input_text: RollMap) -> None:
    total_count = 0
    while True:
        count = 0
        for y, row in enumerate(input_text.rows):
            for x, col in enumerate(row):
                if input_text.less_than_four_adjacent(y, x, mod=True):
                    count += 1
        total_count += count
        if not count:
            break
    print(f"part two: {total_count}")


if __name__ == "__main__":
    input_text = import_text("inputs/input_4.txt")
    input_text = RollMap(rows=[[column=="@" for column in row] for row in input_text])
    part_one(input_text)
    part_two(input_text)