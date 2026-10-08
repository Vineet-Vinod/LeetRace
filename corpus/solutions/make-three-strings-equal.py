class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        length = 0
        for chars in zip(s1, s2, s3):
            if chars[0] == chars[1] == chars[2]:
                length += 1
            else:
                break
        return -1 if length == 0 else len(s1) + len(s2) + len(s3) - 3 * length
