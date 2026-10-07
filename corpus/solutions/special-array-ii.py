class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + int(nums[i] % 2 == nums[i - 1] % 2))
        return [prefix[right] == prefix[left] for left, right in queries]
