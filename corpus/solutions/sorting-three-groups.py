class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        length = [0, 0, 0]
        for value in nums:
            if value == 1:
                length[0] += 1
            elif value == 2:
                length[1] = max(length[0], length[1]) + 1
            else:
                length[2] = max(length[0], length[1], length[2]) + 1
        return len(nums) - max(length)
