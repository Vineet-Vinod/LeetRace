import random


def generate(seed: int = 0) -> list[str]:
    """For cyclic inputs the tail is connected to a valid node index; other inputs are acyclic."""
    r = random.Random(seed)
    vals = [[], [1], [1, 2], [3, 2, 0, -4]]

    def call(values, pos):
        if pos < 0 or not values:
            return f"candidate(head=list_node({values!r}))"
        tail = "h" + ".next" * (len(values) - 1)
        target = "h" + ".next" * pos
        return f"candidate(head=(lambda h: (setattr({tail}, 'next', {target}), h)[1])(list_node({values!r})))"

    calls = [call(a, -1) for a in vals]
    while len(calls) < 600:
        n = r.randint(0, 80)
        a = [r.randint(-100, 100) for _ in range(n)]
        pos = -1 if n == 0 or r.randrange(2) == 0 else r.randrange(n)
        expression = call(a, pos)
        if expression not in calls:
            calls.append(expression)
    return calls


_BASE_GENERATE = generate
_BOUNDARY_CALLS = []


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]


_values = [0] * 10000
_BOUNDARY_CALLS.append(
    f"candidate(head=(lambda h: (setattr(reduce(lambda node, _: node.next, range({len(_values) - 1}), h), 'next', h), h)[1])(list_node({_values!r})))"
)

_BOUNDARY_CALLS.append(
    "candidate(head=(lambda h: (setattr(h.next, 'next', h), h)[1])(list_node([-100000, 100000])))"
)


_EXAMPLE_CALLS = [
    "candidate(head=(lambda h: (setattr(h.next, 'next', h), h)[1])(list_node([1, 2])))",
    "candidate(head=(lambda h: (setattr(h.next.next.next, 'next', h.next), h)[1])(list_node([3, 2, 0, -4])))",
]

_PREVIOUS_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = _PREVIOUS_GENERATE(seed)
    return calls + [call for call in _EXAMPLE_CALLS if call not in calls]
