class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen: set[int] = set()
        for value in arr:
            if value * 2 in seen or (value % 2 == 0 and value // 2 in seen):
                return True
            seen.add(value)
        return False
