class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        possible = [False] * (len(nums) + 1)
        possible[0] = True
        for end in range(2, len(nums) + 1):
            if nums[end - 1] == nums[end - 2] and possible[end - 2]:
                possible[end] = True
            if end >= 3 and possible[end - 3]:
                triple = nums[end - 3 : end]
                if (
                    triple[0] == triple[1] == triple[2]
                    or triple[0] + 1 == triple[1]
                    and triple[1] + 1 == triple[2]
                ):
                    possible[end] = True
        return possible[-1]
