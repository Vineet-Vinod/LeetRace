class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest = {"0": 0, "1": 0}
        current = 0
        previous = ""
        for char in s:
            current = current + 1 if char == previous else 1
            longest[char] = max(longest[char], current)
            previous = char
        return longest["1"] > longest["0"]
