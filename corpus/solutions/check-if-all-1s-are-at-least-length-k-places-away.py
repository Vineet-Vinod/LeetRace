class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        previous = -k - 1
        for i, value in enumerate(nums):
            if value:
                if i - previous - 1 < k:
                    return False
                previous = i
        return True
