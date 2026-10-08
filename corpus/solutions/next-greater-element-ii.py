class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        answer = [-1] * len(nums)
        stack = []
        for index in range(2 * len(nums)):
            current = nums[index % len(nums)]
            while stack and nums[stack[-1]] < current:
                answer[stack.pop()] = current
            if index < len(nums):
                stack.append(index)
        return answer
