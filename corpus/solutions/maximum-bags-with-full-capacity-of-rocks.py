class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        missing = sorted(c - r for c, r in zip(capacity, rocks))
        answer = 0
        for amount in missing:
            if amount > additionalRocks:
                break
            additionalRocks -= amount
            answer += 1
        return answer
