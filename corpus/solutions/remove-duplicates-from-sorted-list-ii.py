class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy
        current = head
        while current is not None:
            if current.next is not None and current.val == current.next.val:
                duplicate = current.val
                while current is not None and current.val == duplicate:
                    current = current.next
                previous.next = current
            else:
                previous = current
                current = current.next
        return dummy.next
