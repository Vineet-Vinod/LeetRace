def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        f"candidate(cpdomains={['10000 a.b.com'] * 100!r})",
        "candidate(cpdomains=['9001 discuss.leetcode.com'])",
        "candidate(cpdomains=['900 google.mail.com', '50 yahoo.com', '1 intel.mail.com', '5 wiki.org'])",
    }
    while len(cases) < 600:
        entries = []
        for _ in range(rng.randint(1, 20)):
            labels = [
                rng.choice(["a", "b", "x", "site", "mail", "dev"])
                for _ in range(rng.choice([2, 2, 3]))
            ]
            entries.append(f"{rng.randint(1, 10000)} {'.'.join(labels)}")
        assert 1 <= len(entries) <= 100 and all(1 <= len(x) <= 100 for x in entries)
        cases.add(f"candidate(cpdomains={entries!r})")
    return sorted(cases)
