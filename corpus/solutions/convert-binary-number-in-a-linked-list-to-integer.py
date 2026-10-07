class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        value = 0
        node = head
        while node is not None:
            value = value * 2 + node.val
            node = node.next
        return value
