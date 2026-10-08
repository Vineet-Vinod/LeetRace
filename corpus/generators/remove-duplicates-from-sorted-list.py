from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(head=list_node([1, 1, 2]))",
    "candidate(head=list_node([1, 1, 2, 3, 3]))",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    pid = "remove-duplicates-from-sorted-list"
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(head=list_node([1]*300))")
    cases.add("candidate(head=list_node([1]*300))")
    cases.add("candidate(head=list_node([-100]*150+[100]*150))")
    while len(cases) < 600:
        if pid == "merge-two-sorted-lists":
            a = sorted(rng.randint(-100, 100) for _ in range(rng.randint(0, 25)))
            b = sorted(rng.randint(-100, 100) for _ in range(rng.randint(0, 25)))
            call = f"candidate(list1=list_node({a!r}), list2=list_node({b!r}))"
        else:
            a = sorted(rng.randint(-100, 100) for _ in range(rng.randint(0, 100)))
            call = f"candidate(head=list_node({a!r}))"
        cases.add(call)
    return sorted(cases)
