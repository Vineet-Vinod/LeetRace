import random


def gene(rng: random.Random) -> str:
    return "".join(rng.choice("ACGT") for _ in range(8))


def generate(seed: int = 0) -> list[str]:
    """Generate 8-character A/C/G/T genes and banks of at most 10 distinct genes."""
    rng = random.Random(seed)
    calls = {
        "candidate(startGene='AACCGGTT', endGene='AACCGGTA', bank=['AACCGGTA'])",
        "candidate(startGene='AACCGGTT', endGene='AAACGGTA', bank=['AACCGGTA', 'AACCGCTA', 'AAACGGTA'])",
        "candidate(startGene='AAAAAAAA', endGene='TTTTTTTT', bank=[])",
    }
    while len(calls) < 600:
        start = gene(rng)
        if rng.random() < 0.75:
            distance = rng.randint(1, 8)
            positions = rng.sample(range(8), distance)
            current = list(start)
            bank: list[str] = []
            for position in positions:
                current[position] = rng.choice(
                    [base for base in "ACGT" if base != current[position]]
                )
                bank.append("".join(current))
            end = bank[-1]
            while len(bank) < min(10, 8):
                extra = gene(rng)
                if extra not in bank and extra != start:
                    bank.append(extra)
        else:
            end = gene(rng)
            bank = list({gene(rng) for _ in range(rng.randint(0, 10))})
            if rng.random() < 0.4 and end not in bank:
                bank.append(end)
            bank = bank[:10]
        bank = sorted(set(bank))
        assert len(start) == len(end) == 8 and all(c in "ACGT" for c in start + end)
        assert len(bank) <= 10 and all(
            len(item) == 8 and all(c in "ACGT" for c in item) for item in bank
        )
        calls.add(f"candidate(startGene={start!r}, endGene={end!r}, bank={bank!r})")
    return sorted(calls)
