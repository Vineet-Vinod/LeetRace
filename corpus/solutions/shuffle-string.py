class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = [""] * len(s)
        for char, destination in zip(s, indices):
            result[destination] = char
        return "".join(result)
