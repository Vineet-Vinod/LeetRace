class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = 0
        total = 0
        answer = 0
        for right, (position, amount) in enumerate(fruits):
            total += amount
            while left <= right:
                a = max(0, startPos - fruits[left][0])
                b = max(0, position - startPos)
                if a + b + min(a, b) <= k:
                    break
                total -= fruits[left][1]
                left += 1
            answer = max(answer, total)
        return answer
