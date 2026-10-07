class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        lower = float("-inf")
        stack = []
        for value in preorder:
            if value <= lower:
                return False
            while stack and value > stack[-1]:
                lower = stack.pop()
            stack.append(value)
        return True
