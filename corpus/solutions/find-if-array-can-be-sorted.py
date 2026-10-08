class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        previous_max = 0
        i = 0
        while i < len(nums):
            bits = nums[i].bit_count()
            j = i
            values: list[int] = []
            while j < len(nums) and nums[j].bit_count() == bits:
                values.append(nums[j])
                j += 1
            values.sort()
            if values[0] < previous_max:
                return False
            previous_max = values[-1]
            i = j
        return True
