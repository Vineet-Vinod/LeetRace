import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(arr1, arr2):
        return (
            1 <= len(arr1) <= 2000
            and 1 <= len(arr2) <= 2000
            and all(0 <= x <= 10**9 for x in arr1 + arr2)
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for arr2 in [[1, 3, 2, 4], [4, 3, 1], [1, 6, 3, 3]]:
        emit(arr1=[1, 5, 3, 6, 7], arr2=arr2)
    emit(arr1=[10**9] * 2000, arr2=list(range(2000)))
    emit(arr1=list(range(2000)), arr2=[10**9] * 2000)
    while len(calls) < 600:
        arr1 = [rng.randint(0, 30) for _ in range(rng.randint(1, 15))]
        arr2 = [rng.randint(0, 30) for _ in range(rng.randint(1, 20))]
        if rng.randrange(4) == 0:
            arr1 = sorted(set(arr1))
        emit(arr1=arr1, arr2=arr2)
    assert len(calls) == 600
    return list(calls)
