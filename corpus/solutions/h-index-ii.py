class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n
        while left < right:
            middle = (left + right) // 2
            if citations[middle] >= n - middle:
                right = middle
            else:
                left = middle + 1
        return n - left
