class Solution:
    def getLucky(self, s: str, k: int) -> int:
        value = "".join(str(ord(char) - 96) for char in s)
        for _ in range(k):
            value = str(sum(map(int, value)))
        return int(value)
