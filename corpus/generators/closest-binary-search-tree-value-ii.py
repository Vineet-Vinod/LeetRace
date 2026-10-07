import random
from collections import deque

EXAMPLES = [
    "candidate(root=tree_node([4, 2, 5, 1, 3]), target=3.714286, k=2)",
    "candidate(root=tree_node([1]), target=0.0, k=1)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def balanced(values):
        if not values:
            return None
        mid = len(values) // 2
        return (values[mid], balanced(values[:mid]), balanced(values[mid + 1 :]))

    def level(tree):
        result = []
        queue = deque([tree])
        while queue:
            node = queue.popleft()
            if node is None:
                result.append(None)
            else:
                result.append(node[0])
                queue.extend(node[1:])
        while result and result[-1] is None:
            result.pop()
        return result

    def add(values, target, k):
        assert 1 <= k <= len(values) <= 10000
        assert len(set(values)) == len(values) and all(0 <= v <= 10**9 for v in values)
        assert -(10**9) <= target <= 10**9
        distances = sorted(abs(v - target) for v in values)
        assert k == len(values) or distances[k - 1] < distances[k]
        emit(
            f"candidate(root=tree_node({level(balanced(sorted(values)))!r}), target={target!r}, k={k})"
        )

    add(list(range(10000)), 10**9, 10000)
    add([0, 10**9], -(10**9), 1)
    while len(calls) < 600:
        values = rng.sample(range(1000), rng.randint(1, 35))
        # Non-half-integral fractional targets preclude a tied cutoff between distinct integer keys.
        target = rng.randint(-200, 1200) + 0.125
        add(values, target, rng.randint(1, len(values)))
    return calls
