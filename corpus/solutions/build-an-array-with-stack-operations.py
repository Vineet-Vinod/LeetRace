class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations: List[str] = []
        wanted = set(target)
        for value in range(1, target[-1] + 1):
            operations.append("Push")
            if value not in wanted:
                operations.append("Pop")
        return operations
