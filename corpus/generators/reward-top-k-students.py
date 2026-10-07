import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    vocab = [chr(97 + i // 26) + chr(97 + i % 26) for i in range(50)]
    while len(calls) < 600:
        positive = rng.sample(vocab, rng.randint(1, 20))
        negative = rng.sample(
            [word for word in vocab if word not in positive], rng.randint(1, 20)
        )
        n = rng.randint(1, 100)
        report = [" ".join(rng.choices(vocab, k=rng.randint(1, 20))) for _ in range(n)]
        student_id = rng.sample(range(1, 10**9), n)
        k = rng.randint(1, n)
        calls.add(
            f"candidate(positive_feedback={positive!r}, negative_feedback={negative!r}, report={report!r}, student_id={student_id!r}, k={k})"
        )
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(positive_feedback=['smart', 'brilliant', 'studious'], negative_feedback=['not'], report=['this student is not studious', 'the student is smart'], student_id=[1, 2], k=2)",
    "candidate(positive_feedback=['smart', 'brilliant', 'studious'], negative_feedback=['not'], report=['this student is studious', 'the student is smart'], student_id=[1, 2], k=2)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
