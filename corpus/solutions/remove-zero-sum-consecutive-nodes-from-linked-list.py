class Solution:
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0)
        dummy.next = head
        last = {}
        prefix = 0
        node = dummy
        while node:
            prefix += node.val
            last[prefix] = node
            node = node.next
        prefix = 0
        node = dummy
        while node:
            prefix += node.val
            node.next = last[prefix].next
            node = node.next
        return dummy.next
