class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        pos = {x: i for i, x in enumerate(nums)}
        for a, b in operations:
            i = pos.pop(a)
            nums[i] = b
            pos[b] = i
        return nums
