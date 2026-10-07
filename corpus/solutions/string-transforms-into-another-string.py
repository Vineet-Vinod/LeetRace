class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        mapping = {}
        for a, b in zip(str1, str2):
            if a in mapping and mapping[a] != b:
                return False
            mapping[a] = b
        return len(set(str2)) < 26
