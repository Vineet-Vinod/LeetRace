class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotate = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        digits = str(n)
        if any(ch not in rotate for ch in digits):
            return False
        rotated = "".join(rotate[ch] for ch in reversed(digits)).lstrip("0") or "0"
        return rotated != digits
