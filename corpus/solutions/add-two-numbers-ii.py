class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        first = []
        second = []
        while l1 is not None:
            first.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            second.append(l2.val)
            l2 = l2.next
        carry = 0
        head = None
        while first or second or carry:
            total = carry
            if first:
                total += first.pop()
            if second:
                total += second.pop()
            node = ListNode(total % 10)
            node.next = head
            head = node
            carry = total // 10
        return head
