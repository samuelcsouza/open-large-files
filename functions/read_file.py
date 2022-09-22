from typing import Iterable


def read_file(file_path: str, skip: int, limit: int) -> Iterable:

    with open(file_path, "r") as _fp:
        col_names = next(_fp).strip().split(",")

        for _ in range(skip):
            next(_fp)

        for i, line in enumerate(_fp):
            if i >= limit:
                break

            line_values = line.strip().split(",")

            observation_dict = dict(zip(col_names, line_values))

            yield observation_dict
