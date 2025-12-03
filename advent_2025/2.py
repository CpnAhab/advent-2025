from .util import import_text
from pydantic import BaseModel


class IdRange(BaseModel):
    start: int
    end: int

    def as_range(self) -> range:
        return range(self.start, self.end+1)
    

def check_range(r: range, p_two: bool = False) -> set[int]:
    invalid_set = set()
    for n in r:
        m = str(n)
        if p_two:
            if (w := brute_force(m)):
                invalid_set.add(w)
        else:
            a, b = m[:len(m)//2], m[len(m)//2:]
            if a == b:
                invalid_set.add(n)
    return invalid_set


def brute_force(n: str) -> int | None:
    for i in range(1,len(n)//2+1):
        substrings = set(n[j:j+i] for j in range(0,len(n),i))
        if len(substrings) == 1:
            return int(n)
    return None
    

def part_one(input_text: list[str]) -> None:
    range_list = [IdRange(start=int(i[0]), end=int(i[1])) for i in [j.split("-") for j in input_text[0].split(",")]]
    invalids = set()
    for r in range_list:
        invalids.update(check_range(r.as_range()))
    print(f"part one: {sum(invalids)}")


def part_two(input_text: list[str]) -> None:
    range_list = [IdRange(start=int(i[0]), end=int(i[1])) for i in [j.split("-") for j in input_text[0].split(",")]]
    invalids = set()
    for r in range_list:
        invalids.update(check_range(r.as_range(), p_two=True))
    print(f"part two: {sum(invalids)}")


if __name__ == "__main__":
    input_text = import_text("inputs/input_2.txt")
    part_one(input_text)
    part_two(input_text)