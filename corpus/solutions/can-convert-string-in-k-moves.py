class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        used = [0] * 26
        for source, target in zip(s, t):
            shift = (ord(target) - ord(source)) % 26
            if shift:
                used[shift] += 1
                if shift + 26 * (used[shift] - 1) > k:
                    return False
        return True
