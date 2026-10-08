import random
import string

EXAMPLES = [
    "candidate(req_skills=['java', 'nodejs', 'reactjs'], people=[['java'], ['nodejs'], ['nodejs', 'reactjs']])",
    "candidate(req_skills=['algorithms', 'math', 'java', 'reactjs', 'csharp', 'aws'], people=[['algorithms', 'math', 'java'], ['algorithms', 'math', 'reactjs'], ['java', 'csharp', 'aws'], ['reactjs', 'csharp'], ['csharp', 'math'], ['aws', 'java']])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(skills, people):
        assert 1 <= len(skills) <= 16 and len(set(skills)) == len(skills)
        assert all(
            1 <= len(s) <= 16 and set(s) <= set(string.ascii_lowercase) for s in skills
        )
        assert 1 <= len(people) <= 60
        assert all(
            len(p) <= 16 and len(p) == len(set(p)) and set(p) <= set(skills)
            for p in people
        )
        assert set().union(*map(set, people)) == set(skills)
        emit(f"candidate(req_skills={skills!r}, people={people!r})")

    add(
        list(string.ascii_lowercase[:16]),
        [[c] for c in string.ascii_lowercase[:16]] + [[]] * 44,
    )
    add(["abcdefghijklmnop"], [[]] * 59 + [["abcdefghijklmnop"]])
    while len(calls) < 600:
        skills = list(string.ascii_lowercase[: rng.randint(1, 8)])
        people = [
            [s for s in skills if rng.random() < 0.4] for _ in range(rng.randint(1, 18))
        ]
        missing = set(skills) - set().union(*map(set, people))
        for s in sorted(missing):
            people[rng.randrange(len(people))].append(s)
        for p in people:
            p.sort()
        add(skills, people)
    return calls
