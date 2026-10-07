def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    possible = {
        "candidate(start='RXXLRXRXL',result='XRLXXRRLX')",
        f"candidate(start={'R' + 'X' * 9998 + 'L'!r},result={'R' + 'L' + 'X' * 9998!r})",
    }
    impossible = {
        f"candidate(start={'L' + 'X' * 9998 + 'R'!r},result={'R' + 'X' * 9998 + 'L'!r})",
    }
    while len(possible) < 300:
        n = rng.randint(1, 100)
        start = "".join(rng.choice("LRX") for _ in range(n))
        state = list(start)
        for _ in range(rng.randint(1, 3 * n)):
            moves = [
                index
                for index in range(n - 1)
                if state[index : index + 2] in (["X", "L"], ["R", "X"])
            ]
            if moves:
                index = rng.choice(moves)
                state[index], state[index + 1] = state[index + 1], state[index]
        result = "".join(state)
        possible.add(f"candidate(start={start!r},result={result!r})")
    while len(impossible) < 300:
        n = rng.randint(2, 100)
        left = rng.randint(1, n - 1)
        right = rng.randint(1, n - left)
        blanks = n - left - right
        start = "L" * left + "R" * right + "X" * blanks
        result = "R" * right + "L" * left + "X" * blanks
        impossible.add(f"candidate(start={start!r},result={result!r})")
    return sorted(possible | impossible)
