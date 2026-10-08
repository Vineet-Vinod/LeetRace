def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(accounts=[['John','johnsmith@mail.com','john_newyork@mail.com'],['John','johnsmith@mail.com','john00@mail.com'],['Mary','mary@mail.com'],['John','johnnybravo@mail.com']])",
        "candidate(accounts=[['Gabe','Gabe0@m.co','Gabe3@m.co','Gabe1@m.co'],['Kevin','Kevin3@m.co','Kevin5@m.co','Kevin0@m.co'],['Ethan','Ethan5@m.co','Ethan4@m.co','Ethan0@m.co'],['Hanzo','Hanzo3@m.co','Hanzo1@m.co','Hanzo0@m.co'],['Fern','Fern5@m.co','Fern1@m.co','Fern0@m.co']])",
    }
    cases.add("candidate(accounts=[['A','a0@x.co']])")
    while len(cases) < 600:
        n = rng.randint(1, 12)
        accounts = []
        pool_by_name = {}
        for i in range(n):
            name = chr(65 + rng.randrange(5))
            emails = []
            pool = pool_by_name.setdefault(name, [])
            if pool and rng.random() < 0.55:
                emails.append(rng.choice(pool))
            for _ in range(rng.randint(1, 4)):
                e = f"u{rng.randrange(100000)}{name.lower()}@x.co"
                if e not in pool and e not in emails:
                    emails.append(e)
                    pool.append(e)
            accounts.append([name, *emails])
        cases.add(f"candidate(accounts={accounts!r})")
    return sorted(cases)
