class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False
        i = j = 0
        while i < len(start) and j < len(target):
            while i < len(start) and start[i] == "_":
                i += 1
            while j < len(target) and target[j] == "_":
                j += 1
            if i == len(start) or j == len(target):
                break
            if start[i] == "L" and i < j or start[i] == "R" and i > j:
                return False
            i += 1
            j += 1
        return True
