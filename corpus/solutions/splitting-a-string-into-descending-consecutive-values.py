class Solution:
    def splitString(self, s: str) -> bool:
        def search(start: int, previous: int, parts: int) -> bool:
            if start == len(s):
                return parts >= 2
            value = 0
            for end in range(start, len(s)):
                value = value * 10 + int(s[end])
                if value >= previous:
                    break
                if value == previous - 1 and search(end + 1, value, parts + 1):
                    return True
            return False

        for end in range(1, len(s)):
            first = int(s[:end])
            if search(end, first, 1):
                return True
        return False
