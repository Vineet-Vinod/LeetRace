class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        balances: dict[int, int] = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
            else:
                left = balances.get(id(node.left), 0)
                right = balances.get(id(node.right), 0)
                moves += abs(left) + abs(right)
                balances[id(node)] = node.val + left + right - 1
        return moves
