import random


def as_ip(address: int) -> str:
    return ".".join(str((address >> shift) & 255) for shift in (24, 16, 8, 0))


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: valid IPv4 and n1..1000; generated addresses leave enough valid IPv4 range."""
    rng = random.Random(seed)
    calls = {"candidate(ip='255.0.0.7', n=10)", "candidate(ip='117.145.102.62', n=8)"}
    while len(calls) < 600:
        count = rng.randint(1, 1000)
        address = rng.randint(0, (1 << 32) - count)
        calls.add(f"candidate(ip={as_ip(address)!r}, n={count})")
    return sorted(calls)
