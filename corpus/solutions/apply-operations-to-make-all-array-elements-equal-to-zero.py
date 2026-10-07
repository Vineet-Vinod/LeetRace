class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        active = 0
        ending = [0] * (n + 1)
        for i, value in enumerate(nums):
            active -= ending[i]
            required = value - active
            if required < 0:
                return False
            if i + k > n:
                if required:
                    return False
                continue
            active += required
            ending[i + k] += required
        return True
