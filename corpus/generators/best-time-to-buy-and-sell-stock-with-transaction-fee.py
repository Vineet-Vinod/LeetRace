import ast
import random


_MAX_PRICE = 49_999
_MAX_DAYS = 50_000
_MAX_FEE = 49_999


def generate(seed: int = 0) -> list[str]:
    """Prices, fees, and lengths stay within the original bounds, including maxima."""
    rng = random.Random(seed)
    cases = {
        "candidate(prices=[1, 3, 2, 8, 4, 9], fee=2)",
        "candidate(prices=[1, 3, 7, 5, 10, 3], fee=3)",
        "candidate(prices=[1], fee=0)",
        f"candidate(prices={[max(1, _MAX_PRICE - day) for day in range(_MAX_DAYS)]!r}, fee={_MAX_FEE})",
        f"candidate(prices={[1, _MAX_PRICE] * (_MAX_DAYS // 2)!r}, fee=0)",
        f"candidate(prices={[1, _MAX_PRICE] * (_MAX_DAYS // 2)!r}, fee={_MAX_FEE})",
    }
    while len(cases) < 600:
        size = rng.randint(1, 100)
        prices = [rng.randint(1, _MAX_PRICE) for _ in range(size)]
        fee = rng.randint(0, _MAX_FEE)
        cases.add(f"candidate(prices={prices!r}, fee={fee})")

    for call in cases:
        keywords = ast.parse(call, mode="eval").body.keywords
        arguments = {
            keyword.arg: ast.literal_eval(keyword.value) for keyword in keywords
        }
        prices = arguments["prices"]
        fee = arguments["fee"]
        assert 1 <= len(prices) <= _MAX_DAYS
        assert all(1 <= price <= _MAX_PRICE for price in prices)
        assert 0 <= fee <= _MAX_FEE
    return sorted(cases)
