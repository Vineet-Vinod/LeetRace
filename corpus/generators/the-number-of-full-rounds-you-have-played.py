def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(loginTime='09:31',logoutTime='10:14')"}
    while len(cases) < 600:
        start = rng.randrange(1440)
        end = rng.randrange(1440)
        while end == start:
            end = rng.randrange(1440)
        login = f"{start // 60:02d}:{start % 60:02d}"
        logout = f"{end // 60:02d}:{end % 60:02d}"
        assert start != end
        cases.add(f"candidate(loginTime={login!r},logoutTime={logout!r})")
    return sorted(cases)
