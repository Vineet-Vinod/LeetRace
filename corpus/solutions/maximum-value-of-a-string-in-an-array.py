class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(value) if value.isdigit() else len(value) for value in strs)
