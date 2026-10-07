import random


_MAX_EQUATIONS = 20
_MAX_QUERIES = 20


def generate(seed: int = 0) -> list[str]:
    """Each case is a consistent positive-ratio graph with 1..20 equations and queries."""
    rng = random.Random(seed)
    cases = {
        "candidate(equations=[['a', 'b'], ['b', 'c']], values=[2.0, 3.0], queries=[['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']])",
        "candidate(equations=[['a', 'b'], ['b', 'c'], ['bc', 'cd']], values=[1.5, 2.5, 5.0], queries=[['a', 'c'], ['c', 'b'], ['bc', 'cd'], ['cd', 'bc']])",
        "candidate(equations=[['a', 'b']], values=[0.5], queries=[['a', 'b'], ['b', 'a'], ['a', 'c'], ['x', 'y']])",
    }
    while len(cases) < 600:
        edge_count = rng.randint(1, _MAX_EQUATIONS)
        names = [f"v{index}" for index in range(edge_count + 1)]
        equations = [[names[index], names[index + 1]] for index in range(edge_count)]
        values = [rng.randint(1, 20) / rng.randint(1, 5) for _ in range(edge_count)]
        query_count = rng.randint(1, _MAX_QUERIES)
        query_names = names + [f"u{index}" for index in range(3)]
        queries = [
            [rng.choice(query_names), rng.choice(query_names)]
            for _ in range(query_count)
        ]
        call = f"candidate(equations={equations!r}, values={values!r}, queries={queries!r})"
        cases.add(call)

    assert len(cases) == 600
    return sorted(cases)
