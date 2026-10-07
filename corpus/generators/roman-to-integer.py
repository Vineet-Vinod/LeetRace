import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Canonical Roman numerals representing 1..3999."""
    rng = random.Random(seed)

    def roman(n: int) -> str:
        pairs = (
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        )
        out = ""
        for value, symbol in pairs:
            count, n = divmod(n, value)
            out += symbol * count
        return out

    values = set(range(1, 501))
    values.update({999, 944, 1984, 3999})
    while len(values) < 700:
        values.add(rng.randint(1, 3999))
    generated_calls = [f"candidate(s={roman(n)!r})" for n in values]
    example_calls = ["candidate(s='MCMXCIV')"]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
