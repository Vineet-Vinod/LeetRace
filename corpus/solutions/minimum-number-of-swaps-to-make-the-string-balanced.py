class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        minimum = 0
        for char in s:
            balance += 1 if char == "[" else -1
            minimum = min(minimum, balance)
        return (-minimum + 1) // 2
