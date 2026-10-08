import random
import string

EXAMPLES = [
    "candidate(tickets=[['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']])",
    "candidate(tickets=[['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(tickets):
        assert 1 <= len(tickets) <= 300
        assert all(
            len(t) == 2
            and all(len(v) == 3 and set(v) <= set(string.ascii_uppercase) for v in t)
            and t[0] != t[1]
            for t in tickets
        )
        # Every input comes from a continuous trail beginning at JFK, then is shuffled.
        emit(f"candidate(tickets={tickets!r})")

    add([["JFK", "AAA"], ["AAA", "JFK"]] * 150)
    while len(calls) < 600:
        airports = ["JFK", "AAA", "AAB", "AAC", "ATL", "SFO", "ZZZ"]
        path = ["JFK"]
        for _ in range(rng.randint(1, 40)):
            path.append(rng.choice([a for a in airports if a != path[-1]]))
        tickets = [path[i : i + 2] for i in range(len(path) - 1)]
        rng.shuffle(tickets)
        add(tickets)
    return calls
