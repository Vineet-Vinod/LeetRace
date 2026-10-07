class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        counts = Counter(nums)
        for value in sorted(counts):
            amount = counts[value]
            if amount:
                for next_value in range(value, value + k):
                    if counts[next_value] < amount:
                        return False
                    counts[next_value] -= amount
        return True
