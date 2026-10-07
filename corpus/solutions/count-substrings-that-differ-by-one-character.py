class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        total = 0
        for start_s in range(len(s)):
            for start_t in range(len(t)):
                mismatches = 0
                offset = 0
                while start_s + offset < len(s) and start_t + offset < len(t):
                    if s[start_s + offset] != t[start_t + offset]:
                        mismatches += 1
                    if mismatches == 1:
                        total += 1
                    elif mismatches > 1:
                        break
                    offset += 1
        return total
