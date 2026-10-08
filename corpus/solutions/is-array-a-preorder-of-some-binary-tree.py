class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        if not nodes or nodes[0][1] != -1:
            return False
        root = nodes[0][0]
        seen = {root}
        child_count: dict[int, int] = {}
        ancestors = [root]
        for node, parent in nodes[1:]:
            if node in seen or parent not in ancestors:
                return False
            while ancestors[-1] != parent:
                ancestors.pop()
            child_count[parent] = child_count.get(parent, 0) + 1
            if child_count[parent] > 2:
                return False
            ancestors.append(node)
            seen.add(node)
        return True
