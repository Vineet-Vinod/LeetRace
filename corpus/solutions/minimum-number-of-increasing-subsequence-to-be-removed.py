from bisect import bisect_right


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            index = bisect_right(tails, -x)
            if index == len(tails):
                tails.append(-x)
            else:
                tails[index] = -x
        return len(tails)
