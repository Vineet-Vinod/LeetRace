class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        required = Counter(char.lower() for char in licensePlate if char.isalpha())
        return min((word for word in words if not required - Counter(word)), key=len)
