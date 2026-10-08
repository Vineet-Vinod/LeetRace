class Solution:
    def plusOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        last_not_nine = dummy
        node = head
        while node is not None:
            if node.val != 9:
                last_not_nine = node
            node = node.next
        last_not_nine.val += 1
        node = last_not_nine.next
        while node is not None:
            node.val = 0
            node = node.next
        return dummy if dummy.val else head
