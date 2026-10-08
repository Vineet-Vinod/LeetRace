import random

DOMAIN_SIZE = 682


def generate(seed: int = 0) -> list[str]:
    random.Random(seed)
    calls: dict[str, None] = {}

    def add(mat):
        assert 1 <= len(mat) <= 3 and 1 <= len(mat[0]) <= 3
        assert all(len(r) == len(mat[0]) and all(v in (0, 1) for v in r) for r in mat)
        call = (
            "candidate("
            + ", ".join(f"{name}={value!r}" for name, value in (("mat", mat),))
            + ")"
        )
        calls[call] = None

    add(mat=[[0, 0], [0, 1]])
    add(mat=[[0]])
    add(mat=[[1, 0, 0], [1, 0, 0]])
    for rows in range(1, 4):
        for cols in range(1, 4):
            for mask in range(1 << (rows * cols)):
                add(
                    mat=[
                        [(mask >> (r * cols + c)) & 1 for c in range(cols)]
                        for r in range(rows)
                    ]
                )
    return list(calls)
