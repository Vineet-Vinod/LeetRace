import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()

    def balanced_values(values: list[int]) -> list[int | None]:
        size = len(values)
        slots: list[int | None] = [None] * size
        cursor = 0

        def fill(index: int) -> None:
            nonlocal cursor
            if index >= size:
                return
            fill(index * 2 + 1)
            slots[index] = values[cursor]
            cursor += 1
            fill(index * 2 + 2)

        fill(0)
        return slots

    for i in range(600):
        vals1 = sorted(rng.sample(range(-1000, 1001), 1 + rng.randrange(31)))
        vals2 = sorted(rng.sample(range(-1000, 1001), 1 + rng.randrange(31)))
        t = rng.randint(-2000, 2000)
        if i % 2 == 0:
            t = rng.choice(vals1) + rng.choice(vals2)
        first, second = balanced_values(vals1), balanced_values(vals2)
        cases.add(
            f"candidate(root1=tree_node({first!r}), root2=tree_node({second!r}), target={t})"
        )
    return sorted(cases)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(root1=tree_node([0, -10, 10]), root2=tree_node([5, 1, 7, 0, 2]), target=18)",
    "candidate(root1=tree_node([2, 1, 4]), root2=tree_node([1, 0, 3]), target=5)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
