import random


def generate(seed: int = 0) -> list[str]:
    """Generate valid directory listings with simple filenames/content and occasional duplicates."""
    rng = random.Random(seed)
    calls = [
        'candidate(paths=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])',
        'candidate(paths=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"])',
    ]
    seen = set(calls)
    i = 0
    while len(calls) < 600:
        count = 1 + i % 8
        paths = []
        for d in range(count):
            files = []
            for f in range(1 + (i + d) % 5):
                content = (
                    f"c{rng.randrange(1, 12)}"
                    if rng.random() < 0.5
                    else f"unique{i}_{d}_{f}"
                )
                files.append(f"f{f}.txt({content})")
            paths.append(f"root/d{d} " + " ".join(files))
        call = f"candidate(paths={paths!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
