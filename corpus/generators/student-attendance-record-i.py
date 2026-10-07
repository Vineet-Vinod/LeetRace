from __future__ import annotations
import random

# Valid records are built with at most one A and no run of three Ls.
EXAMPLE_CALLS = ["candidate(s='PPALLP')", "candidate(s='PPALLL')"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    valid = {
        "candidate(s='P')",
        "candidate(s='A')",
        "candidate(s='LL')",
        f"candidate(s={'P' * 1000!r})",
        f"candidate(s={'A' + 'P' * 999!r})",
        f"candidate(s={'LL' + 'P' * 998!r})",
        *[call for call in EXAMPLE_CALLS if call.endswith("'PPALLP')")],
    }
    invalid = {
        "candidate(s='AA')",
        "candidate(s='LLL')",
        f"candidate(s={'P' * 998 + 'AA'!r})",
        f"candidate(s={'LLL' + 'P' * 997!r})",
        *[call for call in EXAMPLE_CALLS if call.endswith("'PPALLL')")],
    }

    def make_valid(length: int) -> str:
        record = []
        absences = 0
        late_run = 0
        for _ in range(length):
            options = ["P"]
            if late_run < 2:
                options.append("L")
            if absences == 0:
                options.append("A")
            char = rng.choice(options)
            record.append(char)
            absences += char == "A"
            late_run = late_run + 1 if char == "L" else 0
        return "".join(record)

    while len(valid) < 300:
        length = 1000 if rng.random() < 0.02 else rng.randint(1, 1000)
        valid.add(f"candidate(s={make_valid(length)!r})")

    while len(invalid) < 300:
        length = 1000 if rng.random() < 0.02 else rng.randint(3, 1000)
        if rng.random() < 0.5:
            record = list(make_valid(length))
            first, second = rng.sample(range(length), 2)
            record[first] = "A"
            record[second] = "A"
        else:
            record = list(make_valid(length))
            start = rng.randint(0, length - 3)
            record[start : start + 3] = ["L", "L", "L"]
        invalid.add(f"candidate(s={''.join(record)!r})")

    assert len(valid) == 300 and len(invalid) == 300
    return sorted(valid | invalid)
