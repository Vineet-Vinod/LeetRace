class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        node = head
        while node is not None:
            values.append(node.val)
            node = node.next

        kept_from_right = []
        greatest_to_right = 0
        for value in reversed(values):
            if value >= greatest_to_right:
                kept_from_right.append(value)
                greatest_to_right = value

        result = None
        for value in kept_from_right:
            result = ListNode(value, result)
        return result
