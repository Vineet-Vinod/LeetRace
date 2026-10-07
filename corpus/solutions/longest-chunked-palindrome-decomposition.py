class Solution:
    def longestDecomposition(self, text: str) -> int:
        left, right = 0, len(text)
        answer = 0
        while left < right:
            for size in range(1, (right - left) // 2 + 1):
                if text[left : left + size] == text[right - size : right]:
                    answer += 2
                    left += size
                    right -= size
                    break
            else:
                return answer + 1
        return answer
