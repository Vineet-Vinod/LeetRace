def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    letters = string.ascii_letters + string.digits + " "
    cases = {
        'candidate(input="dir\\n\\tsubdir1\\n\\tsubdir2\\n\\t\\tfile.ext")',
        'candidate(input="dir\\n\\tsubdir\\n\\t\\tfile.txt")',
        'candidate(input="dir\\n\\tsubdir")',
        'candidate(input="dir\\n\\tsubdir1\\n\\t\\tfile1.ext\\n\\t\\tsubsubdir1\\n\\tsubdir2\\n\\t\\tsubsubdir2\\n\\t\\t\\tfile2.ext")',
        'candidate(input="a")',
    }
    while len(cases) < 599:
        entries = []
        directory_stack = []
        for _ in range(rng.randint(1, 30)):
            depth = rng.randint(0, len(directory_stack))
            directory_stack = directory_stack[:depth]
            is_file = rng.random() < 0.35
            name = "".join(rng.choice(letters) for _ in range(rng.randint(1, 8)))
            if is_file:
                name += "." + "".join(
                    rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 4))
                )
            entries.append("\t" * depth + name)
            if not is_file:
                directory_stack.append(name)
        filesystem = "\n".join(entries)
        assert len(filesystem) <= 10000
        cases.add(f"candidate(input={filesystem!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    lines = ["dir"]
    depth = 1
    while True:
        candidate_lines = lines + ["\t" * depth + "file.txt"]
        value = "\n".join(candidate_lines)
        if len(value) > 10000:
            lines.append("\t" * depth + "dir")
            break
        best = (value, depth)
        lines.append("\t" * depth + "dir")
        depth += 1
    value, _ = best
    value = value[:-4] + "a" * (10000 - len(value)) + ".txt"
    assert len(value) == 10000
    boundary = f"candidate(input={value!r})"
    if boundary not in calls:
        calls.append(boundary)
    assert 500 <= len(calls) <= 999
    return calls
