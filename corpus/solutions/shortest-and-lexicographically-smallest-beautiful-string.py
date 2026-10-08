class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        best = ""
        left = 0
        ones = 0
        for right, char in enumerate(s):
            ones += char == "1"
            while left <= right and ones > k:
                ones -= s[left] == "1"
                left += 1
            if ones == k:
                while left <= right and s[left] == "0":
                    left += 1
                candidate = s[left : right + 1]
                if not best or (len(candidate), candidate) < (len(best), best):
                    best = candidate
        return best
