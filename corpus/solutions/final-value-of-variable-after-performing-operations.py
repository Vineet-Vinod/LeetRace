class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum(1 if operation[1] == "+" else -1 for operation in operations)
