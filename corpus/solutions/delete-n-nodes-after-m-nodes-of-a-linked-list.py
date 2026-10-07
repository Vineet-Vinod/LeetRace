class Solution:
    def deleteNodes(
        self, head: Optional[ListNode], m: int, n: int
    ) -> Optional[ListNode]:
        current = head
        while current is not None:
            for _ in range(m - 1):
                if current.next is None:
                    return head
                current = current.next
            removed = current.next
            for _ in range(n):
                if removed is None:
                    break
                removed = removed.next
            current.next = removed
            current = removed
        return head
