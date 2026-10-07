class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        first = [int(part) for part in version1.split(".")]
        second = [int(part) for part in version2.split(".")]
        size = max(len(first), len(second))
        first.extend([0] * (size - len(first)))
        second.extend([0] * (size - len(second)))
        for a, b in zip(first, second):
            if a != b:
                return 1 if a > b else -1
        return 0
