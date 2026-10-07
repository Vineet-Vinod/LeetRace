"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(800):
        items = [
            [
                r.choice("abcdefghijklmnopqrstuvwxyz"),
                r.choice("abcdefghijklmnopqrstuvwxyz"),
                r.choice("abcdefghijklmnopqrstuvwxyz"),
            ]
            for _ in range(r.randint(1, 30))
        ]
        key = r.choice(["type", "color", "name"])
        val = r.choice("abcdefghijklmnopqrstuvwxyz")
        cases.add(f"candidate(items={items!r}, ruleKey={key!r}, ruleValue={val!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        [
            "candidate(items=[['type', 'color', 'name']] * 10000, ruleKey='type', ruleValue='type')"
        ]
    )
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(items=[['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone']], ruleKey='color', ruleValue='silver')",
            "candidate(items=[['phone', 'blue', 'pixel'], ['computer', 'silver', 'phone'], ['phone', 'gold', 'iphone']], ruleKey='type', ruleValue='phone')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
