class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        for _ in range(k - 1):
            first = first.next
        from_start = first
        from_end = head
        while first.next is not None:
            first = first.next
            from_end = from_end.next
        from_start.val, from_end.val = from_end.val, from_start.val
        return head
