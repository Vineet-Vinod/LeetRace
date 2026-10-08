class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        ordered = sorted(properties, key=lambda pair: (-pair[0], pair[1]))
        strongest_defense = 0
        weak = 0
        for _, defense in ordered:
            if strongest_defense > defense:
                weak += 1
            else:
                strongest_defense = defense
        return weak
