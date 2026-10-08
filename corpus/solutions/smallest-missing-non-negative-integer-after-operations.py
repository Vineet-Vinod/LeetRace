class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counts = Counter(number % value for number in nums)
        mex = 0
        while counts[mex % value] > 0:
            counts[mex % value] -= 1
            mex += 1
        return mex
