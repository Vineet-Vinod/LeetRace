class Solution:
    def maximumCoins(
        self, heroes: List[int], monsters: List[int], coins: List[int]
    ) -> List[int]:
        ordered = sorted(zip(monsters, coins))
        powers = [power for power, _ in ordered]
        prefix = [0]
        for _, value in ordered:
            prefix.append(prefix[-1] + value)
        return [prefix[bisect_right(powers, hero)] for hero in heroes]
