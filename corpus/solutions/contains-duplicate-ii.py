class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = {}
        for index, value in enumerate(nums):
            if value in last and index - last[value] <= k:
                return True
            last[value] = index
        return False
