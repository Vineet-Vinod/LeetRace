import random

_STATEMENT_EXAMPLES = ("candidate(x=121)", "candidate(x=-121)", "candidate(x=10)")


def generate(seed: int = 0) -> list[str]:
    """Mix positive palindrome integers with negative and non-palindrome values."""
    rng = random.Random(seed)
    palindromes: set[int] = set(range(10))
    for number in range(1, 300):
        digits = str(number)
        palindromes.add(int(digits + digits[-2::-1]))
    palindromes = {value for value in palindromes if value <= 2**31 - 1}
    false_values = {-value for value in range(1, 301) if value != 121}
    false_values.add(10)
    true_values = sorted(palindromes)[:300]
    false_list = sorted(false_values)[:300]
    rng.shuffle(true_values)
    rng.shuffle(false_list)
    return [f"candidate(x={value})" for value in true_values[:300] + false_list[:300]]


_BASE_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = list(_STATEMENT_EXAMPLES)
    seen = set(calls)
    for call in _BASE_GENERATE(seed):
        if call not in seen:
            calls.append(call)
            seen.add(call)
    limit = globals().get("DOMAIN_SIZE", 600)
    if len(calls) < limit:
        raise ValueError("Generator did not produce enough distinct cases")
    return calls[:limit]
