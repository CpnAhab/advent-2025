from .util import import_text
import math


def format_input(input_text: list[str]) -> list[tuple[int, int, int]]:
    return [tuple(map(int, l.split(","))) for l in input_text]


def part_one(coord_pairs: list[tuple[int, int, int]]) -> None:
    print(f"chugga chugga")
    coord_distances = {math.dist(c, d): {c, d} for c in coord_pairs for d in coord_pairs}
    circuits = 1000
    circuit_list = []
    for k, cp in sorted(coord_distances.items(), key=lambda x: x[0])[:circuits+1][1:]:
        p, q = cp
        included = None
        for i, c in enumerate(circuit_list):
            if (p in c) or (q in c):
                if included:
                    circuit_list[included].update(circuit_list.pop(i))
                    break
                c.update({p, q})
                included = i

        if included is None:
            circuit_list.append({p, q})
    print(f"part one: {math.prod([len(c) for c in sorted(circuit_list, key=lambda y: len(y), reverse=True)[:3]])}")


def part_two(coord_pairs: list[tuple[int, int, int]]) -> None:
    coord_distances = {math.dist(c, d): {c, d} for c in coord_pairs for d in coord_pairs}
    circuit_list = []
    for k, cp in sorted(coord_distances.items(), key=lambda x: x[0])[1:]:
        p, q = cp
        included = None
        for i, c in enumerate(circuit_list):
            if (p in c) or (q in c):
                if included is not None:
                    circuit_list[included].update(circuit_list.pop(i))
                    break
                c.update({p, q})
                included = i
    
        if included is None:
            circuit_list.append({p, q})

        if len(circuit_list[0]) == len(coord_pairs):
            print(p, q)
            print(f"part two: {p[0] * q[0]}")
            break


if __name__ == "__main__":
    input_text = import_text("inputs/input_8.txt")
    input_text = format_input(input_text)
    part_one(input_text)
    part_two(input_text)