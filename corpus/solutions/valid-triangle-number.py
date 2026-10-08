class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for largest in range(len(nums) - 1, 1, -1):
            left, right = 0, largest - 1
            while left < right:
                if nums[left] + nums[right] > nums[largest]:
                    total += right - left
                    right -= 1
                else:
                    left += 1
        return total
