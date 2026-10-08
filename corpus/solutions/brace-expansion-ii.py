class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        pos = 0

        def union() -> set[str]:
            nonlocal pos
            result = product()
            while pos < len(expression) and expression[pos] == ",":
                pos += 1
                result |= product()
            return result

        def product() -> set[str]:
            nonlocal pos
            result = {""}
            while pos < len(expression) and expression[pos] not in ",}":
                if expression[pos] == "{":
                    pos += 1
                    part = union()
                    pos += 1
                else:
                    part = {expression[pos]}
                    pos += 1
                result = {a + b for a in result for b in part}
            return result

        return sorted(union())
