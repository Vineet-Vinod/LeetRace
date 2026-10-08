class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        left = [-1] * n
        stack: list[int] = []
        for i, value in enumerate(nums):
            while stack and nums[stack[-1]] >= value:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        right = [n] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        return max(
            nums[i] * (prefix[right[i]] - prefix[left[i] + 1]) for i in range(n)
        ) % (10**9 + 7)
