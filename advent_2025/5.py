from .util import import_text
from pydantic import BaseModel


class Ingredient(BaseModel):
    fresh_ids: list
    object_id: int

    def is_fresh(self):
        return any(self.object_id in r for r in self.fresh_ids)


def sum_ranges(fresh_ids: list[range]) -> int:
    clean_ranges = []
    curr_range = None
    for id_range in fresh_ids:
        if not curr_range:
            curr_range = id_range
            continue
        if id_range.start <= curr_range.stop:
            curr_range = range(curr_range.start, max(id_range.stop, curr_range.stop))
        else:
            clean_ranges.append(curr_range)
            curr_range = id_range
    clean_ranges.append(curr_range)
    return sum(len(c) for c in clean_ranges)
                

def process_text(input_text: list[str]) -> list[Ingredient]:
    text_broken = False
    fresh_ids = []
    ingredients = []
    for l in input_text:
        if not l.strip():
            text_broken = True
            continue
        if not text_broken:
            bot, top = (int(i) for i in l.split("-"))
            fresh_ids.append((range(bot, top+1)))
        if text_broken:
            ingredients.append(Ingredient(fresh_ids=fresh_ids, object_id=int(l)))
    return ingredients


def part_one(object_list: list[Ingredient]) -> None:
    print(f"part_one: {sum(i.is_fresh() for i in object_list)}")


def part_two(object_list: list[Ingredient]) -> None:
    sorted_ids = object_list[0].fresh_ids
    sorted_ids.sort(key=lambda x: x.start)
    print(f"part_two: {sum_ranges(sorted_ids)}")


if __name__ == "__main__":
    input_text = import_text("inputs/input_5.txt")
    input_text = process_text(input_text)
    part_one(input_text)
    part_two(input_text)