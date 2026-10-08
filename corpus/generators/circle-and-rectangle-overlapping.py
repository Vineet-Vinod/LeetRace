import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(rad, cx, cy, x1, y1, x2, y2):
        key = (rad, cx, cy, x1, y1, x2, y2)
        if key not in seen:
            assert (
                1 <= rad <= 2000
                and all(-10000 <= v <= 10000 for v in (cx, cy, x1, y1, x2, y2))
                and x1 < x2
                and y1 < y2
            )
            seen.add(key)
            cases.append(
                f"candidate(radius={rad}, xCenter={cx}, yCenter={cy}, x1={x1}, y1={y1}, x2={x2}, y2={y2})"
            )

    for i in range(300):
        rad = r.randint(1, 2000)
        cx = r.randint(-5000, 5000)
        cy = r.randint(-5000, 5000)
        dx = r.randint(-rad, rad)
        dy = 0
        x, y = cx + dx, cy + dy
        add(rad, cx, cy, x, y, x + 1, y + 1)
    for i in range(300):
        rad = r.randint(1, 2000)
        cx = r.randint(-3000, 3000)
        cy = r.randint(-3000, 3000)
        gap = rad + 1 + r.randint(0, 3000)
        add(rad, cx, cy, cx + gap, cy, cx + gap + 1, cy + 1)
    add(2000, 0, 0, -10000, -10000, -9999, -9999)
    add(2000, 0, 0, 2001, 0, 2002, 1)
    return cases
