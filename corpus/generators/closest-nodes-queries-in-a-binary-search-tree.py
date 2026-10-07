from __future__ import annotations
import random


def encode(values: list[int]) -> list[int | None]:
    if not values:
        return []
    mid = len(values) // 2
    out: list[int | None] = [values[mid]]
    queue = [(0, values[:mid]), (0, values[mid + 1 :])]
    while queue:
        parent, part = queue.pop(0)
        if not part:
            continue
        mid = len(part) // 2
        part[mid]
        child_index = parent * 2 + (1 if parent == 0 else 0)
        # Constructing arbitrary sparse heap layout is unnecessary; use recursive slots below.
        del child_index

    def put(arr: list[int | None], index: int, part: list[int]) -> None:
        if not part:
            return
        m = len(part) // 2
        while len(arr) <= index:
            arr.append(None)
        arr[index] = part[m]
        put(arr, index * 2 + 1, part[:m])
        put(arr, index * 2 + 2, part[m + 1 :])

    out = []
    put(out, 0, values)
    while out and out[-1] is None:
        out.pop()
    return out


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        size = rng.randint(2, 30)
        vals = sorted(rng.sample(range(1, 1000001), size))
        tree = encode(vals)
        queries = [rng.randint(1, 1000000) for _ in range(rng.randint(1, 25))]
        calls.add(f"candidate(tree_node({tree!r}), queries={queries!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(root=tree_node([4, None, 9]), queries=[3])",
    "candidate(root=tree_node([6, 2, 13, 1, 4, 9, 15, None, None, None, None, None, None, 14]), queries=[2, 5, 16])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
