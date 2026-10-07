class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        operations = 0
        for index, char in enumerate(s):
            if char == "1":
                ones += 1
            elif index + 1 < len(s) and s[index + 1] == "1":
                operations += ones
        return operations
