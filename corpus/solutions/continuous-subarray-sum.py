class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        earliest = {0: -1}
        prefix = 0
        for index, value in enumerate(nums):
            prefix = (prefix + value) % k
            if prefix in earliest:
                if index - earliest[prefix] >= 2:
                    return True
            else:
                earliest[prefix] = index
        return False
