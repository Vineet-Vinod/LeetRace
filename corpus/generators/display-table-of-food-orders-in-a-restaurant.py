import random
import string


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: 1..50000 orders; table IDs 1..500; generator emits nonempty valid orders."""
    rng = random.Random(seed)
    calls = {
        'candidate(orders=[["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"]])'
    }
    foods = ["Soup", "Pasta", "Tea", "Fried Rice", "Water", "Cake"]
    while len(calls) < 600:
        orders = []
        for _ in range(rng.randint(1, 40)):
            name = "".join(
                rng.choice(string.ascii_letters) for _ in range(rng.randint(1, 10))
            )
            orders.append([name, str(rng.randint(1, 500)), rng.choice(foods)])
        calls.add(f"candidate(orders={orders!r})")
    return sorted(calls)
