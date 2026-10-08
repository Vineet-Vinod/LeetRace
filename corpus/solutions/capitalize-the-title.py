class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.lower().split(" ")
        return " ".join(word.capitalize() if len(word) > 2 else word for word in words)
