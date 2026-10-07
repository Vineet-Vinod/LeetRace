class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def longest_with_flips(target: str) -> int:
            left = flips = best = 0
            for right, char in enumerate(answerKey):
                if char != target:
                    flips += 1
                while flips > k:
                    if answerKey[left] != target:
                        flips -= 1
                    left += 1
                best = max(best, right - left + 1)
            return best

        return max(longest_with_flips("T"), longest_with_flips("F"))
