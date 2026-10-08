class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less_tail = less_dummy
        greater_tail = greater_dummy
        node = head
        while node is not None:
            following = node.next
            node.next = None
            if node.val < x:
                less_tail.next = node
                less_tail = node
            else:
                greater_tail.next = node
                greater_tail = node
            node = following
        less_tail.next = greater_dummy.next
        return less_dummy.next
