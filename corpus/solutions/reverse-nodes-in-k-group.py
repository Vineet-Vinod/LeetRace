class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy
        while True:
            end = before
            for _ in range(k):
                end = end.next
                if end is None:
                    return dummy.next
            after = end.next
            current = before.next
            previous = after
            while current is not after:
                following = current.next
                current.next = previous
                previous = current
                current = following
            old = before.next
            before.next = end
            before = old
