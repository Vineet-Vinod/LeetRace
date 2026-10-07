class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combinations = [""]
        for digit in digits:
            combinations = [
                prefix + char for prefix in combinations for char in mapping[digit]
            ]
        return sorted(combinations)
