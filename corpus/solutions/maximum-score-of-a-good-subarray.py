from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = right = k
        minimum = answer = nums[k]
        while left > 0 or right < len(nums) - 1:
            if left == 0 or (
                right < len(nums) - 1 and nums[right + 1] > nums[left - 1]
            ):
                right += 1
                minimum = min(minimum, nums[right])
            else:
                left -= 1
                minimum = min(minimum, nums[left])
            answer = max(answer, minimum * (right - left + 1))
        return answer
