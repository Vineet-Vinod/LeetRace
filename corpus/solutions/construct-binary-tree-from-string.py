class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        stack: list[TreeNode] = []
        index = 0
        root: Optional[TreeNode] = None
        while index < len(s):
            if s[index] == ")":
                stack.pop()
                index += 1
            elif s[index] == "(":
                index += 1
            else:
                end = index
                if s[end] == "-":
                    end += 1
                while end < len(s) and s[end].isdigit():
                    end += 1
                node = TreeNode(int(s[index:end]))
                if stack:
                    parent = stack[-1]
                    if parent.left is None:
                        parent.left = node
                    else:
                        parent.right = node
                else:
                    root = node
                stack.append(node)
                index = end
        return root
