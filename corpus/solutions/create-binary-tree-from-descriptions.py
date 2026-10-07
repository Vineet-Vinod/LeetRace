class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes: Dict[int, TreeNode] = {}
        children = set()
        for parent, child, is_left in descriptions:
            nodes.setdefault(parent, TreeNode(parent))
            nodes.setdefault(child, TreeNode(child))
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            children.add(child)
        root = next(value for value in nodes if value not in children)
        return nodes[root]
