class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        length = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            length += 1
        shift = k % length
        if shift == 0:
            return head
        tail.next = head
        steps = length - shift
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
