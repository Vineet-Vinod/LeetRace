class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        ordered = sorted(potions)
        return [
            len(ordered) - bisect_left(ordered, (success + spell - 1) // spell)
            for spell in spells
        ]
