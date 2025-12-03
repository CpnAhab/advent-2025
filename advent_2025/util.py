def import_text(loc: str = "input.txt") -> list[str]:
    with open(loc, "r") as f:
        return f.readlines()