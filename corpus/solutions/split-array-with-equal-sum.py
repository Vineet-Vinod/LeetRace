from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        for j in range(3, n - 3):
            sums = set()
            for i in range(1, j - 1):
                if prefix[i] == prefix[j] - prefix[i + 1]:
                    sums.add(prefix[i])
            for k in range(j + 2, n - 1):
                if (
                    prefix[k] - prefix[j + 1] == prefix[n] - prefix[k + 1]
                    and prefix[k] - prefix[j + 1] in sums
                ):
                    return True
        return False
