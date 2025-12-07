from .util import import_text
from pydantic import BaseModel
from collections import Counter


class TachyonLayer(BaseModel):
    splitters: list[int]
    total_len: int

    def split_beams(self, beams: list[int]) -> tuple[list[int], int]:
        # Accepts beam locs, returns beam locs and # of splits.
        new_beams = set()
        splits = 0
        for b in beams:
            if b in self.splitters:
                new_beams.update((b+1, b-1))
                splits += 1
            else:
                new_beams.add(b)
        return list(new_beams), splits
    
    def split_beams_ptwo(self, beams: Counter) -> Counter:
        # Accepts # of beams in each column, returns # of beams in each column.
        for pos in range(self.total_len):
            if pos not in self.splitters:
                continue
            if pos-1 in self.splitters:
                # Already changed it, can't be a splitter
                continue
            beams[pos-1] += beams[pos]
            beams[pos+1] += beams[pos]
            beams[pos] = 0
        return beams
    

def format_input(input_text: list[str]) -> tuple[int, list[TachyonLayer]]:
    beam_start = input_text[0].index("S")
    tach_layers = []
    for tl in input_text[1:]:
        split_locs = []
        for loc in range(len(tl)):
            if tl[loc] == "^":
                split_locs.append(loc)
        tach_layers.append(TachyonLayer(splitters=split_locs, total_len=len(tl)))
    return beam_start, tach_layers
    

def part_one(beam_start: int, tach_layers: list[TachyonLayer]) -> None:
    splits = 0
    beams = [beam_start]
    for tl in tach_layers:
        beams, new_splits = tl.split_beams(beams)
        splits += new_splits
    print(f"part one: {splits}")


def part_two(beam_start: int, tach_layers: list[TachyonLayer]) -> None:
    beams = Counter()
    beams[beam_start] = 1
    for tl in tach_layers:
        beams = tl.split_beams_ptwo(beams)
    print(f"part two: {sum(beams[i] for i in range(tl.total_len))}")
    

if __name__ == "__main__":
    input_text = import_text("inputs/input_7.txt")
    beam_start, tach_layers = format_input(input_text)
    part_one(beam_start, tach_layers)
    part_two(beam_start, tach_layers)