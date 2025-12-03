from .util import import_text
from pydantic import BaseModel


class BatteryBank(BaseModel):
    batteries: list[int]

    def find_max_joltage(self) -> int:
        first_digit, second_digit = -1, -1
        for pos, bat in enumerate(self.batteries):
            if bat > first_digit and pos < len(self.batteries)-1:
                first_digit = bat
                second_digit = -1
                continue
            elif bat > second_digit:
                second_digit = bat
        return int(f"{first_digit}{second_digit}")
    
    def find_twelve_bat_joltage(self, size: int = 12) -> int:
        max_joltage_bat = self.batteries[:size] # start with first 12
        for bat in self.batteries[size:]:
            max_joltage_bat.append(bat)
            if len(set(max_joltage_bat)) == 1:
                max_joltage_bat.pop()
                continue
            prev_val = 10
            for pos, val in enumerate(max_joltage_bat):
                if val > prev_val:
                    max_joltage_bat.pop(pos-1)
                    break
                prev_val = val
            if len(max_joltage_bat) > 12:
                max_joltage_bat.pop()
        return int("".join([str(b) for b in max_joltage_bat]))

def part_one(input_text: list[BatteryBank]):
    print(f"part_one: {sum([b.find_max_joltage() for b in input_text])}")


def part_two(input_text: list[BatteryBank]):
    print(f"part two: {sum([b.find_twelve_bat_joltage() for b in input_text])}")


if __name__ == "__main__":
    input_text = import_text("inputs/input_3.txt")
    input_text = [BatteryBank(batteries=[int(j) for j in row.strip()]) for row in input_text]
    part_one(input_text)
    part_two(input_text)