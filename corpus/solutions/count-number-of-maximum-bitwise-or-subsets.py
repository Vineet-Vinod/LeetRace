class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        target = 0
        for value in nums:
            target |= value
        counts = [0] * (1 << len(nums))
        answer = 0
        for mask in range(1, 1 << len(nums)):
            bit = mask & -mask
            index = bit.bit_length() - 1
            previous = mask ^ bit
            counts[mask] = counts[previous] | nums[index]
            answer += counts[mask] == target
        return answer
