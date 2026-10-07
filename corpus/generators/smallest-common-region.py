def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = {
        "candidate(regions=[['Earth','North America','South America'],['North America','United States','Canada'],['United States','New York','Boston'],['Canada','Ontario','Quebec'],['South America','Brazil']], region1='Quebec', region2='New York')",
        "candidate(regions=[['Earth','North America','South America'],['North America','United States','Canada'],['United States','New York','Boston'],['Canada','Ontario','Quebec'],['South America','Brazil']], region1='Canada', region2='South America')",
    }
    while len(cases) < 600:
        count = rng.randint(3, 100)
        names = [
            f"Region{chr(65 + index // 26)}{chr(65 + index % 26)}"
            for index in range(count)
        ]
        regions = [[names[0], names[1]]]
        index = 2
        while index < count:
            parent = rng.randrange(index)
            child_count = rng.randint(1, min(5, count - index))
            children = names[index : index + child_count]
            regions.append([names[parent], *children])
            index += child_count
        region1, region2 = rng.sample(names[1:], 2)
        assert 2 <= len(regions) <= 10_000
        assert all(2 <= len(group) <= 20 for group in regions)
        assert len({child for group in regions for child in group[1:]}) == count - 1
        cases.add(
            f"candidate(regions={regions!r}, region1={region1!r}, region2={region2!r})"
        )
    return sorted(cases)
