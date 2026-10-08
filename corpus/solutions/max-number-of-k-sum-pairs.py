class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        operations = 0
        for value in list(counts):
            complement = k - value
            if complement not in counts:
                continue
            if complement == value:
                pairs = counts[value] // 2
            else:
                pairs = min(counts[value], counts[complement])
            operations += pairs
            counts[value] -= pairs
            counts[complement] -= pairs
        return operations
