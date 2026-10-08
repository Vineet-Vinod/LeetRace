class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = root.right
            while successor.left is not None:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root
