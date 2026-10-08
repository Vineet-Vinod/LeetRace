class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        for value in nums:
            if write == 0 or nums[write - 1] != value:
                nums[write] = value
                write += 1
        return write
