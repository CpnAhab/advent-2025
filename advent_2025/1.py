from .util import import_text
from pydantic import BaseModel

DIAL_START = 50

class DialTurn(BaseModel):
    direction: str
    amount: int

    def perform_turn(self) -> int:
        return self.amount if self.direction == "R" else -1*self.amount


def filter_turns(turns: list[str]) -> list[DialTurn]:
    turn_list = []
    for i in turns:
        try:
            d, a = i[0], int(i[1:])
            if d not in ("L", "R"):
                raise
            turn_list.append(DialTurn(direction=d, amount=a))
        except:
            print(f"Issue with line: {i}")
    return turn_list


def part_one(turn_list: list[DialTurn]) -> int:
    # Returns the number of times the dial ends on 0.
    val = DIAL_START
    zeroes = 0
    for t in turn_list:
        val += t.perform_turn()
        if val % 100 == 0:
            zeroes += 1
    return zeroes


def part_two(turn_list: list[DialTurn]) -> int:
    # Returns the number of times the dial crosses 0 during a turn.
    val = DIAL_START
    zeroes = 0
    for t in turn_list:
        zeroes += part_two_logic(val, val + t.perform_turn())
        val = val + t.perform_turn()
        val = val % 100
    return zeroes


def part_two_logic(start: int, end: int) -> int:
    zeroes = 0
    if start > end:
        for n in range(end, start):
            if not n % 100:
                zeroes += 1
        return zeroes
    for n in range(start+1, end+1):
        if not n % 100:
            zeroes += 1
    return zeroes
        
if __name__ == "__main__":
    turns = import_text("inputs/input_1.txt")
    turn_list = filter_turns(turns)
    print(f"part 1: {part_one(turn_list)}")
    print(f"part 2: {part_two(turn_list)}")