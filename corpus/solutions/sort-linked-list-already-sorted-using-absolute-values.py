class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        current = head
        while current is not None:
            following = current.next
            if current.val < 0:
                current.next = dummy.next
                dummy.next = current
            else:
                tail.next = current
                tail = current
                tail.next = None
            current = following
        return dummy.next
