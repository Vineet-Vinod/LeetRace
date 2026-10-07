import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = {
        "candidate(nums1=[100000]*100000, nums2=[0]*100000, k1=0, k2=0)",
        "candidate(nums1=[1]*100000, nums2=[0]*100000, k1=1000000000, k2=0)",
        "candidate(nums1=[100000]*100000, nums2=[0]*100000, k1=1000000000, k2=0)",
    }
    while len(calls) < 200:
        n = rng.randint(1, 80)
        first = [rng.randint(0, 1000) for _ in range(n)]
        second = [rng.randint(0, 1000) for _ in range(n)]
        calls.add(f"candidate(nums1={first!r}, nums2={second!r}, k1=0, k2=0)")
    while len(calls) < 400:
        n = rng.randint(1, 80)
        differences = [rng.randint(1, 1000) for _ in range(n)]
        first = [1000] * n
        second = [1000 - diff for diff in differences]
        operations = rng.randint(1, sum(differences) - 1) if sum(differences) > 1 else 0
        first_ops = rng.randint(0, operations)
        calls.add(
            f"candidate(nums1={first!r}, nums2={second!r}, k1={first_ops}, k2={operations - first_ops})"
        )
    while len(calls) < 600:
        n = rng.randint(1, 80)
        values = [rng.randint(0, 100000) for _ in range(n)]
        calls.add(f"candidate(nums1={values!r}, nums2={values!r}, k1=0, k2=0)")
    assert 500 <= len(calls) <= 999 and len(calls) == len(set(calls))
    return sorted(calls)
