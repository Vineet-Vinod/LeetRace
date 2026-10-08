class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = Counter(value for row in nums for value in set(row))
        return sorted(value for value, count in counts.items() if count == len(nums))
