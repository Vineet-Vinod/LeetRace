class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        differences = sorted(
            (first - second for first, second in zip(reward1, reward2)), reverse=True
        )
        return sum(reward2) + sum(differences[:k])
