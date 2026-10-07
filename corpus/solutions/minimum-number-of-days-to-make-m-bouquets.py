class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left, right = min(bloomDay), max(bloomDay)

        def enough(day):
            bouquets = flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        while left < right:
            middle = (left + right) // 2
            if enough(middle):
                right = middle
            else:
                left = middle + 1
        return left
