class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lengths = [1] * len(nums)
        counts = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        longest = max(lengths)
        return sum(counts[i] for i in range(len(nums)) if lengths[i] == longest)
