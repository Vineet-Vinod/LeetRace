class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        differences = sorted(a - b for a, b in zip(nums1, nums2))
        left, right = 0, len(differences) - 1
        answer = 0
        while left < right:
            if differences[left] + differences[right] > 0:
                answer += right - left
                right -= 1
            else:
                left += 1
        return answer
