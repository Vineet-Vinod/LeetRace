class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))
        counts = defaultdict(int)
        left = 0
        total = 0
        for right, value in enumerate(nums):
            counts[value] += 1
            while len(counts) == target:
                total += len(nums) - right
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                left += 1
        return total
