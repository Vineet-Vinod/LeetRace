class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        nodes = {id(root): root}
        parents = {id(root): None}
        depths = {id(root): 0}
        queue = deque([root])
        deepest = 0
        leaves: list[TreeNode] = []
        while queue:
            node = queue.popleft()
            depth = depths[id(node)]
            if depth > deepest:
                deepest = depth
                leaves = []
            if depth == deepest:
                leaves.append(node)
            for child in (node.left, node.right):
                if child is not None:
                    child_id = id(child)
                    nodes[child_id] = child
                    parents[child_id] = id(node)
                    depths[child_id] = depth + 1
                    queue.append(child)
        common = set()
        current = id(leaves[0])
        while current is not None:
            common.add(current)
            current = parents[current]
        for leaf in leaves[1:]:
            ancestors = set()
            current = id(leaf)
            while current is not None:
                ancestors.add(current)
                current = parents[current]
            common.intersection_update(ancestors)
        answer = max(common, key=lambda node_id: depths[node_id])
        return nodes[answer]
