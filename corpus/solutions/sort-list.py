class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        size = 1
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        dummy = ListNode(0, head)
        while size < length:
            prev = dummy
            current = dummy.next
            while current:
                left = current
                right = self._cut(left, size)
                current = self._cut(right, size)
                merged, tail = self._merge(left, right)
                prev.next = merged
                prev = tail
            size *= 2
        return dummy.next

    def _cut(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        if head is None:
            return None
        tail = head
        for _ in range(size - 1):
            if tail.next is None:
                break
            tail = tail.next
        rest = tail.next
        tail.next = None
        return rest

    def _merge(
        self, left: Optional[ListNode], right: Optional[ListNode]
    ) -> tuple[Optional[ListNode], ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while left and right:
            if left.val <= right.val:
                tail.next, left = left, left.next
            else:
                tail.next, right = right, right.next
            tail = tail.next
        tail.next = left or right
        while tail.next:
            tail = tail.next
        return dummy.next, tail
