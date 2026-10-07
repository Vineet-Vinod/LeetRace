import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        users = rng.randint(1, 8)
        username, timestamp, website = [], [], []
        time = 1
        for user_id in range(users):
            count = rng.randint(3, 6) if user_id == 0 else rng.randint(1, 6)
            for _ in range(count):
                username.append(f"u{user_id}")
                timestamp.append(time)
                website.append(f"w{rng.randrange(8)}")
                time += rng.randint(1, 3)
        order = list(range(len(username)))
        rng.shuffle(order)
        username = [username[i] for i in order]
        timestamp = [timestamp[i] for i in order]
        website = [website[i] for i in order]
        key = (tuple(username), tuple(timestamp), tuple(website))
        if key not in seen:
            seen.add(key)
            assert len(set(zip(username, timestamp, website))) == len(username)
            assert any(username.count(f"u{i}") >= 3 for i in range(users))
            cases.append(
                f"candidate(username={username!r}, timestamp={timestamp!r}, website={website!r})"
            )
    return cases
