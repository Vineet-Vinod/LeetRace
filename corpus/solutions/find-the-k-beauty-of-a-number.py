class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        text = str(num)
        return sum(
            (value := int(text[i : i + k])) != 0 and num % value == 0
            for i in range(len(text) - k + 1)
        )
