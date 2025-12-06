from .util import import_text
from pydantic import BaseModel
import math
import re


class MathRow(BaseModel):
    numbers: list[int]


class MathRowStr(BaseModel):
    numbers: list[str]


class OpRow(BaseModel):
    operations: list[str]

    def perform_ops(self, mr: list[MathRow]) -> int:
        total = 0
        for i in range(len(self.operations)):
            current_op = [m.numbers[i] for m in mr]
            if self.operations[i] == "+":
                total += sum(current_op)
            elif self.operations[i] == "*":
                total += math.prod(current_op)
            else:
                print(f"FUCKED UP SHIT HAPPENING")
        return total
    
    def perform_p2_ops(self, mr: list[MathRow]) -> int:
        total = 0
        for i, op in enumerate(self.operations):
            if op == "+":
                total += sum(mr[i].numbers)
            elif op == "*":
                total += math.prod(mr[i].numbers)
            else:
                print("oop")
        return total


def format_input(input_text: list[str]) -> tuple[list[MathRow], OpRow]:
    math_rows = []
    for i in input_text:
        line = i.split()
        try:
            int(line[0])
            math_rows.append(MathRow(numbers=[int(n) for n in line]))
        except:
            return math_rows, OpRow(operations=line)
    print(F"FUCKED UP SHIT TWO")        


def part_one(math_rows: list[MathRow], op_row: OpRow) -> None:
    print(f"part one: {op_row.perform_ops(math_rows)}")


def part_two(math_rows: list[MathRowStr], op_row: OpRow) -> None:
    total = 0
    for col in range(len(math_rows[0].numbers)):
        new_elements = []
        col_elements = [list(m.numbers[col]) for m in math_rows]
        while any(col_elements):
            new_num = ""
            for c in col_elements:
                try:
                    if (popped_char := c.pop(0)):
                        new_num += popped_char
                except:
                    continue
            try:
                new_elements.append(int(new_num))
            except ValueError:
                # Sometimes all ' '
                continue
        if op_row.operations[col] == "+":
            total += sum(new_elements)
        elif op_row.operations[col] == "*":
            total += math.prod(new_elements)
        else:
            print("oop")
    print(f"part two: {total}")


if __name__ == "__main__":
    input_text = import_text()
    input_text = [i.strip("\n") for i in input_text]
    math_rows, op_row = format_input(input_text)
    part_one(math_rows, op_row)
    prev_i = 0
    part_two_rows = []
    for _ in range(len(input_text)-1):
        part_two_rows.append([])
    for i in range(len(input_text[0])):
        if any([row[i] != ' ' for row in input_text[:-1]]):
            continue
        for j in range(len(input_text[:-1])):
            part_two_rows[j].append(input_text[j][prev_i:i])
        prev_i = i+1
    for k in range(len(input_text[:-1])):
        part_two_rows[k].append(input_text[k][prev_i:])
    part_two_lists = [MathRowStr(numbers=l) for l in part_two_rows]
    part_two(part_two_lists, op_row)
