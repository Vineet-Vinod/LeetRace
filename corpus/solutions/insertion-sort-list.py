class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        node = head
        while node is not None:
            next_node = node.next
            previous = sentinel
            while previous.next is not None and previous.next.val <= node.val:
                previous = previous.next
            node.next = previous.next
            previous.next = node
            node = next_node
        return sentinel.next
