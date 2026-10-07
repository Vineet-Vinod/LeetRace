class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
        return previous
