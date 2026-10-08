class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        left = occurrences = answer = 0
        for right, value in enumerate(nums):
            if value == maximum:
                occurrences += 1
            while occurrences >= k:
                if nums[left] == maximum:
                    occurrences -= 1
                left += 1
            answer += left
        return answer
