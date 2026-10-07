class Solution:
    def countLetters(self, s: str) -> int:
        total = 0
        run = 0
        previous = ""
        for char in s:
            run = run + 1 if char == previous else 1
            total += run
            previous = char
        return total
