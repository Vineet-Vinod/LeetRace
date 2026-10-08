import ast
import random


_MAX_SIZE = 30_000
_MAX_VALUE = 2**31 - 1


def generate(seed: int = 0) -> list[str]:
    """Greed and cookie arrays satisfy the original independent length and value bounds."""
    rng = random.Random(seed)
    cases = {
        "candidate(g=[1, 2, 3], s=[1, 1])",
        "candidate(g=[1, 2], s=[1, 2, 3])",
        "candidate(g=[1], s=[])",
        "candidate(g=[1], s=[1])",
        "candidate(g=[2, 2, 3], s=[1, 2, 3])",
    }
    while len(cases) < 600:
        greed = [rng.randint(1, 100) for _ in range(rng.randint(1, 30))]
        cookies = [rng.randint(1, 100) for _ in range(rng.randint(0, 30))]
        cases.add(f"candidate(g={greed!r}, s={cookies!r})")

    cases.update(
        {
            f"candidate(g={[1] * _MAX_SIZE!r}, s={[1] * _MAX_SIZE!r})",
            f"candidate(g={[1] * _MAX_SIZE!r}, s=[])",
            f"candidate(g={[_MAX_VALUE]!r}, s={[_MAX_VALUE]!r})",
            f"candidate(g={[1, _MAX_VALUE]!r}, s={[1, _MAX_VALUE]!r})",
            f"candidate(g=[1], s={[_MAX_VALUE] * _MAX_SIZE!r})",
        }
    )
    for call in cases:
        keywords = ast.parse(call, mode="eval").body.keywords
        values = {keyword.arg: ast.literal_eval(keyword.value) for keyword in keywords}
        greed = values["g"]
        cookies = values["s"]
        assert 1 <= len(greed) <= _MAX_SIZE
        assert 0 <= len(cookies) <= _MAX_SIZE
        assert all(1 <= value <= _MAX_VALUE for value in greed + cookies)
    return sorted(cases)
