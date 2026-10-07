class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results: List[str] = []
        current: List[str] = []

        def build(opened: int, closed: int) -> None:
            if opened == n and closed == n:
                results.append("".join(current))
                return
            if opened < n:
                current.append("(")
                build(opened + 1, closed)
                current.pop()
            if closed < opened:
                current.append(")")
                build(opened, closed + 1)
                current.pop()

        build(0, 0)
        return sorted(results)
