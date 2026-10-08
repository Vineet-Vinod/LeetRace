import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    alphabet = string.ascii_lowercase[:8]
    while len(cases) < 600:
        products = set()
        while len(products) < rng.randint(1, 30):
            products.add(
                "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 12)))
            )
        products = sorted(products)
        search = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 12)))
        key = (tuple(sorted(products)), search)
        if key not in seen:
            seen.add(key)
            assert 1 <= len(products) <= 1000
            assert all(1 <= len(product) <= 3000 for product in products)
            assert sum(map(len, products)) <= 20_000
            assert len(products) == len(set(products))
            assert all(product.islower() and product.isalpha() for product in products)
            assert 1 <= len(search) <= 1000 and search.islower() and search.isalpha()
            cases.append(f"candidate(products={products!r}, searchWord={search!r})")
    return sorted(cases)
