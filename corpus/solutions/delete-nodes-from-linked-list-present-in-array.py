class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        removed = set(nums)
        sentinel = ListNode(0, head)
        previous = sentinel
        node = head
        while node is not None:
            if node.val in removed:
                previous.next = node.next
            else:
                previous = node
            node = node.next
        return sentinel.next
