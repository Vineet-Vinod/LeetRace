class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = {0}
        current = 0
        turn = 1
        while True:
            current = (current + turn * k) % n
            if current in seen:
                break
            seen.add(current)
            turn += 1
        return [player for player in range(1, n + 1) if player - 1 not in seen]
