def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    valid = {
        "candidate(preorder=[5,2,1,3,6])",
        f"candidate(preorder={list(range(1, 10001))!r})",
    }
    invalid = {
        "candidate(preorder=[5,2,6,1])",
        f"candidate(preorder={([5000] + list(range(1, 4999)) + list(range(5001, 10001)) + [4999])!r})",
    }
    while len(valid) < 300:
        n = rng.randint(1, 100)
        keys = rng.sample(range(1, 10001), n)
        root = keys[0]
        left = sorted((key for key in keys[1:] if key < root), reverse=True)
        right = sorted(key for key in keys[1:] if key > root)
        preorder = [root] + left + right
        valid.add(f"candidate(preorder={preorder!r})")
    while len(invalid) < 300:
        n = rng.randint(4, 100)
        root = rng.randint(n + 3, 9999)
        lower = sorted(rng.sample(range(1, root - 1), n - 3), reverse=True)
        preorder = [root] + lower + [root + 1, root - 1]
        assert len(preorder) == n and len(set(preorder)) == n
        invalid.add(f"candidate(preorder={preorder!r})")
    return sorted(valid | invalid)
