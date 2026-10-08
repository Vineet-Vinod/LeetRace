import random
import string

_STATEMENT_EXAMPLES = (
    "candidate(name='alex', typed='aaleex')",
    "candidate(name='saeed', typed='ssaaedd')",
)


def generate(seed: int = 0) -> list[str]:
    """Create 300 long-press matches and 300 guaranteed failures within length bounds."""
    rng = random.Random(seed)
    boundary_name = "a" * 1000
    calls = [f"candidate(name={boundary_name!r}, typed={boundary_name!r})"]
    seen = set(calls)
    while len(calls) < 600:
        name = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 249))
        )
        matched = "".join(char * rng.randint(1, 4) for char in name)
        if len(calls) % 2:
            variant = (len(calls) // 2) % 3
            if variant == 0:
                replacement = "a" if name[0] != "a" else "b"
                typed = replacement + matched[1:]
            elif variant == 1:
                replacement = "a" if matched[-1] != "a" else "b"
                typed = matched + replacement
            elif len(name) > 1:
                typed = name[:-1]
            else:
                replacement = "a" if name != "a" else "b"
                typed = replacement
        else:
            typed = matched
        call = f"candidate(name={name!r}, typed={typed!r})"
        if call not in seen:
            calls.append(call)
            seen.add(call)
    return calls


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
