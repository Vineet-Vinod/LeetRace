class Solution:
    def deleteDuplicatesUnsorted(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counts: Counter[int] = Counter()
        node = head
        while node is not None:
            counts[node.val] += 1
            node = node.next
        sentinel = ListNode(0, head)
        previous = sentinel
        node = head
        while node is not None:
            if counts[node.val] > 1:
                previous.next = node.next
            else:
                previous = node
            node = node.next
        return sentinel.next
