def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    names = [f"{chr(97 + index // 26)}{chr(97 + index % 26)}" for index in range(70)]
    max_names = []
    max_times = []
    for index, name in enumerate(names):
        amount = 1429 if index < 40 else 1428
        for minute in range(amount):
            max_names.append(name)
            max_times.append(f"{minute // 60:02d}:{minute % 60:02d}")
    cases = {
        "candidate(keyName=['a','a','a'],keyTime=['00:00','00:30','01:00'])",
        "candidate(keyName=['late','late','late'],keyTime=['23:00','23:30','23:59'])",
        f"candidate(keyName={max_names!r},keyTime={max_times!r})",
    }
    while len(cases) < 600:
        if rng.random() < 0.5:
            name = f"u{rng.randrange(7)}"
            start = rng.randrange(1380)
            minutes = [start, start + 20, start + 40]
            key_names = [name] * 3
            key_times = [f"{minute // 60:02d}:{minute % 60:02d}" for minute in minutes]
            used = set(zip(key_names, key_times))
            for _ in range(rng.randint(0, 12)):
                while True:
                    extra_name = f"u{rng.randrange(7)}"
                    minute = rng.randrange(1440)
                    extra_time = f"{minute // 60:02d}:{minute % 60:02d}"
                    if (extra_name, extra_time) not in used:
                        used.add((extra_name, extra_time))
                        break
                key_names.append(extra_name)
                key_times.append(extra_time)
        else:
            key_names = [f"u{index}" for index in range(rng.randint(1, 20))]
            minutes = [rng.randrange(1440) for _ in key_names]
            key_times = [f"{minute // 60:02d}:{minute % 60:02d}" for minute in minutes]
        assert 1 <= len(key_names) == len(key_times) <= 100000
        assert len(set(zip(key_names, key_times))) == len(key_names)
        cases.add(f"candidate(keyName={key_names!r},keyTime={key_times!r})")
    return sorted(cases)
