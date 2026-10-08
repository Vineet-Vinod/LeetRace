class Solution:
    def reformat(self, s: str) -> str:
        letters = [char for char in s if char.isalpha()]
        digits = [char for char in s if char.isdigit()]
        if abs(len(letters) - len(digits)) > 1:
            return ""
        first, second = (
            (letters, digits) if len(letters) > len(digits) else (digits, letters)
        )
        result = []
        for i in range(len(first)):
            result.append(first[i])
            if i < len(second):
                result.append(second[i])
        return "".join(result)
