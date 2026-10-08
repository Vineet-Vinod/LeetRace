class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        node = head
        while node is not None and node.next is not None:
            following = node.next
            node.next = ListNode(gcd(node.val, following.val), following)
            node = following
        return head
