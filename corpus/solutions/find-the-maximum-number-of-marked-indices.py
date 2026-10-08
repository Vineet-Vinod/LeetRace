class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        values = sorted(nums)
        size = len(values)
        first_large = size // 2
        matched = 0
        for small in range(size // 2):
            if 2 * values[small] <= values[first_large]:
                matched += 1
                first_large += 1
        return 2 * matched
