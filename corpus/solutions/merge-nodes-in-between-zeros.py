class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        total = 0
        node = head.next if head is not None else None
        while node is not None:
            if node.val == 0:
                tail.next = ListNode(total)
                tail = tail.next
                total = 0
            else:
                total += node.val
            node = node.next
        return dummy.next
