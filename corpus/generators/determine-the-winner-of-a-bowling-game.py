import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Equal length 1..1000 arrays of pin counts in [0,10]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 40)
        a = tuple(rng.randint(0, 10) for _ in range(n))
        b = tuple(rng.randint(0, 10) for _ in range(n))
        cases.add((a, b))
    generated_calls = [
        f"candidate(player1={list(a)!r}, player2={list(b)!r})" for a, b in cases
    ]
    example_calls = [
        "candidate(player1=[5, 10, 3, 2], player2=[6, 5, 7, 3])",
        "candidate(player1=[3, 5, 7, 6], player2=[8, 10, 10, 2])",
        "candidate(player1=[2, 3], player2=[4, 1])",
        "candidate(player1=[1, 1, 1, 10, 10, 10, 10], player2=[10, 10, 10, 10, 1, 1, 1])",
    ]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
