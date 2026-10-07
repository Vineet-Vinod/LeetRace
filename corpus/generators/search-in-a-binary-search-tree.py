from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(root=tree_node([4, 2, 7, 1, 3]), val=2)",
    "candidate(root=tree_node([4, 2, 7, 1, 3]), val=5)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add(
        "candidate(root=tree_node([1, None, 2, None, 3, None, 4, None, 5]), val=5)"
    )
    while len(cases) < 600:
        n = rng.randint(1, 50)
        vals = sorted(
            rng.sample(range(1, 100000), n)
        )  # serialize as level-order using a balanced BST

        def bt(lo, hi):
            if lo >= hi:
                return None
            mid = (lo + hi) // 2
            return [vals[mid], bt(lo, mid), bt(mid + 1, hi)]

        # build level order
        root = bt(0, n)
        arr = []
        q = [root]
        while q:
            z = q.pop(0)
            if z is None:
                arr.append(None)
            else:
                arr.append(z[0])
                q.extend(z[1:])
        while arr and arr[-1] is None:
            arr.pop()
        target = rng.choice(vals + [100001])
        call = f"candidate(root=tree_node({arr!r}), val={target})"
        cases.add(call)
    return sorted(cases)
