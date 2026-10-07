class Solution:
    def getDirections(self, root, startValue: int, destValue: int) -> str:
        paths = {}
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node:
                continue
            paths[node.val] = path
            stack.append((node.right, path + "R"))
            stack.append((node.left, path + "L"))
        start_path = paths[startValue]
        dest_path = paths[destValue]
        common = 0
        while (
            common < min(len(start_path), len(dest_path))
            and start_path[common] == dest_path[common]
        ):
            common += 1
        return "U" * (len(start_path) - common) + dest_path[common:]
