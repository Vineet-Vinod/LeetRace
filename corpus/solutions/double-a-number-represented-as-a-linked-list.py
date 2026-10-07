class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.val >= 5:
            head = ListNode(0, head)
        node = head
        while node is not None:
            node.val = (node.val * 2) % 10
            if node.next is not None and node.next.val >= 5:
                node.val += 1
            node = node.next
        return head
