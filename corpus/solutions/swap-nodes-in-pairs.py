class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy
        while previous.next is not None and previous.next.next is not None:
            first = previous.next
            second = first.next
            first.next = second.next
            second.next = first
            previous.next = second
            previous = first
        return dummy.next
