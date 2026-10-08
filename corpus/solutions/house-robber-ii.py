class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def linear_max(values: List[int]) -> int:
            two_back = 0
            one_back = 0
            for value in values:
                two_back, one_back = one_back, max(one_back, two_back + value)
            return one_back

        return max(linear_max(nums[:-1]), linear_max(nums[1:]))
