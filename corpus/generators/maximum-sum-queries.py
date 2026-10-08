import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a, b, q = kwargs["nums1"], kwargs["nums2"], kwargs["queries"]
        assert 1 <= len(a) == len(b) <= 100000 and 1 <= len(q) <= 100000
        assert all(1 <= v <= 10**9 for v in a + b) and all(
            len(row) == 2 and all(1 <= v <= 10**9 for v in row) for row in q
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(
        nums1=list(range(1, 100001)),
        nums2=list(range(100000, 0, -1)),
        queries=[[i, i] for i in range(1, 100001)],
    )
    add(nums1=[10**9], nums2=[10**9], queries=[[1, 1], [10**9, 10**9]])
    add(nums1=[4, 3, 1, 2], nums2=[2, 4, 9, 5], queries=[[4, 1], [1, 3], [2, 5]])
    add(nums1=[3, 2, 5], nums2=[2, 3, 4], queries=[[4, 4], [3, 2], [1, 1]])
    add(nums1=[2, 1], nums2=[2, 3], queries=[[3, 3]])
    while len(calls) < 600:
        n = rng.randint(1, 30)
        nums1 = [rng.randint(1, 100) for _ in range(n)]
        nums2 = [rng.randint(1, 100) for _ in range(n)]
        queries = []
        for _ in range(rng.randint(1, 25)):
            if rng.randrange(2):
                j = rng.randrange(n)
                queries.append([rng.randint(1, nums1[j]), rng.randint(1, nums2[j])])
            else:
                queries.append([rng.randint(1, 130), rng.randint(1, 130)])
        add(nums1=nums1, nums2=nums2, queries=queries)
    return calls
