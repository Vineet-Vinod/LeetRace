class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len({str(int(match)) for match in re.findall(r"[0-9]+", word)})
