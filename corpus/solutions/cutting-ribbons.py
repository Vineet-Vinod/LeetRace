class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left, right = 1, max(ribbons)
        answer = 0
        while left <= right:
            middle = (left + right) // 2
            pieces = sum(ribbon // middle for ribbon in ribbons)
            if pieces >= k:
                answer = middle
                left = middle + 1
            else:
                right = middle - 1
        return answer
