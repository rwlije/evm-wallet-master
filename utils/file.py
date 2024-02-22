def read_lines(path: str, encoding: str = "utf-8"):
    with open(path, encoding=encoding) as f:
        lines = f.readlines()

    lines = list(filter(lambda x: x, [line.rstrip() for line in lines]))

    return lines


def append_line(path: str, line: str):
    with open(path, "a") as file:
        file.write(line + "\n")


def clear_file(path: str):
    with open(path, "w") as file:
        file.truncate(0)