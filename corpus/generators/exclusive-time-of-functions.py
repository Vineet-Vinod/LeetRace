import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: n1..100; valid properly nested logs; event times within 0..10^9; generator emits matched nested calls with distinct starts/ends."""
    rng = random.Random(seed)
    calls = {"candidate(n=2, logs=['0:start:0', '1:start:2', '1:end:5', '0:end:6'])"}
    while len(calls) < 600:
        n = rng.randint(1, 8)
        logs: list[str] = []
        timestamp = 0
        call_count = 0

        def emit(depth: int) -> None:
            nonlocal timestamp, call_count
            function_id = rng.randrange(n)
            logs.append(f"{function_id}:start:{timestamp}")
            timestamp += 1
            call_count += 1
            if depth < 4 and call_count < 20:
                for _ in range(rng.randint(0, 2)):
                    emit(depth + 1)
            logs.append(f"{function_id}:end:{timestamp}")
            timestamp += 1

        emit(0)
        calls.add(f"candidate(n={n}, logs={logs!r})")
    return sorted(calls)
